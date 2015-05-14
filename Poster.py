import sublime, sublime_plugin
import sys 
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))

import requests

class PosterCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view_text = self.view.substr(sublime.Region(0, self.view.size()))
		settings = sublime.load_settings('Poster.sublime-settings')
		url = settings.get('poster_url')
		if url != None:
			print(url)
			postData = {
				"content" : view_text
			}
			settingsPostData = settings.get('poster_data')
			if settingsPostData != None:
				postData.update(settingsPostData)
				pass
			r = requests.post(url, data=postData)
			pass

