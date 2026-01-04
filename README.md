# lilitodolist

一个使用 Flask + SQLAlchemy + MySQL 构建的待办事项（Todo List）示例应用，提供事项的新增、编辑、完成/撤销以及逻辑删除等功能，并通过简单的前端页面进行展示与交互。

## 代码架构
```
app.py                # 应用入口，初始化 Flask、数据库并注册蓝图
config/db_config.py   # MySQL 连接配置
controllers/          # 路由与业务逻辑
  └─ todo_controller.py
models/               # 数据模型定义
  └─ todo_model.py
views/templates/      # 前端模板与脚本
  └─ index.html
requirements.txt      # 依赖列表
```
- **app.py**：创建 Flask 应用，加载数据库配置，初始化 SQLAlchemy，并注册 `todo` 蓝图。在应用上下文中调用 `db.create_all()`，首次运行会自动根据模型创建表。
- **config/db_config.py**：集中管理数据库连接信息（主机、用户名、密码、端口、数据库名、字符集）。
- **models/todo_model.py**：定义 `TodoModel`，包含 `Title`、`Status`、`IsDelete`、`CreateTime` 等字段，并提供 `to_dict()` 方便模板渲染。
- **controllers/todo_controller.py**：定义蓝图路由，完成页面渲染、添加、状态更新、编辑和逻辑删除等操作。
- **views/templates/index.html**：简单表格页面，使用原生 JS 调用后端接口，实现列表展示、筛选、增删改查交互。

## 环境与配置
1. **Python**：建议 3.10+。
2. **数据库**：MySQL，需要提前创建数据库（默认名 `todo_db`）。表会在首次运行时自动创建。
3. **依赖安装**：位于 `requirements.txt`，包含 Flask、Flask-SQLAlchemy、PyMySQL。
4. **数据库配置**：修改 `config/db_config.py` 中的 `DB_CONFIG`，填入实际的 MySQL 连接信息（主机、用户名、密码、端口、数据库名、字符集）。

## 运行步骤
1. 准备虚拟环境（可选）：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows 使用 venv\Scripts\activate
   ```
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 确认并创建数据库：
   ```bash
   # 登录 MySQL 后创建数据库
   CREATE DATABASE todo_db DEFAULT CHARACTER SET utf8mb4;
   ```
4. 启动应用：
   ```bash
   python app.py
   ```
   服务器默认在 `http://127.0.0.1:5000/` 提供服务，首次启动会根据模型自动创建 `todolist` 表。

## 实现的功能
- **事项列表展示**：读取未删除 (`IsDelete=0`) 的记录，显示总数、已完成数、未完成数。
- **新增事项**：通过 `/add` 接口保存新 Todo。
- **状态更新**：`/update_status` 允许标记完成或撤销。
- **编辑标题**：`/edit` 更新事项名称。
- **逻辑删除**：`/delete` 将 `IsDelete` 置为 1，不直接物理删除。
- **前端筛选**：页面按钮可切换显示全部/已完成/未完成。

## 实现思路
- **MVC 组织**：使用 Flask 蓝图将路由与业务逻辑集中在 `controllers`，数据模型独立在 `models`，模板放在 `views`，入口负责装配。
- **数据库持久化**：利用 SQLAlchemy 定义模型并在应用启动时初始化，自动创建表，避免手写 SQL；通过会话提交变更。
- **接口与前端交互**：路由返回 JSON 状态码，前端使用 `fetch` 发送请求，成功后刷新页面以展示最新数据。
- **逻辑删除与统计**：保留数据可追溯性，通过过滤 `IsDelete=0` 展示，结合 `Status` 计算统计数字用于页面展示。

## 运行与部署提示
- 默认使用开发模式 (`debug=True`)，生产环境建议关闭调试并结合 WSGI 服务器（如 gunicorn）部署。
- 如需切换数据库或连接云端 MySQL，只需更新 `config/db_config.py`，无需改动业务代码。
- 可根据需要在 `TodoModel` 增加字段（如优先级、截止时间），并调整模板与路由即可扩展功能。
