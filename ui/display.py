"""
Display management for the malware builder UI.
"""

import os
import colorama
from colorama import Fore, Back, Style
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from config.settings import BuilderConfig

# Initialize colorama for cross-platform colored output
colorama.init()


class DisplayManager:
    """Manages display and formatting for the UI."""
    
    @staticmethod
    def clear_screen():
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    @staticmethod
    def print_banner():
        """Print the application banner."""
        banner = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
║                Educational Malware Builder - Lab Use Only              ║
║                                                                      ║
║  ⚠️  WARNING: This tool is for educational purposes only!           ║
║     Use only in isolated lab environments.                          ║
╚══════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
        print(banner)
        
    @staticmethod
    def print_menu(config: 'BuilderConfig'):
        """Display the main feature selection menu."""
        print(f"\n{Fore.YELLOW}Select features to include in your build:{Style.RESET_ALL}\n")
        
        # Core features
        print(f"[{'✓' if config.features['core_keylogger'] else ' '}] {Fore.GREEN}Core Keylogger{Style.RESET_ALL}")
        print(f"[{'✓' if config.features['log_to_file'] else ' '}] {Fore.GREEN}Log to File{Style.RESET_ALL}")
        print(f"[{'✓' if config.features['webhook_exfiltration'] else ' '}] {Fore.GREEN}Webhook Exfiltration{Style.RESET_ALL}")
        print(f"[{'✓' if config.features['persistence'] else ' '}] {Fore.GREEN}Persistence{Style.RESET_ALL}")
        print(f"[{'✓' if config.features['polymorphism'] else ' '}] {Fore.GREEN}Polymorphism (Randomize names){Style.RESET_ALL}")
        print(f"[{'✓' if config.features['uninstall_script'] else ' '}] {Fore.GREEN}Include Uninstall Script{Style.RESET_ALL}")
        print(f"[{'✓' if config.features['debug_mode'] else ' '}] {Fore.GREEN}Debug Mode (Console window){Style.RESET_ALL}")
        print(f"[{'✓' if config.features['system_info_collection'] else ' '}] {Fore.GREEN}System Information Collection{Style.RESET_ALL}")
        print(f"[{'✓' if config.features['startup_screenshot'] else ' '}] {Fore.GREEN}Startup Screenshot{Style.RESET_ALL}")
        
        # Persistence sub-options
        if config.features['persistence']:
            print(f"\n{Fore.CYAN}Persistence Options:{Style.RESET_ALL}")
            print(f"  [{'✓' if config.persistence_options['registry_run'] else ' '}] Registry Run Key")
            print(f"  [{'✓' if config.persistence_options['task_scheduler'] else ' '}] Task Scheduler XML")
            print(f"  [{'✓' if config.persistence_options['startup_shortcut'] else ' '}] Startup Folder Shortcut")
            
        # Settings
        if config.features['webhook_exfiltration']:
            print(f"\n{Fore.CYAN}Webhook URL:{Style.RESET_ALL} {config.settings['webhook_url'] or 'Not set'}")
            
        print(f"\n{Fore.CYAN}Flush Interval:{Style.RESET_ALL} {config.settings['flush_interval']} seconds")
        
        print(f"\n{Fore.YELLOW}Navigation:{Style.RESET_ALL}")
        print("  [1-9] Toggle features")
        print("  [10] Configure persistence options")
        print("  [11] Configure settings")
        print("  [B] Build Now")
        print("  [Q] Quit")
        
    @staticmethod
    def print_persistence_menu(config: 'BuilderConfig'):
        """Display the persistence configuration menu."""
        print(f"\n{Fore.YELLOW}Configure Persistence Options:{Style.RESET_ALL}\n")
        
        print(f"[{'✓' if config.persistence_options['registry_run'] else ' '}] Registry Run Key")
        print(f"[{'✓' if config.persistence_options['task_scheduler'] else ' '}] Task Scheduler XML")
        print(f"[{'✓' if config.persistence_options['startup_shortcut'] else ' '}] Startup Folder Shortcut")
        
        print(f"\n{Fore.YELLOW}Navigation:{Style.RESET_ALL}")
        print("  [1-3] Toggle persistence options")
        print("  [B] Back to main menu")
        
    @staticmethod
    def print_settings_menu(config: 'BuilderConfig'):
        """Display the settings configuration menu."""
        print(f"\n{Fore.YELLOW}Configure Settings:{Style.RESET_ALL}\n")
        
        if config.features['webhook_exfiltration']:
            print(f"Webhook URL: {config.settings['webhook_url'] or 'Not set'}")
            print("1. Set webhook URL")
            
        print(f"Flush Interval: {config.settings['flush_interval']} seconds")
        print("2. Set flush interval")
        
        print(f"\n{Fore.YELLOW}Navigation:{Style.RESET_ALL}")
        print("  [B] Back to main menu")
        
    @staticmethod
    def print_success(message: str):
        """Print a success message."""
        print(f"\n{Fore.GREEN}{message}{Style.RESET_ALL}")
        
    @staticmethod
    def print_error(message: str):
        """Print an error message."""
        print(f"\n{Fore.RED}{message}{Style.RESET_ALL}")
        
    @staticmethod
    def print_warning(message: str):
        """Print a warning message."""
        print(f"\n{Fore.YELLOW}{message}{Style.RESET_ALL}")
        
    @staticmethod
    def print_info(message: str):
        """Print an info message."""
        print(f"\n{Fore.CYAN}{message}{Style.RESET_ALL}") 