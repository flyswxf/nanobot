import asyncio

async def slow_api_call(duration: float) -> str:
    """模拟一个慢速的 API 调用"""
    await asyncio.sleep(duration)
    return "success"

async def fetch_with_timeout(duration: float, timeout: float) -> str:
    """
    TODO: 使用 asyncio.wait_for 实现超时控制
    
    参数:
        duration: 任务实际需要的时间
        timeout: 允许的最大等待时间
    返回:
        如果成功: 返回 "success"
        如果超时: 捕获 TimeoutError 并返回 "timeout_error"
    """
    try:
        # YOUR CODE HERE
        # 提示：result = await asyncio.wait_for(...)
        result = await asyncio.wait_for(slow_api_call(duration),timeout)
    except asyncio.TimeoutError:
        # YOUR CODE HERE
        return "timeout_error"
    
    return "success"

if __name__ == "__main__":
    async def main():
        # 测试1: 任务快，不超时
        res1 = await fetch_with_timeout(1.0, 2.0)
        print(f"任务(1s) 限时(2s) -> {res1}")  # 应该输出 success
        
        # 测试2: 任务慢，超时
        res2 = await fetch_with_timeout(3.0, 2.0)
        print(f"任务(3s) 限时(2s) -> {res2}")  # 应该输出 timeout_error

    asyncio.run(main())
