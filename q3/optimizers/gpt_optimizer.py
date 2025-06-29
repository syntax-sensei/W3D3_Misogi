from .base_optimizer import BaseOptimizer
from typing import Dict, Any

class GPTOptimizer(BaseOptimizer):
    """
    Optimizer for GPT-4 (OpenAI) prompts.
    GPT-4 works best with:
    - Clear, concise instructions
    - Explicit input/output format
    - Examples and edge cases
    - Requests for reasoning or explanations
    """
    def optimize(self, prompt: str, analysis: Dict[str, Any]) -> str:
        optimized_prompt = prompt
        self.explanation = []
        self.optimization_steps = []
        # Add input/output format
        if not analysis.get('has_io_format', False):
            optimized_prompt = self._add_io_format(optimized_prompt)
            self.add_explanation(
                "Added input/output format",
                "GPT-4 performs best with explicit input/output format instructions"
            )
        # Add examples
        if not analysis.get('has_examples', False):
            optimized_prompt = self._add_examples(optimized_prompt)
            self.add_explanation(
                "Added examples",
                "Examples help GPT-4 understand the expected behavior and edge cases"
            )
        # Add request for reasoning
        if not analysis.get('asks_for_reasoning', False):
            optimized_prompt = self._add_reasoning_request(optimized_prompt)
            self.add_explanation(
                "Added request for reasoning",
                "GPT-4 can provide reasoning and explanations for its answers"
            )
        self.add_summary(f"Optimized prompt for GPT-4 with {len(self.optimization_steps)} improvements")
        return optimized_prompt
    def _add_io_format(self, prompt: str) -> str:
        if 'input:' not in prompt.lower() and 'output:' not in prompt.lower():
            prompt += "\n\n# Specify the input and output format explicitly."
        return prompt
    def _add_examples(self, prompt: str) -> str:
        if 'example' not in prompt.lower():
            prompt += "\n\n# Provide at least one example input and output."
        return prompt
    def _add_reasoning_request(self, prompt: str) -> str:
        if 'reason' not in prompt.lower() and 'explain' not in prompt.lower():
            prompt += "\n\n# After solving, explain your reasoning."
        return prompt
    def get_tool_name(self) -> str:
        return "GPT-4 (OpenAI)"
    def get_capabilities(self) -> Dict[str, Any]:
        return {
            'strengths': [
                'General-purpose reasoning',
                'Flexible input/output',
                'Example-driven learning',
                'Natural language understanding',
                'Code generation and review'
            ],
            'best_for': [
                'General code generation',
                'Complex reasoning',
                'Explanatory answers',
                'Example-driven tasks'
            ],
            'limitations': [
                'May require explicit format for best results',
                'Can be verbose or over-explain'
            ],
            'optimization_focus': [
                'Explicit input/output format',
                'Examples',
                'Reasoning and explanations'
            ]
        } 