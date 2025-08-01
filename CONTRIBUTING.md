# Contributing to KeyDrain

Thank you for your interest in contributing to this educational project! This document provides guidelines for contributing to KeyDrain.

## 🎯 Purpose

This project is designed for **educational purposes only**. All contributions must:
- Be for legitimate educational and research purposes
- Comply with applicable laws and regulations
- Not promote or enable malicious use
- Focus on cybersecurity education and awareness

## 📋 Code of Conduct

### What We Accept
- ✅ Educational features and improvements
- ✅ Security research and analysis tools
- ✅ Documentation improvements
- ✅ Bug fixes and performance optimizations
- ✅ Testing and validation tools

### What We Don't Accept
- ❌ Malicious features or exploits
- ❌ Code designed for real-world attacks
- ❌ Features that bypass legitimate security measures
- ❌ Contributions that promote illegal activities

## 🛠️ Development Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/modded-soldier-9/keydrain.git
   cd keydrain
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Test your setup**
   ```bash
   python test_executable.py
   ```

## 📝 Making Changes

### 1. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes
- Follow the existing code style
- Add appropriate comments and documentation
- Include error handling
- Test your changes thoroughly

### 3. Test Your Changes
```bash
python main.py
# Test the feature you added
```

### 4. Commit Your Changes
```bash
git add .
git commit -m "Add descriptive commit message"
```

### 5. Push and Create Pull Request
```bash
git push origin feature/your-feature-name
```

## 📋 Pull Request Guidelines

### Before Submitting
- [ ] Code follows the existing style
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Feature is for educational purposes only
- [ ] No sensitive data is included

### Pull Request Template
```markdown
## Description
Brief description of the changes

## Educational Purpose
Explain how this contributes to cybersecurity education

## Testing
Describe how you tested the changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Educational purpose clearly stated
- [ ] No malicious functionality added
```

## 🏗️ Project Structure

### Key Directories
- `config/` - Configuration management
- `generators/` - Code generation modules
- `builders/` - Build system components
- `ui/` - User interface components
- `utils/` - Utility functions

### Adding New Features
1. **Configuration**: Add to `config/settings.py`
2. **UI**: Update `ui/menu.py` and `ui/display.py`
3. **Generation**: Extend `generators/source_generator.py`
4. **Documentation**: Update README.md

## 🧪 Testing Guidelines

### Manual Testing
- Test all features in isolated environment
- Verify webhook functionality
- Check persistence mechanisms
- Validate polymorphic code generation

### Automated Testing
- Add unit tests for new features
- Test error handling
- Verify cross-platform compatibility

## 📚 Documentation

### Code Documentation
- Add docstrings to new functions
- Include type hints where appropriate
- Document complex algorithms
- Explain security considerations

### User Documentation
- Update README.md for new features
- Add usage examples
- Document configuration options
- Include troubleshooting steps

## 🔒 Security Considerations

### Code Review Checklist
- [ ] No hardcoded credentials
- [ ] Proper error handling
- [ ] Input validation
- [ ] Secure file operations
- [ ] Educational purpose only

### Testing Environment
- Use isolated virtual machines
- No production systems
- Controlled network environment
- Proper logging and monitoring

## 🐛 Bug Reports

### Before Reporting
1. Check existing issues
2. Test in isolated environment
3. Verify steps to reproduce
4. Include system information

### Bug Report Template
```markdown
## Bug Description
Clear description of the issue

## Steps to Reproduce
1. Step one
2. Step two
3. Step three

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## System Information
- OS: Windows 10/11
- Python version: 3.7+
- Dependencies: All installed

## Additional Context
Any other relevant information
```

## 🎓 Educational Focus

### Acceptable Contributions
- **Security Research**: Understanding malware behavior
- **Detection Methods**: Learning about AV evasion
- **Defense Techniques**: Developing countermeasures
- **Analysis Tools**: Improving malware analysis capabilities

### Learning Objectives
- Understanding malware architecture
- Learning about persistence mechanisms
- Studying exfiltration techniques
- Developing defensive strategies

## 📞 Getting Help

### Questions and Support
- Create an issue for questions
- Use GitHub Discussions for general topics
- Check existing documentation first
- Provide detailed information

### Community Guidelines
- Be respectful and professional
- Focus on educational value
- Share knowledge constructively
- Help others learn

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## ⚠️ Legal Notice

Contributors are responsible for:
- Ensuring compliance with local laws
- Using the software only for educational purposes
- Not deploying against real systems
- Accepting full responsibility for their contributions

---

**Thank you for contributing to cybersecurity education! 🛡️** 