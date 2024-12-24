# Synchronizer
The main (and only) functionality is to synchronize time and video, that is, if you want the video to arrive at a **specific** time at 00:00, this program was made for that!!

### How it works
- With the time and moment of the video, it uses a calculation involving multiplication to transform the two things "into the same format", then it does the subtraction and uses more calculation involving division to transform the formatted time back into what we know as *"XX:XX:XX"*.
- Then it waits for the correct time, and when it arrives it presses "K" and plays the video **(It is expected to be used in the YouTube)**.

### How to use
1. Start the program executable.
2. Add the specific moment of the video in the first field, for example: `hours:minutes:seconds`
3. Add the specific frame of the video in the second field, if you don't have one, set it to 1. (If you don't know, you can go to YouTube and go through the frames using `,` and `.`, then see when the seconds change)
4. Add the fps of the video in the third field, to find out, right-click and click on "Statistics for Nerds". Then locate the "Current / Optimal Res" section and then the fps, which is after the `@`. Example: Current / Optimal Res 2560x1440@**60**.
5. Add the chosen time in the fourth field, in the same way as in step 2.
6. The last one is a checkbox, where you can decide. If checked, it will go to the other tab to wait for the moment to play, if unchecked, it will just calculate and give you the right moment to play.

### Warning
- The calculation involving frames is not precise, depending on the value it may advance or delay some frames. However, this is not a cause for concern, since the advance or delay is not very noticeable to human vision. I believe this happens due to the division that occurs during the calculation after the subtraction.
