# Python Playlist Manager

This project is a **Python-based playlist manager** designed to organize and manage video playlists directly from the console. The script includes various features such as creating, updating, and playing videos, as well as saving the playlist to a file for future use.

---

## Features

- **Create Playlists**: Add videos with titles and links.
- **View Playlists**: Display playlist details and videos.
- **Play Videos**: Open video links directly in the default web browser.
- **Update Playlist**: Modify playlist name, description, or rating.
- **Add Videos**: Append new videos to an existing playlist.
- **Remove Videos**: Delete specific videos from the playlist.
- **Save/Load Playlists**: Store playlists in a text file for persistence.

---

## How It Works

### Menu Options
Upon running the script, the user is greeted with a main menu:

```
Main Menu:
|-------------------------|
|Option 1: Create Playlist|
|Option 2: Show Playlist  |
|Option 3: Play A Video   |
|Option 4: Add Videos     |
|Option 5: Update Playlist|
|Option 6: Remove Video   |
|Option 7: Save and Exit  |
|-------------------------|
```

#### Option 2: Show Playlist
- Displays the playlist name, description, and rating.
- Lists all the videos in the playlist, showing their titles and links.

#### Option 3: Play A Video
- Displays a list of videos in the playlist.
- Allows the user to select a video by its number.
- Opens the selected video link in the default web browser.

#### Option 4: Add Videos
- Prompts the user to specify how many videos to add.
- Collects the title and link for each new video.
- Appends the new videos to the existing playlist.

#### Option 5: Update Playlist
- Provides options to update the playlist's name, description, or rating.
- Ensures updates are saved only after confirmation.

#### Option 6: Remove Video
- Displays the current list of videos in the playlist.
- Allows the user to select a video by its number to remove it from the playlist.

#### Option 7: Save and Exit
- Saves the playlist data, including all videos, to a text file.
- Exits the program safely.

### Example Console Output

Here is a demonstration of the console output for creating a playlist:

```
Main Menu:
|-------------------------|
|Option 1: Create Playlist|
|Option 2: Show Playlist  |
|Option 3: Play A Video   |
|Option 4: Add Videos     |
|Option 5: Update Playlist|
|Option 6: Remove Video   |
|Option 7: Save and Exit  |
|-------------------------|

Enter option (1-7): 1

Enter playlist name: My Favorite Videos
Enter playlist description: A collection of my favorite videos.
Enter playlist rating (1-5): 5

How many playlist: 2
--------
    ENTER VIDEO 1
Enter title 1: Python Tutorial
Enter link 1: https://www.youtube.com/watch?v=rfscVS0vtbw
--------
    ENTER VIDEO 2
Enter title 2: AI Basics
Enter link 2: https://www.youtube.com/watch?v=aircAruvnKk
--------
```

---

