# 6. Analitik Performans Değerlendirmesi (Clause 6 – Analytical Performance Evaluation)

---

## 6.1 General Requirements

### 6.1.1 Evaluation protocol

Evaluation of analytical performance characteristics shall be conducted as part of the manufacturer’s design and development process. The requirements specified in ISO 13485 for design verification apply.

> NOTE 1 The evaluations in Clause 6 are design verification activities, which are intended to provide assurance that the device has the capability to consistently meet the performance specifications set for it.  
> NOTE 2 This International Standard is not intended to specify all design verification activities that may be required to demonstrate that the design outputs meet the design input requirements for analytical performance.

The performance verification studies shall be performed according to a written protocol. The protocol shall specify the acceptance criteria, the statistical design, including the number and type of samples and the numbers of meters, reagent units and replication measurements, experimental conditions and other relevant details, and the data analysis procedures including the treatment of outliers.

Where a specified experimental requirement is not practicable, an alternative statistically valid study design shall be described and justified in the protocol.

The performance criteria for system accuracy in 6.3.3 shall not be directly applied to verification of other performance characteristics, such as precision, bias or influence quantities. Acceptability criteria for these components of system accuracy shall be determined by the manufacturer, taking into account their contribution to system accuracy performance.

All components of the blood-glucose monitoring system, including meters, reagent system and accessories, shall be representative of routine production units. Any differences shall be described and justified.

The blood-glucose monitoring system shall be adjusted according to the manufacturer’s instructions (e.g. via coding, chips), if adjustment is required. No adjustments shall be made between replicate measurements unless the manufacturer’s instructions specify an adjustment is required before each measurement.

The manufacturer’s specified setup and control procedures shall be performed prior to each evaluation.

---

### 6.1.2 Samples

Samples shall meet the requirements of the instructions for use and be appropriate for the performance characteristic being evaluated. Additional requirements for samples may be specified in 6.2 to 6.5.

If higher glucose concentrations are needed, blood samples may be collected with an appropriate anticoagulant and then supplemented with a saline solution of 0.9 % mass concentration containing a high concentration of glucose. The dilution should be as minimal as possible and shall not significantly alter the sample matrix. Supplemented samples shall be allowed to stand for at least 15 min before use to allow the added glucose to equilibrate between the plasma and red blood cells.

If lower glucose concentrations are needed, blood samples may be collected with an appropriate anticoagulant and incubated to allow glycolysis to occur. The anticoagulated blood samples may be allowed to age until glucose is depleted to the desired levels. Incubation conditions (e.g. temperature, mixing) that produce samples compatible with the blood-glucose monitoring system being evaluated (e.g. without haemolysis) shall be determined by the manufacturer. The maximum temperature for aging shall be 37°C.

Commutability of modified samples shall be verified with the blood-glucose monitoring system being evaluated.

> NOTE Reference[20] provides guidelines for demonstrating commutability of a reference material.

Unexpected results when using modified samples shall be investigated by comparison to fresh, unaltered blood samples.

---

### 6.1.3 Data exclusion criteria

If a measurement result is generated during a performance evaluation, it may be excluded from the data only in the following circumstances:

— the blood-glucose monitoring system user recognizes that an error was made and documents the details;

— the meter system error or failure requires the user to retest; if displayed, the meter error (e.g. error number or failure type) shall be documented;

— the meter QC results are out of tolerance or not obtained;

— the sample was tested when QC results from the reference measurement procedure were out of acceptable limits or were not obtained;

— the blood sample was outside the manufacturer’s specifications for an influence quantity, such as packed cell volume;

— the change between first and last reference values indicate glucose instability in the sample based on predetermined criteria;

> EXAMPLE Reference values differ by > 4 % at glucose ≥ 5,55 mmol/l (≥100 mg/dl) or > 0,22 mmol/l (>4 mg/dl) at glucose < 5,55 mmol/l (<100 mg/dl)

