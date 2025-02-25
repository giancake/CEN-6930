![GenI-Banner](https://github.com/genilab-fau/genial-fau.github.io/blob/8f1a2d3523f879e1082918c7bba19553cb6e7212/images/geni-lab-banner.png?raw=true)

# Wilders Prompt Engeering Lab

In This Lab we seek to execute different Prompting Techniques in our Prompting Lab and test the Ollama local installs and the FAU open-webui servers. We will do the requirement analysis for using Prompt Engineering to find out our best solution description, making use of the GenAI Pipelines. This Lab is a hands-on experience with diverse techniques around Prompt Engineering to get thinking about different Prompts, Pipelines, and Models.

<!-- WHEN APPLICABLE, REMOVE THE COMMENT MARK AND COMPLETE
This is a response to the Assignment part of the COURSE.
-->

* Authors: [Wilder Villacorta](https://github.com/giancake/PromptEngineeringLab.git)
* Academic Supervisor: [Dr. Fernando Koch](http://www.fernandokoch.me)


# Research Question

Generate a prompt utilizing the GenAI Prompt Engineering Techniques. We will use the following prompt for our experiment:
"My professor in GenAI SDLC has left me an assignment which consists in building a Prompt Engineering Laboratory in python, using the https://chat.hpc.fau.edu/ or Ollama local install LLM servers. I need to know the requirements for building an IT network that supports LAN and WAN access for voice and data applications, that is very fast and renders a good performance"

## Arguments

#### What is already known about this topic

* We know that pipelines play a crucial role in managing the end-to-end process of developing, tuning, and maintaining AI models. GenAI pipelines, are a structured sequence of automated steps, designed to fine tune, test and deploy generative AI models. Among the different types of pipelines, there exist Data pipelines that handle, clean, transform and augment the data which are essential for ensuring high quality for training and fine-tuning models.

* The challenges of Gen AI SDLC pipelines may include the data handling because it requires extensive cleaning, augmentation and labeling, handling biases and ensuring data diversity. The data privacy and security could be at risk of exposing sensitive information when training real-world model datasets, there are lots of scalability challenges in data handling, because LLM's require massive datasets leading to high storage and processing costs.

* Model training requires high computational CPU/GPU energy consumption costs. Fine-tuning and modeling could be catastrophic new data can lead to the model forgetting earlier knowledge.

#### What this research is exploring

<!-- Free-format; use the topics that are applicable to your exploration  -->

* The GenAI SDLC Prompt Engineering Lab is exploring how to build a structured prompt engineering framework using Python language.
* Developing a Lab environment using local Ollama or the FAU servers and experimenting with different prompting techniques.
* We are exploring the automation of the prompt evaluation, creating pipelines to refine and evaluate prompts systematically

#### Implications for practice

<!-- Free-format; use the topics that are applicable to your exploration  -->

* The implications span across multiple areas of the AI development and efficiency, automation, system reliability and ethical considerations.
* Improving the standardization of Prompt Engineering Workflows with structured methodologies for testings could reduce the trial-and-error in GenAI development.
* Enhancing the Model request pipelines ensuring a better consistency and task aligned responses.

# Research Method

Combination of Experimental, Iterative and Comparative Analysis Research

<!-- WHEN APPLICABLE AND AVAILABLE -->

# Results

1. With the ZERO-SHOT prompting technique and using llama3.2 the prompt took 86.091s to generate. The resulting prompt was very precise in context and important but didn't complete at the end.
```python
MESSAGE = "My professor in GenAI SDLC has left me an assignment which consists in building a Prompt Engeneering Laboratory in python, using the https://chat.hpc.fau.edu/ or Ollama local install LLM servers. I need to know the requirements for building an IT network that supports LAN and WAN access for voice and data applications, that is very fast and renders a good performance"

PROMPT = MESSAGE 

payload = create_payload(target="ollama",
                            model = "llama3.2",
                            prompt=PROMPT,
                            temperature=1.0, 
                            num_ctx=300, 
                            num_predict=300)
```

2. With the ZERO-SHOT prompting technique and using llama2 the prompt took 177.861s The resulting prompt was more detailed, extensive and complete.
```python
MESSAGE = "My professor in GenAI SDLC has left me an assignment which consists in building a Prompt Engeneering Laboratory in python, using the https://chat.hpc.fau.edu/ or Ollama local install LLM servers. I need to know the requirements for building an IT network that supports LAN and WAN access for voice and data applications, that is very fast and renders a good performance"

PROMPT = MESSAGE 

payload = create_payload(target="ollama",
                            model = "llama2",
                            prompt=PROMPT,
                            temperature=1.0, 
                            num_ctx=300, 
                            num_predict=300)
```

3. With the ZERO-SHOT prompting technique and using gemma the prompt took 220.707s The resulting prompt was much slower but very extensive and detailed.
```python
MESSAGE = "My professor in GenAI SDLC has left me an assignment which consists in building a Prompt Engeneering Laboratory in python, using the https://chat.hpc.fau.edu/ or Ollama local install LLM servers. I need to know the requirements for building an IT network that supports LAN and WAN access for voice and data applications, that is very fast and renders a good performance"

PROMPT = MESSAGE 

payload = create_payload(target="ollama",
                            model = "gemma",
                            prompt=PROMPT, 
                            temperature=1.0, 
                            num_ctx=300, 
                            num_predict=300)
```

4. With the FEW-SHOT prompting technique and using llama3.2 the prompt took 38.08s The resulting prompt response information was more extensive, however not complete at the end.
```python
MESSAGE = "My professor in GenAI SDLC has left us an assignment which consist in building a prompt eng lab in python, using the https://chat.hpc.fau.edu/ or Ollama local install LLM servers. I need to know the requirements for building an IT network that supports LAN and WAN access for voice and data applications, that is very fast and renders a good performance"

FEW_SHOT = "You are a network architect specialist. If a client asked a consult; respond with an excellent assesment"
PROMPT = FEW_SHOT + '\n' + MESSAGE

payload = create_payload(target="ollama",
                            model = "llama3.2",
                            prompt=PROMPT, 
                            temperature=1.0, 
                            num_ctx=300, 
                            num_predict=300)
```

5. With the FEW-SHOT prompting technique and using llama3.2 and adding 1 level of automation using a FEW-SHOT prompting technique llama3.2 model, the first prompt took 41.425s and the automated prompt 47.464s The resulting prompt response time was 88s and the prompt was shorter in information but complete.
```python
MESSAGE = "My professor in GenAI SDLC has left us an assignment which consist in building a prompt eng lab in python, using the https://chat.hpc.fau.edu/ or Ollama local install LLM servers. I need to know the requirements for building an IT network that supports LAN and WAN access for voice and data applications, that is very fast and renders a good performance"

FEW_SHOT = "You are a network architect specialist. If a client asked a consult; respond with an excellent assesment"
PROMPT = FEW_SHOT + '\n' + MESSAGE 

payload = create_payload(target="ollama",
                        model = "llama3.2",
                        prompt=PROMPT, 
                        temperature=1.0, 
                        num_ctx=300, 
                        num_predict=300)

time, response = model_req(payload=payload)
if time: print(f'Time taken: {time}s')

MESSAGE = response
FEW_SHOT = "Use the given prompt to build an even better assesment"
PROMPT = FEW_SHOT + '\n' + MESSAGE 

payload = create_payload(target="ollama",
                        model="llama3.2",
                        prompt=PROMPT, 
                        temperature=1.0, 
                        num_ctx=300,
                        num_predict=300)

time, response = model_req(payload=payload)
print(response)
if time: print(f'Time taken: {time}s')
```

6. With the PROMPT TEMPLATE PROMPTING technique and using llama3.2 the prompt took 37.068s The resulting prompt response time decreased, and the information returned was detailed, however not completed at the end.
```python
MESSAGE = "My professor in GenAI SDLC has left us an assignment which consist in building a prompt eng lab in python, using the https://chat.hpc.fau.edu/ or Ollama local install LLM servers. I need to know the requirements for building an IT network that supports LAN and WAN access for voice and data applications, that is very fast and renders a good performance"

TEMPLATE_BEFORE = "You are a network architect specialist and one of your class mates in the masters asked you"
TEMPLATE_AFTER= "Respond with an excellent assesment"
PROMPT = TEMPLATE_BEFORE + '\n' + MESSAGE + '\n' + TEMPLATE_AFTER

payload = create_payload(target="ollama",
                            model = "llama3.2",
                            prompt=PROMPT, 
                            temperature=1.0, 
                            num_ctx=300, 
                            num_predict=300)
```
7. With the PROMPT TEMPLATE PROMPTING technique using llama3.2 and 1 level of automation using PROMPT TEMPLATE PROMPTING technique the first prompt took 36.885s and the second prompt 45.404s The resulting prompt response time was 82s and the information returned was very detailed, and extensive, however not complete.
```python
MESSAGE = "My professor in GenAI SDLC has left us an assignment which consist in building a prompt eng lab in python, using the https://chat.hpc.fau.edu/ or Ollama local install LLM servers. I need to know the requirements for building an IT network that supports LAN and WAN access for voice and data applications, that is very fast and renders a good performance"
TEMPLATE_BEFORE = "You are a network architect specialist and one of your class mates in the masters asked you"
TEMPLATE_AFTER= "Respond with an excellent assesment"
PROMPT = TEMPLATE_BEFORE + '\n' + MESSAGE + '\n' + TEMPLATE_AFTER

payload = create_payload(target="ollama",
                        model="llama3.2",
                        prompt=PROMPT,
                        temperature=1.0,
                        num_ctx=300,
                        num_predict=300)

time, response = model_req(payload=payload)
if time: print(f'Time taken: {time}s')

MESSAGE = response
TEMPLATE_BEFORE = "You are a Scientist in Technology and receive this information:"
TEMPLATE_AFTER= "Build an assesment based on best standards and practices"
PROMPT = TEMPLATE_BEFORE + '\n' + MESSAGE + '\n' + TEMPLATE_AFTER

payload = create_payload(target="ollama",
                        model="llama3.2",
                        prompt=PROMPT,
                        temperature=1.0,
                        num_ctx=300,
                        num_predict=300)
```

8. With the ZERO-SHOT prompting technique using open-webui the prompt took 17.214s The resulting prompt response information returned was very fast, detailed, and extensive.
```python
MESSAGE = "My professor in GenAI SDLC has left me an assignment which consists in building a Prompt Engeneering Laboratory in python, using the https://chat.hpc.fau.edu/ or Ollama local install LLM servers. I need to know the requirements for building an IT network that supports LAN and WAN access for voice and data applications, that is very fast and renders a good performance"
PROMPT = MESSAGE 

payload = create_payload(target="open-webui",
                        model = "phi4:latest",
                        prompt=PROMPT,
                        temperature=1.0, 
                        num_ctx=300, 
                        num_predict=300)
```
9. With the ZERO-SHOT prompting technique using open-webui and one level of automation using a chained ZERO-SHOT prompting technique the first prompt took 18.298s and the second prompt 19.903s The resulting prompt response information returned was somewhat fast but very detailed, and extensive.
```python
MESSAGE = "My professor in GenAI SDLC has left me an assignment which consists in building a Prompt Engeneering Laboratory in python, using the https://chat.hpc.fau.edu/ or Ollama local install LLM servers. I need to know the requirements for building an IT network that supports LAN and WAN access for voice and data applications, that is very fast and renders a good performance"
PROMPT = MESSAGE 

payload = create_payload(target="open-webui",
                        model = "phi4:latest",
                        prompt=PROMPT,
                        temperature=1.0, 
                        num_ctx=300, 
                        num_predict=300)

time, response = model_req(payload=payload)
if time: print(f'Time taken: {time}s')

MESSAGE = response
PROMPT = MESSAGE 

payload = create_payload(target="open-webui",
                        model = "phi4:latest",
                        prompt=PROMPT,
                        temperature=1.0, 
                        num_ctx=300, 
                        num_predict=300)
```
10. With the PROMPT TEMPLATE PROMPTING technique the prompt took 19.12s and the resulting prompt response information was very fast detailed, and consistent.
```python
MESSAGE = "My professor in GenAI SDLC has left us an assignment which consist in building a prompt eng lab in python, using the https://chat.hpc.fau.edu/ or Ollama local install LLM servers. I need to know the requirements for building an IT network that supports LAN and WAN access for voice and data applications, that is very fast and renders a good performance"

TEMPLATE_BEFORE = "You are a network architect specialist and one of your class mates in the masters asked you"
TEMPLATE_AFTER= "Respond with an excellent assesment"
PROMPT = TEMPLATE_BEFORE + '\n' + MESSAGE + '\n' + TEMPLATE_AFTER

payload = create_payload(target="open-webui",
                            model="phi4:latest",
                            prompt=PROMPT, 
                            temperature=1.0, 
                            num_ctx=300,
                            num_predict=300)
```

11. With the PROMPT TEMPLATE PROMPTING technique using open-webui and one level of automation using PROMPT TEMPLATE PROMPTING technique the first prompt took 16.068s and the second prompt 7.522s The resulting prompt response information returned was very detailed and short.
```python
MESSAGE = "My professor in GenAI SDLC has left us an assignment which consist in building a prompt eng lab in python, using the https://chat.hpc.fau.edu/ or Ollama local install LLM servers. I need to know the requirements for building an IT network that supports LAN and WAN access for voice and data applications, that is very fast and renders a good performance"

TEMPLATE_BEFORE = "You are a network architect specialist and one of your class mates in the masters asked you"
TEMPLATE_AFTER= "Respond with an excellent assesment"
PROMPT = TEMPLATE_BEFORE + '\n' + MESSAGE + '\n' + TEMPLATE_AFTER

payload = create_payload(target="open-webui",
                            model="phi4:latest",
                            prompt=PROMPT, 
                            temperature=1.0, 
                            num_ctx=300,
                            num_predict=300)
    
time, response = model_req(payload=payload)
if time: print(f'Time taken: {time}s')

MESSAGE = response
TEMPLATE_BEFORE = "You are a Scientist in Technology and receive this information:"
TEMPLATE_AFTER= "Build an assesment based on best standards and practices"
PROMPT = TEMPLATE_BEFORE + '\n' + MESSAGE + '\n' + TEMPLATE_AFTER

payload = create_payload(target="open-webui",
                        model="tinyllama:latest",
                        prompt=PROMPT,
                        temperature=1.0,
                        num_ctx=300,
                        num_predict=300)
```    

# Further research

New ideas of improving GenAI SDLC could be focused on the efficiency, reliability and adaptability of the GenAI outputs. Some of these concepts could be summarized into the following key points:

- Automated Prompt Optimization: develop AI techniques to refine the automated prompt generation, fine tune LLM's for prompt self improvements with reinforcement learning, Meta-learning feedback based for dynamic prompting optimization and Hyper parameter tuning for good structure prompt performance.

- Adaptive Prompting: build adaptive prompts that evolve based on software context, contextual embedding based on prompts project history, augmented memory on LLM's to retrieve past responses dynamically and multi-turn prompts that adjust based on user interaction.

- Standardized Prompting in SDLC: creating frameworks for standardizing prompt engineering across different SDLC tasks, defining prompt templates, developing benchmarks for metric evaluations and creating API's that integrate to the CI/CD pipeline.

- Multi Agent Prompting Collaboration: research on multiagent prompts in GenAI systems for different models collaboration using specialized prompts, distributed prompting for multiple LLM handling SDLC tasks, multiagent coordination for debugging, testing and risk analysis and hierarchical prompting where on AI' verifies another's output.

- Trust, Bias Mitigation and Explainability in Prompts: make GenAI driven software more trustworthy and transparent, explainable AI for prompt responses (how output was generated), bias reduction techniques and Ethical prompt design.


