# G.A.L-Gamers-As-Legions-System-Optimizer
G.A.L (Gamers As Legions) - A system optimization tool for gamers to clean junk files, optimize settings, and boost performance.

# About
G.A.L (Gamers As Legions) System Optimizer
What is G.A.L?
G.A.L, short for Gamers As Legions, is a system optimization tool designed specifically for gamers and power users who want to squeeze every last drop of performance out of their Windows PC. It’s like a swiss army knife for system maintenance, cleaning up junk files, optimizing settings, and ensuring your rig is running at peak performance. Whether you're battling in a high-stakes esports match or exploring vast open worlds, G.A.L ensures your system is free of clutter and optimized for maximum responsiveness.

What does G.A.L do?
G.A.L performs a series of cleaning and optimization tasks to free up system resources, reduce latency, and improve overall performance. Here’s a breakdown of what it does:

Clean RAM Cache:

Clears out unused RAM, freeing up memory for your games and applications.

This is like giving your system a fresh breath of air, ensuring no background processes are hogging your precious RAM.

Clean Windows Temp Folder:

Deletes temporary files from the C:\Windows\Temp folder.

These files are often leftovers from installations or updates and can pile up over time, taking up valuable disk space.

Clean Prefetch Folder:

Clears out the C:\Windows\Prefetch folder, which stores preloaded data to speed up application launches.

Over time, this folder can become bloated with outdated data, and cleaning it can help improve boot times.

Clean Recycle Bin:

Empties the Recycle Bin for all users, freeing up disk space.

No more forgotten files taking up space on your SSD or HDD.

Clean Windows Update Cache:

Deletes the cache from C:\Windows\SoftwareDistribution\Download.

This is where Windows stores update files, and clearing it can resolve update-related issues and free up space.

Clean Temporary Internet Files:

Removes cached files from your browser’s temporary internet files folder.

This helps free up space and can improve browser performance.

Clean Thumbnails:

Deletes thumbnail caches, which are used to speed up the display of images and videos in File Explorer.

Over time, these caches can grow large and become outdated.

Clean Delivery Optimization Files:

Removes files used by Windows Update’s Delivery Optimization feature, which shares updates with other PCs over the internet.

This can free up space and reduce unnecessary network usage.

Clean Temp Folder:

Clears out the %temp% folder for all users, which stores temporary files created by applications.

This is a common source of disk clutter.

Flush DNS Cache:

Clears the DNS cache, which can resolve connectivity issues and improve network performance.

Essential for gamers who rely on low-latency connections.

Set Cloudflare DNS:

Configures your system to use Cloudflare’s fast and privacy-focused DNS servers (1.1.1.1 and 1.0.0.1).

This can improve internet speed and reduce latency in online games.

Set Ultimate Power Plan:

Activates the Ultimate Performance power plan, which maximizes system performance by prioritizing speed over energy savings.

Perfect for gaming rigs where every frame counts.

Why is G.A.L a gamer’s best friend?
G.A.L is designed to eliminate bottlenecks that can slow down your system. By cleaning up junk files, optimizing system settings, and freeing up resources, it ensures your PC is ready to handle the most demanding games. It’s like having a pit crew for your gaming rig, keeping it in top shape so you can focus on dominating the competition.

Install.bat
What is Install.bat?
Install.bat is a batch script that ensures your system has everything it needs to run G.A.L. It checks for the necessary software and libraries, and if they’re missing, it guides you through the installation process.

What does Install.bat do?

Checks for Python:

Python is required to run the G.A.L script. The script checks if Python is installed on your system.

If Python is missing, it prompts you to install it before proceeding.

Checks for pip:

pip is Python’s package manager, used to install third-party libraries. The script ensures pip is installed.

If pip is missing, it advises you to install it.

Installs Required Libraries:

G.A.L relies on the psutil library to perform tasks like cleaning RAM. The script automatically installs psutil using pip.

If the installation fails (e.g., due to no internet connection), it notifies you and exits.

Why is Install.bat important?
It ensures that your system is ready to run G.A.L without any hiccups. By automating the setup process, it saves you the hassle of manually installing dependencies and ensures everything is in place for a smooth experience.

Run.bat
What is Run.bat?
Run.bat is a batch script that launches the G.A.L system optimizer. It’s designed to make running G.A.L as simple as possible, so you don’t need to fiddle with command prompts or scripts.

What does Run.bat do?

Displays a Cool Intro:

It starts with a gamer-style intro message, setting the tone for what’s to come.

The message “For Gamers by Gamers!” reinforces the tool’s purpose.

Launches G.A.L:

It runs the G.A.L.py script using pythonw, which ensures the script runs in the background without a terminal window cluttering your screen.

This makes the experience seamless and user-friendly.

