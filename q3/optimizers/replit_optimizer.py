from .base_optimizer import BaseOptimizer
from typing import Dict, Any
import re

class ReplitOptimizer(BaseOptimizer):
    """
    Optimizer for Replit prompts.
    Replit works best with:
    - Web application development
    - Interactive coding environments
    - Package and dependency management
    - Deployment and hosting considerations
    - Collaborative development features
    """
    
    def optimize(self, prompt: str, analysis: Dict[str, Any]) -> str:
        optimized_prompt = prompt
        
        # Reset explanations for new optimization
        self.explanation = []
        self.optimization_steps = []
        
        # Add web development context
        if analysis.get('intent') == 'web_development' or 'web' in prompt.lower():
            optimized_prompt = self._add_web_development_context(optimized_prompt)
            self.add_explanation(
                "Added web development context",
                "Replit excels at web application development with built-in hosting"
            )
        
        # Add package management
        if analysis.get('has_dependencies', False) == False:
            optimized_prompt = self._add_package_management(optimized_prompt)
            self.add_explanation(
                "Added package management",
                "Replit can automatically handle dependencies and package installation"
            )
        
        # Add deployment considerations
        if analysis.get('intent') == 'project_creation':
            optimized_prompt = self._add_deployment_guidance(optimized_prompt)
            self.add_explanation(
                "Added deployment guidance",
                "Replit provides seamless deployment and hosting capabilities"
            )
        
        # Add interactive features
        if analysis.get('complexity') in ['medium', 'high']:
            optimized_prompt = self._add_interactive_features(optimized_prompt)
            self.add_explanation(
                "Added interactive features",
                "Replit supports interactive elements and real-time collaboration"
            )
        
        # Add environment setup
        optimized_prompt = self._add_environment_setup(optimized_prompt)
        self.add_explanation(
            "Added environment setup",
            "Replit can configure development environments automatically"
        )
        
        # Optimize language for Replit
        optimized_prompt = self._optimize_language(optimized_prompt)
        self.add_explanation(
            "Optimized language",
            "Used Replit-specific language patterns for better understanding"
        )
        
        self.add_summary(f"Optimized prompt for Replit with {len(self.optimization_steps)} improvements")
        
        return optimized_prompt
    
    def _add_web_development_context(self, prompt: str) -> str:
        """Add web development specific context."""
        web_context = [
            "# Web Development Context:",
            "# - Use modern web frameworks (Flask, Django, React, etc.)",
            "# - Include responsive design considerations",
            "# - Add proper routing and API endpoints",
            "# - Consider client-side and server-side functionality",
            "# - Include static file handling and templates"
        ]
        
        if not any(line.startswith('# Web Development Context:') for line in prompt.split('\n')):
            prompt = '\n'.join(web_context) + '\n\n' + prompt
        
        return prompt
    
    def _add_package_management(self, prompt: str) -> str:
        """Add package and dependency management."""
        package_management = [
            "# Package Management:",
            "# - Include requirements.txt or package.json",
            "# - Specify exact versions for reproducibility",
            "# - Add development dependencies if needed",
            "# - Consider virtual environment setup"
        ]
        
        if 'requirements' not in prompt.lower() and 'package.json' not in prompt.lower():
            prompt += '\n\n' + '\n'.join(package_management)
        
        return prompt
    
    def _add_deployment_guidance(self, prompt: str) -> str:
        """Add deployment and hosting guidance."""
        deployment_guidance = [
            "# Deployment Considerations:",
            "# - Configure for Replit's hosting environment",
            "# - Set up proper environment variables",
            "# - Include deployment scripts if needed",
            "# - Consider database setup and configuration",
            "# - Add proper error handling for production"
        ]
        
        if not any(line.startswith('# Deployment Considerations:') for line in prompt.split('\n')):
            prompt += '\n\n' + '\n'.join(deployment_guidance)
        
        return prompt
    
    def _add_interactive_features(self, prompt: str) -> str:
        """Add interactive and collaborative features."""
        interactive_features = [
            "# Interactive Features:",
            "# - Add user input handling and validation",
            "# - Include real-time updates if applicable",
            "# - Consider collaborative editing features",
            "# - Add debugging and logging capabilities"
        ]
        
        if not any(line.startswith('# Interactive Features:') for line in prompt.split('\n')):
            prompt += '\n\n' + '\n'.join(interactive_features)
        
        return prompt
    
    def _add_environment_setup(self, prompt: str) -> str:
        """Add environment setup and configuration."""
        env_setup = [
            "# Environment Setup:",
            "# - Configure for Replit's development environment",
            "# - Set up proper file structure for the platform",
            "# - Include configuration files (.replit, replit.nix)",
            "# - Add proper entry point configuration"
        ]
        
        if not any(line.startswith('# Environment Setup:') for line in prompt.split('\n')):
            prompt += '\n\n' + '\n'.join(env_setup)
        
        return prompt
    
    def _optimize_language(self, prompt: str) -> str:
        """Optimize language for Replit's understanding."""
        # Replace vague terms with specific ones
        replacements = {
            'web app': 'web application with proper routing, templates, and API endpoints',
            'website': 'responsive website with modern design and interactive features',
            'deploy': 'deploy to Replit with proper environment configuration',
            'host': 'host on Replit with automatic deployment and scaling'
        }
        
        for old, new in replacements.items():
            prompt = prompt.replace(old, new)
        
        return prompt
    
    def get_tool_name(self) -> str:
        return "Replit"
    
    def get_capabilities(self) -> Dict[str, Any]:
        return {
            'strengths': [
                'Web application development',
                'Built-in hosting and deployment',
                'Package and dependency management',
                'Interactive coding environment',
                'Collaborative development',
                'Multi-language support'
            ],
            'best_for': [
                'Web applications and websites',
                'Educational projects',
                'Prototyping and MVPs',
                'Collaborative coding',
                'Quick deployment'
            ],
            'limitations': [
                'Limited to web-based development',
                'Resource constraints on free tier',
                'May not support all advanced features'
            ],
            'optimization_focus': [
                'Web development frameworks',
                'Package management',
                'Deployment configuration',
                'Interactive features',
                'Environment setup'
            ]
        } 