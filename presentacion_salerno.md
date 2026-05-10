# Propuesta de Presentación: "Computational Methods for the Design of Adsorptive and Separation Materials: From Molecular Simulations to Continuum Models"

## 1. Estructura General de la Charla

La presentación está diseñada para durar aproximadamente 50 minutos, dejando 10-15 minutos para preguntas. Para permitir una discusión profunda sin saturar visualmente a la audiencia, se ha subdividido el contenido en unas 36 diapositivas. Se divide en 5 grandes bloques que reflejan la evolución desde la escala molecular hasta modelos continuos y sistemas integrados.

| Bloque | Tema Principal | Tiempo Estimado | Diapositivas |
| :--- | :--- | :--- | :--- |
| **I** | **Introducción y Motivación:** El desafío del diseño multiescala | 5 min | 1 - 5 |
| **II** | **La Escala Molecular (MC & DFT):** Carbones, Mezclas y MOFs | 18 min | 6 - 18 |
| **III** | **La Mesoescala:** Teoría Termodinámica e Hidrogeles | 12 min | 19 - 24 |
| **IV** | **El Dispositivo Macroscópico:** Iontrónica y Modelos Continuos | 12 min | 25 - 32 |
| **V** | **Conclusiones, Perspectivas y Agradecimientos** | 3 min | 33 - 36 |

---

## 2. Guión Detallado Slide por Slide

### Bloque I: Introducción (0-5 min)

**Slide 1: Título de la Presentación**
*   **Objetivo:** Presentación formal y captura de atención.
*   **Contenido:** Título completo, nombre del orador, afiliación (INIFTA, CONICET, UNLP).
*   **Visual:** Diseño minimalista con logotipos institucionales y una figura de fondo sutil que fusione una red molecular con un gradiente continuo.

**Slide 2: El Desafío del Diseño de Materiales Modernos**
*   **Objetivo:** Establecer el problema general.
*   **Contenido:** Urgencia global: eficiencia energética en separación de gases, captura de CO2, remediación de contaminantes (glifosato). Limitaciones del ensayo y error.
*   **Visual:** Esquema conceptual: "Laberinto" (Ensayo y Error) vs "Línea Recta" (Diseño Racional In-Silico).

**Slide 3: El Paradigma Multiescala en Fisicoquímica Computacional**
*   **Objetivo:** Presentar el mapa de ruta.
*   **Contenido:** Cómo conectar la química atómica con el flujo de un fluido. (QM/DFT) -> (Monte Carlo / Dinámica Molecular) -> (Modelos Continuos/Poisson-Nernst-Planck).
*   **Visual:** Flecha de escalas espaciotemporales (Å a mm, ps a s) resaltando las técnicas que se presentarán.

**Slide 4: Mi Trayectoria Científica (Breve)**
*   **Objetivo:** Posicionar tu experiencia y autoridad.
*   **Contenido:** 20 años de evolución: desde tesis en adsorción sobre carbono, hasta biomateriales blandos y nanomembranas iontrónicas actuales.
*   **Visual:** Línea de tiempo con iconos de (1) Grafito, (2) MOFs, (3) Nanogeles, (4) Nanoporos.

**Slide 5: Pregunta Conductora**
*   **Objetivo:** Enganchar a la audiencia.
*   **Contenido:** "¿Cómo predecir la funcionalidad macroscópica de un material a partir de sus interacciones atómicas locales?"
*   **Visual:** Texto grande y llamativo sobre fondo oscuro.

---

### Bloque II: La Escala Molecular - MC y DFT (5-23 min)

**Slide 6: La Lupa Subatómica (DFT y Curvatura)**
*   **Objetivo:** Mostrar cómo los electrones dictan la química superficial.
*   **Contenido:** Primeros estudios: Efecto de la curvatura en nanotubos vs grafeno plano para adsorción de gases simples.
*   **Visual:** Mapas de potencial electrostático sobre superficies curvas. *(Cita: Rev. Inf. Tec. 2009)*.

**Slide 7: Efectos del Solvente en Especies Complejas (Glifosato)**
*   **Objetivo:** Profundizar en interacciones soluto-solvente con DFT.
*   **Contenido:** Estudio de confórmeros de glifosato y sus formas desprotonadas en 8 solventes diferentes. Determinación del orden de protonación (amino -> fosfonato -> carboxilo).
*   **Visual:** Estructuras zwitteriónicas optimizadas y espectros NMR calculados. *(Cita: Chem. Phys. Impact 2023)*.

