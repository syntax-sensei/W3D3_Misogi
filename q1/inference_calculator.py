def estimate_latency(model_size_b, tokens, batch_size, hardware_type):
    base_latency = {
        "cpu": 15,
        "gpu": 5,
        "a100": 2,
        "tpu": 2
    }

    latency = base_latency.get(hardware_type.lower(), 10)
    latency += (model_size_b / 7) * 1.5  # Heavier models → more latency
    latency += (batch_size * tokens) / 1000  # Basic estimate
    return round(latency, 2)

def estimate_memory_usage(model_size_b, batch_size):
    return round(model_size_b * 2 + batch_size * 0.5, 2)  # in GB

def estimate_cost(model_size_b, tokens, hardware_type):
    cost_per_sec = {
        "cpu": 0.001,
        "gpu": 0.01,
        "a100": 0.12,
        "tpu": 0.10
    }

    latency = estimate_latency(model_size_b, tokens, 1, hardware_type)
    cost = latency * cost_per_sec.get(hardware_type.lower(), 0.02)
    return round(cost, 4)

def is_compatible(memory_usage, hardware_type):
    limits = {
        "cpu": 32,
        "gpu": 24,
        "a100": 80,
        "tpu": 64
    }
    return memory_usage <= limits.get(hardware_type.lower(), 16)

def calculate(model_size_b, tokens, batch_size, hardware_type, deployment_mode="local"):
    latency = estimate_latency(model_size_b, tokens, batch_size, hardware_type)
    memory = estimate_memory_usage(model_size_b, batch_size)
    cost = estimate_cost(model_size_b, tokens, hardware_type)
    compatible = is_compatible(memory, hardware_type)

    return {
        "Latency (ms)": latency,
        "Memory Usage (GB)": memory,
        "Cost per request ($)": cost,
        "Hardware Compatible": compatible
    }
