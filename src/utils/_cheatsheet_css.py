cheatsheet_css = {
    "selectors": {
        ".": {
            "example": ".my-class",
            "explanation": "Select elements with class 'my-class'"
        },
        "#": {
            "example": "#my-id",
            "explanation": "Select element with id 'my-id'"
        },
        "tag": {
            "example": "div, button",
            "explanation": "Select all elements of this tag"
        },
        "A B": {
            "example": "ul li",
            "explanation": "Select all 'li' elements inside 'ul' at any nesting level"
        },
        "A > B": {
            "example": "ul > li",
            "explanation": "Select 'li' elements direct children of 'ul'"
        },
        "[attr]": {
            "example": "input[name]",
            "explanation": "Select elements with attribute 'name' (any value)"
        },
        '[attr="value"]': {
            "example": 'input[name="email"]',
            "explanation": 'Select elements with attribute "name" equal to "email"'
        },
        '[attr^="val"]': {
            "example": 'a[href^="https"]',
            "explanation": 'Select elements whose "href" starts with "https"'
        },
        '[attr$="val"]': {
            "example": 'img[src$=".png"]',
            "explanation": 'Select elements whose "src" ends with ".png"'
        },
        '[attr*="val"]': {
            "example": 'div[class*="active"]',
            "explanation": 'Select elements whose "class" contains substring "active"'
        },
        ":hover": {
            "example": "button:hover",
            "explanation": "Select elements when mouse is hovering over them"
        },
        ":checked": {
            "example": "input:checked",
            "explanation": "Select checked checkboxes or radio buttons"
        },
        "text=": {
            "example": "text=Submit",
            "explanation": "Playwright selector: elements containing text 'Submit'"
        },
        "$()": {
            "example": "page.$('div')",
            "explanation": "Select single element matching selector (Playwright/Puppeteer)"
        },
        "$$()": {
            "example": "page.$$('div')",
            "explanation": "Select all elements matching selector (Playwright/Puppeteer)"
        }
    },
}
