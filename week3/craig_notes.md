HuggingFace Platform - https://huggingface.co
Offers access to 3 categories of things
1). over 1.6M open source models
2). over 390k datasets (like caggle)
3). spaces - write an app and expose it - runs on hugging face cloud. Code is open source though
    most apps are made in gradio. Leader boards are gradio apps which rank and score LLMs

HuggingFace also offer libraries. Gives a head start
For example:
- hub library - allows you to login to huggingface and download and upload datasets and models (and possibly more)
- datasets library - gives us access to the datasets in huggingface
- transformers library - wrapper for LLMs that follow the transformer architecture
- peft library - parameter efficient fine tuning - utilities that allow us to train LLMs
- trl library - transformer reinforcement learning
    - reward modeling (rm)
    - proximal policy optimisation (ppo) 
    - supervised fine tuning (sft)
- accelerate library - allows our transformers over a distributed configuration - better performance

Google CoLab - https://colab.research.google.com/?authuser=1
