# Poster

A super simple Sublime Text plugin for posting text in the current tab content to a server.

### Configuration

Settings are accessed via the `Preferences` > `Package Settings` > `Poster` menu.
The settings can take the following options:

* **poster_url** - The url to post data to.
* **poster_data** - An object containing any extra variables you want to add to the post data.

**The `poster_url` setting is required for Poster to work**. A typical settings file will look like this:

``` json
{
	"poster_url": "http://example.com",
	"poster_data": {
		"a": "This is an example post item",
		"b": "Another post variable"
	}
}
``` 

The contents of the current tab will be added to the post data with a key of `content`.


### How to use

A shortcut is available, `ctrl+shift+o`, or you can find the option `Poster` in the tools menu.

### Contributing

If you find any issues or would like a new feature feel free to add a github issue or create a pull-request.

### Attribution

This plugin uses the [Requests](http://docs.python-requests.org/) HTTP library.