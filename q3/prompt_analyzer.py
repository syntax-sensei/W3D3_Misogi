from typing import Dict
import re

class PromptAnalyzer:
    """
    Analyzes a prompt for intent, complexity, requirements, and other features.
    """
    def analyze_prompt(self, prompt: str) -> Dict:
        analysis = {}
        prompt_lower = prompt.lower()
        # Intent
        if any(word in prompt_lower for word in ['function', 'method', 'def ']):
            analysis['intent'] = 'function_generation'
        elif any(word in prompt_lower for word in ['project', 'app', 'create', 'build']):
            analysis['intent'] = 'project_creation'
        elif 'review' in prompt_lower or 'refactor' in prompt_lower:
            analysis['intent'] = 'code_review'
        elif 'web' in prompt_lower or 'website' in prompt_lower:
            analysis['intent'] = 'web_development'
        elif 'cloud' in prompt_lower or 'aws' in prompt_lower:
            analysis['intent'] = 'cloud_development'
        elif 'infrastructure' in prompt_lower:
            analysis['intent'] = 'infrastructure'
        else:
            analysis['intent'] = 'general'
        # Complexity
        if len(prompt) > 300 or any(word in prompt_lower for word in ['complex', 'algorithm', 'architecture', 'system']):
            analysis['complexity'] = 'high'
        elif len(prompt) > 120 or any(word in prompt_lower for word in ['test', 'documentation', 'multiple', 'several']):
            analysis['complexity'] = 'medium'
        else:
            analysis['complexity'] = 'low'
        # Requirements
        analysis['has_context'] = any(word in prompt_lower for word in ['context', 'background', 'requirement'])
        analysis['has_examples'] = 'example' in prompt_lower
        analysis['has_testing'] = 'test' in prompt_lower
        analysis['has_documentation'] = 'documentation' in prompt_lower or 'readme' in prompt_lower
        analysis['has_dependencies'] = 'requirement' in prompt_lower or 'dependency' in prompt_lower or 'package' in prompt_lower
        analysis['has_aws_context'] = 'aws' in prompt_lower or 'cloudformation' in prompt_lower or 'lambda' in prompt_lower
        analysis['has_security'] = 'security' in prompt_lower or 'iam' in prompt_lower
        analysis['has_io_format'] = 'input:' in prompt_lower and 'output:' in prompt_lower
        analysis['has_requirements'] = 'requirement' in prompt_lower or 'constraint' in prompt_lower
        analysis['asks_for_explanation'] = 'explain' in prompt_lower or 'why' in prompt_lower
        analysis['asks_for_reasoning'] = 'reason' in prompt_lower or 'explain' in prompt_lower
        return analysis 