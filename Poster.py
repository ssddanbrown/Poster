import sublime, sublime_plugin
import sys 
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))

import requests

class PosterCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# Get current view text
		view_text = self.view.substr(sublime.Region(0, self.view.size()))

		# Load settings and get url
		settings = sublime.load_settings('Poster.sublime-settings')
		url = settings.get('poster_url')

		# Get key for the tab text, defaults to 'content'
		content_key = settings.get('poster_content_key')
		content_key = content_key if content_key is not None else "content"
		
		# Return if we have no URL to post to
		if url is None:
			sublime.error_message('Poster: No URL set, Add a "poster_url" item to your settings with the URL you want to post to.')
			return

		# Create inital data to send
		postData = {
			content_key : view_text
		}

		# Merge any extra post data from the settings
		extraPostData = settings.get('poster_data')
		if extraPostData is not None:
			postData.update(extraPostData)
			pass

		# Send post request
		r = requests.post(url, data=postData)
		pass