**Slide 8: Empujando los Límites Computacionales (Metadinámica y ReaxFF)**
*   **Objetivo:** Mostrar técnicas de vanguardia en la escala atómica.
*   **Contenido:** Colaboración para el cálculo eficiente de pKa. Superando las barreras del "biasing" unidimensional usando Dinámica Acelerada y campos de fuerza reactivos.
*   **Visual:** Superficies de energía libre en 2D (coordinación vs distancia catión-anión). *(Cita: J. Phys. Chem. B 2023 con C. Wexler)*.

**Slide 9: Simulaciones Monte Carlo (GCMC): El Patrón Oro en Adsorción**
*   **Objetivo:** Transición a la escala estadística molecular.
*   **Contenido:** GCMC: equilibrio de potencial químico, volumen y temperatura. Cómo predecir la isoterma termodinámica ideal.
*   **Visual:** Animación o snapshot de moléculas (esferas de Lennard-Jones) fluctuando en un poro tipo ranura.

**Slide 10: Modelos Atomísticos en Materiales Carbonosos**
*   **Objetivo:** Adsorción de gases simples.
*   **Contenido:** Grafeno exfoliado, nanohorns y nanotubos (SWNTs). Sinergia entre microcalorimetría experimental y calores isostéricos simulados.
*   **Visual:** Gráficos de isotermas simuladas vs experimentales para N2, CH4, CO2.

**Slide 11: Escalamiento hacia Moléculas Grandes: Modelos "Coarse-Grained"**
*   **Objetivo:** Cómo resolver sistemas más pesados (alcanos).
*   **Contenido:** Reducción de grados de libertad para n-butano y n-octano en carbones activados. Comparativa de precisión computacional vs tiempo.
*   **Visual:** Esquema de reducción (4 átomos de carbono mapeados a un pseudoátomo CG). *(Cita: Adsorption 2019)*.

**Slide 12: Búsqueda de Nuevos Adsorbentes: Nanografenos y Hélices de Rileno**
*   **Objetivo:** Adsorción de CO2 en materiales sintéticos de última generación.
*   **Contenido:** Evaluación in-silico de materiales cristalinos puros (nanoconos, macrociclos C72, Rilenos). 
*   **Visual:** Estructuras moleculares complejas de los rilenos y sus poros interconectados. *(Cita: Adsorption 2024)*.

**Slide 13: El Reto de las Mezclas Gaseosas y Selectividad Competitiva**
*   **Objetivo:** Acercamiento a aplicaciones reales de separación.
*   **Contenido:** Separación Ar/CH4 y CO2/CH4. Efectos de inversión de selectividad a bajas presiones estudiados por GCMC e IAST.
*   **Visual:** Diagramas de fase adsorbida y selectividades cruzadas. *(Cita: Chem. Phys. Lett. 2016 con M. Rafti)*.

**Slide 14: MOFs: El Paraíso del Diseño Reticular**
*   **Objetivo:** Introducir los Metal-Organic Frameworks.
*   **Contenido:** Ventajas de los MOFs para el modelado: cristalinidad perfecta y parametrización clara frente a la heterogeneidad del carbón.
*   **Visual:** Estructura tipo andamio de un ZIF-8 o UiO-66.

**Slide 15: "Respiración" en MOFs: El Efecto Gate-Opening**
*   **Objetivo:** Superar la idea de un poro rígido.
*   **Contenido:** Adsorción de Xenón en ZIF-8. Las isotermas experimentales tienen "escalones" que la simulación de red rígida no captura hasta introducir flexibilidad rotacional.
*   **Visual:** Isoterma escalonada característica del "gate-opening".

**Slide 16: Expansión Inducida por Adsorción en GOFs**
*   **Objetivo:** Expansión macroscópica por presión interna de gas.
*   **Contenido:** Graphene Oxide Frameworks (GOFs) puenteados por ácido benceno-1,4-diborónico. Dinámica Molecular para simular la expansión interlaminar de hasta ~1 nm al adsorber metano/xenón.
*   **Visual:** Serie temporal (snapshots de MD) mostrando los planos de grafeno separándose. *(Cita: ACS Omega 2022)*.

**Slide 17: Separación Fina: Isómeros Petroquímicos en MOFs Funcionalizados**
*   **Objetivo:** Aplicación industrial punta.
*   **Contenido:** Separación de isómeros de pentano en UiO-66 funcionalizado. Diferenciación geométrica estricta.
*   **Visual:** Mapas de densidad espacial (isoficies) que muestran dónde se aloja preferentemente el isómero lineal vs el ramificado. *(Cita: Separations 2025)*.

**Slide 18: Límites de la Simulación Atomística y Transición**
*   **Objetivo:** Conectar el Bloque II con el Bloque III.
*   **Contenido:** MC y MD son perfectos para gases y MOFs. ¿Pero qué pasa al intentar modelar redes de polímeros que se hinchan en solvente explícito, atrapando herbicidas masivos?
*   **Visual:** "Cuello de botella" computacional: Demasiados átomos, tiempos de relajación muy lentos.