— information required to determine that the sample met the inclusion criteria is missing (e.g. no value for packed cell volume).

---

### 6.1.4 Data analysis and presentation of results

Data analysis shall be based on the statistical methods specified in the protocol.

Where data have been excluded, the reason for each exclusion shall be documented in the study report.

In addition to the specific requirements of 6.2 to 6.5, the following information shall be included in the study report:

a) a summary of the study design and reference to the evaluation protocol;

b) a full description of the samples used, including details of any sample alteration procedures that were used and identification of the samples that were altered;

c) detailed description of the reference measurement procedure, including relevant analytical performance characteristics, calibration traceability and validation or verification of imprecision and bias;

d) results and conclusions of the evaluation, including calculated statistical parameters with confidence intervals where appropriate;

e) a summary of data analysis procedures and references to the statistical methods;

f) a summary of outliers identified and excluded from statistical analysis, including the method of identification and the results of the investigation;

> NOTE ISO 5725-2 and Reference[7] provide guidelines for identifying outliers.

g) graphical presentation of the results, where appropriate.
---

## 6.2 Measurement Precision

### 6.2.1 General Requirements

Measurement repeatability and intermediate measurement precision shall be evaluated in simulated conditions of intended use.

> NOTE 1 ISO 5725-1 and Reference [7] describe general principles regarding the evaluation of precision of a measurement method.  
> NOTE 2 The experiments can be designed to evaluate the effect of such factors as different lots, different sample materials, different users, or other variables (e.g. effect of temperature, humidity).  
> NOTE 3 When multiple factors are evaluated, analysis of variance (ANOVA) is the preferred statistical method.

---

### 6.2.2 Acceptance Criteria

Acceptance criteria shall be established in the study protocol.

Criteria for measurement repeatability and intermediate measurement precision should be related to the system accuracy performance criteria in 6.3.3.

> NOTE 1 Measurement repeatability and intermediate measurement precision, along with measurement bias, are components of system accuracy.  
> NOTE 2 Separate criteria for minimum acceptable precision and bias are not specified in this International Standard. The system accuracy evaluation in 6.3 is designed to verify acceptability of the combined effects of random error (imprecision) and systematic error (bias) for the blood-glucose monitoring system under evaluation.

---

### 6.2.3 Measurement Repeatability

#### 6.2.3.1 Study Design

Measurement repeatability shall be evaluated with a series of measurements within a short interval of time, by a single individual using the same meter and reagent lot.

The evaluation shall be conducted with a minimum of 10 meters, 3 reagent lots, and 5 samples with glucose concentrations representing hyperglycaemic, euglycaemic and hypoglycaemic conditions. At least 10 measurements shall be performed with each combination of meter, reagent lot and sample.

Measurement repeatability data shall be collected over a span of time not to exceed one day per meter and reagent lot combination.

> NOTE: Evaluation may include one or multiple users. Use of ANOVA or other valid statistical methods is acceptable if multiple factors are included.

#### 6.2.3.2 Samples

Samples should be venous blood within 0.35 to 0.50 l/l hematocrit. Each glucose interval in Table 1 should be represented.

> Table 1 – Blood-glucose concentration intervals for measurement repeatability evaluation  
> | Interval | Glucose Concentration (mmol/l) | Glucose Concentration (mg/dl) |  
> |---------|-------------------------------|-------------------------------|  
> | 1       | 1.7 – 2.8                     | 30 – 50                       |  
> | 2       | 2.9 – 6.1                     | 51 – 110                      |  
> | 3       | 6.2 – 8.3                     | 111 – 150                     |  
> | 4       | 8.4 – 13.9                    | 151 – 250                     |  
> | 5       | 14.0 – 22.2                   | 251 – 400                     |

#### 6.2.3.3 Evaluation Procedure

Each combination of sample and meter should yield 10 measurements. Control strips may be used. Reference measurements must be taken at the start and end of measurement cycle to confirm glucose stability.

