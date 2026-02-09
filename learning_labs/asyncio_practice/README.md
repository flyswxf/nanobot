# Asyncio 实战练习指南

欢迎来到 Asyncio 实验室！在这里，我们将通过 3 个具体的练习，亲手实现 nanobot 中用到的核心异步模式。

## 练习说明
每个练习都包含一个 `todo_*.py` 文件和一个 `test_*.py` 文件。你的任务是补全 `todo_*.py` 中的代码，使其通过测试。

### Lab 1: 并发下载 (asyncio.gather)
模拟 nanobot 启动时同时初始化多个服务的场景。你需要实现一个并发下载器。
- **目标**: 补全 `todo_gather.py`
- **验证**: 运行 `python learning_labs/asyncio_practice/test_gather.py`

### Lab 2: 永不卡死的请求 (asyncio.wait_for)
模拟 nanobot 等待消息时的超时机制。你需要给一个慢速任务加上超时控制。
- **目标**: 补全 `todo_timeout.py`
- **验证**: 运行 `python learning_labs/asyncio_practice/test_timeout.py`

### Lab 3: 真正的后台任务 (create_task)
模拟 nanobot 的心跳或日志系统。你需要启动一个后台任务，确保它不阻塞主线程。
- **目标**: 补全 `todo_background.py`
- **验证**: 运行 `python learning_labs/asyncio_practice/test_background.py`

## 开始练习
请按照 Lab 1 -> Lab 2 -> Lab 3 的顺序进行。
准备好了吗？让我们开始吧！