Why is Run.bat important?
It simplifies the process of running G.A.L, making it accessible even to users who aren’t tech-savvy. With just a double-click, you can optimize your system and get back to gaming.

Summary
G.A.L: A powerful system optimizer for gamers, cleaning junk files, optimizing settings, and freeing up resources to ensure peak performance.

Install.bat: Ensures your system has Python and the necessary libraries to run G.A.L.

Run.bat: Launches G.A.L with a gamer-friendly interface, making it easy to use.

Together, these tools form a complete package for gamers who want to keep their systems running smoothly and efficiently. Whether you're a casual player or a hardcore esports competitor, G.A.L is your ultimate ally in the quest for performance.

# Install

To download G.A.L (Gamers As Legions System Optimizer) from its GitHub repository, follow these steps. This guide will walk you through downloading the project using Git or directly as a ZIP file if you don’t want to use Git.

Option 1: Download Using Git (Recommended for Developers)

Step 1: Install Git

If you don’t have Git installed:

Go to git-scm.com.

Download the installer for your operating system.

Run the installer and follow the prompts.

Step 2: Clone the Repository

Open a terminal (Command Prompt, PowerShell, or Git Bash).

Navigate to the directory where you want to download G.A.L. For example:

cd C:\Users\YourUsername\Documents

Run the git clone command to download the repository:

git clone https://github.com/xxxnightvoidxxx/G.A.L-Gamers-As-Legions-System-Optimizer.git

This will create a folder named G.A.L-Gamers-As-Legions-System-Optimizer in your current directory.

Step 3: Navigate to the G.A.L Folder

After cloning, navigate into the G.A.L folder:

cd G.A.L-Gamers-As-Legions-System-Optimizer

Option 2: Download as a ZIP File (Easiest for Non-Developers)

Step 1: Go to the GitHub Repository

Open your web browser and go to the G.A.L repository:

https://github.com/xxxnightvoidxxx/G.A.L-Gamers-As-Legions-System-Optimizer.

Step 2: Download the ZIP File

On the repository page, click the green Code button.

In the dropdown menu, click Download ZIP.

Download ZIP

The repository will be downloaded as a ZIP file to your computer.

Step 3: Extract the ZIP File

Locate the downloaded ZIP file (usually in your Downloads folder).

Right-click the ZIP file and select Extract All.

Choose a location to extract the files (e.g., C:\Users\YourUsername\Documents).

Click Extract. This will create a folder named G.A.L-Gamers-As-Legions-System-Optimizer.

Step 4: Navigate to the G.A.L Folder

Open the extracted folder:

C:\Users\YourUsername\Documents\G.A.L-Gamers-As-Legions-System-Optimizer

Step 5: Install Dependencies

G.A.L requires the psutil library to function. Install it using pip:

Open a terminal (Command Prompt, PowerShell, or Git Bash).

Navigate to the G.A.L folder (if you’re not already there):

cd C:\Users\YourUsername\Documents\G.A.L-Gamers-As-Legions-System-Optimizer

Run the following command to install the required library:

pip install psutil

Step 6: Run the Installer

G.A.L comes with an Install.bat script to set up everything:

Run the Install.bat script:

Install.bat

This script will:

Check if Python and pip are installed.

Install the psutil library if it’s not already installed.

Step 7: Launch G.A.L

Once the installation is complete, you can run G.A.L using the Run.bat script:

Run the Run.bat script:

Run.bat

This will launch the G.A.L GUI, where you can start optimizing your system.

Step 8: (Optional) Run G.A.L Directly

If you prefer to run G.A.L without using the batch scripts, you can do so directly with Python:

Navigate to the G.A.L folder (if you’re not already there):

cd C:\Users\YourUsername\Documents\G.A.L-Gamers-As-Legions-System-Optimizer

Run the G.A.L.py script:

python G.A.L.py

Troubleshooting

Error: Python not found:

Make sure Python is installed and added to your system’s PATH. You can check by running:

python --version

If this doesn’t work, reinstall Python and ensure the Add Python to PATH option is checked.

Error: pip not found:

Ensure pip is installed by running:

pip --version

If it’s not installed, you can install it by following the official guide: pip installation.

Permission Errors:

If you encounter permission errors, make sure to run your terminal or command prompt as an administrator.

Summary

Download the repository:

Using Git:

git clone https://github.com/xxxnightvoidxxx/G.A.L-Gamers-As-Legions-System-Optimizer.git

Or download the ZIP file from GitHub and extract it.

Navigate to the G.A.L folder:

cd G.A.L-Gamers-As-Legions-System-Optimizer

Install dependencies:

pip install psutil

Run the installer:

Install.bat

Launch G.A.L:

Run.bat

by xxxnightvoidxxx aka xxxsilentdeviantxxx
