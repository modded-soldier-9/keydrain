# 🔐 Educational Malware Builder

> **⚠️ DISCLAIMER: This tool is for EDUCATIONAL PURPOSES ONLY. Use only in isolated lab environments for learning about cybersecurity, penetration testing, and malware analysis.**

A comprehensive Python-based malware builder that creates advanced keyloggers with multiple exfiltration methods, persistence mechanisms, and system reconnaissance capabilities.

## 🚀 Features

### Core Functionality
- **Advanced Keylogger** - Captures keystrokes with timestamp and window focus
- **File Logging** - Saves captured data to local files
- **Webhook Exfiltration** - Real-time data transmission via Discord/Slack webhooks
- **Enhanced Webhook Formatting** - Rich, organized embeds with system information

### System Reconnaissance (NEW)
- **System Information Collection** - Comprehensive system data gathering
  - Hostname, username, OS details, architecture
  - Network information (local/public IP, MAC address)
  - Hardware specifications (RAM, CPU, disk usage)
  - System status (uptime, boot time, process count)
- **Startup Screenshot** - High-quality PNG screenshot capture on startup
- **Startup-Only Transmission** - System data sent only on keylogger initialization

### Persistence & Evasion
- **Multiple Persistence Methods**
  - Registry modification
  - Task Scheduler integration
  - Startup folder placement
- **Polymorphism** - Randomizes function and variable names
- **Debug Mode** - Optional console window for testing
- **Uninstall Script** - Clean removal utility

### Build System
- **PyInstaller Integration** - Creates standalone executables
- **Cross-Platform Support** - Windows-focused with extensible architecture
- **Modular Design** - Easy to extend with new features

## 📋 Requirements

- Python 3.7+
- Windows OS (primary target)
- Internet connection (for webhook features)

## 🛠️ Installation

### Quick Setup (Windows)
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/educational-malware-builder.git
   cd educational-malware-builder
   ```

2. Run the automated setup:
   ```bash
   install_requirements.bat
   ```

3. Test the installation:
   ```bash
   test_setup.bat
   ```

4. Start the builder:
   ```bash
   start_builder.bat
   ```

### Manual Installation
```bash
pip install -r requirements.txt
python main.py
```

## 🎯 Usage

### Basic Usage
1. Run `start_builder.bat` or `python main.py`
2. Configure your desired features using the interactive menu
3. Set up webhook URL (if using webhook exfiltration)
4. Build your keylogger
5. Find the executable in `build_output/keylogger.exe`

### Feature Configuration

| Option | Feature | Description |
|--------|---------|-------------|
| 1 | Core Keylogger | Basic keystroke capture |
| 2 | Log to File | Save data to local files |
| 3 | Webhook Exfiltration | Send data via webhook |
| 4 | Persistence | Auto-start mechanisms |
| 5 | Polymorphism | Randomize code names |
| 6 | Uninstall Script | Include removal utility |
| 7 | Debug Mode | Show console window |
| 8 | System Information | Collect system data on startup |
| 9 | Startup Screenshot | Capture screen on startup |

### Webhook Setup
1. Create a Discord webhook or Slack incoming webhook
2. Copy the webhook URL
3. Enable "Webhook Exfiltration" in the builder
4. Enter your webhook URL when prompted

## 📁 Project Structure

```
educational-malware-builder/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── QUICK_START.txt        # Quick setup guide
├── install_requirements.bat # Automated setup script
├── start_builder.bat      # Application launcher
├── test_setup.bat         # Dependency tester
├── config/                # Configuration management
│   ├── __init__.py
│   └── settings.py
├── generators/            # Code generation modules
│   ├── __init__.py
│   ├── source_generator.py
│   └── polymorphism.py
├── builders/              # Build system
│   ├── __init__.py
│   ├── compiler.py
│   └── uninstaller.py
├── ui/                    # User interface
│   ├── __init__.py
│   ├── display.py
│   └── menu.py
├── utils/                 # Utility functions
│   ├── __init__.py
│   └── logger.py
└── build_output/          # Generated files
    ├── keylogger.exe      # Final executable
    └── uninstall.bat      # Removal script
```

## 🔧 Configuration

### Settings File
Key configuration options in `config/settings.py`:

```python
# Webhook Configuration
webhook_url = "https://discord.com/api/webhooks/your-webhook-url"

# Build Settings
flush_interval = 30  # Seconds between data transmission
debug_mode = False   # Show console window

# Persistence Options
registry_key = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
startup_folder = "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
```

## 🛡️ Security Considerations

### For Educational Use
- **Isolated Environment**: Always test in virtual machines or isolated lab environments
- **No Real Targets**: Never deploy against real systems or networks
- **Legal Compliance**: Ensure compliance with local laws and regulations
- **Ethical Use**: Use only for educational and research purposes

### Detection Evasion
The generated keyloggers include basic evasion techniques:
- Polymorphic code generation
- Multiple persistence methods
- Stealth file logging
- Encrypted webhook communication

## 🐛 Troubleshooting

### Common Issues

**"Python not found"**
- Install Python 3.7+ from python.org
- Ensure Python is added to PATH

**"Module not found"**
- Run `install_requirements.bat` to install dependencies
- Use `test_setup.bat` to verify installation

**"Webhook not working"**
- Verify webhook URL is correct
- Check internet connection
- Ensure Discord/Slack webhook is active

**"Build fails"**
- Check available disk space (requires ~100MB)
- Ensure antivirus isn't blocking PyInstaller
- Try running as administrator

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## ⚠️ Legal Disclaimer

This software is provided for **EDUCATIONAL PURPOSES ONLY**. The authors are not responsible for any misuse of this software. Users are responsible for ensuring compliance with applicable laws and regulations.

**By using this software, you agree to:**
- Use it only for educational and research purposes
- Not deploy it against real systems or networks
- Comply with all applicable laws and regulations
- Accept full responsibility for any consequences of use

## 📞 Support

For educational questions or issues:
- Create an issue on GitHub
- Ensure you're using the latest version
- Provide detailed error messages and system information

---

**Remember: Knowledge is power, but with great power comes great responsibility. Use this tool wisely and ethically.** 