import webbrowser

class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link
		self.seen = True

	def open(self):
		webbrowser.open(self.link)
		self.seen = False

class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name
		self.description = description
		self.rating = rating
		self.videos = videos

def read_video(i):
	title = input(f"Enter title {i}: ") + "\n"
	link = input(f"Enter link {i}: ") + "\n"
	video = Video(title, link)
	return video

def print_video(video, i):
	print(f"Titile {i}: " + video.title, end="")
	print(f"Link {i}: " + video.link, end="")

def read_videos():
	videos = []
	total = int(input("How many playlist: "))
	print("--------")
	for i in range (total):
		print(f"\tENTER VIDEO {i+1}")
		vid = read_video(i+1)
		videos.append(vid)
		print("--------")	
	return videos

def print_videos(videos):
	for i in range (len(videos)):
		print(f"\tVideo {i+1}")
		print_video(videos[i], i+1)
		print("--------")

def write_video_txt(video, file):
	file.write(video.title)
	file.write(video.link)

def write_videos_txt(videos, file):
	total = len(videos)
	file.write(str(total) + "\n")
	for i in range (total):
		write_video_txt(videos[i], file)

def read_video_from_txt(file):
	title = file.readline()
	link = file.readline()
	video = Video(title, link)
	return video

def read_videos_from_txt(file):
	videos = []
	total = int(file.readline())
	for i in range (total):
		vid = read_video_from_txt(file)
		videos.append(vid)
	return videos

def read_playlist():
	playlist_name = input("Enter playlist name: ") + "\n"
	playlist_discription = input("Enter playlist description: ") + "\n"
	playlist_rating = input("Enter playlist rating: ") + "\n"
	playlist_videos = read_videos()
	playlist = Playlist(playlist_name, playlist_discription, playlist_rating, playlist_videos)
	return playlist

def write_playlist_txt(playlist):
	with open("2.txt", "w") as file:
		file.write(playlist.name)
		file.write(playlist.description)
		file.write(playlist.rating)
		write_videos_txt(playlist.videos, file)

def read_playlist_from_txt():
	with open("2.txt", "r") as file:
		playlist_name = file.readline()
		playlist_description = file.readline()
		playlist_rating = file.readline()
		playlist_videos = read_videos_from_txt(file)
		playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
		return playlist

def  print_playlist(playlist):
	print("Playlist name: " + playlist.name, end="")
	print("Playlist description: " + playlist.description, end="")
	print("Playlist rating: " + playlist.rating, end="")
	print("--------")
	print_videos(playlist.videos)

def show_menu():
	print("Main Menu:")
	print("|-------------------------|")	
	print("|Option 1: Create Playlist|")
	print("|Option 2: Show Playlist  |")
	print("|Option 3: Play A Video   |")
	print("|Option 4: Add a videos   |")
	print("|Option 5: Update Playlist|")
	print("|Option 6: Remove Video	 |")
	print("|Option 7: Save and Exit  |")
	print("|-------------------------|")	

def menu_option_7(playlist):
	write_playlist_txt(playlist)
	exit()

def select_in_range(promt, min, max):
	choice = input(promt)
	while not choice.isdigit() or int(choice) < min or int(choice) > max:
		print("Please enter validate answer!")
		choice = input(promt)
	choice = int(choice)
	return choice

def play_video(playlist):
	print_videos(playlist.videos)
	total = len(playlist.videos)
	choice = select_in_range(f"Select video you want to open (1-{total}): ", 1, total)
	print(f"Open video: {playlist.videos[choice - 1].title} - {playlist.videos[choice - 1].link}" , end="")
	playlist.videos[choice-1].open()

def add_video(playlist):
	while True:
		try:
			n = int(input("Number of videos you want to add: "))
			break
		except ValueError:
			print("Invalid answer")
			
	for i in range(n):
		print(f"\tEnter new video {i+1}")
		new_title = input(f"Enter new title: ") + "\n"
		new_link = input(f"Enter new link: ") + "\n"
		print("--------")	
		new_video = Video(new_title, new_link)
		playlist.videos.append(new_video)
	return playlist

def update_playlist(playlist):
	while True:
		print("Update Playlist")
		print("1. Playlist Name")
		print("2. Playlist Description")
		print("3. Playlist Rating")
		print("4. Exit")

		choice = select_in_range("Enter option you want to update: ", 1, 4)

		if choice == 1:
			playlist.name = input("Enter new playlist name: ") + "\n"
			print("Update Successfully!")
			input("\nPress enter to continue \n")

		elif choice == 2:
			playlist.description = input("Enter new playlist description: ") + "\n"
			print("Update Successfully!")
			input("\nPress enter to continue \n")

		elif choice == 3:
			playlist.rating = str(select_in_range("Enter new playlist rating (1-5): ", 1, 5)) + "\n"
			print("Update Successfully!")
			input("\nPress enter to continue \n")

		elif choice == 4:
			print("Exiting Update Playlist...")
			break
    
	return playlist

def delete_video(playlist):
	print_videos(playlist.videos)
	choice = select_in_range("Enter video you want to remove: ", 1, len(playlist.videos))
	del playlist.videos[choice - 1]
	return playlist

def main():
	try:
		playlist = read_playlist_from_txt()
		print("Load date successfully!")
	except:
		print("You are the fisrt user")
	while True:
		show_menu()
		choice = select_in_range("\nEnter option (1-7): ", 1, 7)
		print("--------")	
		if choice == 1:
			playlist = read_playlist()
			input("\nPress enter to continue \n")
		elif choice == 2:
			print_playlist(playlist)
			input("\nPress enter to continue \n")
		elif choice == 3:
			play_video(playlist)
			input("\nPress enter to continue \n")
		elif choice == 4:
			playlist = add_video(playlist)
			input("\nPress enter to continue \n")
		elif choice == 5:
			playlist = update_playlist(playlist)
			input("\nPress enter to continue \n")
		elif choice == 6:
			playlist = delete_video(playlist)
			input("\nPress enter to continue \n")
		elif choice == 7:
			menu_option_7(playlist)	
main()