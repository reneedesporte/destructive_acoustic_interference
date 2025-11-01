# Destructive Acoustic Interference
## Introduction
Experience the principles of [Active Noise Control](https://en.wikipedia.org/wiki/Active_noise_control) firsthand! This codebase takes a 2-channel capable output device — e.g., your laptop speakers — and plays a signal which will destructively interefere at some point in space.

Check out my blog post on this experiment, and try it out yourself: find the "dead zone" based on your speaker configuration.

Run the code with `uv run main.py` to find your audio devices. Add the `-d` flag when you're ready to specify an output device, e.g., `uv run main.py -d 1`. To hear the audio without destructive interference, use the `--normal` flag.

To see it working on my laptop, check out the [YouTube video](https://youtu.be/bKjprY37uNE) I uploaded, as well as [my blog explanation](https://reneedesporte.com/2025/09/11/destructive-interference-a-python-demonstration/) (there's not much to it).
## Dependencies
### Code
Code dependencies are managed with uv.
### Hardware
1 speaker is needed: a output device with 2-channel capabilities. An optional second microphone can be used to verify the "dead zone", but you can also just use your ears!

Code was written and tested on Macbook.
