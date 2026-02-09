import asyncio
import time

async def download_image(image_id: int, duration: float) -> str:
    """模拟下载图片的异步任务"""
    print(f"开始下载图片 {image_id}...")
    await asyncio.sleep(duration)
    print(f"图片 {image_id} 下载完成！")
    return f"image_{image_id}.jpg"

async def batch_download(tasks_config: list[tuple[int, float]]) -> list[str]:
    """
    TODO: 使用 asyncio.gather 并发执行下载任务
    
    参数:
        tasks_config: 包含 (image_id, duration) 的列表
    返回:
        下载结果的文件名列表，顺序必须与 tasks_config 一致
    """
    # 1. 创建任务列表
    # 提示：使用 download_image(id, duration) 创建 coroutines
    coroutines = []
    
    # YOUR CODE HERE
    for id,duration in tasks_config:
        coroutines.append(download_image(id,duration))
    
    # 2. 并发执行并等待结果
    # 提示：使用 await asyncio.gather(...)
    results = []
    
    # YOUR CODE HERE
    results = await asyncio.gather(*coroutines)
    
    return results

if __name__ == "__main__":
    # 手动测试
    async def main():
        start = time.time()
        # 任务1耗时2秒，任务2耗时1秒，任务3耗时3秒
        # 如果是串行，总耗时应该是 2+1+3=6秒
        # 如果是并行，总耗时应该是 max(2,1,3)=3秒
        tasks = [(1, 2.0), (2, 1.0), (3, 3.0)]
        results = await batch_download(tasks)
        end = time.time()
        
        print(f"结果: {results}")
        print(f"总耗时: {end - start:.2f}秒")
        
    asyncio.run(main())
