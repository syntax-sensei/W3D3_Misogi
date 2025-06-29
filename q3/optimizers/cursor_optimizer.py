from .base_optimizer import BaseOptimizer
from typing import Dict, Any
import re

class CursorOptimizer(BaseOptimizer):
    """
    Optimizer for Cursor prompts.
    Cursor works best with:
    - Detailed, step-by-step instructions
    - File structure and architecture guidance
    - Testing and documentation requirements
    - Code review and refactoring requests
    """
    
    def optimize(self, prompt: str, analysis: Dict[str, Any]) -> str:
        optimized_prompt = prompt
        
        # Reset explanations for new optimization
        self.explanation = []
        self.optimization_steps = []
        
        # Add file structure guidance
        if analysis.get('intent') == 'project_creation' or 'create' in prompt.lower():
            optimized_prompt = self._add_file_structure_guidance(optimized_prompt)
            self.add_explanation(
                "Added file structure guidance",
                "Cursor excels at creating complete project structures with proper organization"
            )
        
        # Optimize for testing
        if analysis.get('has_testing', False) == False and analysis.get('complexity') in ['medium', 'high']:
            optimized_prompt = self._add_testing_requirements(optimized_prompt)
            self.add_explanation(
                "Added testing requirements",
                "Cursor can generate comprehensive test suites and testing strategies"
            )
        
        # Add documentation requirements
        if analysis.get('has_documentation', False) == False:
            optimized_prompt = self._add_documentation_requirements(optimized_prompt)
            self.add_explanation(
                "Added documentation requirements",
                "Cursor can generate comprehensive documentation including README, API docs, and inline comments"
            )
        
        # Optimize for code review
        if analysis.get('intent') == 'code_review':
            optimized_prompt = self._optimize_for_code_review(optimized_prompt)
            self.add_explanation(
                "Optimized for code review",
                "Cursor provides detailed code analysis and improvement suggestions"
            )
        
        # Add architecture considerations
        if analysis.get('complexity') == 'high':
            optimized_prompt = self._add_architecture_guidance(optimized_prompt)
            self.add_explanation(
                "Added architecture guidance",
                "Cursor can suggest optimal architecture patterns and design decisions"
            )
        
        # Optimize language for Cursor
        optimized_prompt = self._optimize_language(optimized_prompt)
        self.add_explanation(
            "Optimized language",
            "Used Cursor-specific language patterns for better understanding"
        )
        
        self.add_summary(f"Optimized prompt for Cursor with {len(self.optimization_steps)} improvements")
        
        return optimized_prompt
    
    def _add_file_structure_guidance(self, prompt: str) -> str:
        """Add file structure and project organization guidance."""
        structure_guidance = [
            "# Project Structure:",
            "# - Organize code into logical modules/packages",
            "# - Separate concerns (models, views, controllers, etc.)",
            "# - Include configuration files and environment setup",
            "# - Add proper __init__.py files for Python packages"
        ]
        
        if not any(line.startswith('# Project Structure:') for line in prompt.split('\n')):
            prompt = '\n'.join(structure_guidance) + '\n\n' + prompt
        
        return prompt
    
    def _add_testing_requirements(self, prompt: str) -> str:
        """Add testing requirements and strategies."""
        testing_requirements = [
            "# Testing Requirements:",
            "# - Unit tests for all functions and classes",
            "# - Integration tests for API endpoints",
            "# - Test coverage should be >80%",
            "# - Include test data and fixtures",
            "# - Add CI/CD pipeline configuration"
        ]
        
        if 'test' not in prompt.lower():
            prompt += '\n\n' + '\n'.join(testing_requirements)
        
        return prompt
    
    def _add_documentation_requirements(self, prompt: str) -> str:
        """Add documentation requirements."""
        doc_requirements = [
            "# Documentation Requirements:",
            "# - Comprehensive README.md with setup instructions",
            "# - API documentation with examples",
            "# - Inline code comments for complex logic",
            "# - Architecture and design decisions documentation"
        ]
        
        if 'documentation' not in prompt.lower() and 'readme' not in prompt.lower():
            prompt += '\n\n' + '\n'.join(doc_requirements)
        
        return prompt
    
    def _optimize_for_code_review(self, prompt: str) -> str:
        """Optimize prompt for code review tasks."""
        review_guidance = [
            "# Code Review Focus Areas:",
            "# - Code quality and best practices",
            "# - Performance optimizations",
            "# - Security vulnerabilities",
            "# - Maintainability and readability",
            "# - Error handling and edge cases",
            "# - Testing coverage and quality"
        ]
        
        if not any(line.startswith('# Code Review Focus Areas:') for line in prompt.split('\n')):
            prompt = '\n'.join(review_guidance) + '\n\n' + prompt
        
        return prompt
    
    def _add_architecture_guidance(self, prompt: str) -> str:
        """Add architecture and design guidance."""
        arch_guidance = [
            "# Architecture Considerations:",
            "# - Design patterns and principles",
            "# - Scalability and performance",
            "# - Security best practices",
            "# - Error handling and logging",
            "# - Configuration management"
        ]
        
        if not any(line.startswith('# Architecture Considerations:') for line in prompt.split('\n')):
            prompt += '\n\n' + '\n'.join(arch_guidance)
        
        return prompt
    
    def _optimize_language(self, prompt: str) -> str:
        """Optimize language for Cursor's understanding."""
        # Replace vague terms with specific ones
        replacements = {
            'build': 'create a complete, production-ready application with proper structure',
            'make': 'develop a comprehensive solution with all necessary components',
            'implement': 'implement with proper error handling, testing, and documentation',
            'create': 'create a well-structured, maintainable solution'
        }
        
        for old, new in replacements.items():
            prompt = prompt.replace(old, new)
        
        return prompt
    
    def get_tool_name(self) -> str:
        return "Cursor"
    
    def get_capabilities(self) -> Dict[str, Any]:
        return {
            'strengths': [
                'Complete project generation',
                'Multi-file code generation',
                'Architecture and design guidance',
                'Testing and documentation generation',
                'Code review and refactoring',
                'Context-aware development'
            ],
            'best_for': [
                'Full project creation',
                'Complex system architecture',
                'Code review and improvement',
                'Testing strategy development',
                'Documentation generation'
            ],
            'limitations': [
                'May generate more code than needed',
                'Requires clear project scope',
                'Context window limitations for large projects'
            ],
            'optimization_focus': [
                'Detailed, step-by-step instructions',
                'File structure and organization',
                'Testing and documentation requirements',
                'Architecture and design patterns'
            ]
        } 