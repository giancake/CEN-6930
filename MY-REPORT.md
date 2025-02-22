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

* Perform the requierement analysis to achieve the solution description.
* the challenges of {doing something}
* the possibility of {doing something else}
* ...

#### What this research is exploring

<!-- Free-format; use the topics that are applicable to your exploration  -->

* we employ {some technique}
* we are building {something}
* we are exploring {some idea or technology}

#### Implications for practice

<!-- Free-format; use the topics that are applicable to your exploration  -->

* it will be easier to {do something}
* it will optimize {some process}
* we will better understand {some process}
* ...

# Research Method

Describe how you are building this research process.

<!-- WHEN APPLICABLE AND AVAILABLE -->

# Results

With the ZERO-SHOT configuration it took 71.51s The result Answer was short but very important.

payload = create_payload(target="ollama",
                            model = "llama3.2",
                            temperature=1.0, 
                            num_ctx=100, 
                            num_predict=100)

With the ZERO-SHOT configuration it took 78.40s The result Answer was mode detailed and extensive but it didn't complete the prompt at the end.

payload = create_payload(target="ollama",
                            model = "llama3.2",
                            temperature=1.0, 
                            num_ctx=300, 
                            num_predict=300)

With the FEW-SHOT configuration it took 17.53s The result Answer was much more faster but very short and tight, not as extensive and detailed.

payload = create_payload(target="ollama",
                            model = "llama3.2",
                            prompt=PROMPT, 
                            temperature=1.0, 
                            num_ctx=100, 
                            num_predict=100)

With the FEW-SHOT configuration it took 91.23s The result Answer was much lenghtier, but the information was more extensive, however not  completed at the end.

payload = create_payload(target="ollama",
                            model = "llama3.2",
                            prompt=PROMPT, 
                            temperature=1.0, 
                            num_ctx=100, 
                            num_predict=100)

With the PROMPT TEMPLATE PROMPTING configuration it took 84.68s The result Answer was much lenghtier, but the information was more extensive, however not  completed at the end.

payload = create_payload(target="ollama",
                            model = "llama3.2",
                            prompt=PROMPT, 
                            temperature=1.0, 
                            num_ctx=300, 
                            num_predict=300)

# Further research

Describe what we could do next and propose new ideas for further research.
