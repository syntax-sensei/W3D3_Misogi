from .base_optimizer import BaseOptimizer
from typing import Dict, Any

class ClaudeOptimizer(BaseOptimizer):
    """
    Optimizer for Claude (Anthropic) prompts.
    Claude works best with:
    - Detailed, step-by-step reasoning
    - Explicit requirements and constraints
    - Requests for explanations and justifications
    - Multi-step problem solving
    """
    def optimize(self, prompt: str, analysis: Dict[str, Any]) -> str:
        optimized_prompt = prompt
        self.explanation = []
        self.optimization_steps = []
        # Add step-by-step reasoning guidance
        if analysis.get('complexity') in ['medium', 'high']:
            optimized_prompt = self._add_step_by_step_guidance(optimized_prompt)
            self.add_explanation(
                "Added step-by-step reasoning guidance",
                "Claude excels at multi-step, explicit reasoning and explanations"
            )
        # Add explicit requirements
        if not analysis.get('has_requirements', False):
            optimized_prompt = self._add_explicit_requirements(optimized_prompt)
            self.add_explanation(
                "Added explicit requirements",
                "Claude benefits from clear, explicit requirements and constraints"
            )
        # Add request for explanations
        if not analysis.get('asks_for_explanation', False):
            optimized_prompt = self._add_explanation_request(optimized_prompt)
            self.add_explanation(
                "Added request for explanations",
                "Claude can provide detailed explanations and justifications for its answers"
            )
        self.add_summary(f"Optimized prompt for Claude with {len(self.optimization_steps)} improvements")
        return optimized_prompt
    def _add_step_by_step_guidance(self, prompt: str) -> str:
        if 'step-by-step' not in prompt.lower():
            prompt += "\n\n# Please solve this problem step-by-step and explain your reasoning at each stage."
        return prompt
    def _add_explicit_requirements(self, prompt: str) -> str:
        if 'requirements' not in prompt.lower() and 'constraints' not in prompt.lower():
            prompt += "\n\n# List all requirements and constraints explicitly before starting."
        return prompt
    def _add_explanation_request(self, prompt: str) -> str:
        if 'explain' not in prompt.lower():
            prompt += "\n\n# After solving, explain why this solution is correct and optimal."
        return prompt
    def get_tool_name(self) -> str:
        return "Claude (Anthropic)"
    def get_capabilities(self) -> Dict[str, Any]:
        return {
            'strengths': [
                'Step-by-step reasoning',
                'Detailed explanations',
                'Multi-step problem solving',
                'Explicit constraint handling',
                'Natural language understanding'
            ],
            'best_for': [
                'Complex problem solving',
                'Explanatory answers',
                'Multi-step tasks',
                'Constraint satisfaction problems'
            ],
            'limitations': [
                'May be verbose',
                'Requires explicit instructions for best results'
            ],
            'optimization_focus': [
                'Step-by-step reasoning',
                'Explicit requirements',
                'Explanations and justifications'
            ]
        } 