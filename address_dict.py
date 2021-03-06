# encoding=utf-8
# 分析地址所需的数据和字典资料


# 分析后格式
parsed_format = {
	'区':'',
	'街道':'',
	'小区':'',
	'楼号': '',
	'单元': '',
	'门牌':'',
	'~街道和小区':'',
	'~单元和门牌':''
	}

# 城市
cities = [
	"北京"
]

# 区
districts = [
	"东城",
	"西城",
	"崇文",
	"宣武",
	"朝阳",
	"丰台",
	"石景山",
	"海淀",
	"门头沟",
	"房山",
	"通州",
	"顺义",
	"昌平",
	"大兴",
	"怀柔",
	"平谷",
	"密云",
	"延庆"
]

# 旧区-新区 转换
deprecated_districts = [
	("崇文","东城"),
	("宣武","西城")
]

# 楼号终止词,如果一词由另一词加前缀构成,应位于较前方
building_stopwords = [
	"号楼",
	"楼",
	"座"
]

# 街道终止词
street_stopwords = [
	"大街",
	"街道",
	"街",
	"路",
	"道"
]
