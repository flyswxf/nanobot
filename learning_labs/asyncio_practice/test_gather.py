import unittest
import asyncio
import time
from todo_gather import batch_download

class TestGather(unittest.IsolatedAsyncioTestCase):
    async def test_concurrency(self):
        """测试任务是否真的并发执行了"""
        start = time.time()
        # 3个任务，每个耗时1秒
        # 串行需要3秒，并行只需要1秒多一点
        tasks = [(1, 1.0), (2, 1.0), (3, 1.0)]
        results = await batch_download(tasks)
        end = time.time()
        
        duration = end - start
        
        # 验证结果正确性
        expected = ["image_1.jpg", "image_2.jpg", "image_3.jpg"]
        self.assertEqual(results, expected, "返回的结果列表不正确")
        
        # 验证并发性 (允许0.2秒的误差)
        self.assertLess(duration, 1.5, f"执行太慢了 ({duration:.2f}s)，看起来像是串行执行的！应该在1秒左右。")
        print(f"\n测试通过！3个1秒的任务总耗时: {duration:.2f}秒 (并发成功)")

if __name__ == '__main__':
    unittest.main()
