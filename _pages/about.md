---
permalink: /
title: ""
excerpt: "About"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

About
======

I am **Claire (Nayoung) Kim**, a Computer Science Ph.D. candidate at the [School of Computing and Augmented Intelligence (SCAI)](https://scai.engineering.asu.edu/) at Arizona State University. My research advances trustworthiness and truthfulness in AI, with the goal of building fair, robust, and accurate NLP and LLM systems &mdash; spanning fairness, bias mitigation, robustness, and human-centered evaluation.

I have worked as a research assistant at the [DHS Center for Accelerating Operational Efficiency (CAOE)](https://caoe.asu.edu/) and the Data Mining and Machine Learning (DMML) Lab, advised by [Dr. Huan Liu](https://scholar.google.com/citations?hl=en&user=Dzf46C8AAAAJ) and [Dr. Mickey Mancenido](https://scholar.google.com/citations?user=f_0QDJUAAAAJ&hl=en). I previously earned my B.S. and M.E. at Korea University, where I was advised by [Dr. Jaewoo Kang](https://dmis.korea.ac.kr/home).

<div class="open-to">
<strong>Currently seeking</strong> full-time <strong>Applied Scientist / ML Engineer / Research Scientist</strong> roles starting Summer 2026.
</div>

<a class="btn btn--primary" href="{{ base_path }}/files/ClaireKim_resume.pdf"><i class="fas fa-file-pdf"></i> Download Resume</a>


Experience
------
* **Applied Scientist Intern**, Amazon &mdash; Bellevue, WA · Fall 2025
* **AI/ML Intern**, AMD &mdash; Austin, TX · Fall 2024 & Summer 2025
* **Research Assistant**, DHS-CAOE &mdash; Tempe, AZ · 2022 – 2025
* **Research Assistant**, ASU DMML Lab &mdash; Tempe, AZ · 2021 – 2022
* **Research Assistant**, Korea University DMIS Lab &mdash; Seoul, KR · 2017 – 2019


Skills
------
<div class="skills" markdown="0">
  <div class="skill-row"><div class="skill-label">Languages</div><div class="skill-list">Python, SQL, JavaScript</div></div>
  <div class="skill-row"><div class="skill-label">ML & DL</div><div class="skill-list">PyTorch, TensorFlow, Hugging Face (Transformers, PEFT, Accelerate, Datasets), Pandas, NumPy</div></div>
  <div class="skill-row"><div class="skill-label">Fine-tuning</div><div class="skill-list">Supervised fine-tuning (SFT) · classification · forecasting · RLHF · parameter-efficient methods (LoRA, P-tuning)</div></div>
  <div class="skill-row"><div class="skill-label">LLM Systems</div><div class="skill-list">RAG, vector DBs (Weaviate, Chroma, Faiss), LLM-as-a-judge, synthetic QA generation, multi-agent LLM, hallucination mitigation, prompt engineering, inference-time scaling</div></div>
  <div class="skill-row"><div class="skill-label">Frameworks</div><div class="skill-list">LangChain, LlamaIndex, Node.js, Flask, Streamlit</div></div>
  <div class="skill-row"><div class="skill-label">AI-Assisted Dev</div><div class="skill-list">Claude Code, Cursor, GitHub Copilot, agentic coding workflows, MCP (Model Context Protocol)</div></div>
  <div class="skill-row"><div class="skill-label">Production & MLOps</div><div class="skill-list">End-to-end pipelines, model serving, Python packaging, inference optimization (throughput / latency), AWS (SageMaker, S3, Redshift, Glue, Lambda), GCP, Docker, WandB, MLflow</div></div>
  <div class="skill-row"><div class="skill-label">NLP & Models</div><div class="skill-list">Claude, GPT-4o, Llama-3, Mistral, DeepSeek, BERT · topic modeling, sentiment & stance detection, text summarization</div></div>
  <div class="skill-row"><div class="skill-label">Methods & Tooling</div><div class="skill-list">Bayesian inference &amp; uncertainty quantification · Git · Linux / shell · Jupyter</div></div>
</div>


News
------
* **Fall 2025** &mdash; Joined Amazon as an Applied Scientist Intern (Bellevue, WA).
* **2025** &mdash; *PADTHAI-MM* paper accepted to *AI Magazine*.
* **Summer 2025** &mdash; Returning to AMD as an AI/ML Intern (Austin, TX).
* **Fall 2024** &mdash; Joined AMD as an AI/ML Intern (Austin, TX).
* **2024** &mdash; *Robust Stance Detection* paper accepted at ASONAM 2024.


Selected Projects
------

**Reasoning-Level Fairness in LLMs** &mdash; *Under submission*\
Built a reasoning-aware framework for bias mitigation in LLMs, modeling reasoning as Q → {R} → A. Introduced the **Reasoning Bias Rate (RBR)** metric and a hybrid pipeline of process supervision, fairness-aware RL, and inference-time guided decoding. Reduced BBQ bias scores by **>20%** while preserving accuracy within 1% on GPT-3.5 and LLaMA-2.\
*Tech: Python · PyTorch · OpenR · Inference-time scaling · Fairness-aware RL*

**Towards Fair Language Modeling via Parameter-Efficient Methods** &mdash; *2024*\
Mitigated social biases in T5, BERT, and LLaMA-2 for toxicity and hate-speech detection using RL combined with parameter-efficient tuning (LoRA, P-tuning).\
*Tech: Python · PyTorch · Hugging Face · LoRA · RL*

**MEGAWATT: MAST for Evaluating Generative AI** &mdash; *2024*\
Applied the MAST trust-assessment framework to evaluate GPT-4 in intelligence-analysis tasks; ran human-subject studies and improved response quality with prompt engineering and RAG.\
*Tech: Python · GPT-4 API · RAG · Human-subject study design*

See the [full project list]({{ base_path }}/projects/).


Selected Publications
------

**PADTHAI-MM: A Principled Approach for the Design of Trustworthy, Human-Centered AI Systems Using the MAST Methodology**\
Myke C. Cohen, **Nayoung Kim**, Yang Ba, et al.\
*AI Magazine, 2025.*\
[[pdf](https://arxiv.org/pdf/2401.13850.pdf)] [[code](https://github.com/nayoungkim94/PADTHAI-MM)]

**Robust Stance Detection: Understanding Public Perceptions in Social Media**\
**Nayoung Kim**, David Mosallanezhad, Lu Cheng, Michelle V. Mancenido, Huan Liu\
*ASONAM, 2024.*\
[[pdf](https://browse.arxiv.org/pdf/2309.15176.pdf)] [[code](https://github.com/Davood-M/RobustStanceDet)]

**Debiasing Word Embeddings with Nonlinear Geometry**\
Lu Cheng, **Nayoung Kim**, Huan Liu\
*COLING, 2022.*\
[[pdf](https://arxiv.org/pdf/2208.13899.pdf)] [[code](https://github.com/GitHubLuCheng/Implementation-of-JoSEC-COLING-22)]

See the [full publication list]({{ base_path }}/publications/).
