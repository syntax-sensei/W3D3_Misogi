# Adaptive Prompt Optimizer

Optimize your prompts for specific AI coding tools like Copilot, Cursor, Replit, CodeWhisperer, Claude, and GPT-4. This tool analyzes your prompt and generates an optimized version tailored to the selected tool's capabilities, with explanations for each optimization.

## Features
- **Real Documentation Integration**: Based on official documentation from each tool
- **Tool-Specific Optimization**: Custom strategies for each AI coding tool
- **Before/After Comparison**: Side-by-side view of original vs optimized prompts
- **Detailed Explanations**: Step-by-step breakdown of optimizations made
- **Tool Information**: Comprehensive details about each tool's capabilities
- **Documentation Links**: Direct links to official documentation and examples
- **Real Examples**: Practical examples of effective prompts for each tool

## Supported Tools
- **GitHub Copilot** - AI pair programmer for code completion and generation
- **Cursor** - AI-first code editor with advanced code generation
- **Replit** - Online IDE with AI-powered code assistance
- **Amazon CodeWhisperer** - AI-powered code generator for AWS development
- **Claude (Anthropic)** - Advanced AI assistant for coding and analysis
- **GPT-4 (OpenAI)** - Large language model for code generation and review

## Project Structure
```
q3/
├── app.py                 # Main Flask application
├── prompt_analyzer.py     # Prompt analysis and intent detection
├── tool_analysis.json     # Detailed tool capabilities and documentation
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── optimizers/           # Tool-specific optimization modules
│   ├── __init__.py
│   ├── base_optimizer.py
│   ├── copilot_optimizer.py
│   ├── cursor_optimizer.py
│   ├── replit_optimizer.py
│   ├── codewhisperer_optimizer.py
│   ├── claude_optimizer.py
│   └── gpt_optimizer.py
└── templates/
    └── index.html        # Web interface
```

## Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation
1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd q3
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open in browser**
   Go to [http://localhost:5000](http://localhost:5000)

## Usage

### Basic Usage
1. Enter your base prompt in the text area
2. Select the target AI coding tool from the dropdown
3. Click "Optimize Prompt" to see the optimized version
4. Review the before/after comparison and explanations

### Understanding the Results
- **Original Prompt**: Your input prompt
- **Optimized Prompt**: Tool-specific optimized version
- **Analysis**: Automatic analysis of your prompt's intent and complexity
- **Optimization Steps**: Detailed explanation of each improvement made
- **Tool Information**: Comprehensive details about the selected tool

### Tool Information Displayed
- **Strengths**: What the tool excels at
- **Best For**: Ideal use cases
- **Limitations**: Current constraints and limitations
- **Optimization Focus**: What the optimizer prioritizes
- **Documentation Links**: Official documentation and resources
- **Real Examples**: Practical examples of effective prompts

## How It Works

### Prompt Analysis
The system analyzes your prompt for:
- **Intent**: Function generation, project creation, code review, etc.
- **Complexity**: Low, medium, or high based on length and keywords
- **Requirements**: Context, examples, testing, documentation needs
- **Tool-specific features**: AWS context, security requirements, etc.

### Optimization Strategies
Each tool has specific optimization strategies:

#### GitHub Copilot
- Clear, specific comments and docstrings
- Function signature patterns with type hints
- Context provision through comments
- Error handling and edge case specifications

#### Cursor
- Detailed project requirements and scope
- File structure and organization specifications
- Testing and documentation requirements
- Architecture and design pattern preferences

#### Replit
- Web framework selection and setup
- Package and dependency management
- Deployment and hosting configuration
- Interactive and collaborative features

#### Amazon CodeWhisperer
- AWS service selection and integration
- Security best practices and compliance
- Cloud-native patterns and architectures
- Infrastructure as Code and automation

#### Claude (Anthropic)
- Step-by-step reasoning instructions
- Explicit requirements and constraints
- Requests for explanations and justifications
- Safety and ethical considerations

#### GPT-4 (OpenAI)
- Explicit input/output format specifications
- Examples and edge cases
- Requests for reasoning and explanations
- Clear, concise instructions

## Documentation References

### Official Documentation Links
- **GitHub Copilot**: [docs.github.com/en/copilot](https://docs.github.com/en/copilot)
- **Cursor**: [cursor.sh/docs](https://cursor.sh/docs)
- **Replit**: [docs.replit.com](https://docs.replit.com)
- **Amazon CodeWhisperer**: [docs.aws.amazon.com/codewhisperer](https://docs.aws.amazon.com/codewhisperer)
- **Claude**: [docs.anthropic.com](https://docs.anthropic.com)
- **GPT-4**: [platform.openai.com/docs](https://platform.openai.com/docs)

## Adding More Tools

### Creating a New Optimizer
1. Create a new file in `optimizers/` following the `BaseOptimizer` interface
2. Implement the required methods:
   - `optimize(prompt, analysis)`: Main optimization logic
   - `get_tool_name()`: Return tool name
   - `get_capabilities()`: Return tool capabilities

3. Register the optimizer in `app.py`
4. Add tool information to `tool_analysis.json`

### Example Optimizer Structure
```python
from .base_optimizer import BaseOptimizer

class NewToolOptimizer(BaseOptimizer):
    def optimize(self, prompt: str, analysis: Dict[str, Any]) -> str:
        # Your optimization logic here
        return optimized_prompt
    
    def get_tool_name(self) -> str:
        return "New Tool Name"
    
    def get_capabilities(self) -> Dict[str, Any]:
        return {
            'strengths': [...],
            'best_for': [...],
            'limitations': [...],
            'optimization_focus': [...],
            'documentation': {...}
        }
```

## Contributing

### Areas for Improvement
- Add more AI coding tools
- Enhance optimization strategies based on user feedback
- Improve prompt analysis accuracy
- Add support for more programming languages
- Integrate with actual tool APIs for real-time optimization

### Testing
- Test with various prompt types and complexities
- Validate optimization strategies against real tool behavior
- Gather user feedback on optimization effectiveness

## License
MIT License - feel free to use, modify, and distribute this project.

## Acknowledgments
- Official documentation from all supported tools
- Community feedback and testing
- Best practices from the AI coding assistant community 