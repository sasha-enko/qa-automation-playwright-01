cheatsheet_actions_click = [
  {
    "action": "Left Click",
    "example": "page.locator(\"selector\").click()",
    "description": "Performs a standard left mouse button click on the center of the element."
  },
  {
    "action": "Right Click",
    "example": "page.locator(\"selector\").click(button=\"right\")",
    "description": "Performs a right mouse button click, usually opening the context menu."
  },
  {
    "action": "Middle Click",
    "example": "page.locator(\"selector\").click(button=\"middle\")",
    "description": "Performs a middle mouse button click (useful for opening links in a new tab)."
  },
  {
    "action": "Double Click",
    "example": "page.locator(\"selector\").dblclick()",
    "description": "Performs a double left mouse button click. Can specify another button."
  },
  {
    "action": "Triple Click",
    "example": "page.locator(\"selector\").click(click_count=3)",
    "description": "Performs three quick clicks, often used to select all text in a field."
  },
  {
    "action": "Click with Modifiers",
    "example": "page.locator(\"selector\").click(modifiers=[\"Shift\", \"Control\"])",
    "description": "Performs a click while holding keyboard keys like Shift, Control, Alt, or Meta."
  },
  {
    "action": "Long Click (Press & Hold)",
    "example": "page.locator(\"selector\").click(delay=1000)",
    "description": "Performs a click and holds the button down for a specified delay in milliseconds."
  },
  {
    "action": "Click at Specific Position",
    "example": "page.locator(\"selector\").click(position={\"x\": 10, \"y\": 5})",
    "description": "Performs a click at specific coordinates relative to the top-left of the element."
  },
  {
    "action": "Mouse Click by Coordinates",
    "example": "page.mouse.click(100, 200)",
    "description": "Performs a click at the specified page coordinates without targeting a specific element."
  }
]