---

### Bloque III: La Mesoescala (23-35 min)

**Slide 19: Teoría Molecular de Sistemas Blandos (Molecular Theory)**
*   **Objetivo:** Presentar el marco teórico termodinámico de campo medio (I. Szleifer / G. Longo).
*   **Contenido:** Minimización de Energía Libre. Integra la entropía conformacional del polímero con equilibrios ácido-base e interacciones electrostáticas.
*   **Visual:** Ecuación de Energía Libre simplificada y grilla de discretización del espacio (1D/2D).

**Slide 20: Polímeros Sensibles al Medio Ambiente**
*   **Objetivo:** Introducir "smart materials".
*   **Contenido:** Films de polialilamina (PAH) en agua. Su estado de carga y conformación cambian con el pH y la salinidad.
*   **Visual:** Representación de un polímero "colapsado" vs "hinchado" (brush).

**Slide 21: Remediación Ambiental: Secuestro de Glifosato**
*   **Objetivo:** Aplicación de alto impacto local.
*   **Contenido:** Adsorción de glifosato y AMPA en PAH. La teoría revela una fuerte competencia con los aniones de la sal.
*   **Visual:** Perfiles de densidad. Función no-monotónica de adsorción vs pH. *(Cita: Langmuir 2018, Adsorption 2019)*.

**Slide 22: Desprotonación Confinada (El Microambiente Local)**
*   **Objetivo:** Profundidad termodinámica.
*   **Contenido:** Descubrimiento clave: El pH dentro del film de PAH es distinto al "bulk". El glifosato altera su estado de protonación localmente al ingresar al polímero.
*   **Visual:** Gráfico de pKa aparente vs pKa intrínseco.

**Slide 23: Nanomedicina: Liberación Controlada de Fármacos**
*   **Objetivo:** De films a Microgeles (esferas 3D).
*   **Contenido:** Nanogeles de NIPAm/MAA. Absorción de Daunorubicina/Doxorubicina. La liberación es activada por competencia con poliaminas o cambios de pH.
*   **Visual:** Gráficos de Transición de Fase de Volumen (VPTT). *(Cita: Soft Matter 2020, Macromolecules 2020)*.

**Slide 24: Coronas Proteicas y Arquitectura "Janus"**
*   **Objetivo:** Interacciones biológicas (proteínas) y recientes simulaciones MD de polímeros.
*   **Contenido:** Impacto de la arquitectura del nanogel (NIPAm en el núcleo vs azar vs superficie). Formación de parches hidrofóbicos al calentarse (colapso térmico).
*   **Visual:** Mapas de adsorción de insulina/citocromo. Estructuras Janus simuladas. *(Cita: JPCB 2024, Macromolecules 2025)*.

---

### Bloque IV: Modelos Continuos e Iontrónica (35-47 min)

**Slide 25: El Salto a la Escala Macroscópica y Dispositivos**
*   **Objetivo:** Presentar los canales de estado sólido.
*   **Contenido:** Dejamos la adsorción estática y pasamos al flujo dinámico. Nanoporos asimétricos (cónicos) en PET modificados superficialmente.
*   **Visual:** Esquema de un "track-etched nanopore" bajo un gradiente eléctrico.

**Slide 26: Iontrónica: El Diodo Nanofluídico**
*   **Objetivo:** Qué es y para qué sirve.
*   **Contenido:** Control direccional del transporte de iones. Rectificación de corriente debido a la carga superficial asimétrica (igual que un diodo semiconductor, pero con iones).
*   **Visual:** Curvas I-V asimétricas características (estado abierto vs cerrado).

**Slide 27: El Modelo Matemático: PNP-NS (Poisson-Nernst-Planck-Navier-Stokes)**
*   **Objetivo:** Herramientas de Elementos Finitos (COMSOL).
*   **Contenido:** Acoplamiento de la termodinámica iónica con la fluidodinámica clásica y la electrostática.
*   **Visual:** Perfil 2D axilsimétrico del cono coloreado según la concentración iónica local o líneas de flujo electroosmótico.

**Slide 28: Diodos Inteligentes con "Brushes" Supramoleculares**
*   **Objetivo:** Conectar el polímero del Bloque III con el poro del Bloque IV.
*   **Contenido:** Nanoporos recubiertos con poliaminas (PAH). La rectificación se vuelve reversible con el pH y sensible al acoplamiento supramolecular con iones fosfato.
*   **Visual:** Esquemas "host-guest" dentro del canal cónico. *(Cita: Chem. Sci 2017, Small 2018)*.

