#密碼程式設計
#設定密碼為password = 'wces6313'
#最多輸入3次
#不對的話，就印出"密碼錯誤!還有__次機會"
#對的話就印出 成功登入

password = 'wces6313'
i=3
while True:
	pwd = input('請輸入密碼:(最多三次機會)')
	if pwd == password:
		print('登入成功')
		break 
	else:
		i= i - 1
		print('密碼錯誤,還有',i,'次機會' )
		if i== 0:
			break
					