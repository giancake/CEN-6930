# Assignment 1 - Prompt Engeneering Lab
Prompt Engineering Lab, is a programming Laboratory for exercising Ollama, Prompt Engineering, and coding of GenAI Pipelines. This Lab is a hands-on experiences with diverse techniques around Prompt Engineering to get thinking about different Prompts, Pipelines, and Models

## Table of Contents
- [Installation](#Installation)
- [Usage](#Usage)
- [Prompt-Engineering-Techniques](#Prompt-Engineering-Techniques)
- [Experimenting](#Experimenting)
- [References](References)
- [Contact](#Contact)
- [License](#License)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/giancake/PromptEngineeringLab.git

2. Install the Lab requierements:
   ```sh
   pip install -r requirements.txt

## Usage
3. Run the application:
   ```sh
   python3 _pipeline.py

## Prompt-Engineering-Techniques
For our Lab, we will be experimenting with the following prompt Engeneering techniques

- Zero-Shot
- Few-Shot
- Prompt Template
- Chain-of-Thought
- Meta Prompting

## Experimenting

#### (1) In a ZERO-SHOT example, We will be adjusting our prompt, simulating that we are a user inputting a request to the system

```python
MESSAGE = "My professor in GenAI SDLC has left me an assignment which consists in building a Prompt Engeneering Laboratory in python, using the https://chat.hpc.fau.edu/ or Ollama local install LLM servers. I need to know the requirements for building an IT network that supports LAN and WAN access for voice and data applications, that is very fast and renders a good performance"
```

#### (2) For the ZERO-SHOT, which is one of the most basic prompts, the message is passed directly to the system.

```python
PROMPT = MESSAGE 
```

#### (3) We will be configuring different models request to vary the workflow Orchestration

```python
payload = create_payload(target="ollama",
                           model = "llama3.2",
                           prompt=PROMPT,
                           temperature=1.0, 
                           num_ctx=300, 
                           num_predict=300)
```

## Contact
- Author: Wilder Villacorta
- Email: wvillacorta2024@fau.edu
- GitHub: giancake (https://github.com/giancake/PromptEngineeringLab.git)

## References
* [Meta - Prompting Guide](https://www.llama.com/docs/how-to-guides/prompting/)
* [OpenAI Prompting Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
* [Ollama API](https://github.com/ollama/ollama/blob/main/docs/api.md)
* [Open WebUI Endpoints](https://docs.openwebui.com/getting-started/api-endpoints/)

## License

Prompt Engineering Lab
Platform for Education and Experimentation with Prompt NEngineering in Generative Intelligent Systems
_pipeline.py :: Simulated GenAI Pipeline 
 
Copyright (c) 2025 Dr. Fernando Koch, The Generative Intelligence Lab @ FAU
 
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 
Documentation and Getting Started: https://github.com/GenILab-FAU/prompt-eng

Disclaimer: Generative AI has been used extensively while developing this package.