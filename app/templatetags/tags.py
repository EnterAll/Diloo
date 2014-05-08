from django import template
import re
register = template.Library()
from django.utils.encoding import smart_str, smart_unicode


@register.filter(name='topictag')
def topictag(content):
	#prevent possible XSS attack
	result_content  = content.replace('<', '&lt;')
	result_content  = result_content.replace('>', '&gt;')

	topic_tags = re.split(r'(=[A-Za-z0-9_\x80-\xff]+)',result_content)

	res = ''
	#each detected tag convert to HTML
	for i in topic_tags:
		if i != u'':
			if i[0] == u'=':
				res = res + "<a href=\"tag?search="+i[1:]+"\">"+i+"</a>"
			else:
				res = res + i 
		else:
			res = res + i 
	return smart_str(res)
