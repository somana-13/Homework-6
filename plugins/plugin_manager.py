"""
Plugin Manager module to dynamically load command plugins
Enhanced with logging support
"""
import os
import importlib.util
import inspect
from typing import Dict, Type, List
from commands.command_interface import Command
from utils.logger import get_logger

class PluginManager:
    """
    Plugin Manager class responsible for loading command plugins dynamically
    Enhanced with logging support
    """
    
    def __init__(self, plugins_directory: str = "plugins"):
        """Initialize the plugin manager with the plugins directory"""
        self.logger = get_logger(__name__)
        self.logger.debug(f"Initializing PluginManager with directory: {plugins_directory}")
        self.plugins_directory = plugins_directory
        self.commands: Dict[str, Command] = {}
    
    def discover_plugins(self) -> List[str]:
        """
        Discover Python files in the plugins directory that might contain plugins
        Returns list of Python file paths
        """
        self.logger.debug("Discovering plugin files")
        plugin_files = []
        
        # Get the absolute path to the plugins directory
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        plugins_path = os.path.join(base_dir, self.plugins_directory)
        
        # Check if plugins directory exists
        if not os.path.isdir(plugins_path):
            self.logger.warning(f"Plugins directory not found: {plugins_path}")
            return plugin_files
        
        # Find all .py files in the plugins directory
        for filename in os.listdir(plugins_path):
            if filename.endswith('.py') and not filename.startswith('__'):
                plugin_path = os.path.join(plugins_path, filename)
                plugin_files.append(plugin_path)
                self.logger.debug(f"Discovered plugin file: {filename}")
                
        self.logger.info(f"Found {len(plugin_files)} potential plugin files")
        return plugin_files
    
    def load_plugins(self) -> Dict[str, Command]:
        """
        Load discovered plugins and register their commands
        Returns dictionary of command names to command instances
        """
        self.logger.info("Loading plugins...")
        plugin_files = self.discover_plugins()
        
        for plugin_path in plugin_files:
            try:
                # Load the module from file path
                module_name = os.path.basename(plugin_path)[:-3]  # Remove .py extension
                self.logger.debug(f"Loading plugin module: {module_name}")
                
                spec = importlib.util.spec_from_file_location(module_name, plugin_path)
                if spec is None or spec.loader is None:
                    self.logger.error(f"Could not load spec for {plugin_path}")
                    continue
                    
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # Find all Command subclasses in the module
                commands_found = 0
                for name, obj in inspect.getmembers(module):
                    if (inspect.isclass(obj) and 
                        issubclass(obj, Command) and 
                        obj is not Command):
                        
                        # Extract command name from class name (remove 'Command' suffix)
                        command_name = name.lower()
                        if command_name.endswith('command'):
                            command_name = command_name[:-7]  # Remove 'command' suffix
                        
                        # Create instance and register command
                        self.commands[command_name] = obj()
                        commands_found += 1
                        self.logger.info(f"Loaded plugin command: {command_name}")
                
                if commands_found == 0:
                    self.logger.warning(f"No command classes found in {module_name}")
                else:
                    self.logger.debug(f"Loaded {commands_found} commands from {module_name}")
                
            except Exception as e:
                self.logger.error(f"Error loading plugin {plugin_path}: {e}", exc_info=True)
        
        self.logger.info(f"Finished loading plugins. Total commands: {len(self.commands)}")
        return self.commands

    def register_command(self, name: str, command: Command) -> None:
        """Register a command with the given name"""
        self.logger.debug(f"Manually registering command: {name}")
        self.commands[name] = command
        self.logger.info(f"Command '{name}' registered successfully")
        
    def get_commands(self) -> Dict[str, Command]:
        """Get all registered commands"""
        self.logger.debug(f"Returning {len(self.commands)} registered commands")
        return self.commands
