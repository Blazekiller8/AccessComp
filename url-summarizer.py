# importing libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Input text - to summarize
text = "Alacritty is a modern terminal emulator that comes with sensible defaults but allows for extensive configuration. It claims to be the fastest terminal emulator in existence. Integrating with other applications, rather than reimplementing their functionality, provides a flexible set of features with high performance. Using the GPU for rendering enables optimizations that aren’t possible without it. The supported platforms currently consist of BSD, Linux, macOS, and Windows.The software is considered to be at a beta level of readiness; there are a few missing features and bugs to be fixed, but it is already used by many as a daily driver.Here’s a link to Alacritty’s open source repository on GitHubAbout the project :Alacritty is the result of frustration with existing terminal emulators. Using vim inside tmux in many terminals was a particularly bad experience. None of them were ever quite fast enough. Even so, Linux does have some decent alternatives. For example, urxvt and st give good experiences. The major downside with those options is the difficulty of configuration and the inability to run on non-X11 platforms. The options for macOS are prolonged–especially with a full-screen terminal on a 4k monitor. None of these terminals are cross-platform–they are usually married to the windowing and font rendering APIs of their native platform.Alacritty aims to address these issues.A set of values guides the project’s architecture and features:Correctness: Alacritty should be able to properly render modern terminal applications like tmux and vim.Performance: Alacritty should be the fastest terminal emulator available anywhere.Appearance: Alacritty should have beautiful font rendering and look fantastic on all supported platforms.Simplicity: Alacritty should be conservative about which features it offers.Portability: Alacritty should support major operating systems including Linux, macOS, and Windows.Features:This section will give an overview of Alacritty’s features beyond its terminal emulation capabilities.Control Sequences -To get a list with supported control sequences take a look at Alacritty’s escape sequence support.Vi Mode — The vi mode allows moving around Alacritty’s viewport and scrolling back using the keyboard.Motion — The cursor motions are set up by default to mimic vi, however, they are fully configurable.Selection — One useful feature of vi modes is the ability to make selections and copy text to the clipboard.Search — Search allows you to find anything in Alacritty’s scrollback buffer.Vi Search -In vi mode the search is bound to / for forward and for backward search. This allows you to move around quickly and help with selecting content.Normal Search -During a normal search, you don’t have the opportunity to move around freely, but you can still jump between matches using Enter and Shift+Enter.Hints — Terminal hints allow easily interacting with visible text without having to start vi mode.Selection expansion -After making a selection, you can use the right mouse button to expand it.Opening URLs with the mouse -You can open URLs with your mouse by clicking on them.Multi-Window -Alacritty supports running multiple terminal emulators from the same Alacritty instance.OpenGL Rendering — Alacritty’s renderer is capable of doing ~500 FPS with a large screen full of text. This is made possible by efficient OpenGL usage. Alacritty is very good at processing huge amounts of text.The Parser — Alacritty’s performance is enhanced by having a good parser, Rust helped significantly with this.Zero-cost abstractions — Rust’s zero-cost abstractions enable building nicely abstracted components and later combining them as if they were hand-written as one initially.New libraries — Developing Alacritty required several pieces of library infrastructure which were not available. A non-GPL licensed cross-platform clipboard library, a vte parser, cross-platform font rasterization, and fontconfig bindings were all needed to build this project. vte and utf8parse have been published on crates.io. The remaining libraries are still in Alacritty’s source tree and will be published independently at some point.Installation for Ubuntu:```sudo add-apt-repository ppa:mmstick76/alacrittysudo apt updatesudo apt install alacrittysudo curl https://sh.rustup.rs -sSf | sh```or we can download it directly from SnapVerdict:Alacritty is a great minimal terminal emulator that can replace most everyday terminals. But it’s far from being perfect, there are still more features to be added and bugs to be fixed. In my opinion, the multiple windows feature is still unusable right now and it’s to use alternatives like tmux. The speed difference between using Alacritty and normal terminal is not too noticeable. We can’t verify the usage of GPU. It’s no different from a standard terminal for those without a GPU. But I believe that this is just the beginning and recommend everyone with a GPU to try it. In the future, there will be some serious debates between users of Alacritty and Warp, a similar terminal available only on Mac for now. Till then I guess this is it. !HAPPY-CODING!"

# Tokenizing the text
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

# Creating a frequency table to keep the
# score of each word

freqTable = dict()
for word in words:
	word = word.lower()
	if word in stopWords:
		continue
	if word in freqTable:
		freqTable[word] += 1
	else:
		freqTable[word] = 1

# Creating a dictionary to keep the score
# of each sentence
sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
	for word, freq in freqTable.items():
		if word in sentence.lower():
			if sentence in sentenceValue:
				sentenceValue[sentence] += freq
			else:
				sentenceValue[sentence] = freq



sumValues = 0
for sentence in sentenceValue:
	sumValues += sentenceValue[sentence]

# Average value of a sentence from the original text

average = int(sumValues / len(sentenceValue))

# Storing sentences into our summary.
summary = ''
for sentence in sentences:
	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
		summary += " " + sentence
print(summary)