**Slide 29: Optimización Geométrica para "Blue Energy"**
*   **Objetivo:** Generación de energía por gradiente salino (Energía Osmótica).
*   **Contenido:** ¿Por qué un cono recto no es suficiente? El descubrimiento de los canales "bullet-shaped" (forma de bala).
*   **Visual:** Gráficos de potencia generada: Bala vs Cono vs Cilindro. *(Cita: Nano Energy 2020)*.

**Slide 30: Mitigando la Polarización de Concentración**
*   **Objetivo:** Explicación teórica del éxito "bullet-shaped".
*   **Contenido:** La punta suave de la "bala" reduce los vórtices electroosmóticos limitantes, mejorando masivamente la conductancia diferencial.
*   **Visual:** Mapas vectoriales de flujo fluido (Navier-Stokes) mostrando la eliminación de vórtices.

**Slide 31: Anomalías No-Lineales: Resistencia Incremental Negativa**
*   **Objetivo:** Fenómenos emergentes fascinantes en nanoporos.
*   **Contenido:** Transporte de sales de solubilidad moderada (KClO4). Al aumentar el voltaje, el canal se "tapona" reversiblemente por precipitación inducida en la punta asimétrica, bajando la corriente.
*   **Visual:** Curva I-V con forma de "N" invertida. *(Cita: Nanoscale 2024)*.

**Slide 32: La Obra Maestra Multiescala: "Pore-in-Pore"**
*   **Objetivo:** El clímax que une todos los bloques (Iontrónica + MOFs).
*   **Contenido:** Crecimiento de MOFs *dentro* de un canal de estado sólido. Dominando regímenes de transporte combinando confinamiento macroscópico con tamizado atómico.
*   **Visual:** Render espectacular de un nanoporo relleno de cristales de MOF. *(Cita: ACS Nano 2024)*.

---

### Bloque V: Conclusiones y Cierre (47-50 min)

**Slide 33: El Mapa Completo (Recapitulación)**
*   **Objetivo:** Demostrar cómo se resolvió la pregunta inicial (Slide 5).
*   **Contenido:** DFT dio los parámetros -> MC validó los poros rígidos -> Teoría molecular entendió los polímeros blandos -> PNP diseñó el dispositivo funcional. Todo está interconectado.
*   **Visual:** Gráfico central conectando las técnicas de los distintos bloques en un solo ecosistema predictivo.

**Slide 34: Perspectivas Futuras**
*   **Objetivo:** Mirar hacia adelante.
*   **Contenido:** Gemelos digitales de membranas completas. La integración de Machine Learning e Inteligencia Artificial (tu nueva área de trabajo) para acelerar el cribado de materiales sin requerir millones de horas de cálculo tradicional.
*   **Visual:** Íconos de redes neuronales intersecando con estructuras moleculares.

**Slide 35: Agradecimientos Institucionales y Colaboradores**
*   **Objetivo:** Reconocimiento.
*   **Contenido:** INIFTA, CONICET, UNLP, AGENCIA. Grupos experimentales clave (Azzaroni, Rafti, Longo). Investigadores internacionales (Wexler, Toimil-Molares). 
*   **Visual:** Logos institucionales claros.

**Slide 36: Agradecimientos Especiales: El Equipo**
*   **Objetivo:** Reconocer a tesistas y becarios que hicieron el trabajo de trinchera computacional (Pérez-Chávez, Farías Hermosilla, Cruz González).
*   **Visual:** Foto grupal y correo de contacto (alberto.albesa@gmail.com). Apertura a preguntas.

---

## 3. Integración Directa con la Audiencia (Speaker Notes)

*   **Evita la sobrecarga cognitiva:** Al haber subdividido las slides, tienes un máximo de 1 idea principal por pantalla. Si hay un gráfico complejo (como el campo PNP o la isoterma de adsorción multicomponente), tómate 20 segundos solo para explicar los ejes (X e Y) antes de explicar la física.
*   **Manejo del Tiempo:** Como ahora tienes ~36 diapositivas, debes mantener un ritmo de **1.2 a 1.5 minutos por slide**. Las slides de transición (ej. Slide 18, 25) deben pasarse en menos de 30 segundos, actuando como simples marcadores de capítulo.
*   **Conexiones Experimentales:** Siempre que muestres un resultado teórico (especialmente en Iontrónica y MOFs), usa frases como: *"Nuestros cálculos demostraron por qué los experimentos de nuestros colegas en el laboratorio estaban observando este comportamiento anómalo..."* Esto resalta el valor de la teoría aplicada, no la simulación como un ente aislado.
