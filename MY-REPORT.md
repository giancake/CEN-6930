![GenI-Banner](https://github.com/genilab-fau/genial-fau.github.io/blob/8f1a2d3523f879e1082918c7bba19553cb6e7212/images/geni-lab-banner.png?raw=true)

# Wilders Prompt Engeering Lab

In This Lab we seek to execute different Prompting Techniques in our Prompting Lab and test the Ollama local installs and the FAU open-webui servers. We will do the requierment analysis for using Prompt Engineering to find out our best solution description, making use of the GenAI Pipelines. This Lab is a hands-on experiences with diverse techniques around Prompt Engineering to get thinking about different Prompts, Pipelines, and Models.

<!-- WHEN APPLICABLE, REMOVE THE COMMENT MARK AND COMPLETE
This is a response to the Assignment part of the COURSE.
-->

* Authors: [Wilder Villacorta](https://github.com/giancake/PromptEngineeringLab.git)
* Academic Supervisor: [Dr. Fernando Koch](http://www.fernandokoch.me)


# Research Question

Generate a prompt utilizing the GenAI Prompt Engeneering Techniques. We will use the following prompt for our experiment:
"My professor in GenAI SDLC has left me an assignment which consists in building a Prompt Engeneering Laboratory in python, using the https://chat.hpc.fau.edu/ or Ollama local install LLM servers. I need to know the requirements for building an IT network that supports LAN and WAN access for voice and data applications, that is very fast and renders a good performance"

## Arguments

#### What is already known about this topic

* We know that pipelines play a crucial role in managing the end to end process of developing, tuning, and mantaining AI models. GenAI pipelines, are a strucutred sequence of automated steps, designed to fine tune, test and deploy generative AI models. Among the different types of pipelines, there exist Data pipelines that handle, clean, transform and augment the data which are esential for ensuring high quality for training and fine tunning models.

* The challenges of Gen AI SDLC pipelines may include the data handling because it requires extensive cleaning, augmentation and labeling, handling biases and ensuring data diversity. The data privacy and security could be at risk of exposing sensitive information when trainig real-world model datasets, there are alos scalability challenges in data handling, because LLM's requiere massive datasets leading to high high storage and processing costs.

* Model training requires high computational CPU/GPU energy consumption costs. Fine tunning and modeling could be catastrophic new data can lead to the model forgetting earlier knowledge.

#### What this research is exploring

<!-- Free-format; use the topics that are applicable to your exploration  -->

* The GenAI SDLC Prompt Engineering Lab is exploring how to build a structured prompt engineering framework using Python language.
* Developing a Lab environment using local Ollama or the FAU servers and experimenting with different prompting techniques.
* We are exploring the automation of prompt prompt evaluation, creating pipelines to refine and evaluate prompts systematically

#### Implications for practice

<!-- Free-format; use the topics that are applicable to your exploration  -->

* it will be easier to {do something}
* it will optimize {some process}
* we will better understand {some process}
* ...

# Research Method

Combination of Experimental, Iterative and Comparative Analysis Research

<!-- WHEN APPLICABLE AND AVAILABLE -->

# Results

With the ZERO-SHOT prompting technique and using llama 3.2 the prompt took 71.51s to generate. The resulting prompt was very short in context but important.
```python
payload = create_payload(target="ollama",
                            model = "llama3.2",
                            temperature=1.0, 
                            num_ctx=100, 
                            num_predict=100)
```

With the ZERO-SHOT prompting technique and using llama 3.2 the prompt took 78.40s The resulting prompt was more detailed and extensive but the resulting prompt wasn't fully complete.
```python
payload = create_payload(target="ollama",
                            model = "llama3.2",
                            temperature=1.0, 
                            num_ctx=300, 
                            num_predict=300)
```

With the FEW-SHOT prompting technique and using llama 3.2 the prompt took 17.53s The result prompt was much more faster but very short and not extensive nor detailed.
```python
payload = create_payload(target="ollama",
                            model = "llama3.2",
                            prompt=PROMPT, 
                            temperature=1.0, 
                            num_ctx=100, 
                            num_predict=100)
```

With the FEW-SHOT prompting technique and using llama 3.2 the prompt took 91.23s The resulting prompt delayed more to be returned and the prompt information was more extensive, however not complete at the end.
```python
payload = create_payload(target="ollama",
                            model = "llama3.2",
                            prompt=PROMPT, 
                            temperature=1.0, 
                            num_ctx=300, 
                            num_predict=300)
```

With the PROMPT TEMPLATE PROMPTING technique and using llama 3.2 the prompt took 84.68s The resulting prompt delayed more to be returned and the information was more extensive, however not  completed at the end.
```python
payload = create_payload(target="ollama",
                            model = "llama3.2",
                            prompt=PROMPT, 
                            temperature=1.0, 
                            num_ctx=300, 
                            num_predict=300)
```
# Further research

Describe what we could do next and propose new ideas for further research.
