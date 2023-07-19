# What is the MeMa Page Framework?
MeMa's interface stucture is optimized around **ease of expansion** and **ease of modification**. Each `page` is it's own class, and should be created in it's own file, similar to the [State Design Pattern](https://en.wikipedia.org/wiki/State_pattern), however instead of states, MeMa uses `pages`. This might bring the question ...

### What is a page in MeMa? Is it like a HTML Page?
> In MeMa, a **page** is a **frame** that displays content to the user. In order to **maintain integrity with expansion**, the MeMa Page Framework doesn't facilitate direct input through the page, as this can become inaccessible if there isn't a **direct physical button mapping.**<br><br>So, this in turn will beg the question: *How can I manage inputs?* Well, in the framework, inputs are handled through a simple `callback` function that will get called when a button gets pressed, the user says something or the dial is rotated on the machine. These are passed to the `page` through `json-style` dictionaries, representing what was done, and through what means.

### Why implement this through a framework?
> The MeMa Page Framework has **several notable advantages over direct application design**, One of these is that the process of updating the buttons has been **abstracted to a single function** where you pass the new button names, callbacks and a boolean representing whether or not to read the new buttons aloud to the user.<br><br>The Framework still facilitates and caters for all [Tkinter](https://wiki.python.org/moin/TkInter) widgets, meaning that you can still access direct widget **creation, modification and deletion**. Alongside this, it helps maintain individual responsibility between pages, and ease of transition between pages. In short, **the page framework should make it fast and easy to expand on and add to the MeMa System**.

# How to add a new page to the MeMa Framework?
This is