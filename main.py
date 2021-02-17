import requests
import sys, os
from tqdm import tqdm
from time import sleep
os.system('clear')
new_url = "https://nuubi.herokuapp.com"

def tik(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		sleep(10. / 100)
print ('')
nama = input('What is your Name: ')
print('-'*26)
tik ('Welcome: '+nama)
sleep(3)
os.system('clear')

top = '[!]'
logo = ('''
    +-----------------------+
    |  YOUTUBE | DOWNLOADER |
    +-----------------------+ ''')

def main():
	try:
		print ('')
		print ('------------------')
		print ('[+] MENU:         ')
		print ('------------------')
		print ('[1] Youtube DL    ')
		print ('[2] y2mate        ')
		print ('[0] Exit          ')
		print ('------------------')
	except:
		pass

def youtube_1():
	try:
		os.system('clear')
		print ('')
		print (logo)
		print ('')
		print ('[?] Please Insert a valid Video URL: ')
		url = input ('=>: ')
		os.system('clear')
		print ('')
		print (logo)
		print ('')
		print ('------------------')
		print ('[+] MENU:         ')
		print ('------------------')
		print ('[1] Download MP3  ')
		print ('[2] Download MP4  ')
		print ('------------------')
		print ('[+] Enter Number: ')
		download = input('=>: ')
		print ()
		tik ('[?] Download in process')
		def mp3():
			os.system('youtube-dl --extract-audio --audio-format mp3 {0} -o /Downloader/Audio/%(title)s.%(ext)s'.format(url))
			print ('-'*30)
			tik ('[?] Download Audio Successpully')
			print ('')

		def mp4():
			os.system('youtube-dl -f mp4 {0} --no-check-certificate -o /Downloader/Video/%(title)s.%(ext)s'.format(url))
			print ('-'*30)
			tik ('[?] Download Video Successpully')
			print ('')

		if '1' in download:
			mp3()
		elif '2' in download:
			mp4()
		else:
			pass
	except KeyboardInterrupt:
		print (top + ' Stopped')
		print ('')
	except KeyboardInterrupt:
		print ('')

def youtube_2():
	os.system('clear')
	try:
		try:
			os.mkdir('Downloader')
		except:
			pass
		def downldoad(url,judul):
			r = requests.get(url, stream=True)
			total_size = int(r.headers.get('content-length', 0))
			print(f"\nDownload: {judul}")
			block_size = 1024
			t=tqdm(total=total_size, unit='iB', unit_scale=True)
			with open(f'Downloader/{judul.replace("/",",")}','wb') as f:
				for data in r.iter_content(chunk_size=block_size):
					if data:
						t.update(len(data))
						f.write(data)
			t.close()
			print ('--------------------')
			tik ('[+] File Saved At ~/Downloader\n')
			print ('')
		print (logo)
		print ('')
		url = input("[?] Please insert a valid Video URL:\n=>: ")
		os.system('clear')
		print (logo)
		print ('')
		choose = int(input("\n--------------------\n[+] MENU:\n--------------------\n[1] Download MP3\n[2] Download MP4\n--------------------\n[+] Enter Number:\n=>: "))
		os.system('clear')
		print ('')
		print (logo)
		print ('')
		print ('-'*20)
		print ('[+] MENU: ')
		print ('-'*20)
		if choose == 1:
			choose = 'mp3'
		elif choose == 2:
			choose = 'mp4'
		else:
			sys.exit("[!] Check out the options")
		resu = requests.get(f"{new_url}/api/y2mate/check_reso/{choose}?url={url}").json()['result']
		n=1
		if choose == 'mp4':
			for x,y in resu.items():
				print(f"{n}. {x} | {y}")
				n+=1
		elif choose == 'mp3':
			for x in resu:
				print(f"{n}. {x}")
				n+=1
		if len(resu) == 0:
			sys.exit('[!] Cannot find Video')
		pil = int(input("--------------------\n[+] select quality:\n=>: "))
		if choose == 'mp3':
			qualy=resu[pil-1].split(' ')[0]
		elif choose == 'mp4':
			qualy=list(resu.keys())[pil-1].split(' ')[0]
		down = requests.get(f"{new_url}/api/y2mate/download/{choose}?url={url}&quality={qualy}")
		if down.json()['status'] == 'success':
			downldoad(down.json()['url'], down.json()['judul'])
		else:
			print(f"Error: {down.text}, Try Again")
	except KeyboardInterrupt:
		print (top + ' Stopped')
		print ('')
	except KeyboardInterrupt:
		print ('')

def ex():
	print ('')
	print ('-----------------')
	tik ('[+] Thank YOU    ')
	sys.exit()


reset = 'y'
while (reset != 't'):
	os.system('clear')
	print (logo)
	main()
	print ('[+] Enter Number: ')
	choose = input('=>: ')
	if choose == '1':
		youtube_1()
	elif choose == '2':
		youtube_2()
	elif choose == '0':
		ex()
	else:
		print ('')
		print ('-----------------')
		tik ('[!] Wrong Input    ')
		print ('')
	reset = input('[+] back to menu: (y/t): ')

if __name__ == '__main__':
	print (logo)
	main()