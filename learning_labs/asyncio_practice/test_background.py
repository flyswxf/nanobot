import unittest
import asyncio
from todo_background import start_background_task, BACKGROUND_LOGS

class TestBackground(unittest.IsolatedAsyncioTestCase):
    async def test_fire_and_forget(self):
        """测试后台任务是否真的是后台运行"""
        BACKGROUND_LOGS.clear()
        
        # 启动后台任务
        # 如果 start_background_task 使用了 await log_writer()，这里会卡住2秒
        # 如果使用了 create_task，这里会瞬间完成
        import time
        start = time.time()
        await start_background_task()
        end = time.time()
        
        # 验证启动是非阻塞的
        self.assertLess(end - start, 0.1, "启动后台任务太慢了！一定要用 create_task，不要 await 它！")
        
        # 此时任务刚启动，日志应该是空的
        self.assertEqual(len(BACKGROUND_LOGS), 0, "主程序刚结束时，后台任务不应该已经完成")
        
        # 等待后台任务跑一会儿
        await asyncio.sleep(1.2)
        self.assertEqual(len(BACKGROUND_LOGS), 1, "1.2秒后应该有一条日志")
        
        await asyncio.sleep(1.2)
        self.assertEqual(len(BACKGROUND_LOGS), 2, "2.4秒后应该有两条日志")

if __name__ == '__main__':
    unittest.main()