#### 6.2.3.4 Data Analysis and Presentation of Results

- For each concentration:  
  - Calculate: average, standard deviation, CV (coefficient of variation)
- Across lots:  
  - Calculate pooled average, pooled variance, pooled SD (95% CI), and pooled CV

---

### 6.2.4 Intermediate Measurement Precision

#### 6.2.4.1 Study Design

Test must be done with:
- 10 meters
- 3 reagent lots
- 3 glucose concentrations  
- Over minimum 10 days  
- With 1 test per day per sample

> NOTE: ISO 5725-3 applies. At least one reading per sample per day. Reagents remain from the same lot per meter for all 10 days.

#### 6.2.4.2 Samples

Use manufacturer's control materials. Concentration intervals:

> Table 2 – Glucose concentration intervals for intermediate precision  
> | Interval | Glucose (mmol/l) | Glucose (mg/dl) |  
> |----------|------------------|------------------|  
> | 1        | 1.7 – 2.8        | 30 – 50          |  
> | 2        | 5.3 – 8.0        | 96 – 144         |  
> | 3        | 15.5 – 23.3      | 280 – 420        |

#### 6.2.4.3 Evaluation Procedure

Each day:
- 1 measurement per sample  
- 10 days  
- 3 concentrations  
- 10 meters  
- Use same reagent vial per meter across days

#### 6.2.4.4 Data Analysis and Presentation of Results

- Calculate: average, SD, CV per concentration and lot  
- Calculate: pooled SD (with 95% CI) and pooled CV  
- Use ANOVA to separate variance components

---

> 📌 Devamı için 6.3 – System Accuracy bölümüne geçmeden önce bu içeriği `.md` dosyasına ekleyip kaydedin.
---

## 6.3 System Accuracy

### 6.3.1 General Requirements

System accuracy capability shall be evaluated with fresh blood samples by comparing glucose measurements from the blood-glucose monitoring system to reference glucose values.

The evaluation shall be conducted in actual conditions of use, preferably in a diabetes outpatient clinic or hospital setting. Ambient temperature shall be maintained at 23°C ± 5°C.

---

### 6.3.2 Glucose Reference Values

A reference measurement procedure conforming to ISO 17511 shall be used to assign glucose values. Reference values must be based on duplicate or more measurements.

Reference method must be traceable and verified for trueness and precision.

If the reference method is not directly applicable to whole blood, samples must be centrifuged for plasma.

---

### 6.3.3 Minimum System Accuracy Performance Criteria

The blood-glucose monitoring system shall meet BOTH of the following:

**a)** 95% of results shall fall within:  
- ±0.83 mmol/L (±15 mg/dL) of reference for glucose <5.55 mmol/L (<100 mg/dL)  
- ±15% of reference for glucose ≥5.55 mmol/L (≥100 mg/dL)

**b)** 99% of results shall fall within zones A and B of the Consensus Error Grid (CEG)

> NOTE 1: Criteria A applies to each reagent lot individually.  
> NOTE 2: Criteria B applies to the full dataset combined from 3 lots.

---

### 6.3.4 Study Design

- At least **100 subjects**  
- Each subject provides a **fresh capillary blood sample**  
- Each of **3 reagent lots** is used  
- Minimum **600 total data points**

If a combined device (skin puncture + measurement) is used, an alternative statistically valid study design is acceptable.

The study must include realistic sources of variability such as:
- Different operators  
- Different meters  
- Real-use environment

---

### 6.3.5 Samples

Samples must be:
- Fresh capillary blood
- Collected according to manufacturer’s instructions

Sample glucose concentrations must span from low to high per Table 3:

> **Table 3 – Glucose Bins**  
> | Bin # | % of Samples | Glucose Range (mmol/L) | mg/dL |
> |-------|--------------|------------------------|-------|
> 1 | 5%   | ≤ 2.77       | ≤ 50  
> 2 | 15%  | 2.78 – 4.44  | 51–80  
> 3 | 20%  | 4.45 – 6.66  | 81–120  
> 4 | 30%  | 6.67 – 11.10 | 121–200  
> 5 | 15%  | 11.11 – 16.65| 201–300  
> 6 | 10%  | 16.66 – 22.20| 301–400  
> 7 | 5%   | > 22.20      | > 400  

Modified samples may be used ONLY for bins 1, 2, 6, and 7 with restrictions.

---

### 6.3.6 Evaluation Procedure

Steps:
a) Assign vial/package numbers  
b) Collect blood by skin puncture  
c) Measure reference glucose before first test  
d) Prepare plasma if required  
e) Perform 2 device measurements using 2 meters  
f) Repeat for all 3 lots  
g) Measure reference glucose again after tests  
h) Confirm sample stability  
i) Repeat for next subject  

Samples not meeting stability criteria must be excluded and replaced.

---

### 6.3.7 Data Analysis and Presentation of Results

#### 6.3.7.1 General Requirements

- Use ALL valid data points  
- Outliers cannot be removed for accuracy determination  
- Exclusion reasons must be documented  
- Include statistical summaries, confidence intervals, plots

#### 6.3.7.2 Graphical Analysis

Plot difference between system result and reference value.  
Outliers should be marked separately.

> NOTE: Difference plots are preferred. Percentage differences at low glucose are discouraged.

---

#### 6.3.7.3 Determination of Acceptability

**Criterion A:**  
- Apply individually to each lot  
- Calculate how many points fall within accuracy ranges  
- Each lot must meet the 95% criterion

**Criterion B:**  
- Apply to combined data from all lots  
- 99% of values must fall in zones A + B of the Consensus Error Grid

---

#### 6.3.7.4 Presentation of Results

Results must be tabulated in the following format:

> **Table 4 – <100 mg/dL**
| Range           | Count (n/N) | Percent |
|------------------|-------------|---------|
| ±5 mg/dL         | 68/150       | 45.3%   |
| ±10 mg/dL        | 105/150      | 70.0%   |
| ±15 mg/dL        | 143/150      | 95.3%   |

> **Table 5 – ≥100 mg/dL**
| Range           | Count (n/N) | Percent |
|------------------|-------------|---------|
| ±5%              | 221/450      | 49.1%   |
| ±10%             | 383/450      | 85.1%   |
| ±15%             | 439/450      | 97.6%   |

> **Table 6 – Combined Results**
| Range           | Count (n/N) | Percent |
|------------------|-------------|---------|
| ±15 mg/dL or ±15%| 582/600      | 97.0%   |

---

> 📌 Sonraki adım: 6.4 – Influence Quantities (girişim yapan etkenler)
---

## 6.4 Influence Quantities

### 6.4.1 General Requirements

The effect of influence quantities, such as packed cell volume and interfering substances in blood, shall be evaluated and addressed in the risk management process. Effects that exceed the acceptability criteria shall be disclosed in the instructions for use.

- Three reagent lots shall be used.
- Multiple meters may be used.
- Design shall prevent meter-to-meter variation from confounding results.

---

### 6.4.2 Test Sample Requirements

- Samples must be fresh blood, preferably venous.
- Equilibrated to 23°C ± 5°C and maintained within ±3°C during testing.
- All testing must be completed within 36 hours of blood collection.
- Reference and device testing must be done within the same time frame.

> NOTE: Blood samples may deteriorate with age, affecting result accuracy.

---

### 6.4.3 Packed Cell Volume Evaluation

#### 6.4.3.1 Study Design

- Minimum of 5 packed cell volumes at 3 glucose concentrations.
- Experimental design: Packed Cell Volume (PCV) × Glucose Concentration.
- Use traceable and validated reference procedures.

#### 6.4.3.2 Acceptance Criteria

For glucose <5.55 mmol/L (<100 mg/dL):  
- Difference from mid-level PCV exceeds 0.55 mmol/L (10 mg/dL)

