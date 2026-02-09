import asyncio
import time

# 全局变量，用来记录后台任务的状态
BACKGROUND_LOGS = []

async def log_writer():
    """模拟一个后台日志写入任务"""
    print("后台任务启动...")
    await asyncio.sleep(1)
    BACKGROUND_LOGS.append("log_entry_1")
    print("后台任务写入第一条...")
    await asyncio.sleep(1)
    BACKGROUND_LOGS.append("log_entry_2")
    print("后台任务写入第二条...")

async def start_background_task():
    """
    TODO: 使用 asyncio.create_task 启动后台任务
    
    注意：这个函数本身应该立即返回，不应该等待 log_writer 执行完毕
    """
    # YOUR CODE HERE
    # 提示：task = asyncio.create_task(...)
    # 为了防止 task 被垃圾回收，你可能需要把它赋值给一个变量并返回，或者只是启动它
    task = asyncio.create_task(log_writer())
    return task

async def main_logic():
    print("主程序开始")
    
    # 启动后台任务
    # TODO: 调用上面的函数
    await start_background_task()
    
    print("主程序继续执行，不等待后台任务...")
    # 这里模拟主程序做了一些很快的事情
    await asyncio.sleep(0.5)
    
    return "main_done"

if __name__ == "__main__":
    async def main():
        # 清空日志
        BACKGROUND_LOGS.clear()
        
        # 运行主逻辑
        result = await main_logic()
        print(f"主程序结果: {result}")
        
        # 此时后台任务应该还在运行，BACKGROUND_LOGS 应该是空的
        print(f"当前日志 (主程序结束时): {BACKGROUND_LOGS}")
        
        # 等待一会儿让后台任务跑完（仅为了观察）
        print("等待后台任务完成...")
        await asyncio.sleep(3)
        print(f"最终日志: {BACKGROUND_LOGS}")

    asyncio.run(main())
