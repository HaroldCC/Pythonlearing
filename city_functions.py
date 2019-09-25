def city_describe(city_name,city_country,population=0):
	"""接受城市名，国家名，返回完整的名字"""
	full_city_name = city_name+","+city_country
	if population:
		full_city_name += " - population "+str(population)
	return full_city_name.title()