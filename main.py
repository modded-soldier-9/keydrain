#!/usr/bin/env python3
"""
Educational Malware Builder - Lab Use Only
Main application entry point.
"""

import sys
from pathlib import Path

# Add the current directory to Python path for imports
sys.path.insert(0, str(Path(__file__).parent))

from config.settings import BuilderConfig
from ui.menu import MenuSystem
from ui.display import DisplayManager
from generators.source_generator import SourceGenerator
from generators.polymorphism import PolymorphismEngine
from builders.compiler import Compiler
from builders.uninstaller import UninstallerGenerator
from utils.logger import BuildLogger


class MalwareBuilder:
    """Main application class that orchestrates all components."""
    
    def __init__(self):
        self.config = BuilderConfig()
        self.menu = MenuSystem(self.config)
        self.display = DisplayManager()
        self.source_generator = SourceGenerator(self.config)
        self.polymorphism_engine = PolymorphismEngine()
        self.compiler = Compiler(self.config)
        self.uninstaller = UninstallerGenerator(self.config)
        self.logger = BuildLogger(self.config)
        
    def run(self):
        """Main application loop."""
        while True:
            result = self.menu.run_main_menu()
            
            if result == 'BUILD':
                self.build_payload()
            elif result == 'QUIT':
                self.display.print_info("Goodbye!")
                break
                
    def build_payload(self):
        """Build the payload with selected features."""
        self.display.print_info("Building payload...")
        
        # Create output directory
        output_dir = Path(self.config.settings['output_dir'])
        output_dir.mkdir(exist_ok=True)
        
        # Generate source code
        self.display.print_info("Generating source code...")
        source_code = self.source_generator.generate_source_code()
        
        # Apply polymorphism if enabled
        if self.config.features['polymorphism']:
            self.display.print_info("Applying polymorphism...")
            source_code = self.polymorphism_engine.apply_polymorphism(source_code)
            
        # Write source file
        self.display.print_info("Writing source file...")
        source_file = self.logger.write_source_file(source_code, output_dir)
            
        # Compile to exe
        self.display.print_info("Compiling to executable...")
        if self.compiler.compile_to_exe(source_file, output_dir):
            self.display.print_success("Compilation successful!")
        else:
            self.display.print_error("Compilation failed!")
            return
        
        # Generate uninstall script if requested
        if self.config.features['uninstall_script']:
            self.display.print_info("Generating uninstall script...")
            self.uninstaller.generate_uninstall_script(output_dir)
            
        # Write build log
        self.logger.write_build_log(output_dir)
        
        self.display.print_success("Build completed!")
        self.display.print_info(f"Output directory: {output_dir.absolute()}")
        
        # Provide usage instructions
        if not self.config.features['debug_mode']:
            self.display.print_warning("Note: The executable runs silently. Enable debug mode to see console output.")
        self.display.print_info("To test the executable, run it from the output directory.")


if __name__ == '__main__':
    builder = MalwareBuilder()
    builder.run() 