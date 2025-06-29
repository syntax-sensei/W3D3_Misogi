from .base_optimizer import BaseOptimizer
from typing import Dict, Any
import re

class CopilotOptimizer(BaseOptimizer):
    """
    Optimizer for GitHub Copilot prompts.
    Based on official GitHub Copilot documentation and best practices.
    Documentation: https://docs.github.com/en/copilot
    """
    
    def optimize(self, prompt: str, analysis: Dict[str, Any]) -> str:
        optimized_prompt = prompt
        
        # Reset explanations for new optimization
        self.explanation = []
        self.optimization_steps = []
        
        # Add context if missing (Copilot works best with clear context)
        if analysis.get('has_context', False) == False:
            optimized_prompt = self._add_context_hints(optimized_prompt)
            self.add_explanation(
                "Added context hints",
                "Copilot performs better when given clear context about requirements and constraints"
            )
        
        # Optimize for function generation with docstrings
        if analysis.get('intent') == 'function_generation':
            optimized_prompt = self._optimize_for_functions(optimized_prompt)
            self.add_explanation(
                "Optimized for function generation",
                "Added function signature patterns, type hints, and docstring templates based on Copilot best practices"
            )
        
        # Add inline comments for complex logic
        if analysis.get('complexity') == 'high':
            optimized_prompt = self._add_inline_comments(optimized_prompt)
            self.add_explanation(
                "Added inline comment suggestions",
                "Complex logic benefits from step-by-step comments for better Copilot understanding"
            )
        
        # Add error handling specifications
        if 'error' not in prompt.lower() and 'exception' not in prompt.lower():
            optimized_prompt = self._add_error_handling(optimized_prompt)
            self.add_explanation(
                "Added error handling specifications",
                "Copilot can generate robust error handling when explicitly requested"
            )
        
        # Optimize language for Copilot's understanding
        optimized_prompt = self._optimize_language(optimized_prompt)
        self.add_explanation(
            "Optimized language",
            "Used Copilot-friendly language patterns and clear, specific instructions"
        )
        
        # Add code examples if appropriate
        if analysis.get('has_examples', False) == False and analysis.get('complexity') in ['medium', 'high']:
            optimized_prompt = self._add_example_suggestions(optimized_prompt)
            self.add_explanation(
                "Added example suggestions",
                "Examples help Copilot understand expected input/output patterns and edge cases"
            )
        
        # Add testing suggestions for complex functions
        if analysis.get('intent') == 'function_generation' and analysis.get('complexity') in ['medium', 'high']:
            optimized_prompt = self._add_testing_suggestions(optimized_prompt)
            self.add_explanation(
                "Added testing suggestions",
                "Copilot can generate unit tests when explicitly requested for complex functions"
            )
        
        self.add_summary(f"Optimized prompt for GitHub Copilot with {len(self.optimization_steps)} improvements based on official documentation")
        
        return optimized_prompt
    
    def _add_context_hints(self, prompt: str) -> str:
        """Add context hints for better Copilot understanding."""
        context_hints = [
            "# Context: This code should follow best practices and be well-documented",
            "# Consider error handling, edge cases, and input validation",
            "# Use clear variable names, meaningful comments, and proper formatting",
            "# Follow language-specific conventions (PEP 8 for Python, etc.)"
        ]
        
        if not prompt.startswith('#'):
            prompt = '\n'.join(context_hints) + '\n\n' + prompt
        
        return prompt
    
    def _optimize_for_functions(self, prompt: str) -> str:
        """Optimize prompt for function generation with proper docstrings."""
        # Add function signature patterns with type hints
        if 'function' in prompt.lower() and 'def ' not in prompt:
            prompt += "\n\n# Expected function signature with type hints:\n# def function_name(param1: type, param2: type) -> return_type:\n#     \"\"\"\n#     Brief description of what the function does.\n#     \n#     Args:\n#         param1 (type): Description of param1\n#         param2 (type): Description of param2\n#     \n#     Returns:\n#         return_type: Description of return value\n#     \n#     Raises:\n#         ExceptionType: Description of when this exception is raised\n#     \"\"\""
        
        return prompt
    
    def _add_inline_comments(self, prompt: str) -> str:
        """Add inline comment suggestions for complex logic."""
        if 'algorithm' in prompt.lower() or 'complex' in prompt.lower() or 'logic' in prompt.lower():
            prompt += "\n\n# Add inline comments for each major step:\n# Step 1: [description of what this step accomplishes]\n# Step 2: [description of what this step accomplishes]\n# etc."
        
        return prompt
    
    def _add_error_handling(self, prompt: str) -> str:
        """Add error handling specifications."""
        prompt += "\n\n# Include proper error handling and input validation\n# Handle edge cases and potential exceptions appropriately"
        
        return prompt
    
    def _optimize_language(self, prompt: str) -> str:
        """Optimize language for Copilot's understanding based on official best practices."""
        # Replace vague terms with specific ones based on Copilot documentation
        replacements = {
            'make it better': 'improve the code with better error handling, documentation, and following best practices',
            'optimize': 'optimize for performance, readability, and maintainability',
            'clean code': 'write clean, well-documented code following language-specific conventions (PEP 8 for Python)',
            'good code': 'write production-ready code with proper error handling, documentation, and best practices',
            'fix': 'identify and fix issues with proper error handling and edge case consideration',
            'improve': 'improve the code quality, performance, and maintainability'
        }
        
        for old, new in replacements.items():
            prompt = prompt.replace(old, new)
        
        return prompt
    
    def _add_example_suggestions(self, prompt: str) -> str:
        """Add example suggestions for complex prompts."""
        prompt += "\n\n# Example usage:\n# result = function_name(input_data)\n# print(result)\n# \n# Example edge cases to consider:\n# - Empty input\n# - Invalid input types\n# - Boundary conditions"
        
        return prompt
    
    def _add_testing_suggestions(self, prompt: str) -> str:
        """Add testing suggestions for complex functions."""
        prompt += "\n\n# Generate unit tests for this function:\n# - Test normal cases\n# - Test edge cases\n# - Test error conditions\n# - Test with different input types"
        
        return prompt
    
    def get_tool_name(self) -> str:
        return "GitHub Copilot"
    
    def get_capabilities(self) -> Dict[str, Any]:
        return {
            'strengths': [
                'Real-time code completion and suggestions',
                'Function and method generation with context',
                'Multi-language support (Python, JavaScript, TypeScript, Java, C++, etc.)',
                'IDE integration (VS Code, IntelliJ, Neovim)',
                'Context-aware suggestions based on comments and code',
                'Documentation generation from code',
                'Test generation and refactoring suggestions'
            ],
            'best_for': [
                'Function and class generation with docstrings',
                'Code completion and line-by-line assistance',
                'Documentation generation from existing code',
                'Refactoring and code improvement suggestions',
                'Test case generation',
                'Boilerplate code generation'
            ],
            'limitations': [
                'Limited to code generation (no project architecture)',
                'Requires good context and clear comments',
                'May not understand complex business logic without context',
                'Context window limitations for large files',
                'No direct API access for custom integrations'
            ],
            'optimization_focus': [
                'Clear, specific comments and docstrings',
                'Function signature patterns and type hints',
                'Context provision through comments',
                'Inline comments for complex logic',
                'Error handling and edge case specifications',
                'Code style and formatting preferences'
            ],
            'documentation': {
                'official': 'https://docs.github.com/en/copilot',
                'best_practices': 'https://docs.github.com/en/copilot/getting-started-with-github-copilot/using-github-copilot-in-your-editor',
                'api_reference': 'https://docs.github.com/en/copilot/github-copilot-api',
                'examples': 'https://github.com/github/copilot-examples'
            }
        } 