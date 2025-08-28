前端采用vue，由于环境不一致可能会导致的启动问题，相应dist文件夹下提供打包结果代码，可以使用任意web服务浏览

后端接口采用了basic auth验证使用如下命令可验证
curl -u test:123456 http://localhost:8080/hello 
curl -X POST "http://localhost:8080/login" -d "username=test&password=123456"

爬虫部分，只使用了playwright，drisspage的文档过少短时间部分问题无法解决。由于时间与可能的防爬措施，暂时只爬取20页。
对于文章主体部分，文字和图片都按原始顺序记录，并用特殊标记区分段落和图片，最终数据存储于mit_admissions_details.csv中
映射关系如下
!#@p!#@：表示一个段落结束
!#@img[图片备注]!#@：表示图片在文章中的位置，并记录图片 URL
