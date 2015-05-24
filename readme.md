# Poster

A super simple Sublime Text plugin for posting text in the current tab content to a server.

### Configuration

Settings are accessed via the `Preferences` > `Package Settings` > `Poster` menu.
The settings can take the following options:

* **poster_url** - The url to post data to.
* **poster_content_key** - The post key that the current tab content will be sent on. Defaults to 'content'.
* **poster_data** - An object containing any extra variables you want to add to the post data. This can be very useful for sending data to API's and you need to add keys.

**The `poster_url` setting is required for Poster to work**. Here is the default settings file:

``` json
{
    "poster_url": "http://example.com",
    "poster_content_key": "content",
    "poster_data": {
        "a": "This is an example post item",
        "b": "Another post variable"
    }
}
``` 

By default some extra post data is sent, "a" & "b", You can either override with your own `poster_data` or empty out the contents like below which will send no extra data:

``` json
{
    "poster_data": {}
}
```

### How to use

A shortcut is available, `ctrl+shift+o`, or you can find the option `Poster` in the tools menu.

### Contributing

If you find any issues or would like a new feature feel free to add a github issue or create a pull-request.

### Attribution

This plugin uses the [Requests](http://docs.python-requests.org/) HTTP library.