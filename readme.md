# 项目说明

前端
- 使用 Vue 开发
- 由于环境不一致，可能导致启动问题
- dist 文件夹下提供了打包结果，可使用任意 Web 服务浏览

后端
- 接口采用 Basic Auth 验证
- 验证命令示例：
curl -u test:123456 http://localhost:8080/hello
curl -X POST "http://localhost:8080/login" -d "username=test&password=123456"

爬虫
- 仅使用 Playwright
- DrissionPage 文档较少，短时间内部分问题无法解决
- 出于时间和防爬考虑，仅抓取 20 页
- 文章主体部分文字和图片按原始顺序记录，并使用特殊标记区分段落和图片
- 数据最终存储于 mit_admissions_details.csv

数据映射
- !#@p!#@：表示段落结束
- !#@img[图片备注]!#@：表示图片在文章中的位置，并记录图片 URL

CSV 字段说明
- Title：文章标题
- Subtitle：副标题
- Author：作者
- Time：发布时间
- Content：文章正文，段落和图片按顺序记录
- Images In Article：文章中图片 URL 列表
