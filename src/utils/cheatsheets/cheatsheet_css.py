cheatsheet_css = [
  {
    "action": "Class Selector",
    "example": ".my-class",
    "description": "Selects elements with the class 'my-class'."
  },
  {
    "action": "ID Selector",
    "example": "#my-id",
    "description": "Selects the element with the ID 'my-id'."
  },
  {
    "action": "Tag Selector",
    "example": "div, button",
    "description": "Selects all elements with the given tag name(s)."
  },
  {
    "action": "Descendant Selector",
    "example": "ul li",
    "description": "Selects all 'li' elements inside 'ul' at any nesting level."
  },
  {
    "action": "Child Selector",
    "example": "ul > li",
    "description": "Selects 'li' elements that are direct children of 'ul'."
  },
  {
    "action": "Attribute Presence Selector",
    "example": "input[name]",
    "description": "Selects elements with the attribute 'name' (any value)."
  },
  {
    "action": "Attribute Equals Selector",
    "example": "input[name=\"email\"]",
    "description": "Selects elements whose 'name' attribute is exactly 'email'."
  },
  {
    "action": "Attribute Starts With Selector",
    "example": "a[href^=\"https\"]",
    "description": "Selects elements whose 'href' attribute starts with 'https'."
  },
  {
    "action": "Attribute Ends With Selector",
    "example": "img[src$=\".png\"]",
    "description": "Selects elements whose 'src' attribute ends with '.png'."
  },
  {
    "action": "Attribute Contains Selector",
    "example": "div[class*=\"active\"]",
    "description": "Selects elements whose 'class' attribute contains 'active'."
  },
  {
    "action": "Hover Pseudo-class",
    "example": "button:hover",
    "description": "Selects elements when the mouse pointer is over them."
  },
  {
    "action": "Checked Pseudo-class",
    "example": "input:checked",
    "description": "Selects checked checkboxes or radio buttons."
  },
  {
    "action": "Playwright Text Selector",
    "example": "text=Submit",
    "description": "Playwright-specific selector for elements containing the text 'Submit'."
  },
  {
    "action": "Single Element Query",
    "example": "page.$('div')",
    "description": "Selects the first element matching the selector (Playwright/Puppeteer)."
  },
  {
    "action": "Multiple Elements Query",
    "example": "page.$$('div')",
    "description": "Selects all elements matching the selector (Playwright/Puppeteer)."
  }
]