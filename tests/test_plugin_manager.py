"""
Tests for the plugin manager implementation
"""
import os
import sys
import pytest
from unittest.mock import patch, MagicMock
from plugins.plugin_manager import PluginManager
from commands.command_interface import Command

class MockCommand(Command):
    """Mock command class for testing"""
    
    def execute(self, *args, **kwargs):
        """Mock execute method"""
        return "mock result"
    
    @property
    def description(self):
        """Mock description property"""
        return "Mock command description"
    
    @property
    def usage(self):
        """Mock usage property"""
        return "mock <arg1> <arg2>"

class TestPluginManager:
    """Test class for plugin manager"""
    
    def test_init(self):
        """Test initialization of plugin manager"""
        pm = PluginManager()
        assert pm.plugins_directory == "plugins"
        assert isinstance(pm.commands, dict)
        assert len(pm.commands) == 0
    
    def test_register_command(self):
        """Test registering a command"""
        pm = PluginManager()
        mock_command = MockCommand()
        
        pm.register_command("test", mock_command)
        assert "test" in pm.commands
        assert pm.commands["test"] == mock_command
    
    def test_get_commands(self):
        """Test getting all registered commands"""
        pm = PluginManager()
        mock_command = MockCommand()
        
        pm.register_command("test", mock_command)
        commands = pm.get_commands()
        
        assert isinstance(commands, dict)
        assert "test" in commands
        assert commands["test"] == mock_command
    
    @patch('os.path.isdir')
    @patch('os.listdir')
    @patch('os.path.dirname')
    def test_discover_plugins(self, mock_dirname, mock_listdir, mock_isdir):
        """Test discovering plugins in the plugin directory"""
        # Mock directory structure
        mock_dirname.return_value = "/mock/path"
        mock_isdir.return_value = True
        mock_listdir.return_value = ["valid_plugin.py", "__init__.py", "not_a_plugin.txt"]
        
        pm = PluginManager()
        plugin_files = pm.discover_plugins()
        
        assert isinstance(plugin_files, list)
        assert len(plugin_files) == 1
        assert plugin_files[0].endswith("valid_plugin.py")
        
        # Test with non-existent directory
        mock_isdir.return_value = False
        plugin_files = pm.discover_plugins()
        assert len(plugin_files) == 0
    
    @patch('importlib.util.spec_from_file_location')
    @patch('importlib.util.module_from_spec')
    @patch.object(PluginManager, 'discover_plugins')
    def test_load_plugins(self, mock_discover, mock_module_from_spec, mock_spec):
        """Test loading plugins from discovered files"""
        # Setup mocks
        mock_discover.return_value = ["/mock/path/test_plugin.py"]
        
        mock_spec_obj = MagicMock()
        mock_spec.return_value = mock_spec_obj
        
        mock_module = MagicMock()
        mock_module_from_spec.return_value = mock_module
        
        # Mock a command class in the module
        mock_command = MockCommand()
        mock_module.__dict__ = {
            "TestCommand": type("TestCommand", (Command,), {
                "execute": lambda self, *args, **kwargs: "test result",
                "description": property(lambda self: "Test description"),
                "usage": property(lambda self: "test usage")
            })
        }
        
        # Run the test
        pm = PluginManager()
        commands = pm.load_plugins()
        
        # Verify results
        assert isinstance(commands, dict)
        assert mock_discover.called
        assert mock_spec.called
        assert mock_module_from_spec.called
        assert mock_spec_obj.loader.exec_module.called
