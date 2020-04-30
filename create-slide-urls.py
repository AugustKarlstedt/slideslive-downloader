
slide_count = 1102

with open('slide-urls.txt', 'w+') as f:
	for i in range(1, slide_count+1):
		filename = f"0-{str(i).zfill(4)}.jpg"
		url = f"https://d2ygwrecguqg66.cloudfront.net/data/presentations/38926829/slides/big/{filename}"
		f.write(url)
		f.write('\n')
