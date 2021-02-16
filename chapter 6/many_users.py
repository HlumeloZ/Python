users = {
'suchia': {
		'first' :'Sasuke',
		'last': 'Uchia',
		'rank': 'Jounin',
		},
'nuzumaki': {
		'first': 'Naruto',
		'last': 'Uzumazi',
		'rank': 'Hokage',
		},
}
for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	rank = user_info['rank']
	print(f"\tFull name: {full_name.title()}")
	print(f"\tRank: {rank.title()}")