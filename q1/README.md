# 🤖 LLM Inference Calculator

Estimate the **latency, memory usage, and cost** of running LLM inference across different model sizes and hardware.

---

## ✅ Features

- Supports any model size (e.g., 7B, 13B, GPT-4)
- Compare deployment options (CPU, GPU, A100, TPU)
- Estimate memory needs and hardware compatibility
- Run scenario simulations

---

## 📥 Inputs

- `model_size_b`: Model size in billions (e.g., 7, 13)
- `tokens`: Number of tokens in a request
- `batch_size`: Number of requests processed together
- `hardware_type`: One of ["cpu", "gpu", "a100", "tpu"]
- `deployment_mode`: "local" or "api" (optional)

## 📤 Outputs

- `Latency (ms)`
- `Memory Usage (GB)`
- `Cost per request ($)`
- `Hardware Compatible (True/False)`

---

## 🚀 Usage Example

```python
from inference_calculator import calculate

result = calculate(model_size_b=13, tokens=256, batch_size=2, hardware_type="a100")
print(result)
