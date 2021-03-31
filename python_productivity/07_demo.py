from pathlib import PurePath, Path

filename = "e.txt"

# __file__，来取得当前脚本所在的路径。
# .parent：取得当前脚本所在的路径
current_path = PurePath(__file__).parent
file = current_path.joinpath(filename)

p = Path(current_path)
files = [x for x in p.iterdir() if PurePath(x).match('*.txt')]
for file in files:
    with open(file, encoding="utf-8") as f:
        content = f.read()
        words = content.strip()
        nums = len(words)
        print(nums)