"""
Build logging utilities.
"""

import json
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from config.settings import BuilderConfig


class BuildLogger:
    """Handles build logging and file operations."""
    
    def __init__(self, config: 'BuilderConfig'):
        self.config = config
        
    def write_build_log(self, output_dir: Path) -> None:
        """Write build log with selected options."""
        build_info = self.config.get_build_info()
        
        with open(output_dir / "build_log.txt", 'w') as f:
            json.dump(build_info, f, indent=2)
            
    def write_source_file(self, source_code: str, output_dir: Path) -> Path:
        """Write source code to file."""
        source_file = output_dir / "keylogger.py"
        with open(source_file, 'w') as f:
            f.write(source_code)
        return source_file 