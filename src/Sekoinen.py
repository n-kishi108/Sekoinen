import itertools
#入力セクション
def input_sec():
	li = []
	val = "1"
	print("食費を入力してください。0または負数が入力された場合、それ以前のデータで計算を行います。")
	while int(val) > 0:
		val = input()
		if val.isdigit():
			if val is None or int(val) > 0:
				li.append(int(val))

	print("支給上限額を入力してください。")
	val = input()
	if val.isdigit():
		cost = int(val)
	return li, cost
#ここのメソッド計算し直す
##2進数をint配列にし、各桁の値と入力された値の総和を算出
###総和が5000円未満で最大なら最大値を更新
###その組み合わせはlistとして
###5000円を超えていたり組み合わせが最大値でなければcontinue
#最終的にその金額になる組み合わせの配列を出力
def do_calc(li, cost):
	m = 0
	se = ()
	for el in range(0, len(li) + 1):
		for subset in itertools.permutations(li, el):
			s = sum(subset)
			if s <= cost:
				if s > m:
					m = s
					se = subset
	return m, se

def main():
	li, cost  = input_sec()
	m, se = do_calc(li, cost)
	print("支給額：" + str(cost))
	print("支給額内で最も得する組み合わせ：", end="")
	print(se)
	print("合計金額：", end="")
	print(str(m) + "円")

if __name__ == "__main__":
	main()
