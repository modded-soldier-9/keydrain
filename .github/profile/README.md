# 🔐 KeyDrain - Educational Malware Builder

> **⚠️ DISCLAIMER: This tool is for EDUCATIONAL PURPOSES ONLY. Use only in isolated lab environments for learning about cybersecurity, penetration testing, and malware analysis.**

## 🎯 Project Overview

A comprehensive Python-based malware builder that creates advanced keyloggers with multiple exfiltration methods, persistence mechanisms, and system reconnaissance capabilities for **educational use only**.

## 🚀 Key Features

### Core Functionality
- **Advanced Keylogger** - Captures keystrokes with timestamp and window focus
- **File Logging** - Saves captured data to local files
- **Webhook Exfiltration** - Real-time data transmission via Discord/Slack webhooks
- **Enhanced Webhook Formatting** - Rich, organized embeds with system information

### System Reconnaissance
- **System Information Collection** - Comprehensive system data gathering
- **Startup Screenshot** - High-quality PNG screenshot capture on startup
- **Startup-Only Transmission** - System data sent only on keylogger initialization

### Persistence & Evasion
- **Multiple Persistence Methods** - Registry, Task Scheduler, Startup folder
- **Polymorphism** - Randomizes function and variable names
- **Debug Mode** - Optional console window for testing
- **Uninstall Script** - Clean removal utility

## 🛡️ Educational Focus

This project is designed for:
- **Security Research** - Understanding malware behavior and detection
- **Penetration Testing** - Testing security controls in controlled environments
- **Academic Study** - Learning about malware development and defense
- **Red Team Training** - Developing offensive security skills
- **Software Architecture** - Learning about modular design patterns

## 📋 Quick Start

```bash
# Clone the repository
git clone https://github.com/modded-soldier-9/keydrain.git
cd keydrain

# Install dependencies
install_requirements.bat

# Test setup
test_setup.bat

# Start builder
start_builder.bat
```

## 🔒 Security Guidelines

### For Educational Use
- ✅ **Isolated Environment**: Always test in virtual machines or isolated lab environments
- ✅ **No Real Targets**: Never deploy against real systems or networks
- ✅ **Legal Compliance**: Ensure compliance with local laws and regulations
- ✅ **Ethical Use**: Use only for educational and research purposes

### Prohibited Activities
- ❌ Testing against production systems
- ❌ Targeting systems you don't own
- ❌ Using for malicious purposes
- ❌ Violating applicable laws or regulations

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/modded-soldier-9/keydrain?style=social)
![GitHub forks](https://img.shields.io/github/forks/modded-soldier-9/keydrain?style=social)
![GitHub issues](https://img.shields.io/github/issues/modded-soldier-9/keydrain)
![GitHub pull requests](https://img.shields.io/github/issues-pr/modded-soldier-9/keydrain)
![GitHub license](https://img.shields.io/github/license/modded-soldier-9/keydrain)

## 🛠️ Technology Stack

- **Python 3.7+** - Core programming language
- **PyInstaller** - Executable compilation
- **pynput** - Keystroke capture
- **psutil** - System information
- **PIL/Pillow** - Screenshot capture
- **requests** - Webhook communication
- **colorama** - Terminal colors

## 📁 Project Structure

```
keydrain/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── README.md              # Comprehensive documentation
├── LICENSE                # MIT License
├── CONTRIBUTING.md        # Contribution guidelines
├── SECURITY.md            # Security policy
├── CHANGELOG.md           # Version history
├── install_requirements.bat # Automated setup script
├── start_builder.bat      # Application launcher
├── test_setup.bat         # Dependency tester
├── config/                # Configuration management
├── generators/            # Code generation modules
├── builders/              # Build system
├── ui/                    # User interface
├── utils/                 # Utility functions
└── build_output/          # Generated files
```

## 🤝 Contributing

We welcome contributions that promote cybersecurity education! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Before Contributing
- [ ] Read the educational purpose statement
- [ ] Understand the security guidelines
- [ ] Test in isolated environment
- [ ] Follow responsible disclosure practices

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/modded-soldier-9/keydrain/issues)
- **Discussions**: [GitHub Discussions](https://github.com/modded-soldier-9/keydrain/discussions)
- **Security**: [Security Policy](SECURITY.md)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Legal Disclaimer

This software is provided for **EDUCATIONAL PURPOSES ONLY**. Users are responsible for ensuring compliance with applicable laws and regulations.

**By using this software, you agree to:**
- Use it only for educational and research purposes
- Not deploy it against real systems or networks
- Comply with all applicable laws and regulations
- Accept full responsibility for any consequences of use

---

**Remember: Knowledge is power, but with great power comes great responsibility. Use this tool wisely and ethically. 🛡️**

---

<div align="center">

**🔐 KeyDrain** | **🛡️ For Educational Use Only** | **📚 Cybersecurity Learning**

</div> 