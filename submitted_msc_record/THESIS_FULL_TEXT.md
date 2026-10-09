# Application of Machine Learning Modeling in NOAA SHARP Data for Solar Flare Prediction

**Mohamed Fawaz Hussain Fareed**  
MSc Data Science · Cardiff Metropolitan University · Submitted August 2024

**Read the original dissertation:** [Authoritative submitted PDF · 66 pages](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view)  
**Explore the research:** [Repository overview](../README.md) · [2024 methods](../docs/METHODS_SUBMITTED.md) · [Separate 2026 evaluation](../docs/RESEARCH_REVIEWER_GUIDE.md)

> **About this edition:** A structured reading copy of the submitted 2024 dissertation. Its chapters, headings, line wrapping and references have been formatted for accessible GitHub reading; the assessed findings and historical wording have not been substantively rewritten. The original figures, screenshot tables, equation artwork, signatures and page layout are available in the **submitted PDF** at the links provided throughout. The original raw text extraction remains [archived unchanged](THESIS_SOURCE_EXTRACTION_ARCHIVE.md). The separate 2026 research code and results do not retroactively change the 2024 submission.

**Original source SHA-256:** `29be1acce2a8fc43bfd731e71440ca66e0cd3f2af38275cabfe7d18b0d7d8a66` · **Size:** 3,644,962 bytes

## Contents

