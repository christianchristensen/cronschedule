# cronschedule
Intent of this project is to poll a URL at a given frequency and check for a diff - if a there is a diff log the difference and make a callback to another specified URL.

The motivation behind this is to use something like the soupscraper (http://github.com/muhqu/soupscraper) to target a specific changing item on a webpage, check for the difference - log it and then call another URL with the result from the difference. The intent being that we can watch a specific webpage for a change and then receive a notification with those changes.

# demo
* cronschedule.appspot.com

# Contrib Info:
* http://contributing.appspot.com/cronschedule