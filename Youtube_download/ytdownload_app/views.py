# importing all the required modules 
from django.shortcuts import render, redirect 
from pytube import *


# defining function 
OUTPUT_PATH = "C:\my"
def ytube(request): 

	# checking whether request.method is post or not 
	if request.method == 'POST': 
		
		# getting link from frontend 
		link = request.POST['link'] 
		video = YouTube(link) 

		# setting video resolution 
		stream = video.streams.get_lowest_resolution()
		
		# downloads video 
		stream.download(output_path=OUTPUT_PATH) 

		# returning HTML page 
		return render(request, 'ytdownload_app/index.html') 
	return render(request, 'ytdownload_app/index.html')
