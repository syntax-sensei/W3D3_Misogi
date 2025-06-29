# 🧠 LLM Inference Research Notes

## 🧩 Inference Basics

- **Latency**: Time taken for model to respond to input.
- **Memory**: Total RAM/VRAM needed to load the model + run inference.
- **Cost**: Combination of hardware cost + time per inference.

## 🔍 Model Comparisons

| Model    | Parameters | Memory (fp16) | Tokens/sec (A100) | Typical Latency | 
|----------|------------|---------------|-------------------|-----------------|
| LLaMA 7B | 7B         | ~14 GB        | ~70-100 tok/s     | ~50-100 ms      |
| LLaMA 13B| 13B        | ~26 GB        | ~50-70 tok/s      | ~100-150 ms     |
| GPT-4    | ???        | API-only      | N/A               | 1-5 sec (API)   |

## 🖥️ Hardware Types

- **CPU** (slow, low cost)
- **GPU (A100, RTX 3090, etc.)**
- **TPU / Cloud-hosted APIs**

