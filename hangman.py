def hangman(word):
	"""
	This is python test.
	My first GitHub.
		
	"""
	wrong = 0
	stages = ["",
                  "___________         ",
                  "|          |        ",
                  "|          |        ",
                  "|          O        ",
                  "|         /|＼      ",
                  "|         / ＼      ",
                  "|                   ",
                  ]
	rletters = list(word)
	board = ["_"] * len(word)
	win = False
	print("ハングマンへようこそ!")
	while wrong <len(stages) - 1:
		print("\n")
		msg = "1文字予想してね"
		char = input(msg)
		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters[cind] = '$'
		else:
			wrong += 1
		print(" ".join(board))
		e = wrong + 1
		print("\n".join(stages[0:e]))
		if "_" not in board:
			print("あなたの勝ち！")
			print(" ".join(board))
			win = True
			break
	if not win:
		print("\n".join(stages[0:wrong+1]))
		print("あなたの負けです！正解は{}です".format(word))

ans = ["red","white","black","blue","yellow","gold","pink"]
import random
a = random.randint(0,6)
hangman(ans[a])
