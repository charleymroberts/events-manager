# Testing

**********

## HTML

The HTML on each page was tested using [https://validator.w3.org/](https://validator.w3.org/)

A few pages produced error messages initially. 

These have now been fixed and all pass through the HTML validator with no errors found.

### Details

Page: https://festival-manager-2ef1a8933d4d.herokuapp.com/

Error message:
1. **Error: Bad value** button **for attribute** type **on element** [a](https://html.spec.whatwg.org/multipage/#the-a-element)**: Subtype missing.  
**From line 71, column 5; to line 72, column 28  
/div>↩  <a href="/events-programme/" class="btn btn-primary btn-lg px-3 mb-5 rounded-pill" type="button"↩ id="homepage-button">↩

Fixed by: changing "type"= to "role"= on "button"

*******

Page: https://festival-manager-2ef1a8933d4d.herokuapp.com/venue/

Error message:
1.  **Error: End tag for** body **seen, but there were unclosed elements.**From line 110, column 1; to line 110, column 7  
    /script>↩↩</body>↩</htm
2.  **Error: Unclosed element** div**.  
    **From line 74, column 1; to line 74, column 26  
    s here-->↩<div class="container-md">↩  ↩

Fixed by: Removing a stray `<div>` tag that shouldn't have been there.

********

Page: https://festival-manager-2ef1a8933d4d.herokuapp.com/performer/3 (an individual performer page containing a photo)

Error message: 
1. **Error: Attribute** alt **not allowed on element** 

Fixed by: Changing "alt"= to "title"= to the description of the hyperlink intended for screen readers.

2.  **Error: An** img **element must have an** alt **attribute, except under certain conditions. 

Fixed by: Adding an alt attribute to the img element `alt="Photo of {{ performer.name }}`

*****

## CSS 

CSS was checked using https://jigsaw.w3.org/css-validator/

When asked to check the deployed homepage URL https://festival-manager-2ef1a8933d4d.herokuapp.com/, 
the checker returned a number of errors, all of which originated from the link to the Bootstrap CDN contained within the CSS file.

To check my own CSS, I made a copy of the CSS file locally, deleted the CDN links, 
saved it as a file and uploaded it to the checker.  The checker found no errors in this file.

*******

## Python

Python code was checked using [flake8](https://flake8.pycqa.org/).

The majority of the error messages were due to some lines of code exceeding 79 characters.

After the code was reformatted to shorten the line lengths, the remaining error messages were:

$ flake8 events events_manager
events_manager/settings.py:19:5: F401 'env' imported but unused
events_manager/settings.py:103:80: E501 line too long (91 > 79 characters)
events_manager/settings.py:106:80: E501 line too long (81 > 79 characters)
events_manager/settings.py:109:80: E501 line too long (82 > 79 characters)
events_manager/settings.py:112:80: E501 line too long (83 > 79 characters)
events_manager/settings.py:133:80: E501 line too long (84 > 79 characters)

The env.py error message is not possible to fix (as far as I am aware).

The remaining 'line too long' errors refer to lines of code such as long class 
names such as password validators that cannot be split across lines.

*******

## Lighthouse accessibility scores

Each page was checked for accessibility score using the Lighthouse checker 
in DevTools once this version of the app was completed.  

Prior Lighthouse checks had also been carried out during development.

For comparison, the public pages were checked as 'mobile' and the staff pages as 'desktop' (one or the other needs to be selected before Lighthouse will run checks).

All pages scored 100 for accessibility.  


******

## Manual testing

### Manual testing checklist

The following checks were made continuously throughout the development process on the local and deployed versions, and again on the deployed version once this iteration of the app had been completed.

**All pages**

1. Page displays content as expected (particularly conditional text in for loops or if/else statements)


2. Sizing displays correctly at all break points from 320px to above 1200px (checked by using Google Chrome browswer DevTools and manually resizing the browser on my own laptop and desktop screens)


3. All links in the header, navbar and body work correctly.  


4. Links to external websites (from performer info pages) function correctly and open in new tab

**Forms**

All forms:

1. Form submits as expected, with content added to all form fields 


2. Data then appears on the relevant app page(s) as expected (particularly the photos on the performer pages on the Heroku deployed version)

'Edit' forms: 

3. Delete confirm popup appears on clicking the 'delete' button

Form-specific fields:

4. 'Add event' form: Date and time pickers function correctly 


5. 'Add performer' form: Error shown on clicking submit if the 'weblink' field is not in valid URL format