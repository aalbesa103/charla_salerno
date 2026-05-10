# Atlas Teórico Multiescala: Herramientas y Problemas Solucionados

Este atlas documenta la arquitectura científica de tu investigación, clasificada por la escala del fenómeno estudiado. Cubre la totalidad de los 26 papers analizados.

---

## ESCALA 1: ELECTRÓNICA (Teoría Cuántica y DFT)
*Herramientas: Density Functional Theory (DFT), Gaussian, B3LYP, LANL2DZ, 6-311++G(2d,2p).*

### 1.1 Estructura y Solvatación del Glifosato
*Paper: Hermosilla & Albesa (2022) - Gly-Solvent*
*   **Herramienta:** DFT con modelos de solvatación implícita (SMD/IEFPCM).
*   **Pregunta Solucionada:** ¿Cuál es la conformación real del glifosato en diferentes solventes (agua, DMSO, acetona)? El RMN da un promedio, pero la teoría permite identificar los 10 conformeros estables y su población de Boltzmann.
*   **Impacto:** Se demostró que el glifosato cambia drásticamente de estructura según el medio, lo que afecta su movilidad ambiental.

### 1.2 Interacción CO2 - Nanotubos de Carbono
*Paper: CO2_NT__8_*
*   **Herramienta:** DFT para el cálculo de energías de interacción punto a punto.
*   **Pregunta Solucionada:** ¿A qué distancia y con qué orientación es máxima la captura de CO2 dentro de un nanotubo?
*   **Impacto:** Permitió predecir el "diámetro óptimo" de nanotubos para almacenamiento de carbono antes de realizar la síntesis.

---

## ESCALA 2: MOLECULAR (Monte Carlo y Dinámica Molecular)
*Herramientas: GCMC (Grand Canonical Monte Carlo), MD, Metadynamics, Campos de Fuerza (UFF, TraPPE).*

### 2.1 Adsorción Competitiva de Mezclas Binarias
*Paper: Albesa et al. (2016) - Chem. Phys. Letters*
*   **Herramienta:** GCMC en el ensamble Gran Canónico.
*   **Pregunta Solucionada:** ¿Cómo se desplazan mutuamente el metano y el argón en la superficie de un material? El experimento mide la masa total, pero el GCMC permite "ver" cuántas moléculas de cada tipo hay en la monocapa.
*   **Impacto:** Validación del modelo IAST (Ideal Adsorbed Solution Theory) frente a simulaciones reales.

### 2.2 Dinámica de Captura de Agroquímicos
*Paper: Hermosilla et al. (2019) - Gly-Transport*
*   **Herramienta:** Dinámica Molecular (MD) y Metadynamics.
*   **Pregunta Solucionada:** ¿Cuál es la barrera energética que debe superar el glifosato para entrar en una cavidad polimérica?
*   **Impacto:** Identificación del camino de mínima energía para el transporte de herbicidas.

---

## ESCALA 3: MESOSCÓPICA (Teoría Molecular y Nanoconfinamiento)
*Herramientas: Teoría Molecular (Nap/Szleifer), Optimización del Potencial de Helmholtz.*

### 3.1 Diseño de Nanogeles para Captura de Proteínas
*Paper: Pérez-Chávez et al. (2024) - JPCB*
*   **Herramienta:** Teoría Molecular con descripción explícita de topología de red.
*   **Pregunta Solucionada:** ¿Cómo afecta la distribución de carga (Core vs Shell) la capacidad de adsorción de proteínas?
*   **Impacto:** Reveló que funcionalizar el "Core" es superior porque la red protege a la proteína del entorno, maximizando la estabilidad.

### 3.2 Regulación de Carga en Herbicidas
*Paper: Pérez-Mitta et al. (2018) - Small / Adsorption (2019)*
*   **Herramienta:** Teoría Molecular incluyendo equilibrios químicos de protonación.
*   **Pregunta Solucionada:** ¿Por qué el glifosato se adsorbe más de lo esperado según su carga en el bulk?
*   **Impacto:** El modelo predijo la "Regulación de Carga": el glifosato cambia su estado de oxidación al entrar al nanogel para atraerse más fuertemente con el polímero.

---

## ESCALA 4: CONTINUO (Transporte Iónico y Energía)
*Herramientas: Poisson-Nernst-Planck (PNP), Navier-Stokes, Elementos Finitos.*

### 4.1 Conversión de Energía Osmótica (Blue Energy)
*Paper: Laucirica et al. (2020) - Sep. and Purif. Tech.*
*   **Herramienta:** Ecuaciones de PNP acopladas.
*   **Pregunta Solucionada:** ¿Cuál es la geometría de nano-canal que maximiza la potencia de salida?
*   **Impacto:** Se demostró que el diseño "bullet-shaped" optimiza la rectificación iónica y la densidad de potencia, superando a los canales cilíndricos tradicionales.

### 4.2 Iontrónica y Nano-impactos
*Paper: Laucirica et al. (Nano-Impacts)*
*   **Herramienta:** Modelos de transporte de masa y carga en estado estacionario.
*   **Pregunta Solucionada:** ¿Cómo detectar partículas individuales mediante su firma de corriente iontrónica?
*   **Impacto:** Teoría para el desarrollo de sensores de ultra-alta sensibilidad.

---

> [!TIP]
> **Narrativa Sugerida:** Usa este Atlas para decir: *"No usamos una sola herramienta porque el problema no es de una sola escala. Resolvemos la química con DFT, la competencia molecular con GCMC, el nanoconfinamiento con Teoría Molecular y el transporte final con PNP."*