For glucose ≥5.55 mmol/L (≥100 mg/dL):  
- Difference exceeds 10%

#### 6.4.3.3 Sample Preparation

Prepare PCV levels:
1. Separate plasma from whole blood
2. Pool plasma
3. Recombine with cells at different ratios to create PCV gradient
4. Adjust to 5 glucose levels across 3 PCVs

Target mid-level PCV: 42% ± 2%

#### 6.4.3.4 Evaluation Procedure

- Duplicate reference measurements
- At least 10 measurements per reagent lot per PCV level
- Rotate meters to avoid bias
- Repeat reference after device testing
- If glucose instability is detected, discard data

#### 6.4.3.5 Data Analysis and Presentation

For each PCV and glucose concentration:

- Calculate mean and SD
- Calculate bias (%)
- Compare each PCV bias to mid-level
- Graphically present results

---

### 6.4.4 Interference Testing

#### 6.4.4.1 Study Design

- Minimum of 2 glucose levels tested:  
  • Low: 2.8 – 5.5 mmol/L (50–100 mg/dL)  
  • High: 13.9 – 19.4 mmol/L (250–350 mg/dL)

- Risk analysis shall identify potential interferents.
- See Annex A for common substances (e.g., paracetamol, uric acid).

Paired-sample design is recommended:
- Compare test sample with interferent vs. control without

#### 6.4.4.2 Acceptance Criteria

For glucose <5.55 mmol/L:  
- Average difference > 0.55 mmol/L (10 mg/dL) → interference detected

For glucose ≥5.55 mmol/L:  
- Average difference > 10%

#### 6.4.4.3 Sample Preparation

- Collect 2 pools of venous blood
- Adjust glucose concentrations as needed
- Divide each pool:
  - One as control
  - One with interferent added

Ensure sample volumes are identical

#### 6.4.4.4 Evaluation Procedure

- Duplicate reference measurements
- 10 meter tests per lot
- Compare after exposure to interferent
- If deviation exceeds limits, perform dose-response evaluation

Dose-response:  
- Create 5 mixtures (interferent + control in varying ratios)
- Analyze linearity of interference

#### 6.4.4.5 Data Analysis and Presentation

For each interferent and glucose level:
- Calculate average, SD, bias
- Determine deviation from control
- Present graph if dose-response performed
- If consistent across lots, results can be pooled

> Results must be listed in the instructions for use if acceptability limits are exceeded.

---

> 📌 Sonraki adım: 6.5 – Stability of reagents and materials
---

## 6.5 Stability of Reagents and Materials

### 6.5.1 General Requirements

If the reagent system, control materials and other components may be subject to degradation over time, the conditions for storage and use shall be defined and validated.

- The manufacturer shall provide evidence that the product remains stable and performs acceptably over its intended shelf life and use period.
- Stability studies shall simulate real-world storage and transport conditions.
- Conditions must include temperature, humidity, exposure to light, and mechanical stress where applicable.

---

### 6.5.2 Stability Determination

The requirements specified in ISO 23640 that pertain to establishing stability performance and expiry dating apply.

- Manufacturer must define:
  - **Storage conditions** (e.g. 2–30°C, protected from light)
  - **Shelf life** (e.g. 18 months unopened, 90 days after opening)
  - **Expiry date format and placement** on labels

- Studies should address:
  - **Accelerated stability testing**: Predict long-term stability by testing at elevated stress (e.g. 45°C, 75% RH for 2 weeks)
  - **Real-time stability testing**: Store under normal conditions over full claimed shelf life
  - **Open-vial stability**: How long reagents remain usable after opening

> Testing must include performance verification (e.g. precision, bias) at beginning and end of stated period.

---

> 📌 Bu alt bölüm ile Clause 6 – Analytical Performance Evaluation bölümü tamamlanmıştır.  
> Artık bu `.md` dosyasını kapatabilir ve 7. bölüme geçebiliriz.
