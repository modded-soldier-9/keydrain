"""
Uninstaller script generation.
"""

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from config.settings import BuilderConfig


class UninstallerGenerator:
    """Generates uninstall scripts for cleanup."""
    
    def __init__(self, config: 'BuilderConfig'):
        self.config = config
        
    def generate_uninstall_script(self, output_dir: Path) -> None:
        """Generate an uninstall script."""
        uninstall_script = """@echo off
echo Removing keylogger persistence...

REM Remove registry entry
reg delete "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "SystemService" /f 2>nul

REM Remove scheduled task
schtasks /delete /tn "SystemService" /f 2>nul

REM Remove startup shortcut
del "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\SystemService.lnk" 2>nul

REM Remove log file
del "%TEMP%\\system_log.txt" 2>nul

echo Cleanup completed!
pause
"""
        
        with open(output_dir / "uninstall.bat", 'w') as f:
            f.write(uninstall_script) 