- [Declaration](#declaration)
- [Abstract](#abstract)
- [Acknowledgement](#acknowledgement)
- [Figures and tables](#figures-and-tables-in-the-submitted-pdf)
- [Chapter 1. Introduction](#chapter-1-introduction)
  - [1.1 Research Background](#11-research-background)
  - [1.2 Research Rationale, Significance, and Motivation](#12-research-rationale-significance-and-motivation)
  - [1.3 Research Aim](#13-research-aim)
  - [1.4 Research Objectives](#14-research-objectives)
  - [1.5 Research Questions](#15-research-questions)
- [Chapter 2. Literature Review](#chapter-2-literature-review)
  - [2.1 Recent Work in Solar Flare Prediction](#21-recent-work-in-solar-flare-prediction)
  - [2.2 Why Machine Learning?](#22-why-machine-learning)
  - [2.3 What are the Research Gaps and What to Consider?](#23-what-are-the-research-gaps-and-what-to-consider)
  - [2.4 Sampling Techniques to Tackle Class Imbalance](#24-sampling-techniques-to-tackle-class-imbalance)
  - [2.5 Validation Techniques and Their Importance in Solar Flare Prediction](#25-validation-techniques-and-their-importance-in-solar-flare-prediction)
  - [2.6 Variable Selection](#26-variable-selection)
  - [2.7 Prominent Datasets Applied in Existing Literature](#27-prominent-datasets-applied-in-existing-literature)
- [Chapter 3. Methodology](#chapter-3-methodology)
  - [3.1 Introduction to Dataset](#31-introduction-to-dataset)
  - [3.2 Exploratory Data Analysis (EDA)](#32-exploratory-data-analysis-eda)
  - [3.3 Modeling](#33-modeling)
- [Chapter 4. Prediction Results and Discussion](#chapter-4-prediction-results-and-discussion)
  - [4.1 BACC and TSS Results for Original Dataset](#41-bacc-and-tss-results-for-original-dataset)
  - [4.2 BACC and TSS Results for 100 Under-Sampled Datasets](#42-bacc-and-tss-results-for-100-under-sampled-datasets)
  - [4.3 BACC and TSS Results for 100 Over-Sampled Datasets](#43-bacc-and-tss-results-for-100-over-sampled-datasets)
  - [4.4 Overall BACC and TSS Results](#44-overall-bacc-and-tss-results)
- [Chapter 5. Conclusion and Recommendations](#chapter-5-conclusion-and-recommendations)
  - [5.1 Review of Research Objectives and Research Questions](#51-review-of-research-objectives-and-research-questions)
  - [5.2 Research Implications and Contributions](#52-research-implications-and-contributions)
  - [5.3 Recommendations and Future Work](#53-recommendations-and-future-work)
  - [5.4 Research Limitations](#54-research-limitations)
- [Chapter 6. References](#chapter-6-references)

---

## Declaration

I hereby declare that this dissertation entitled ‘Application of Machine Learning Modeling in NOAA SHARP data for Solar Flare Prediction’ is entirely my own work and it has never been submitted nor is it currently being submitted for any other degree. Mohamed Fawaz Hussain Fareed 02/08/2024 Candidate Signature Date Supervisor Signature

## Abstract

Solar flare prediction has a significant role in comprehending and forecasting space weather as well as mitigating consequences of solar flares in and around earth. The primary objective of the Helioseismic and Magnetic Imager (HMI), (a tool housed within the Solar Dynamics Observatory under NASA's supervision), is to understand the origins and evolution of solar fluctuations and interpret the magnetic behavior of the Sun. HMI offers uninterrupted panoramic views of the solar vector magnetic field, accompanied by frequent data updates, that enhance reliable predictive capacities. Nevertheless, solar flare prediction effort applying these data is remains somewhat constrained. 

This dissertation aims to evaluate the performance of various machine learning algorithms on solar flare data, and suggest a suitable machine learning algorithm for solar flare prediction. The first step of the research involves in analyzing the recent work in solar flare prediction which answers questions such as what are the datasets been used so far, what kind of machine learning algorithms applied, what are the research gaps, this study can focus on. Moreover, a comprehensive review of existing literature is conducted to identify the most significant SHARP parameters previously highlighted by researchers which are crucial for assessing solar activity and are used extensively in predicting solar flares. This review was instrumental in choosing a potential solar flare dataset which contains these sharp parameters. Since most of the solar flare datasets are imbalanced (solar flare datasets always include a small number of X class flares because if its rarity), it was essential to look at dedicated sampling and validation techniques such as SMOTE and stratified K fold cross validation to tackle class imbalance. 

After identifying the most suitable dataset, the data analysis and methodology phase involved Exploratory Data Analysis (EDA) and research moves on to training and testing data utilized from the SHARP physical parameters and categorize solar flares into four classes such as B, C, M and X, in accordance with the X-ray flare catalogs available at the NCEI. Furthermore, this study investigates the effectiveness of both conventional and high-performance algorithms using the chosen dataset, 100 under-sampled and 100 oversampled versions of the original dataset. This research has conducted 29400 tests overall before choosing a suitable prediction model. 

Finally, the research, discusses the implications of the results, identifying a suitable algorithm for solar flare prediction and offering recommendations for future work. The research demonstrates that high-performance algorithms like Extra Trees Classifier and Random Forest Classifier, combined with effective sampling strategies, significantly enhance the ability predict solar flares, thereby providing a robust framework for future studies and applications in this area. Overall, this dissertation provides a comprehensive analysis of machine learning algorithms for imbalanced solar flare datasets, contributing valuable insights and practical guidelines for researchers and practitioners in the field.

## Acknowledgement

First of all, I want to thank my mother, my brother and my family for sending all the way from Sri Lanka to UK to pursue my Master’s degree. I owe everything in my life to them and I am grateful I have got them. Moreover, I want to take this opportunity to thank my mentor and supervisor Dr, Amrita Prasad, for advising me throughout this dissertation. Her insights, suggestions, expertise in Astro Physics and Solar Flare Prediction, and feedback are the pillars which made thesis a more refined and presentable work. And her constructive criticism, made sure this research and the approaches used in this research are well questioned, and aligned with the practical application. I feel grateful for her guidance, and motivation. Moreover, I want to express my sincere thanks to each and every person who have helped me throughout this year. This has been a year of sacrifices, hardship, dedication and tears. And I had the opportunity to meet some of the wonderful, kind hearted people in this journey which I am grateful for. Finally, I want to give my thanks to Cardiff School of Technology and the University for giving me this great opportunity to take part in this program and giving me all the equipment to complete this course.

## Figures and tables in the submitted PDF

The figures below can be viewed in the [original submitted document](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view). Captions are retained as submitted, including any original caption inconsistencies.

| Figure | Original caption | PDF page |
|---:|---|---|
| 1 | Initial Conceptual Framework (Generated by Visio) | [p. 24](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=24) |
| 2 | Updated Conceptual Framework (Generated by Visio) | [p. 28](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=28) |
| 3 | Thirteen SHARP Parameters Used in the Research – Descriptions of the Parameters derived from Abduallah et al. (2021) | [p. 30](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=30) |
| 4 | Code Snippet for Removing the Last Two Digits of Solar Flare Classes | [p. 30](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=30) |
| 5 | Initial Data frame Visualization | [p. 31](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=31) |
| 6 | Overall Statistics of DeepSun Solar Flare Dataset | [p. 31](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=31) |
| 7 | Code Snippet for MinMax Normalization | [p. 32](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=32) |
| 8 | Data Distribution of Numerical Columns (SHARP Parameters and AR) – Generated in Google Collaboratory | [p. 33](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=33) |
| 9 | Data Distribution of Solar Flare Classes – Generated in Google Collaboratory | [p. 35](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=35) |
| 10 | Code Snippet for Under-Sampling with Random Under-Sampler | [p. 36](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=36) |
| 11 | Code Snippet for Over-Sampling with SMOTE | [p. 37](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=37) |
| 12 | Feature Correlation Matrix for SHARP Parameters and AR – Generated in Google Collaboratory | [p. 38](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=38) |
| 13 | Stratified K Fold Cross Validation (Pramod 2024) | [p. 42](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=42) |
| 14 | Code Snippet for Defining Stratified K Fold Cross Validation and Implementation . | [p. 43](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=43) |
| 15 | Code Snippet for Calculating BACC per Class and Algorithm | [p. 45](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=45) |
| 16 | Code Snippet for Calculating BACC per Class and Algorithm | [p. 46](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=46) |
| 17 | BACC Results for Original Dataset | [p. 47](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=47) |
| 18 | TSS Results for Original Dataset | [p. 47](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=47) |
| 19 | BACC Results for 100 Under-Sampled Datasets | [p. 48](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=48) |
| 20 | TSS Results for 100 Under-Sampled Datasets | [p. 49](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=49) |
| 21 | BACC Results for 100 Over-Sampled Dataset | [p. 50](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=50) |
| 22 | TSS Results for 100 Under-Sampled Datasets | [p. 50](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=50) |
| 23 | Average BACC Results for Each Class Per Algorithm | [p. 51](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=51) |
| 24 | Average TSS Results for Each Class Per Algorithm | [p. 52](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=52) |

**Table 1:** Numbers of Flares and ARs per Flare Class (Abduallah et al. 2021) · [PDF p. 29](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=29).

**Equations:** MinMax normalization ([p. 32](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=32)); Balanced Accuracy ([p. 44](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=44)); True Skill Statistic ([p. 45](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=45)).

---

## Chapter 1: Introduction

### 1.1 Research Background

In layman's terms, Solar flares are large outbursts of electromagnetic radiation created from the sun, with a duration of minutes to hours. These events happen during the stored free energy in highly non-potential magnetic fields within solar active regions (ARs) is promptly discharged.

Solar flares and the often-associated coronal mass ejections (CMEs) seriously affect the near-earth habitat and the space environment in close proximity to Earth. These major solar events, affect human life to microbial organisms as we know it. Moreover, since most of the modern technology and infrastructure in and around Earth depend on satellites and electromagnetic waves, solar flares pose a significant threat to day-to-day life and life in space. (Kusano et al. 2023) According to Chen et al. (2019), Solar flares of the highest severity start from the intense kilogauss fields in Active Regions (ARs). The release of magnetic energy occurs across a wide range of scales, ranging from the most energetic flares (10^32−33 erg) associated with fast CMEs to the ongoing presence of Nano flares that might contribute to the heating of the quiescent corona (10^22−24 erg).

Solar flare intensities have a vast range of values and are categorized according to the highest emission detected within the 0.1 – 0.8 nm spectral range (soft x-rays) of the NOAA/GOES XRS.

The classification system for X-ray flux starts with the “A” level (usually starting at 10-8 W/m2), moving up to the next category, which is ten times greater, referred to as the “B” level (≥ 10-7 W/m2); followed by “C” flares (10-6 W/m2), “M” flares (10-5 W/m2), and finally “X” flares (10- 4 W/m2) which are the most powerful and destructive. The classification of radio blackouts is determined using a five-level NOAA Space Weather Scale, which is directly associated with the maximum peak of soft X-rays observed or anticipated during a flare. The Space Weather Prediction Center (SWPC) currently issues forecasts regarding the probability of C, M, and X-class flares and establishes correlations with the likelihood of R1-R2, and R3 or severe events as part of the 3-day forecast and forecast discussion services. SWPC also issues an alert in case of an M5 (R2) flare occurrence. (NASA, 2011) The NOAA Space Weather Scales (2018) documented a prevalence of over 2,000 M-class flares during solar cycle 24, contrasting with fewer than 180 X-class flares. Moreover, as outlined by Baker, H (2023), the year 2023 witnessed a total of 12 X-class flares, surpassing the cumulative count observed in the preceding five years. Numerous occurrences featured the expulsion of magnetized plasma clouds, identified as coronal mass ejections (CMEs), which subsequently interacted with Earth. Particularly noteworthy was an unforeseen flare that originated from the remote side of the sun and reached Earth, along with another incident that triggered a phenomenon known as a "solar tsunami," and an eruption emerging from a sunspot of proportions ten times greater than that of Earth.

Meteorologist Covey, Z (2023) asserts that the solar activity report for Solar Cycle 25 was officially released by the Space Weather Prediction Center of NOAA in December 2019.

Anticipation among scientists was centered on a diminished intensity in this specific solar cycle, foreseeing the peak of solar activity to occur between 2023 and 2026. Moreover, the expert panel predicted a range of 95 to 130 sunspots during the anticipated peak of solar activity. A revised forecast was subsequently issued by the Space Weather Prediction Center (SWPC) last December, suggesting that Solar Cycle 25 is likely to demonstrate a higher level of intensity than initially anticipated, characterized by an escalation in sunspot activity in the initial ten months of 2024.

Abduallah et al. (2021) stated that observing and measuring the configuration and advancement of the photospheric magnetic field can offer valuable insights and indications regarding the initiation mechanisms of solar flares and coronal mass ejections. Various physical attributes or variables, which will be further elaborated in this report, are indicative of the stationary nature of the photospheric magnetic field, including the total Lorentz force, injection of magnetic helicity, the magnitude of unsigned magnetic flux, presence of vertical electric currents, magnetic shear, and gradient, as well as the dissipation of magnetic energy.

### 1.2 Research Rationale, Significance, and Motivation

The solar flares release electromagnetic radiation, energetic particles, and magnetized plasma into space, potentially causing disturbances on Earth. With the commencement of solar cycle 25, an increasing number of solar flare occurrences that could disrupt daily activities are expected.

Therefore, accurate and timely forecasting of solar flares is more crucial than ever for disaster risk reduction, mitigation, and readiness. Particularly, the prediction of M- and X-class flares is essential to lessen their damaging impacts (Zhang et al. 2022). The complexity of solar flares, in conjunction with their sporadic occurrence of high-energy phenomena, presents a formidable challenge in the early and precise forecasting of solar flares. An additional factor complicating data-driven approaches is the significant computational resources required for the thorough analysis of frequent and detailed solar observations over an extended period. In recent years, there has been a growing emphasis on using machine-learning techniques for predicting solar flares, prompting a critical assessment of past research gaps and the imperative need to develop a more precise machine-learning model capable of forecasting solar flares within a timeframe conducive to mitigating their potential consequences. (Chen et al. 2019) Researchers have spent considerable amounts of time investigating the correlation between flare productivity and non-potentiality of active regions (ARs) as specified by the physical parameters.

Yasser et al. (2023) suggest that the present focus on the prediction of solar flares has progressed from the use of statistical models based on the attributes of ARs to the application of machine learning methods, particularly exploring deep learning and federated learning approaches like neural networks and convolutional neural networks (CNNs). Machine learning enables computer programs with the capacity to acquire knowledge from data and enhance performance gradually.

This involves the utilization of input data, known as training data, to uncover concealed patterns within the data, allowing for the development of a predictive model. This model is subsequently applied to make predictions on new, unseen test data. Nonetheless, their study highlights that, despite the progress made, the development of accurate and efficient real-time forecasting models for solar flares remains highly challenging, thereby motivating to explore new machine learning algorithms and validation techniques proposed in this study. Therefore, this research will focus on predicting solar flares by utilizing a variety of machine-learning algorithms and data validation techniques such as cross-validation, under-sampling, and oversampling.

### 1.3 Research Aim

The primary aim of the research is to suggest a most suitable predictive machine learning algorithm to predict whether an active region (AR) on the Sun will produce a γ-class solar flare (≥M5.0, ≥M, or ≥C) within the next 24 hours. In terms of modeling, we require a solar flare dataset. Hence a dataset has been chosen after researching many previous studies of solar flare prediction. The chosen dataset consists within a database of solar flare events considering the physical parameters provided by the Space-weather HMI Active Region Patch (SHARP), and has classified solar flares into four major classes, namely B, C, M and X, based on the X-ray flare catalogs available at the National Centers for Environmental Information (NCEI).

### 1.4 Research Objectives

In accordance with the research aim, the research objectives are as follows: O1.Analyze present datasets in the NOAA database which includes the SHARP parameters identified and choose the most suitable dataset.

O2.Review and rigorously analyze relevant past literature to determine the most significant and iterative SHARP parameters from previous literature to formulate hypotheses.

O3.Perform EDA to get a sense of the chosen data and to make informed decisions according to observations and correlations. O4.Identify machine learning algorithms that gave the best and least accuracies in working with solar flare dataset chosen.

O5.Consider several validation techniques and identify which kind of machine learning approach would be most appropriate to the selected dataset.

### 1.5 Research Questions

According to the research objectives listed above, the research questions that the proposed research will try to answer are as follows: R1.What are the research gaps in the existing literature in terms of predicting solar flares?

R2.What kind of datasets are available in predicting solar flares and are these datasets accessible? R3.What are the most significant SHARP parameters that impact solar flare prediction?

R4.What are the machine learning approaches and algorithms most suitable for predicting solar flares according to the chosen dataset and previous work?

R5.What validation techniques can be used to ensure the accuracy of the developed models?

## Chapter 2: Literature Review

### 2.1 Recent Work in Solar Flare Prediction

ML Modeling has been applied in the prediction of solar flares, for nearly two decades following their application in analyzing the impact of solar storms on Earth (Chen et al. 2019). Several research teams, namely (Abduallah et al. 2023), (Zhang et al. 2022), (Chen et al. 2019), (Huang et al. 2018), (Ahmed et al. 2011), and (Song et al. 2008) have forecasted solar flares utilizing data-driven algorithms trained with parameters obtained from mappings of the line-of-sight section of the photospheric magnetic field recorded by the Michelson Doppler Imager instrument onboard the Solar and Helio-spheric Observatory spacecraft.

In terms of solar flare prediction research, recent efforts have been dedicated to enhancing prediction accuracy and interpretability. A key focus has been on the utilization of data-driven techniques like the Flare Transformer model, which integrates physical attributes and images, as well as the incorporation of the Reuven Ramaty High Energy Solar Spectroscopic Imager (RHESSI) dataset to bolster predictive capabilities (Moulshree et al. 2022). Consequently, the primary objective of this study is to heighten prediction accuracy and interpretability. Despite the potential shown by datasets like RHESSI, this research has opted for a dataset that encompasses the crucial variables identified in previous studies.

Moreover, according to previous literature, challenges such as class imbalance and data validation have become unavoidable considering the complexity of solar flare data and the domination of occurrence in M-class solar flares in the previous decade. Researchers have explored techniques like synthetic oversampling of magnetograms to reduce data imbalances (Amar and Ben-Shahar 2024), developed attention-based deep learning models for full-disk flare predictions with improved TSS (True Skill Statistics) and BACC (Balanced Accuracy) scores (Pandey et al. 2023), and employed multivariate time series learning algorithms to predict solar flares based on magnetic field parameters, showcasing the effectiveness of MINIROCKET (a time-series classification algorithm) in handling class-imbalanced datasets without extensive preprocessing (Saini et al. 2024). These studies highlight the importance of leveraging advanced computational methods to enhance the accuracy and reliability of solar flare predictions while also emphasizing the significance of data validation techniques to ensure the robustness of forecasting models.

### 2.2 Why Machine Learning?

When it comes to solar flare prediction history, most studies have centered their attention on deep learning as opposed to machine learning. For example, Nishizuka et al. (2018), created deep neural networks for the prediction of M- and C-class flares within a 24-hour timeframe by utilizing data sourced from the Solar Dynamics Observatory (SDO) and the Geostationary Operational Environmental Satellite (GOES). Sun et al. (2022) utilized 3D CNNs to predict ≥M-class and ≥C-class flares by leveraging SHARP magnetograms from the Joint Science Operations Center (JSOC). Deshmukh et al. (2023) contends that preceding studies in solar flare prediction have consistently progressed from simple to complex machine-learning models. Moreover, it has been observed that less elaborate models with a reduced number of parameters typically outperform their more intricate counterparts, thereby highlighting the significance of the feature selection.

Likewise, many deep learning models have been developed to predict solar flares with complex approaches, whereas machine learning modeling has been overlooked in the recent past but many new machine learning algorithms have been neglected and remain unutilized. This study does not argue that efforts to utilize new modeling techniques such as deep learning and federated learning should be totally dropped but be encouraged, however, it is always best to go back to basics and utilize the new machine learning approaches as well while applying deep and federated learning.

One major purpose of this study is to encourage researchers to consider all possible routes in prediction of solar flares. Moreover, machine learning should be considered in solar flare prediction due to its effectiveness in handling multivariate time series data from active region magnetic parameters, as demonstrated by various state-of-the-art classifiers like MINIROCKET, CIF, and Mr-SEQL (Saini et al. 2024).

Additionally, machine learning models offer reliable forecasting capabilities, crucial for mitigating the risks posed by solar flares to human technology (Francisco et al. 2024). According to Saini et al. (2024) the use of machine learning algorithms allows for the creation of operational systems like SolarFlareNet, capable of making near real-time predictions of solar flares on the Web too.

Moreover, machine learning techniques, such as those employed in the SWAN-SF benchmark dataset, have shown superior performance in predicting solar flares, surpassing deep learning models without the need for extensive data preprocessing steps. Therefore, machine learning stands out as a robust and efficient method for solar flare prediction, offering accurate forecasts and operational utility in real-time scenarios. Thus, the focal point of this study will revolve around machine learning and strategies to enhance the accuracy and interpretability of machine learning models in the domain of solar flare prediction.

### 2.3 What are the Research Gaps and What to Consider?

According to previous literature, there are multiple research gaps in predicting solar flares. For instance, the present models created in the past research have not comprehensively explored the influence of outliers and validation techniques on prediction reliability (Wen et al. 2023).

Furthermore, despite the increase in model complexity, there has been minimal progress in the development of feature sets and machine learning algorithms approaches in solar flare prediction.

Surprisingly, in recent studies, simpler models have frequently demonstrated superior performance compared to their more complex counterparts. This highlights the necessity for a reassessment of feature selection strategies (Deshmukh et al. 2023). Moreover, the absence of dependable physical models concerning flare eruption mechanisms underscores the dependence on data-driven methodologies, highlighting the necessity for additional progress in comprehending solar flare phenomena (Han et al. 2023). These research gaps allow researchers to explore techniques such as outlier detection and removal evaluation, validation techniques implementation, and feature selection strategies re-evaluation, to enhance reliability and increase accuracy in predictive models of solar flares. This research has tried to address all these research gaps in data analysis.

When it comes to machine learning algorithms utilized, Zhang et al. (2022) state that past research has employed a variety of algorithms such as KNN, RF, Conventional Decision Trees, LSTM, GBM Series, SVM, etc. Hence, this research has initially focused on replicating the models that had the best accuracies according to past literature and exploring further into high performance models such as GBM, Extra Tress, Linear Discriminant Analysis. Moreover, Zhang and his colleagues highlight the usage of imbalanced data samples in data analysis, which results in inadequate forecasting of high-intensity solar flares like X-class flares. This motivates the necessity of employing sophisticated resampling approaches such as the Synthetic Minority Oversampling Technique for Regression with Gaussian Noise (SMOGN) to enhance the reliability of prediction models. The datasets employed in most studies had a class imbalance issue because of the fewer instances of X class flares. Hence this research may have to employ sampling techniques to tackle the class imbalance. This research will unravel which model predicts which class with the highest accuracy. For example, the Extra Trees algorithm may predict X solar flares with the best accuracy while predicting other classes with rather low accuracies. It can be concluded that Extra Tress algorithm is most suitable in predicting X class flares alone in a binary classification rather than predicting every class in a multiclass classification. This research will attempt to find out the best predictive model for each class if possible. In addition to that, one of the limitations of this research is limited resources. According to Zhang et al. (2022), there are newly developed time series classifiers such as MINIROCKET, CIF, and Mr-SEQL which are instrumental with time series solar flare data. But these highly effective models require so many computational requirements to run (Especially high-end servers to minimize the runtime) which this research cannot afford. We will discuss more about how these time series classifiers can be implemented on a solar flare dataset in the “Lesson Learned and Future Work” chapter.

### 2.4 Sampling Techniques to Tackle Class Imbalance

Sampling can be simply divided into two major categories which are under sampling and oversampling. In under-sampling, the class which has the least number of entries is known as the minority class and all the other classes are identified as the majority class. Once the minority class and the majority classes are identified, the under-sampling method allows us to reduce the number of instances in the majority class to match the entries of the minority class. Its primary advantage is that it leads to faster computation and reduces the likelihood of overfitting, but it can discard potentially useful data, leading to a loss of information and poorer model performance. On the other hand, oversampling increases the number of instances in the minority class, often through techniques such as duplication or synthetic data generation (e.g., SMOTE). This approach helps the model learn more about the minority class, potentially improving its performance in underrepresented instances. However, it can lead to overfitting, especially if synthetic examples are not varied enough, and it also increases computational load due to the larger dataset size. Both techniques need to be carefully applied to ensure a balanced trade-off between model performance and computational efficiency. (Vairetti et al. 2024) Many sampling techniques enable under sampling and oversampling such as random sampling, stratified sampling, systematic sampling, cluster sampling, and reservoir sampling, and in the past studies, these sampling techniques have been employed in different solar flare prediction models to address the issue of imbalanced datasets. The Synthetic Minority Oversampling Technique (SMOTE) has been widely used to mitigate class imbalances in solar flare data (Wan et al. 2022).

Additionally, a new selective up-sampling method has been proposed to create a balanced dataset by adding small random values to flare-related samples, significantly improving model performance in predicting strong-flare events (Liu et al. 2023). These sampling techniques play a crucial role in improving the reliability and accuracy of machine-learning algorithms in forecasting solar flare events. Therefore, in the data analysis part, this research has employed several data validation techniques to tackle the class imbalance problem such as Random Under sampling and SMOTE. Most importantly, this research has applied rather a method employed in the DeepSun project itself and extended it further in terms of sampling techniques. In the DeepSun project, they have used 100 under sampled datasets for their project and this study uses 100 under sampled datasets and 100 oversampled datasets in the analysis. Moreover, in most studies, researchers always take just one under sampled or oversampled dataset for modeling. However, in this research, 100 under sampled data frames and 100 oversampled data frames were created and the average accuracies have been considered.

### 2.5 Validation Techniques and Their Importance in Solar Flare Prediction

Validation techniques in the field of machine learning play a pivotal role in evaluating a model's capacity to generalize beyond the training dataset. According to Bennett et al. (2022) the holdout validation strategy entails segregating the data into training and testing subsets, where the model is trained on the former and assessed on the latter. On the other hand, K-Fold Cross-Validation enhances reliability by segmenting the data into multiple folds, training the model on K-1 folds, testing it on the remaining fold, and repeating this iterative process K times to derive an averaged and more robust performance evaluation (Fazekas and Kovacs 2024).

Taking a further step, Leave-One-Out Cross-Validation (LOOCV) leverages each data point as a test instance while being trained on the rest of the dataset, offering a comprehensive yet computationally intensive validation approach (Qiu et al. 2024). In terms of, Stratified K-Fold Cross-Validation, Imran et al. (2203) argues that it ensures that each fold maintains an equivalent class distribution to the entire dataset, a particularly advantageous practice for handling imbalanced data. Yazıcı et al. (2023) indicates that Nested Cross-Validation introduces a dual-layered validation mechanism, with one layer dedicated to hyperparameter optimization and the other for assessing performance, thereby mitigating the risk of overfitting and furnishing an unbiased performance estimation.

Cross-validation techniques, such as Leave-One-Out and K-Fold Cross-Validation, play a crucial role in model validation and selection across various fields like ecology and machine learning (Kuipers 2022). These techniques involve splitting the data into training and testing sets to assess the model's predictive performance, even in cases where likelihood derivation is not feasible, or parameter counting is imprecise. By utilizing cross-validation, researchers can mitigate bias, estimation uncertainty, and overfitting, ensuring robust model selection and evaluation. The application of cross-validation methods allows for the identification of the most suitable model based on predictive scores, enhancing the accuracy and generalizability of statistical analyses and machine learning models.

Cross-validation techniques play a crucial role in solar flare prediction models, as demonstrated in various research studies. For instance, Liu et al. (2017) utilized a 10-fold cross-validation scheme to evaluate the performance of a random forest algorithm in predicting different classes of solar flares. Similarly, Saini et al. (2024) employed the true skill statistic (TSS) score to validate the performance of machine learning classifiers in a class-imbalanced dataset for solar flare prediction.

These cross-validation techniques help assess the robustness and generalizability of the prediction models by splitting the data into training and testing sets multiple times, ensuring that the model's performance is not skewed by a particular data partition. By using cross-validation, researchers can enhance the reliability of their predictions and make more accurate forecasts of solar flare events, ultimately contributing to better space weather forecasting and mitigation strategies. This research will apply 10-fold K Cross Validation, Balanced Accuracy, and True Skill Statistics as the validation techniques in data analysis.

Moreover, in the data analysis chapter, a more comprehensive discussion will be carried out on how Balanced Accuracy and True Skill Statistics are defined in terms of the solar flare classes in the dataset.

### 2.6 Variable Selection

In terms of variable selection, the following are some of the significant sharp parameters identified from the existing literature and these variables will be prioritized when choosing the dataset. The following variables have been used in numerous studies and some of these studies are, (Abduallah, Wang, Wang, & Xu, 2023), (Chen, et al., 2019), (Deshmukh et al. 2023), (Zhang et al. 2022).

### 2.6.1 Total Unsigned Current Helicity (TOTUSJH)

The aggregate unsigned current helicity represents the total sum of the absolute values of the current helicities, irrespective of their polarities. Within the realm of solar physics, the notion of magnetic/current helicity has played a pivotal role in understanding the origin of solar magnetic fields and their temporal evolution. (Scheeler et al. 2017) Statistical summarization of the time series of total unsigned current helicity has proven to be more effective in solar flare prediction compared to the simultaneous consideration of all AR parameters. (Hamdi et al. 2017). Previous studies have indicated a correlation between the total unsigned helicity and the multiplication of photospheric and open fluxes, underscoring its significance in comprehending the internal topological configuration of the Sun's coronal magnetic field, as noted by Yeates (2020). Furthermore, in the context of employing machine learning algorithms for predicting solar flares, it has been established that the total unsigned quantities of vertical current, current helicity, and flux near the polarity inversion line are identified as the most critical parameters for categorizing flaring regions into distinct classes, as highlighted by Liu et al. (2017).

### 2.6.2 Total Unsigned Vertical Current (TOTUSJZ)

Total Unsigned Vertical Current represents the combined total of vertical electric currents in active areas of the sun responsible for generating flares. These currents have a critical impact on solar atmospheric events such as eruptions and flares (Haywood et al. 2022). According to Kontogiannis et al. (2017) TOTUSJZ has been identified as a key factor affecting solar flares significantly and they highlight those previous studies have shown that the mean values of unbalanced currents within active regions prone to flares are notably higher compared to regions without flares, indicating a substantial relationship with flare incidence. Furthermore, the Total Unsigned Vertical Current is among a group of nine SHARP parameters that exhibited strong correlations with the model's forecasts, representing its relevance in accurate comprehension and prediction of solar flares (Yi, Moon, Lim, Park, & Lee, 2021).

### 2.6.3 Total Unsigned Flux (USFLUX)

Total Unsigned Flux refers to the complete magnetic flux that lacks a specific polarity, commonly observed in various solar and stellar scenarios (Haywood et al. 2022). In the context of solar flares, Total Unsigned Flux represents the total sum of magnetic flux within an Active Region (AR). This parameter is calculated based on data from SOHO MDI magnetograms and holds significant importance in the prediction of X-, M-, or C-class flares occurring within a 24-hour timeframe. (Han et al. 2019)

### 2.6.4 Absolute Value of The Net Current Helicity (ABSNJZH)

ABSNJZH is utilized to quantify the twisted and sheared non-potential structures present in a magnetic field, which is essential for comprehending the evolution of magnetic fields in diverse scenarios (Low, 2011). As indicated by Hamdi et al. (2017) and Tiwari (2010), ABSNJZH has demonstrated superior performance compared to other variables in their solar prediction models.

They have identified this variable as crucial for enhancing space weather forecasting, particularly based on helicity patterns and chirality correlations.

### 2.6.5 Total Photospheric Magnetic Free Energy Density (TOTPOT)

Zhang (2016) explains that TOTPOT denotes the surplus energy beyond the potential magnetic field energy within the solar corona, which plays a crucial role in phenomena like solar flares and coronal mass ejections. Through the utilization of photo-spheric magnetic field vector data, scholars approximate this available energy on a global scale. Prior research suggests that even minute alterations in the photo-spheric mean magnetic energy density, encompassing the free magnetic energy near magnetic neutral lines, manifest as direct fluctuations preceding intense solar flares (Goodman et al. 2020).

TOTPOT serves as a significant parameter for the anticipation of solar flares, as articulated by Zhang (2016), as it signifies variations prior to the onset of potent flares, denoting the release of stored energy. Furthermore, the study conducted by Goodman et al. (2020) highlights this aspect and concludes that TOTPOT exhibits a distinct correlation with the incidence of M and X flares in the solar corona. Additionally, researchers like Chen et al. (2021) assert that TOTPOT is not solely a pivotal variable but also acknowledged as one of the key determinants for predicting the flare index in machine learning algorithms.

### 2.6.6 Mean Characteristic Twist Parameter, α (MEANALP)

MEANALP quantifies magnetic nonpotentiality within active regions (ARs), facilitating the differentiation between eruptive and confined solar flares through the evaluation of core region non-potentiality in relation to the background field intensity. Previous studies have illustrated that the relative assessment of magnetic nonpotentiality in the core of ARs significantly impacts the likelihood of eruptive flare occurrences (Li et al. 2022). Reinard et al. (2010) have reported that MEANALP effectively forecasts the probability of flaring in active regions 2-3 days in advance, thereby enhancing the solar flare prediction time window. Consequently, this variable is crucial in improving the time window for solar flare prediction. However, this variable will not be significant if the chosen dataset is curated already to predict within a certain time window (e.g., 24, 48 or 72 hrs.).

Incorporating these variables, the conceptual framework would be structured as follows. However, the selected dataset would encompass additional variables beyond these essential variables, which the study would consider during the dataset selection process. Once the dataset is chosen, the conceptual framework will be reformed with all the variables in the dataset.

> **Figure 1: Initial Conceptual Framework (Generated by Visio)**  
> [View Figure 1 in the original dissertation (PDF, p. 24)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=24)

### 2.7 Prominent Datasets Applied in Existing Literature

There are so many datasets available in the solar flare prediction domain which are already preprocessed and cured. For instance, Hollanda et al. (2021) have created a database which consists of records related to solar flare events containing magnetic measures of the last 24 hours. Their data collection process involved recording SHARP data daily every 12 minutes for each Active Region (AR). Moreover, they have utilized the corresponding SHARP data from 24 hours before the flare occurrence to represent positive events (ARs flaring >= M-class flares). This is a perfect dataset to predict whether a solar flare will occur (binary classification) in the next 24 hours.

However, even though Hollanda et al. (2021) team’s dataset is promising, unfortunately, it cannot be applied in this study since it allows only a binary classification, and it diminishes the scope of multiclass classification of this research.

Another popular dataset utilized in solar flare prediction research is the Space Weather Analytics for Solar Flares (SWAN-SF) benchmark dataset, which comprises multivariate time series (MVTS) data of active region properties spanning over 9 years of the Solar Dynamics Observatory (SDO) operations extracted from solar photospheric vector magnetograms in Space Weather HMI active Region Patch (SHARP) series (Saini et al. 2024).

Moreover, this dataset is crucial for addressing challenges such as class-imbalance (Scarcity of large flares M-or X-class) and temporal coherence in solar flare forecasting, with a significant imbalance ratio for different flare classes such as M- and X-class flares, emphasizing the need for specialized handling techniques (Ahmadzadeh et al. 2021). Additionally, researchers have employed various machine learning models such as MINIROCKET, Support Vector Machine (SVM), Canonical Interval Forest (CIF), Multiple Representations SEQuence Learner (Mr-SEQL), Long Short-Term Memory (LSTM), VGGNet-16, and LeNet to analyze and predict solar flares, showcasing the diverse approaches and methodologies used in this field (R. Kaur et al. 2023). This dataset does have all the classes needed for the research and since the dataset is imbalanced, it provides more scope to employ sampling and validation techniques in the data analysis phase as well. Even though this dataset is perfectly suitable for this study, because of popularity and integrity of the data, there are many research papers published by analyzing this dataset already, and most of the research gaps are addressed by existing papers in terms of this dataset and almost all machine learning algorithms and approaches have been exhausted for this dataset as emphasized by R. Kaur et al. (2023).

The Reuven Ramaty High Energy Solar Spectroscopic Imager (RHESSI) dataset is another popular dataset which is crucial for solar flare prediction, as it provides X-ray and gamma-ray imaging spectroscopy capabilities that have significantly contributed to solar physics, astrophysics, and Earth sciences over its 16 years of operation from 2002 to 2018 (Dennis et al. 2024). Machine learning techniques, including Multiple Instance Learning (MIL), have been applied to this dataset to predict solar flares with high accuracy, around 90%, by analyzing spectral data from NASA's IRIS satellite (Huwyler and Melchior 2022).

Just like the SWAN-SF dataset, this dataset is also popular and applied many times before, however it does have its own limitations. One drawback is the discrepancy between RHESSI and GOES data in determining thermal plasma parameters, with RHESSI tending to provide higher temperatures and lower emission measures compared to GOES, indicating a multi thermal plasma scenario (Warmuth and Mann 2016). Additionally, while RHESSI is valuable for analyzing micro flares and estimating electron densities and volumetric filling factors, assumptions such as unity filling factor can lead to unphysical results, requiring careful consideration of cooling times and external heating effects (Baylor et al. 2011). These limits and the fact of RHESSI dataset’s popularity of getting included in so many research papers just like SWAN-SF dataset, does not help the scope and objectives of this research. This study requires a dataset which is not used in many studies, preprocessed, poses class imbalance (Represent scope), and is easily accessible.

Chen et al. (2019) have used another promising dataset in their paper of “Identifying solar flare precursors using time series of SDO/HMI images and SHARP parameters”. This research has used a rather new method of dataset integration where they have extracted data from multiple sources, including the Geostationary Operational Environmental Satellites and the Solar Dynamics Observatory (SDO)/Helioseismic and Magnetic Imager (HMI). According to Chen et al. (2019), this dataset has enabled the researchers to achieve almost as good performance in training the classification models as when using active region parameters provided in HMI/Space-Weather HMI-Active Region Patch (SHARP) data files.

This dataset too has limitations in terms of the number of B flares recorded, as B flares are not always captured when the active regions sustain emission levels exceeding that of B flares, there are challenges related to the under recording of B flares in the dataset, impacting the comprehensive representation of flare events within the data. Moreover, overlapping time series data points between positive and negative classes poses a great challenge, making it harder for machine learning algorithms to differentiate features effectively, especially when forecasting windows are not appropriately managed. (Chen et al. 2019) Another prominent dataset which is compatible with all the objectives and scope of this research.

The dataset used in the DeepSun (machine-learning-as-a-service for solar flare prediction) research encompasses various sources and characteristics. It includes Space-weather HMI Active Region Patches (SHARP) magnetic parameters (Abduallah and Wang 2024), multivariate time series (MVTS) data from the Space Weather Analytics for Solar Flares (SWAN-SF) benchmark dataset (Saini et al. 2024), and line-of-sight magnetograms images for forecasting >= M-class flares (Grim and Gradvohl 2023). This dataset covers the period between May 2010 and December 2016 and consists of 845 flares categorized into classes B, C, M, and X, originating from 472 Active Regions (ARs), containing 128 B class flares, 552 C class flares, 142 M class flares, and 23 X class flares.

Additionally, the dataset has already undergone preprocessing steps such as statistical summarization (Saini et al. 2024). Each data sample in the dataset contains values of 13 SHARP parameters, normalized to a range from 0 to 1, with one data sample corresponding to each flare.

The dataset includes information such as the flare date, start time, and the 13 SHARP parameter values measured at the beginning of the flare date to predict flares within 24 hours. Since the dataset is already preprocessed to predict solar flares within 24 hours, it's easy for researchers not to think about the time window of their predictions. However, this dataset may not be useful when predicting solar flares in 48-72 hours. (Abduallah et al. 2021). The dataset is accessible via: https://nature.njit.edu/spacesoft/Flare-Predict/ Moreover, this dataset includes detailed information on 13 SHARP parameters, providing a comprehensive view of the magnetic field properties of Active Regions, which is crucial for solar flare prediction. Covering a period of over six years, the dataset offers a substantial longitudinal perspective, allowing for the analysis of flare patterns and trends over time. Since this dataset consists of 13 different parameters, all these parameters do have their own scale of measurements and units. Hence choosing a suitable normalization technique is crucial in working with a dataset.

This provides more scope to this study and facilitates the comparison and analysis of different parameters with varying scales and units.

The dataset has imbalanced class distributions which perfectly align with the scope of this research, However, since the instances for X-class flares is much less than instances for other classes, this could affect the performance of algorithms in predicting rare events like X-class flares, in terms of limitations, The dataset's focus on SHARP parameters may limit the inclusion of other potentially relevant features that could enhance the prediction models, such as full vector data on the photospheric magnetic field structure. This dataset has been chosen for data analysis, since it allows multi class prediction within 24 hours, includes the most significant sharp parameters identified from previous literature, longitudinal coverage and is not used in many studies. In a more important note, the sharp parameter, Mean Characteristic Twist Parameter, α (MEANALP) is not included in the dataset since this dataset is already curated to predict solar flares in a 24 hours prediction time window, hence it is negligible.

Therefore, with the chosen dataset, the updated conceptual framework can be formulated as below. The significant variables identified in the literature review are highlighted in green and the additional variables are highlighted in yellow.

> **Figure 2: Updated Conceptual Framework (Generated by Visio)**  
> [View Figure 2 in the original dissertation (PDF, p. 28)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=28)

## Chapter 3: Methodology

### 3.1 Introduction to Dataset

The DeepSun team has created a solar flare database, utilizing the SHARP parameters derived from the solar images accessible at JSOC and the X-ray flare catalogs supplied by NCEI. From May 2010 to December 2016, 845 solar flares were carefully chosen and documented. Out of these occurrences, 128 were classified as class B flares, 552 were categorized as class C, 142 were identified as class M, and 23 were designated as class X. It is worth noting that the locations of the C-, M-, and X-class flares were pinpointed to be approximately within a range of ± 70° of the central meridians. (Liu et al. 2017) These 845 flares originate from 472 Active Regions (ARs). The duration of a flare can varies from a few minutes to several hours. The lifespan of an AR can range from a few days to several months.

In cases where multiple flares occur from the same AR on a single day, only the highest-class flare is documented. Furthermore, if there are multiple highest-class flares on the same day, only the final flare of such magnitude is recorded. When two distinct ARs produce flares simultaneously, the highest-class flare from each AR is individually documented for that particular day. (Abduallah et al. 2021) The original dataset looks like below.

> **Table 1: Numbers of Flares and ARs per Flare Class (Abduallah et al. 2021)**  
> [View Table 1 in the original dissertation (PDF, p. 29)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=29)

Most importantly the dataset is created in a way to reflect one data instance for each flare where there will be no multiple instances representing one flare. And each instance reflects only one date.

The “Flare Date” column reflects the initial moment when all 13 sharp parameters were available. In measuring sharp parameters this way, it allows the algorithms to predict flares within 24h which achieve one of the objectives in this research. Moreover, the flare class column is recorded just not to categorize a flare in to flare classes, but it provides another two digits in front of flare class to explain its intensity in a broader way. For instance, a flare can be categorized as B1.6 in general, in the dataset, it has been classified as B16 for simplicity. However, when predicting flare classes, these two digits are ignored to ensure a 4-class prediction.

> **Figure 3: Thirteen SHARP Parameters Used in the Research – Descriptions of the Parameters derived from Abduallah et al. (2021)**  
> [View Figure 3 in the original dissertation (PDF, p. 30)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=30)

> **Figure 4: Code Snippet for Removing the Last Two Digits of Solar Flare Classes**  
> [View Figure 4 in the original dissertation (PDF, p. 30)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=30)

### 3.2 Exploratory Data Analysis (EDA)

EDA has been performed to get a sense of the dataset, to comprehend what kind of data types we are working with, recognized data anomalies such as missing values, outliers, and redundant data and to make informed decisions based on qualitative and quantitative analysis. (Sandfeld 2023) We will be looking at some important decisions made through EDA and all the decisions made in the EDA and further coding process explained thoroughly in the Google Colab Notebook. The following snapshot provides the overall statistics of the dataset.

One important decision made looking at this table, is this dataset needs normalization more than any other dataset. As it is visible, all the sharp parameters are measured in different scales, and this will be a problem when modeling. Hence choosing a suitable normalization technique is essential

> **Figure 5: Initial Data frame Visualization**  
> [View Figure 5 in the original dissertation (PDF, p. 31)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=31)

> **Figure 6: Overall Statistics of DeepSun Solar Flare Dataset**  
> [View Figure 6 in the original dissertation (PDF, p. 31)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=31)

### 3.2.1 Normalization

In terms of solar flare prediction, there are a variety of normalization techniques used. These techniques include z-score, MinMax, median, decimal, and the clear sky index (CSI) method, which are commonly used to make input data stationary for global horizontal irradiance (GHI) forecasts. These normalization techniques contribute to improving the performance of forecasting models by reducing errors and enhancing the precision of solar flare predictions, crucial for mitigating potential negative impacts on Earth and space environments. (Singla et al. 2022) According to data skewness and dataset’s nature, MinMax scaler has been used as the normalization technique. Moreover, the DeepSun has recommended the MinMax method for their dataset as well. Let 𝑥ො௜ ௞ (𝑥௜ ௞ , respectively) represents the standardized (original, respectively) measure of the 𝑖 ௧௛ parameter 𝑘௧௛ data sample. Subsequently, ௜ ௞ ௫ො ೔ ೖି௠௜௡೔ ௠௔௫೔ି௠௜௡೔ (1) with, 𝑚𝑎𝑥௜(𝑚𝑖𝑛௜, respectively) denoting the highest (lowest, respectively) value of the 𝑖 ௧௛ parameter. The standardized measures vary within the interval of 0 to 1.

> **Figure 7: Code Snippet for MinMax Normalization**  
> [View Figure 7 in the original dissertation (PDF, p. 32)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=32)

### 3.2.2 Data Distribution of Sharp Parameters and AR

> **Figure 8: Data Distribution of Numerical Columns (SHARP Parameters and AR) – Generated in Google**  
> [View Figure 8 in the original dissertation (PDF, p. 33)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=33)

Collaboratory All sharp parameters possess outliers, but these cannot be excluded from solar flare prediction modeling for several important reasons. Firstly, outliers often represent rare but significant events such as X class flares that can provide critical insights into the conditions leading to major solar flares (Aschwanden 2019). Retaining these outliers ensures that the model is robust and capable of generalizing across both typical and extreme scenarios, thus improving its reliability. And removing outliers could reduce the X flare instances in the dataset which is already low.

Additionally, outliers can reveal new patterns or previously unrecognized relationships in the data, offering valuable insights into the underlying processes of solar flare formation. Excluding them might oversimplify the model and fail to capture the full complexity of solar phenomena.

Furthermore, removing outliers could introduce bias and distort the data distribution, leading to a model that performs well under normal conditions but fails under extreme ones. Outliers also provide valuable information about extreme or boundary conditions, which is crucial for understanding the full range of solar activity. Keeping them in the dataset allows for a diverse training set, enhancing the model’s ability to handle various scenarios and improving its accuracy and adaptability in real-world applications. Therefore, including outliers is essential for creating a comprehensive and effective solar flare prediction model. (Wen et al. 2022) Moreover, the box plots reveal significant variability and outliers in several key features, indicating they capture critical and diverse information about solar activity. Features like TOTUSJH, TOTBSQ, TOTUSJZ, USFLUX, and AREA_ACR exhibit high variability and numerous outliers, suggesting they measure important aspects of solar magnetic activity essential for predicting solar flares. For instance, TOTUSJH and USFLUX have extensive ranges and many outliers, highlighting their role in capturing complex magnetic field variations. Conversely, AR shows a more uniform distribution with fewer outliers, suggesting it might be less informative for predicting solar flare classes. AR might be considered for exclusion if it can be proven that AR does not contribute statistically too. This approach ensures that our prediction models focus on the most informative features, enhancing accuracy and reliability.

### 3.2.3 Data Distribution of Flare Classes

This distribution reveals a significant class imbalance in the data. Most of the recorded flares are C-class, followed by M-class and B-class, with X-class flares being much less common.

Especially, when it comes to X class flares which has only 23 flare instances. Over sampling will be important in predicting X class flares.

> **Figure 9: Data Distribution of Solar Flare Classes – Generated in Google Collaboratory**  
> [View Figure 9 in the original dissertation (PDF, p. 35)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=35)

Given the class imbalance in flare prediction data, where some classes such as X-class flares are significantly less frequent than others like C-class, it is crucial to employ sampling techniques. In terms of sampling, random under sampler has been used for under sampling and class M will be used as the threshold for reducing instances of the C class, hence C class will be reduced to 142 instances. However, when performing under sampling, 100 random under-sampled datasets will be created, and the model performance average will be considered. When it comes to oversampling, SMOTE has been applied and C class is identified as the majority class. SMOTE will create instances for other classes where all the classes will have 552 instances. Same as under sampling, 100 random over-sampled datasets are created to train the models. In summary, the class imbalance in flare data reflects the natural distribution of solar flare intensities, with some classes being significantly less common than others. Using sampling techniques is essential to address this imbalance, ensuring that the predictive model performs well across all flare classes and does not unfairly favor the majority class.

> **Figure 10: Code Snippet for Under-Sampling with Random Under-Sampler**  
> [View Figure 10 in the original dissertation (PDF, p. 36)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=36)

> **Figure 11: Code Snippet for Over-Sampling with SMOTE**  
> [View Figure 11 in the original dissertation (PDF, p. 37)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=37)

### 3.2.4 Feature Correlation

Performing feature correlation analysis is essential for solar flare prediction due to various reasons: understanding relationships between different solar observation features like magnetic field measurements and sunspot activity. Identifying how features such as TOTUSJH, TOTBSQ, TOTUSJZ, USFLUX, and AREA_ACR are related helps in determining redundancy and simplifying models. Addressing multicollinearity in linear models enhances parameter reliability by reducing redundant features. This process improves model interpretability and generalizability to unseen data. (Campi et al. 2019) In the solar flare prediction context, correlation analysis is crucial because of the complex and high-dimensional data. Understanding correlations between features with physical meanings in solar physics provides insights into the processes behind solar flares. Accurate feature selection based on correlation analysis boosts predictive accuracy, which is vital for minimizing the effects of solar flares on technologies like satellite communications and power grids. Analyzing the correlation matrix helps in reducing redundancy and selecting the most informative features. This approach, along with model validation and evaluation, ensures the use of robust and accurate predictive models by managing complexity and enhancing performance. (McGuire et al. 2019)

> **Figure 12: Feature Correlation Matrix for SHARP Parameters and AR – Generated in Google**  
> [View Figure 12 in the original dissertation (PDF, p. 38)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=38)

Collaboratory Weak or No Correlations: AR has weak correlations with most features, indicating it does not have a strong linear relationship with them. Several other features show weak correlations with each other, indicating minimal linear relationships. In summary, there are strong positive correlations among TOTUSJH, TOTBSQ, TOTUSJZ, USFLUX, and AREA_ACR, indicating these features tend to increase together. TOTFZ tends to be negatively correlated with several other features, suggesting it often decreases when those features increase. Some features like AR and EPSZ generally show weaker correlations with other features. Understanding these correlations can be important for feature selection in modeling, as highly correlated features might provide redundant information.

Dropping the AR feature in prediction modeling, rather than any other sharp parameter, is a strategic decision I have taken based on its minimal contribution to the overall model and the observations from the data distribution box plots. The correlation analysis reveals that AR exhibits weak correlations with other features, indicating it does not share much informative overlap with them. For instance, its highest correlation, at 0.078 with R_VALUE, is negligible.

This weak inter-feature correlation suggests that AR is not capturing critical underlying patterns necessary for accurate predictions. Additionally, including features with low relevance can introduce noise, complicate the model, and potentially degrade its performance. In contrast, other sharp parameters like TOTUSJH, TOTBSQ, TOTUSJZ, USFLUX, and AREA_ACR show strong correlations with each other, indicating they encapsulate significant and related aspects of solar activity. Retaining these features ensures that the model leverages comprehensive and relevant information. Including AR may increase or decrease model accuracy, however, whatever the accuracy is, it will not be reliable. Therefore, dropping AR streamlines the model by eliminating a feature that offers limited predictive power, leading to improved efficiency, interpretability, and accuracy of the solar flare prediction model.

In astrophysics, AR represents regions on the Sun with heightened magnetic activity, but it does not quantify the specific characteristics and complexities of the magnetic fields that directly influence solar flare production. Hence the Active Region (AR) of the Sun is not particularly important in predicting solar flare class due to its broad and less specific nature compared to other more precise magnetic field parameters. Key predictive features such as TOTUSJH (total unsigned current helicity), USFLUX (total unsigned magnetic flux), and AREA_ACR (area of active regions) provide detailed measurements of the magnetic field's structure, which are crucial for understanding and predicting solar flares. These features capture the intricate magnetic environment and energy buildup necessary for flare initiation. In contrast, AR, being a broader descriptor, does not correlate strongly with these critical parameters, offering limited predictive value. Empirical analyses often show that AR ranks low in feature importance, suggesting it adds minimal information to the predictive models. Therefore, focusing on more specific and strongly correlated magnetic field parameters leads to more accurate and reliable predictions of solar flare classes, making AR a less significant feature in such models.

### 3.3 Modeling

The main objective of this study is to evaluate the performance of various machine learning algorithms on a dataset with imbalanced classes. The evaluation process involved assessing these algorithms using different sampling strategies: the original dataset, under-sampled datasets, and oversampled datasets. The aim was to determine which algorithms perform best in terms of classification accuracy and their ability to distinguish between classes.

### 3.3.1 Data and Distribution

Original Dataset: The algorithms were first evaluated on the original dataset without any modifications. This provided a baseline performance measure against which other sampling methods could be compared.

Under-sampled Datasets: To address class imbalance, the original dataset was under-sampled 100 times randomly with random under-sampler. This technique involves reducing the number of instances in the majority class to match the minority class, thereby creating balanced datasets. The performance of the algorithms was then evaluated on these balanced datasets.

Oversampled Datasets: Similarly, the original dataset was oversampled 100 times to balance the classes with SMOTE. This technique involves increasing the number of instances in the minority class to match the majority class. The algorithms' performance was evaluated on these augmented datasets.

### 3.3.2 Validation Techniques Used

DeepSun team has used the normal K fold cross validation for their research whereas this research has applied rather an extension of K fold cross validation which is stratified K fold cross validation.

The major reason to use stratified CV is because of its ability to handle class imbalance. In normal K fold cross validation, data is randomly divided into K equally sized folds and one of the major disadvantages of this validation is, if the data is imbalanced, some folds may possess a disproportionate representation of classes, leading to biased performance evaluation. However, stratified K fold CV, divides the data in a way, that each fold maintains the equal proportion of every class as in the original dataset. Since our data is imbalanced, it is essential to use stratified K fold cross validation. However, the only drawback is, stratified CV will take more computational time. (Mayangsari et al. 2023)

> **Figure 13: Stratified K Fold Cross Validation (Pramod 2024)**  
> [View Figure 13 in the original dissertation (PDF, p. 42)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=42)

> **Figure 14: Code Snippet for Defining Stratified K Fold Cross Validation and Implementation**  
> [View Figure 14 in the original dissertation (PDF, p. 43)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=43)

This research has used 10-fold cross validation whereas for every dataset, the stratified CV handler, shuffled the dataset in equal proportion of classes, to create 10-fold partitions, applying the stratified CV package included in the scikit-learn library in Python. All the ML algorithms were trained by nine of the ten folds, and the 10th fold was employed for testing. Moreover, as mentioned earlier ach data instance indicates to a single date and represents one flare. Each data instance either included in the training set or in the testing set and there is no data instance included both in training and testing as well. Hence, the testing data were never introduced in the training, which elevates the reliability in the accuracy of the models. To further, mitigate the margin of error, corresponding to cross validation, we have iterated the 10-fold stratified CV in not only with the original dataset but also with the 100 under-sampled and 100 over-sampled datasets which resulted in 2100 tests for each algorithm. If we multiplied the 2100 tests used for each algorithm with the number of algorithms employed (14 ML Algorithms), this research has conducted 29400 tests overall before choosing the suitable prediction model.

### 3.3.3 Algorithms Employed

This study involved the evaluation of both conventional and high-performance machine learning algorithms: Conventional Algorithms:

1. Decision Tree Classifier

2. Extra Tree Classifier

3. Gaussian NB

4. K Neighbors Classifier

5. Linear SVC

6. Passive Aggressive Classifier

7. Ridge Classifier

8. SGD Classifier

9. SVC

High-Performance Algorithms:

10. Bagging Classifier

11. Extra Trees Classifier

12. Gradient Boosting Classifier

13. Linear Discriminant Analysis

14. Random Forest Classifier

### 3.3.4 Evaluation Metrics

The algorithms' performance was evaluated by converting a multi-class classification problem into four binary classification problems. Each class B, C, M, and X was considered separately. For instance, let’s take a data instance in class C, the data sample is labeled as positive if it belonged to class C, and negative if it didn’t. True positives, false positives, true negatives, and false negatives were defined accordingly. True positives are when the algorithm correctly predicts a positive sample, false positives are when it predicts a positive sample incorrectly, true negatives are when it predicts a negative sample correctly, and false negatives are when it predicts a negative sample incorrectly. The terms TP, FP, TN, and FN were used to represent the number of true positives, false positives, true negatives, and false negatives, respectively.

The performance of the algorithms was evaluated using two key metrics: Balanced Accuracy (BACC) BACC is defined as below: 1 2 𝑇𝑃 𝑇𝑃+𝐹𝑁 𝑇𝑁 𝑇𝑁+𝐹𝑃 (2) This metric is particularly useful for evaluating imbalanced datasets. BACC examines both sensitivity (referred to as the true positive rate or recall) and specificity (referred to as the true negative rate). The accuracy is computed individually for the positive dataset and the negative dataset, which proves advantageous in scenarios where there is an imbalance between the datasets, meaning one dataset contains significantly more elements than the other. Moreover, due to its impartiality towards the class-imbalance ratio, BACC is particularly valuable. (Akhilesh et al. 2021).

> **Figure 15: Code Snippet for Calculating BACC per Class and Algorithm**  
> [View Figure 15 in the original dissertation (PDF, p. 45)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=45)

True Skill Statistic (TSS) TSS is defined as below: TSS = ቀ 𝑇𝑃 𝑇𝑃+𝐹𝑁 𝐹𝑃 𝑇𝑁+𝐹𝑃ቁ (3) TSS measures a classifier's ability to distinguish between classes, considering both true positives and false positives. It is a robust metric for evaluating the performance of classifiers in scenarios with imbalanced data. (Bloomfield et al. 2012). Moreover, Saini et al. (2024) employed the true skill statistic (TSS) score to validate the performance of machine learning classifiers in a class-imbalanced dataset for solar flare prediction BACC and TSS are derived for every individual binary classification task. Four binary classification tasks are examined. Subsequently, the mean of the BACC and TSS metrics acquired from these four tasks is computed, and this mean is considered as the outcome for the multi-class classification task. The detailed analysis in the subsequent sections will offer insights into the most effective algorithms and their suitability for tasks involving imbalanced data.

> **Figure 16: Code Snippet for Calculating BACC per Class and Algorithm**  
> [View Figure 16 in the original dissertation (PDF, p. 46)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=46)

## Chapter 4: Prediction Results and Discussion

In terms of results, we will discuss six tables. BACC and TSS results for original dataset, for 100 under-sampled datasets, and 100 over-sampled datasets. Subsequently, we will review how each algorithm as predicted each class in the environment of these different datasets.

### 4.1 BACC and TSS Results for Original Dataset

.

> **Figure 17: BACC Results for Original Dataset**  
> [View Figure 17 in the original dissertation (PDF, p. 47)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=47)

> **Figure 18: TSS Results for Original Dataset**  
> [View Figure 18 in the original dissertation (PDF, p. 47)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=47)

The performance analysis of various classification algorithms with original dataset highlights notable differences in effectiveness across different methods. Gaussian Naive Bayes (NB) consistently exhibits high performance, with superior BAC and TSS scores. Since the original dataset is one simple data frame and the Gaussian Naive Bayes algorithm’s strength lies in its simplicity and efficiency in handling skewed distributions, leading to its high accuracy and skill metrics with original dataset. The Ridge Classifier's poor performance, reflected in its lowest Balanced Accuracy (BACC) and True Skill Statistic (TSS) scores, could be primarily due to its linear nature and L2 regularization. In summary, algorithms that utilize ensemble methods or iterative learning approaches, such as Gaussian NB, Bagging, and Gradient Boosting, generally demonstrate higher performance due to their ability to manage class imbalances and adapt to complex patterns in the data. Conversely, simpler models or those with restrictive assumptions, such as Ridge Classifier, Linear Discriminant Analysis and Linear SVC, tend to exhibit lower accuracy and skill metrics, emphasizing the importance of model complexity and adaptability in achieving high performance.

### 4.2 BACC and TSS Results for 100 Under-Sampled Datasets

> **Figure 19: BACC Results for 100 Under-Sampled Datasets**  
> [View Figure 19 in the original dissertation (PDF, p. 48)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=48)

In analyzing the performance of various machine learning algorithms with 100 under-sampled datasets, it reveals distinct trends in how these algorithms perform across different datasets. The Gradient Boosting Classifier and Linear Discriminant Analysis emerge as the top performers.

The Gradient Boosting Classifier consistently demonstrates high balanced accuracy and TSS, achieving an average BACC of 0.734617 and a TSS of 0.469233. This shows that algorithms which demonstrate high accuracy often benefit from their complex structures and adaptability to the data. Ensemble methods such as the Random Forest Classifier and Extra Trees Classifier also perform well by aggregating the outputs of multiple decision trees, which reduces overfitting and improves robustness. Despite their high accuracy, their True Skill Statistic (TSS) might be lower if the individual trees are not sufficiently diversified. In contrast, some algorithms with lower accuracy and TSS, such as the Passive Aggressive Classifier, K Neighbors Classifier, and Ridge Classifier, face limitations due to their inherent simplicity or assumptions.

> **Figure 20: TSS Results for 100 Under-Sampled Datasets**  
> [View Figure 20 in the original dissertation (PDF, p. 49)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=49)

### 4.3 BACC and TSS Results for 100 Over-Sampled Datasets

> **Figure 21: BACC Results for 100 Over-Sampled Dataset**  
> [View Figure 21 in the original dissertation (PDF, p. 50)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=50)

> **Figure 22: TSS Results for 100 Under-Sampled Datasets**  
> [View Figure 22 in the original dissertation (PDF, p. 50)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=50)

Extra Trees Classifier stands out as the top performer, showing impressive results in both BACC and TSS. Its high average BACC reflects its ability to maintain high accuracy across all classification tasks, while its strong TSS performance indicates its effectiveness in handling diverse data conditions by balancing sensitivity and specificity. The Random Forest Classifier also performs exceptionally well, with high scores in both BACC and TSS. Its ensemble approach, similar to Extra Trees, allows it to handle large datasets and complex patterns effectively, resulting in strong balanced accuracy and TSS scores. On the other hand, algorithms like the Gaussian Naive Bayes (NB) and Passive Aggressive Classifier exhibit notably lower performance in both metrics.

In summary, again ensemble methods like Extra Trees and Random Forest outperform others by effectively managing data complexity and variability, while algorithms like Gaussian NB and Passive Aggressive Classifier face challenges.

### 4.4 Overall BACC and TSS Results

The below tables (respectively), compares the BACC average and TSS average of the 14 machine learning algorithms used in modeling for each binary classification hypothesis and for the overall multi-class classification task predicated on the original dataset, 100 under-sampled and 100 over-sampled datasets.

> **Figure 23: Average BACC Results for Each Class Per Algorithm**  
> [View Figure 23 in the original dissertation (PDF, p. 51)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=51)

When analyzing the performance of machine learning algorithms based on Average Balanced Accuracy (BACC) and Average True Skill Statistic (TSS) from all the datasets, insights emerge about their effectiveness across different binary and multi-class classification tasks. Extra Trees Classifier consistently performs at the top across both metrics, with an impressive Average BACC of 0.829979 and an Average TSS of 0.659958 and register itself as the most suitable machine learning algorithm amongst all the algorithms evaluated. This algorithm benefits from its ensemble approach, which aggregates the predictions from multiple decision trees, enhancing its ability to handle complex and varied data distributions. Passive Aggressive Classifier performs the weakest with an Average BACC of 0.691841 and an Average TSS of 0.311008. Its aggressive update mechanism, designed to adapt quickly to new data, appears to be less effective in accurately distinguishing between classes in this dataset.

> **Figure 24:Average TSS Results for Each Class Per Algorithm**  
> [View Figure 24 in the original dissertation (PDF, p. 52)](https://drive.google.com/file/d/1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N/view#page=52)

Moreover, if we compare the accuracies across datasets, the results from the under-sampled datasets and over-sampled datasets are better (respectively) than those from the original dataset.

This can be a consequence of the refined class distributions in the modified datasets than the original dataset itself with the ratio of X-class flares to C-class flares being higher in the adjusted datasets than in the original dataset. It is important to highlight that performance of all the algorithms decreases when forecasting X-class flares. This is due to the fact that X class having a considerably smaller number of flares than the other classes, leading the algorithms to lack sufficient knowledge about X-class flares. Overall, ensemble methods like Extra Trees and Random Forest achieve the best results due to their ability to aggregate multiple models' predictions, handling complexity and varied data distributions effectively. In contrast, simpler models and those with less complex ensemble strategies struggle to achieve similar performance, often due to their limitations in capturing intricate patterns or handling non-linear class boundaries.

## Chapter 5: Conclusion and Recommendations

### 5.1 Review of Research Objectives and Research Questions

In this section, we retrospectively examine the research objectives and research questions outlined in chapter 1 to assess the extent to which the research has fulfilled the stated objectives and addressed the research questions adequately. The primary research aim stated in chapter 1 is “to suggest a most suitable predictive machine learning algorithm to predict whether an active region (AR) on the Sun will produce a γ-class solar flare (≥M5.0, ≥M, or ≥C) within the next 24 hours”.

The dataset chosen was already preprocessed to predict solar flare within 24 hours and it possessed B, C, M and X solar flare classes. According to the findings and the discussion in the Chapter 4, this research suggests Extra Trees Classifier as the most suitable machine learning algorithm to predict whether an active region (AR) on the Sun will produce a γ-class solar flare (≥M5.0, ≥M, or ≥C) within the next 24 hours. Now let’s review the answers of the research questions and research objectives achieved.

### 5.1.1 Research Objectives Achieved

O1 Objective: In chapter 2.7, this research analyzed variety of present datasets such as SWAN-SF (Saini et al. 2024), RHESSI (Dennis et al. 2024), Hollanda et al. (2021) Team’s curated database and Chen et al. (2019) team’s integrated dataset. However, DeepSun dataset (Abduallah et al. 2021) dataset possessed all the significant parameters identified, not used widely, and aligned with this research’s objectives, which was chosen to continue this research.

O2 Objective: In terms of the most significant SHARP parameters, chapter 2.6 comprehensively review past literature to identify 6 such parameters namely,

1. Total Unsigned Current Helicity (TOTUSJH)

2. Total Unsigned Vertical Current (TOTUSJZ)

3. Total Unsigned Flux (USFLUX)

4. Absolute Value of The Net Current Helicity (ABSNJZH)

5. Total Photospheric Magnetic Free Energy Density (TOTPOT)

6. Mean Characteristic Twist Parameter, α (MEANALP)

These parameters are identified from the model feature selections performed by past studies. O3 Objective: EDA was performed, and the findings of the EDA is included in chapter 3.2. Two major data distributions were presented namely, data distribution of SHARP parameters and flare classes. These visualizations provided a more refined explanation on how informative the dataset is. One of the important decisions made through EDA findings is to exclude “AR” variable from further analysis because of its less informativeness and weaker correlations with other features.

Moreover, even though we identified outliers in EDA, they were not excluded because of reasons discussed in chapter 3.2. O4 Objective: According to the findings in chapter 4.4, the Extra Trees Classifier and Random Forest Classifier are the top performers among the algorithms. Their strength lies in their ensemble methods. In contrast, the Passive Aggressive Classifier and Ridge Classifier are the least effective.

The Passive Aggressive Classifier often struggles with stability and capturing intricate class distinctions due to its aggressive update mechanism. The Ridge Classifier, while effective at preventing overfitting, tends to underperform in modeling complex relationships due to its regularization constraints.

O5 Objective: In chapter 2.5, we have comprehensively discussed about validation techniques such as holdout validation, K-Fold Cross-Validation, LOOCV, Nested Cross-Validation and according to the past literature and considering the suitability to the chosen dataset, Stratified K-Fold Cross-Validation was chosen to further analysis.

### 5.1.2 Research Questions Answered

R1: In chapter 2.3 several research gaps are identified such as:  The influence of outliers and validation techniques on prediction reliability. (Wen et al. 2023)  Inadequate forecasting of high-intensity solar flares like X-class flares. (Zhang et al. 2022)  Minimal progress in the development of feature sets and machine learning algorithms approaches in solar flare prediction. (Wen et al. 2023)  The necessity for a reassessment of feature selection strategies. (Deshmukh et al. 2023)  The absence of dependable physical models. (Han et al. 2023)  Unemployment of newly developed time series classifiers such as MINIROCKET, CIF, and Mr-SEQL. (Zhang et al. 2022) R2: The solar flare datasets available are discussed in O1 objective and in chapter 2.7. In terms of accessibility, all the datasets discussed are open source and accessible to the public. (Links for these datasets can be provided upon request) R3: Discussed in chapter 2.6 and listed again in O2 objective.

R4: Discussed in chapter 4.4 and the summary is included in O4 objective. R5: Discussed in chapter 2.5 and the summary is included in O5 objective.

### 5.2 Research Implications and Contributions

When it comes theoretical implications, the research contributes to the existing literature by addressing the research gaps in past studies and this study. Importantly, most of the past studies were conducted considering just one dataset. But this study is conducted employing the original dataset, 100 under-sampled and over-sampled datasets. Moreover, this research significantly advances the application of machine learning in analyzing solar flare datasets, particularly through its comprehensive approach to dataset selection, feature relevance, and validation techniques. By selecting the DeepSun dataset, which contains all the relevant SHARP parameters, this study highlights the importance of using a dataset that thoroughly covers necessary features for accurate model training. This choice enhances the effectiveness of the machine learning models, highlighting the crucial role of dataset quality in achieving reliable predictions.

The identification of six key SHARP parameters demonstrates how targeted feature selection can significantly impact model performance. By refining the understanding of which parameters are most influential, this research provides valuable guidance for future studies and model development in solar flare prediction. Additionally, the adoption of Stratified K-Fold Cross-Validation is a noteworthy contribution, ensuring that each fold in the validation process accurately represents the distribution of flare classes. This technique not only improves the generalizability of the models but also addresses the limitations of other validation methods in a class imbalance environment, thereby enhancing the stability and reliability of model evaluations. The research also offers clear insights into algorithm performance.

The Extra Trees Classifier and Random Forest Classifier emerged as the top performers, demonstrating the effectiveness of ensemble methods in handling complex datasets. In contrast, the study reveals the limitations of the Passive Aggressive Classifier and Ridge Classifier, providing practical guidance on choosing appropriate algorithms based on data characteristics.

Lastly, the exploration of data distributions and the decision to exclude less informative features underscore the practical value of exploratory data analysis in refining model performance. These contributions collectively advance the field by emphasizing the importance of meticulous dataset handling, parameter selection, and validation, offering actionable insights that can be applied to similar classification challenges across various domains. As far as social contributions are concerned, this research has provided valuable insights in terms of solar prediction, which can mitigate consequences occur from solar flares.

### 5.3 Recommendations and Future Work

For future work, it is important to prioritize comprehensive datasets like DeepSun, which encompass all relevant parameters, however, if anyone can construct a dataset with less flare class imbalance, the solar flare prediction domain will be hugely benefited, since most of the solar flare datasets, include less X flare class instances which results in less prediction knowledge for X class flares in models. The success of the Extra Trees and Random Forest Classifiers in this study highlights the effectiveness of ensemble methods. Hence, employing more ensemble methods such as AdaBoost, CatBoost and GBM series will produce more accurate models. Furthermore, this research suggests to integrate four ensemble algorithms to predict each flare class by each ensemble algorithms according to algorithm’s nature and flare class’s data distribution.

Emphasizing the importance of robust exploratory data analysis (EDA), future research should implement advanced data preprocessing techniques, including feature engineering and outlier detection, to further refine input data and improve model performance. The use of Stratified K-Fold Cross-Validation proved effective in this study, and researchers are encouraged to adopt and experiment with different validation techniques such as Nested Cross-Validation or Time Series Cross-Validation, particularly for solar flare datasets with temporal dependencies. Vis a vis, in terms of time series data, new classifiers such as MINIROCKET, CIF, and Mr-SEQL will be instrumental and recommended according to the literature review in this research.

Future research should integrate new and more diverse datasets as they become available such as the dataset used by Chen et al. (2019). Combining multiple datasets can provide a more comprehensive understanding and enhance the robustness of the prediction models. Expanding the feature set by incorporating additional relevant parameters and employing advanced feature selection techniques can further improve the predictive capabilities of the models. Investigating the impact of different feature combinations on model performance should be a focus. As indicated in the literature review, if future studies employ a large solar flare dataset, this research further suggests to employ dimensionality reduction techniques such as Principal component analysis (PCA) to simplify the dataset into a smaller set while still maintaining significant patterns and trends. Developing real-time prediction systems that can provide timely warnings for solar flares would be a significant advancement such as the DeepSun (MLaaS). This involves optimizing models for speed and integrating them with real-time data streams from solar observation satellites.

Additionally, applying the findings and methodologies from this research to other domains, such as weather forecasting or financial market prediction, can test the generalizability of the approaches and potentially lead to breakthroughs in those fields as well. By following these recommendations and exploring these future research directions, the field of solar flare prediction can continue to advance, leading to more accurate and reliable forecasting methods that can have a significant impact on space weather preparedness and related applications.

### 5.4 Research Limitations

Despite the significant findings and advancements made in this research, several limitations should be acknowledged. First, the reliance on the DeepSun dataset, while comprehensive, may still limit the generalizability of the results to other datasets with different characteristics or additional parameters not included in DeepSun and DeepSun dataset still possess a class imbalance like most solar flare dataset which decreases model interpretability. This could potentially impact the robustness of the predictive models when applied to new or unseen data. Furthermore, the chosen key SHARP parameters, although identified through thorough literature review, may not encompass all relevant features that could enhance prediction accuracy. There might be other influential parameters that were overlooked or not included in the dataset. The study primarily utilized traditional machine learning algorithms, which, although effective, may not fully exploit the complex, high-dimensional nature of solar flare data. While ensemble methods like Extra Trees and Random Forest Classifiers performed well, the research did not extensively explore advanced deep learning techniques that could potentially offer superior performance through their ability to model intricate patterns and relationships.

The validation approach, predominantly using Stratified K-Fold Cross-Validation, though suitable, might not address all aspects of temporal dependencies in the dataset or will not apply for all the other datasets. Future studies could benefit from incorporating validation techniques that better capture the sequential nature of the data, such as Time Series Cross-Validation. Another limitation is the focus on binary and multi-class classification without considering the potential benefits of regression models for predicting the exact timing of solar flares. Moreover, this research hasn’t employed more advanced algorithms such as AdaBoost, CatBoost, GBM series or time series classifiers such as MINIROCKET, CIF, and Mr-SEQL which may provide better models. One of the major reasons for this exclusion is the computational time and the performance requirements these algorithms require. Lastly, the study's interpretability and the understanding of the decision-making process of the models were not extensively addressed. While model performance was a key focus, the lack of emphasis on interpretability might hinder the practical application and trust in these models by domain experts. Enhancing model transparency and understanding could significantly improve their acceptance and usability in real-world scenarios.

Recognizing these limitations is crucial for guiding future research directions and improving the methodologies and findings in subsequent studies.

## Chapter 6: References

Abduallah, Y. and Wang, J.T.L. 2024. A deep learning approach to operational flare forecasting. arXiv (Cornell University). Available at: https://arxiv.org/abs/2405.16080.

Abduallah, Y., L. Wang, J.T., Nie, Y., Liu, C. and Wang, H. 2021. DeepSun: machine-learning-as-a-service for solar flare prediction. Research in Astronomy and Astrophysics 21(7), p. 160. doi: 10.1088/1674-4527/21/7/160.

Abduallah, Y., Wang, J.T.L., Wang, H. and Xu, Y. 2023. Operational prediction of solar flares using a transformer-based framework. Scientific Reports 13(1). doi: 10.1038/s41598-023-40884- 1.

Ahmadzadeh, A., Aydin, B., Georgoulis, M.K., Kempton, D.J., Mahajan, S.S. and Angryk, R.A.

2021. How to train your flare prediction model: Revisiting robust sampling of rare events. ˜the

œAstrophysical Journal. Supplement Series/Astrophysical Journal. Supplement Series 254(2), p.

23. Available at: https://doi.org/10.3847/1538-4365/abec88.

Ahmed, O.W., Qahwaji, R., Colak, T., Higgins, P.A., Gallagher, P.T. and Bloomfield, D.S. 2011. Solar Flare Prediction Using Advanced Feature Extraction, Machine Learning, and Feature Selection. Solar Physics 283(1), pp. 157–175. doi: 10.1007/s11207-011-9896-1.

Akhilesh, Gupta., Nesime, Tatbul., Ryan, Marcus., Zhou, Shengtian., Insup, Lee., Justin, Gottschlich. (2021). Class-Weighted Evaluation Metrics for Imbalanced Data Classification. arXiv: Learning, Amar, E. and Ben-Shahar, O. 2024. Image Synthesis for Solar Flare Prediction. The Astrophysical Journal Supplement Series 271(1), p. 29. doi: 10.3847/1538-4365/ad1dd4.

Angryk, R.A. et al. 2020. Multivariate time series dataset for space weather data analytics. Scientific Data 7(1). Available at: https://doi.org/10.1038/s41597-020-0548-x.

Aschwanden, M.J. 2019. Self-organized criticality in solar and stellar flares: Are extreme events scale-free? The Astrophysical Journal 880(2), p. 105. Available at: https://doi.org/10.3847/1538- 4357/ab29f4.

Baker, H. 2023. 10 solar storms that blew us away in 2023. Live Science 26 December. Available at: https://www.livescience.com/space/the-sun/10-solar-storms-that-blew-us-away-in-2023 [Accessed: 21 July 2024].

Baylor, R.N. et al. 2011. ESTIMATES OF DENSITIES AND FILLING FACTORS FROM a COOLING TIME ANALYSIS OF SOLAR MICROFLARES OBSERVED WITHRHESSI.

Astrophysical Journal/˜the œAstrophysical Journal 736(1), p. 75. Available at: https://doi.org/10.1088/0004-637x/736/1/75. Bennett, M., Nekouei, M., Mehta, A.P.R., Kleczyk, E. and Hayes, K. 2022. Methodology to Create Analysis-Naive Holdout Records as well as Train and Test Records for Machine Learning Analyses in Healthcare. arXiv (Cornell University). Available at: https://arxiv.org/abs/2205.03987.

Bloomfield, D. S., Higgins, P. A., McAteer, R. T. J., & Gallagher, P. T. 2012, ApJ, 747, L41 Campi, C., Benvenuto, F., Massone, A.M., Bloomfield, D.S., Georgoulis, M.K. and Piana, M.

2019. Feature ranking of active region source properties in solar flare forecasting and the

uncompromised stochasticity of flare occurrence. The Astrophysical Journal 883(2), p. 150. Available at: https://doi.org/10.3847/1538-4357/ab3c26.

Chen, Y. et al. 2019. Identifying Solar Flare Precursors Using Time Series of SDO/HMI Images and SHARP Parameters. Space Weather 17(10), pp. 1404–1426. doi: 10.1029/2019sw002214.

Covey, M.Z. 2023. Solar activity may peak in 2024 in latest NOAA forecast. Spectrum News 13 5 November. Available at: https://mynews13.com/fl/orlando/weather/2023/10/31/solar-activity-may-peak-in-2024-in-latest-noaa-forecast [Accessed: 29 May 2024].

D. McGuire, R. Sauteraud and V. Midya, "Window-Based Feature Extraction Method Using XGBoost for Time Series Classification of Solar Flares," 2019 IEEE International Conference on Big Data (Big Data), Los Angeles, CA, USA, 2019, pp. 5836-5843, doi: 10.1109/BigData47090.2019.9006212.

Dennis, B., Shih, A.Y., Hurford, G.J., Saint-Hilaire, P. (2024). Ramaty High Energy Solar Spectroscopic Imager (RHESSI). In: Bambi, C., Santangelo, A. (eds) Handbook of X-ray and Gamma-ray Astrophysics. Springer, Singapore. https://doi.org/10.1007/978-981-19-6960-7_169 Deshmukh, V., Baskar, S., Berger, T.E., Bradley, E. and Meiss, J.D. 2023. Comparing feature sets and machine-learning models for prediction of solar flares. Astronomy &amp; Astrophysics 674, p. A159. doi: 10.1051/0004-6361/202245742.

Fazekas, A. and Kovacs, G. 2024. Enumerating the k-fold configurations in multi-class classification problems. arXiv (Cornell University). Available at: https://arxiv.org/abs/2401.13843.

Francisco, G., Berretti, M., Chierichini, S., Mugatwala, R., Fernandes, J.M., Barata, T. and Moro, D.D. 2024. Limits of solar flare forecasting models and new deep learning approach. Authorea, Inc. Available at: http://dx.doi.org/10.22541/essoar.170688972.24631782/v1 [Accessed: 09 July 2024].

Han, K., Yu, M.-Y., Fu, J.-F., Ling, W.-B., Zheng, D., Wan, J. and E, P. 2023. Research Progress on Solar Flare Forecast Methods Based on Data-driven Models. Research in Astronomy and Astrophysics 23(6), p. 065002. doi: 10.1088/1674-4527/acca01.

Hollanda, A., Da Silva, A.E.A. and Cinto, T. 2021. Data set for solar flare prediction using helioseismic and magnetic imager vector magnetic field data. Data in Brief 37, p. 107203.

Available at: https://doi.org/10.1016/j.dib.2021.107203. Huang, X., Wang, H., Xu, L., Liu, J., Li, R. and Dai, X. 2018. Deep Learning Based Solar Flare Forecasting Model. I. Results for Line-of-sight Magnetograms. The Astrophysical Journal 856(1), p. 7. doi: 10.3847/1538-4357/aaae00.

Huwyler, C. and Melchior, M. 2022. Using multiple instance learning for explainable solar flare prediction. arXiv (Cornell University). Available at: https://arxiv.org/abs/2203.13896. İ. Yazıcı and E. Gures, "A Novel Approach for Machine Learning-based Load Balancing in High-speed Train System using Nested Cross Validation," 2023 10th International Conference on Wireless Networks and Mobile Communications (WINCOM), Istanbul, Turkiye, 2023, pp. 1-6, doi: 10.1109/WINCOM59760.2023.10323006.

Kuipers, F. 2022. Analytic continuation of stochastic mechanics. Journal of Mathematical Physics 63(4). doi: 10.1063/5.0073096. Kusano, K., Toriumi, S., Shiota, D. and Minoshima, T. 2023. Prediction of solar storms. In: Solar-Terrestrial Environmental Prediction. Singapore: Springer Nature Singapore, pp. 289–325.

Available at: http://dx.doi.org/10.1007/978-981-19-7765-7_10 [Accessed: 17 July 2024]. Liu, C., Deng, N., Wang, J.T.L. and Wang, H. 2017. Predicting Solar Flares Using SDO/HMI Vector Magnetic Data Products and the Random Forest Algorithm. The Astrophysical Journal 843(2), p. 104. doi: 10.3847/1538-4357/aa789b.

Liu, S. et al. 2023. A selective up-sampling method applied upon unbalanced data for flare prediction: potential to improve model performance. Frontiers in Astronomy and Space Sciences 10. doi: 10.3389/fspas.2023.1082694.

Mayangsari, M. K., Syarif, I. and Barakbah, A. (2023) “Evaluation of Stratified K-Fold Cross Validation for Predicting Bug Severity in Game Review Classification”, Kinetik: Game Technology, Information System, Computer Network, Computing, Electronics, and Control, 8(3). doi: 10.22219/kinetik.v8i3.1740.

Moulshree, Anjum, M. and Goel, A. 2022. Solar Flare Prediction using Machine Learning Algorithms on RHESSI Dataset. In: 2022 International Conference on Sustainable Computing and Data Communication Systems (ICSCDS). IEEE. Available at: http://dx.doi.org/10.1109/icscds53736.2022.9760755 [Accessed: 21 July 2024].

Moulshree, M. Anjum and A. Goel, "Solar Flare Prediction using Machine Learning Algorithms on RHESSI Dataset," 2022 International Conference on Sustainable Computing and Data Communication Systems (ICSCDS), Erode, India, 2022, pp. 659-664, doi: 10.1109/ICSCDS53736.2022.9760755.

NASA. 2011. X-Class: A Guide to Solar Flares. NASA Scientific Visualization Studio 9 August. Available at: https://svs.gsfc.nasa.gov/10109/ [Accessed: 21 June 2024].

Nishizuka, N., Sugiura, K., Kubo, Y., Den, M. and Ishii, M. 2018. Deep Flare Net (DeFN) Model for Solar Flare Prediction. The Astrophysical Journal 858(2), p. 113. doi: 10.3847/1538- 4357/aab9a7.

NOAA Space Weather Scales. (2018). Current Space Weather Conditions On NOAA Scales. NOAA. [Online]. Available at: https://www.swpc.noaa.gov/noaa-scales-explanation [Accessed: 19 July 2024].

Pandey, C., Ji, A., Angryk, R.A. and Aydin, B. 2023. Towards Interpretable Solar Flare Prediction with Attention-based Deep Neural Networks. In: 2023 IEEE Sixth International Conference on Artificial Intelligence and Knowledge Engineering (AIKE). IEEE. Available at: http://dx.doi.org/10.1109/aike59827.2023.00021 [Accessed: 27 July 2024].

Pramod, O. 2024. Cross Validation - om pramod - Medium. Medium. 29 February. Available at: https://medium.com/@ompramod9921/cross-validation-623620ff84c2. [Accessed: 06 July 2024].

Qiu, J., Lake, D.E. and Henry, T.R. 2024. Fast leave-one-cluster-out cross-validation by clustered Network Information Criteria (NICc). arXiv (Cornell University). Available at: https://arxiv.org/abs/2405.20400.

R. Kaur, P. Yadav and U. Hariharan, "Solar Flare Prediction Using Hybrid CNN-Model," 2023 7th International Conference on Electronics, Materials Engineering & Nano-Technology (IEMENTech), Kolkata, India, 2023, pp. 1-6, doi: 10.1109/IEMENTech60402.2023.10423531.

Saini, K., Alshammari, K., Hamdi, S.M. and Filali Boubrahimi, S. 2024. Solar Flare Prediction from Extremely Imbalanced Multivariate Time Series Data using Minimally Random Convolutional Kernel Transform. MDPI AG. Available at: http://dx.doi.org/10.20944/preprints202403.0210.v1 [Accessed: 2 May 2024].

Saini, K., Alshammari, K., Hamdi, S.M. and Filali Boubrahimi, S. 2024. Solar Flare Prediction from Extremely Imbalanced Multivariate Time Series Data using Minimally Random Convolutional Kernel Transform. MDPI AG. Available at: http://dx.doi.org/10.20944/preprints202403.0210.v1 [Accessed: 23 July 2024].

Sandfeld, S. 2023. Exploratory data analysis. In: ˜The œMaterials Research Society series. pp. 179–206. Available at: https://doi.org/10.1007/978-3-031-46565-9_9.

Singla, P., Duhan, M. and Saroha, S. 2022. Different normalization techniques as data preprocessing for one step ahead forecasting of solar global horizontal irradiance. In: Elsevier eBooks. pp. 209–230. Available at: https://doi.org/10.1016/b978-0-323-90396-7.00004-3.

Song, H., Tan, C., Jing, J., Wang, H., Yurchyshyn, V. and Abramenko, V. 2008. Statistical Assessment of Photospheric Magnetic Features in Imminent Solar Flare Predictions. Solar Physics 254(1), pp. 101–125. doi: 10.1007/s11207-008-9288-3.

Sun, P. et al. 2022. Solar Flare Forecast Using 3D Convolutional Neural Networks. The Astrophysical Journal 941(1), p. 1. doi: 10.3847/1538-4357/ac9e53.

U. Imran, A. Waris, M. Nayab and U. Shafiq, "Examining the Impact of Different K Values on the Performance of Multiple Algorithms in K-Fold Cross-Validation," 2023 3rd International Conference on Digital Futures and Transformative Technologies (ICoDT2), Islamabad, Pakistan, 2023, pp. 1-4, doi: 10.1109/ICoDT259378.2023.10325695.

Vairetti, C., Assadi, J.L. and Maldonado, S. 2024. Efficient hybrid oversampling and intelligent undersampling for imbalanced big data classification. Expert Systems with Applications 246, p. 123149. doi: 10.1016/j.eswa.2024.123149.

Wan, J., Fu, J.-F., Tan, D.-M., Han, K., Yu, M.-Y. and E, P. 2022. Solar Flare Forecast Model Based on Resampling and Fusion Method. Research in Astronomy and Astrophysics 22(8), p. 085020. doi: 10.1088/1674-4527/ac78d0.

Warmuth, A. and Mann, G. 2016. Constraints on energy release in solar flares from RHESSI and GOES X-ray observations. Astronomy & Astrophysics 588, p. A115. Available at: https://doi.org/10.1051/0004-6361/201527474.

Wen, J., Islam, M.R., Ahmadzadeh, A. and Angryk, R.A. 2022. Improving solar flare prediction by time series outlier detection. arXiv (Cornell University). Available at: https://arxiv.org/abs/2206.07197.

Wen, J., Islam, M.R., Ahmadzadeh, A. and Angryk, R.A. 2023. Improving Solar Flare Prediction by Time Series Outlier Detection. In: Artificial Intelligence and Soft Computing. Cham: Springer International Publishing, pp. 152–164. Available at: http://dx.doi.org/10.1007/978-3-031-23480- 4_13 [Accessed: 13 July 2024].

Zhang, H., Li, Q., Yang, Y., Jing, J., Wang, J.T.L., Wang, H. and Shang, Z. 2022. Solar Flare Index Prediction Using SDO/HMI Vector Magnetic Data Products with Statistical and Machine-learning Methods. The Astrophysical Journal Supplement Series 263(2), p. 28. doi: 10.3847/1538- 4365/ac9b17.

---

*Reading edition only. The source PDF governs any question of original figures, reported metrics and historical assessment.*
