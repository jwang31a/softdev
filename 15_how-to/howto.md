# how-to :: Make better forms
---
## Overview
There are many features in real forms that we haven't touched upon, and these could come in useful for the user experience, as well as more customization.

### Estimated Time Cost: .8 hrs

### Prerequisites:

- Knowledge of how forms work (and maybe CSS for styling)
- Have a browser and text editor available

1. Create required files (.html file required, .css optional)
1. Setup the html file, it should look something like this
```
<html>
	<head>
	</head>
	<body>
		<form action="">

		</form>
	</body>
</html>
```
3. To make the form put this between the form tags
```
<input type="" name=""></input>
```
- Input type determines what input it takes. Here are all the input types:
```
<input type="button">
<input type="checkbox">
<input type="color">
<input type="date">
<input type="datetime-local">
<input type="email">
<input type="file">
<input type="hidden">
<input type="image">
<input type="month">
<input type="number">
<input type="password">
<input type="radio">
<input type="range">
<input type="reset">
<input type="search">
<input type="submit">
<input type="tel">
<input type="text">
<input type="time">
<input type="url">
<input type="week">
```
- Name determines how it shows up in the URL (with GET requests). For example, if `name="input"` and the input is `hi` we get `test.html?name=hi`

Now that we have our form we can customize it!  
- We can label the form with `<label>Label</label>`

- We can group forms and put them into a box like this:
```
<form action="">
	<fieldset>
		<input type="radio" name="input1"></input>
		<input type="radio" name="input2"></input>
		<input type="radio" name="input3"></input>
	</fieldset>
</form>
```

### Resources
* [Form documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)
* [Styling forms](https://developer.mozilla.org/en-US/docs/Learn/Forms/Styling_web_forms)
---

Accurate as of (last update): 2022-10-20

#### Contributors:  
Team Spooky Ghosts: Jun Hong Wang, James Yu, Thomas Zhang, pd7  
