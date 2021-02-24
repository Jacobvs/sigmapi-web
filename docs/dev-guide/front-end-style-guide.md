# Sigma Pi, Gamma Iota Chapter: Front-end Styles Developer Guide

[_(Back to project home)_](https://github.com/sigmapi-gammaiota/sigmapi-web/)

## Compile SASS to CSS
Every time you make a change SASS files you will need compile and run this command
```
python3 devl.py static_prod
```

Aside: You could also manually do it with the following command on the command line:
```
sass input_directory output_directory
```

## Development Flow
We recommend to use the Firefox browser as it seems to be more responsive to changes done to the stylesheets.
The development work flow consists of the following: 
1) Edit the style sheets located under
```sigmapiweb/static/css/
```
2) Complie the SASS files with the command below. If you are running the local server open a second terminal and run the following command. If you don't see any changes make sure you brower cache is disabled, you can stop and restart the local server, or use Firefox.
```
python3 devl.py static_prod
```

## Folder structure for styles

## Styles guidelines

## Extra Resources on front-end 

A good website to learn more about sass: [SASS website](https://sass-lang.com/guide)


