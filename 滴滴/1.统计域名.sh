# 给定一个url文本的txt文档 统计不重复域名出现的次数
cat demo.txt | awk -F'(/)' '{print $3}' | uniq | wc -l