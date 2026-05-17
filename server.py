import psutil
from mcp.server.fastmcp import FastMCP

# 1. Initialize FastMCP server
mcp = FastMCP("python-utility-server")

# 2. Tool 1: Mathematical computation (Fibonacci Sequence)
@mcp.tool()
def generate_fibonacci(n: int) -> list[int]:
    """
    Generates a Fibonacci sequence up to N terms.

    Args:
        n: The number of terms to generate. Must be a positive integer.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# 3. Tool 2: Local System Inspection
@mcp.tool()
def get_system_metrics() -> dict:
    """
    Retrieves current local system resource metrics including CPU and RAM usage.
    """
    cpu_usage = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory()

    return {
        "cpu_utilization_percent": cpu_usage,
        "ram_total_gb": round(memory.total / (1024 ** 3), 2),
        "ram_available_gb": round(memory.available / (1024 ** 3), 2),
        "ram_used_percent": memory.percent
    }

if __name__ == "__main__":
    # 4. Run the server on stdio
    mcp.run(transport="stdio")
