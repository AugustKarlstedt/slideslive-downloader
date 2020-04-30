# slideslive-downloader
download slideslive presentations (video + slides)

## what is it
I wanted to download ICLR 2020 videos, so I hacked this together. It should work for any presentation hosted on slideslive.com

## how to use
I have some hardcoded values, change them as appropriate
I also download the main video directly from the webpage in browser by just finding the mp4 file in source.

e.g. 
Beyond “tabula rasa” in reinforcement learning: agents that remember, adapt, and generalize 
https://slideslive.com/38926829/beyond-tabula-rasa-in-reinforcement-learning-agents-that-remember-adapt-and-generalize

slide URL: https://d2ygwrecguqg66.cloudfront.net/data/presentations/38926829/slides/big/0-0001.jpg

slide XML: https://d2ygwrecguqg66.cloudfront.net/data/presentations/38926829/38926829.xml
(contains sync times for slides)


1. download mp4 from page
2. find the slide URL from the page source
3. find the slide XML from the page source and download it. it contains sync times for slides
4. modify `create-slide-urls.py` with correct `slide_count` and `url`
5. run `GO.sh`
6. modify `create-slide-video.py` with correct XML file 
7. run `python3 create-slide-video.py` to turn the slide images into a video that is synced with the main mp4
8. now you can use something like DaVinci Resolve video editor to place the videos side-by-side and render it out

done!

### notes
http://www.betr-rl.ml/2020/program/
