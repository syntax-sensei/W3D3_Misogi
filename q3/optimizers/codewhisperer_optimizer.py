from .base_optimizer import BaseOptimizer
from typing import Dict, Any
import re

class CodeWhispererOptimizer(BaseOptimizer):
    """
    Optimizer for Amazon CodeWhisperer prompts.
    CodeWhisperer works best with:
    - AWS services and integrations
    - Security-focused development
    - Cloud-native applications
    - AWS best practices
    - Infrastructure as Code
    """
    
    def optimize(self, prompt: str, analysis: Dict[str, Any]) -> str:
        optimized_prompt = prompt
        
        # Reset explanations for new optimization
        self.explanation = []
        self.optimization_steps = []
        
        # Add AWS context
        if analysis.get('has_aws_context', False) == False:
            optimized_prompt = self._add_aws_context(optimized_prompt)
            self.add_explanation(
                "Added AWS context",
                "CodeWhisperer excels at AWS service integrations and cloud-native development"
            )
        
        # Add security considerations
        if analysis.get('has_security', False) == False:
            optimized_prompt = self._add_security_guidance(optimized_prompt)
            self.add_explanation(
                "Added security guidance",
                "CodeWhisperer includes security best practices and AWS security patterns"
            )
        
        # Add cloud-native patterns
        if analysis.get('intent') == 'cloud_development':
            optimized_prompt = self._add_cloud_native_patterns(optimized_prompt)
            self.add_explanation(
                "Added cloud-native patterns",
                "CodeWhisperer can suggest optimal cloud architecture and patterns"
            )
        
        # Add AWS service integrations
        if analysis.get('complexity') in ['medium', 'high']:
            optimized_prompt = self._add_aws_service_integrations(optimized_prompt)
            self.add_explanation(
                "Added AWS service integrations",
                "CodeWhisperer can suggest appropriate AWS services and integration patterns"
            )
        
        # Add infrastructure considerations
        if analysis.get('intent') == 'infrastructure':
            optimized_prompt = self._add_infrastructure_guidance(optimized_prompt)
            self.add_explanation(
                "Added infrastructure guidance",
                "CodeWhisperer can help with Infrastructure as Code and AWS resource management"
            )
        
        # Optimize language for CodeWhisperer
        optimized_prompt = self._optimize_language(optimized_prompt)
        self.add_explanation(
            "Optimized language",
            "Used CodeWhisperer-specific language patterns for better understanding"
        )
        
        self.add_summary(f"Optimized prompt for Amazon CodeWhisperer with {len(self.optimization_steps)} improvements")
        
        return optimized_prompt
    
    def _add_aws_context(self, prompt: str) -> str:
        """Add AWS-specific context and considerations."""
        aws_context = [
            "# AWS Context:",
            "# - Use AWS SDKs and best practices",
            "# - Consider AWS service integrations",
            "# - Follow AWS security and compliance guidelines",
            "# - Use AWS-native patterns and architectures",
            "# - Consider cost optimization and resource management"
        ]
        
        if not any(line.startswith('# AWS Context:') for line in prompt.split('\n')):
            prompt = '\n'.join(aws_context) + '\n\n' + prompt
        
        return prompt
    
    def _add_security_guidance(self, prompt: str) -> str:
        """Add security-focused guidance."""
        security_guidance = [
            "# Security Considerations:",
            "# - Implement proper authentication and authorization",
            "# - Use AWS IAM roles and policies",
            "# - Follow the principle of least privilege",
            "# - Implement secure coding practices",
            "# - Use AWS security services (WAF, Shield, etc.)",
            "# - Encrypt data at rest and in transit"
        ]
        
        if 'security' not in prompt.lower():
            prompt += '\n\n' + '\n'.join(security_guidance)
        
        return prompt
    
    def _add_cloud_native_patterns(self, prompt: str) -> str:
        """Add cloud-native development patterns."""
        cloud_patterns = [
            "# Cloud-Native Patterns:",
            "# - Use serverless architectures where appropriate",
            "# - Implement microservices patterns",
            "# - Use event-driven architectures",
            "# - Consider auto-scaling and load balancing",
            "# - Implement proper monitoring and logging",
            "# - Use managed services over self-hosted solutions"
        ]
        
        if not any(line.startswith('# Cloud-Native Patterns:') for line in prompt.split('\n')):
            prompt += '\n\n' + '\n'.join(cloud_patterns)
        
        return prompt
    
    def _add_aws_service_integrations(self, prompt: str) -> str:
        """Add AWS service integration suggestions."""
        service_integrations = [
            "# AWS Service Integrations:",
            "# - Consider appropriate AWS services for your use case",
            "# - Use Lambda for serverless functions",
            "# - Use S3 for object storage",
            "# - Use DynamoDB for NoSQL databases",
            "# - Use API Gateway for REST APIs",
            "# - Use CloudFormation or CDK for infrastructure"
        ]
        
        if not any(line.startswith('# AWS Service Integrations:') for line in prompt.split('\n')):
            prompt += '\n\n' + '\n'.join(service_integrations)
        
        return prompt
    
    def _add_infrastructure_guidance(self, prompt: str) -> str:
        """Add infrastructure and deployment guidance."""
        infra_guidance = [
            "# Infrastructure Considerations:",
            "# - Use Infrastructure as Code (CloudFormation, CDK, Terraform)",
            "# - Implement proper CI/CD pipelines",
            "# - Use AWS CodePipeline or GitHub Actions",
            "# - Consider multi-region deployment",
            "# - Implement proper backup and disaster recovery",
            "# - Use AWS CloudWatch for monitoring"
        ]
        
        if not any(line.startswith('# Infrastructure Considerations:') for line in prompt.split('\n')):
            prompt += '\n\n' + '\n'.join(infra_guidance)
        
        return prompt
    
    def _optimize_language(self, prompt: str) -> str:
        """Optimize language for CodeWhisperer's understanding."""
        # Replace vague terms with AWS-specific ones
        replacements = {
            'database': 'AWS RDS or DynamoDB depending on requirements',
            'storage': 'AWS S3 for object storage',
            'compute': 'AWS Lambda for serverless or EC2 for traditional',
            'api': 'AWS API Gateway with Lambda or ECS',
            'deploy': 'deploy using AWS CodePipeline or AWS CLI',
            'monitor': 'use AWS CloudWatch for monitoring and logging'
        }
        
        for old, new in replacements.items():
            prompt = prompt.replace(old, new)
        
        return prompt
    
    def get_tool_name(self) -> str:
        return "Amazon CodeWhisperer"
    
    def get_capabilities(self) -> Dict[str, Any]:
        return {
            'strengths': [
                'AWS service integrations',
                'Security-focused development',
                'Cloud-native patterns',
                'AWS best practices',
                'Infrastructure as Code',
                'Cost optimization'
            ],
            'best_for': [
                'AWS application development',
                'Cloud-native applications',
                'Security-critical applications',
                'Infrastructure automation',
                'AWS service integration'
            ],
            'limitations': [
                'Primarily focused on AWS ecosystem',
                'May not be optimal for non-AWS development',
                'Requires AWS knowledge for best results'
            ],
            'optimization_focus': [
                'AWS service selection',
                'Security best practices',
                'Cloud-native patterns',
                'Infrastructure as Code',
                'Cost optimization strategies'
            ]
        } 