import unittest
import asyncio
from todo_timeout import fetch_with_timeout

class TestTimeout(unittest.IsolatedAsyncioTestCase):
    async def test_success(self):
        """测试在时间内完成的情况"""
        result = await fetch_with_timeout(0.5, 1.0)
        self.assertEqual(result, "success")

    async def test_failure(self):
        """测试超时的情况"""
        result = await fetch_with_timeout(1.5, 0.5)
        self.assertEqual(result, "timeout_error", "超时应该返回 'timeout_error'")

if __name__ == '__main__':
    unittest.main()
