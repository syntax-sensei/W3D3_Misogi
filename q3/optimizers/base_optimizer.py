from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseOptimizer(ABC):
    """
    Base class for all tool-specific prompt optimizers.
    Defines the interface that all optimizers must implement.
    """
    
    def __init__(self):
        self.explanation = []
        self.optimization_steps = []
    
    @abstractmethod
    def optimize(self, prompt: str, analysis: Dict[str, Any]) -> str:
        """
        Optimize a prompt for the specific tool.
        
        Args:
            prompt: The original prompt to optimize
            analysis: Analysis results from PromptAnalyzer
            
        Returns:
            The optimized prompt
        """
        pass
    
    def get_explanation(self) -> Dict[str, Any]:
        """
        Get explanation of the optimizations made.
        
        Returns:
            Dictionary containing optimization explanation
        """
        return {
            'steps': self.optimization_steps,
            'summary': self.explanation,
            'tool_name': self.get_tool_name(),
            'capabilities': self.get_capabilities()
        }
    
    @abstractmethod
    def get_tool_name(self) -> str:
        """Get the name of the tool this optimizer is designed for."""
        pass
    
    @abstractmethod
    def get_capabilities(self) -> Dict[str, Any]:
        """Get the capabilities and characteristics of the target tool."""
        pass
    
    def add_explanation(self, step: str, reason: str):
        """Add an explanation step for the optimization process."""
        self.optimization_steps.append({
            'step': step,
            'reason': reason
        })
    
    def add_summary(self, summary: str):
        """Add a summary explanation."""
        self.explanation.append(summary) 