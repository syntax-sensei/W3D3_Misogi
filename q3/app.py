from flask import Flask, render_template, request, jsonify
import json
import os
from optimizers.base_optimizer import BaseOptimizer
from optimizers.copilot_optimizer import CopilotOptimizer
from optimizers.cursor_optimizer import CursorOptimizer
from optimizers.replit_optimizer import ReplitOptimizer
from optimizers.codewhisperer_optimizer import CodeWhispererOptimizer
from optimizers.claude_optimizer import ClaudeOptimizer
from optimizers.gpt_optimizer import GPTOptimizer
from prompt_analyzer import PromptAnalyzer

app = Flask(__name__)

# Initialize optimizers
optimizers = {
    'copilot': CopilotOptimizer(),
    'cursor': CursorOptimizer(),
    'replit': ReplitOptimizer(),
    'codewhisperer': CodeWhispererOptimizer(),
    'claude': ClaudeOptimizer(),
    'gpt': GPTOptimizer()
}

# Initialize prompt analyzer
analyzer = PromptAnalyzer()

# Load tool analysis data
def load_tool_analysis():
    try:
        with open('tool_analysis.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

tool_analysis = load_tool_analysis()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/optimize', methods=['POST'])
def optimize_prompt():
    try:
        data = request.get_json()
        base_prompt = data.get('prompt', '')
        target_tool = data.get('tool', '')
        
        if not base_prompt or not target_tool:
            return jsonify({'error': 'Missing prompt or tool selection'}), 400
        
        if target_tool not in optimizers:
            return jsonify({'error': 'Unsupported tool selected'}), 400
        
        # Analyze the base prompt
        analysis = analyzer.analyze_prompt(base_prompt)
        
        # Optimize the prompt for the selected tool
        optimizer = optimizers[target_tool]
        optimized_prompt = optimizer.optimize(base_prompt, analysis)
        
        # Get optimization explanation
        explanation = optimizer.get_explanation()
        
        return jsonify({
            'original_prompt': base_prompt,
            'optimized_prompt': optimized_prompt,
            'analysis': analysis,
            'explanation': explanation,
            'tool': target_tool
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tools')
def get_tools():
    tools = [
        {
            'id': 'copilot',
            'name': 'GitHub Copilot',
            'description': 'AI pair programmer for code completion and generation',
            'icon': '🤖'
        },
        {
            'id': 'cursor',
            'name': 'Cursor',
            'description': 'AI-first code editor with advanced code generation',
            'icon': '📝'
        },
        {
            'id': 'replit',
            'name': 'Replit',
            'description': 'Online IDE with AI-powered code assistance',
            'icon': '🌐'
        },
        {
            'id': 'codewhisperer',
            'name': 'Amazon CodeWhisperer',
            'description': 'AI-powered code generator for AWS development',
            'icon': '☁️'
        },
        {
            'id': 'claude',
            'name': 'Claude (Anthropic)',
            'description': 'Advanced AI assistant for coding and analysis',
            'icon': '🧠'
        },
        {
            'id': 'gpt',
            'name': 'GPT-4 (OpenAI)',
            'description': 'Large language model for code generation and review',
            'icon': '⚡'
        }
    ]
    return jsonify(tools)

@app.route('/tool_details')
def get_tool_details():
    """Return detailed tool information from tool_analysis.json"""
    return jsonify(tool_analysis)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 