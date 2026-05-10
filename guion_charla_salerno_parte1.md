# GUION CHARLA SALERNO — 50 MINUTOS
# Alberto Albesa · INIFTA-CONICET-UNLP
# Parte 1: Introducción → Monte Carlo (~25 min)

---

## ⏱ DISTRIBUCIÓN DE TIEMPOS

| Sección | Tiempo |
|---------|--------|
| Introducción + Tabla | 6 min |
| Nivel Cuántico (DFT) | 8 min |
| Puente Estadístico | 3 min |
| Monte Carlo | 8 min |
| **Total Parte 1** | **25 min** |

---

## SLIDE 1 — Título: "Multiscale Integration" *(~1 min)*

*[Esperar a que el público se acomode. Hablar con calma.]*

Buenos días a todos. Gracias al Instituto Salerno por la invitación.

El título de esta charla es "Multiscale Integration — Rational Design of Functional Materials". Pero podría haber un subtítulo más honesto: **¿cómo diseñamos materiales que todavía no existen, sin fabricar miles de prototipos?**

Esa es la pregunta que ha guiado veinte años de mi trabajo. Y hoy quiero mostrarles cómo se responde usando una jerarquía de métodos computacionales que van desde los electrones hasta los dispositivos.

---

## SLIDE 2 — The Fundamental Question *(~1.5 min)*

Antes de entrar en métodos, tenemos que coincidir en la pregunta.

¿Cómo diseñamos materiales que separen, capturen o transporten moléculas con precisión y eficiencia?

Esta pregunta aparece en tres contextos muy distintos en mi trabajo:
- **Adsorción de gases**: captura de CO₂, separación de mezclas industriales
- **Hidrogeles responsivos**: secuestro de herbicidas, liberación controlada de fármacos
- **Iontrónica**: nanoporos que rectifican corriente iónica como si fueran transistores moleculares

El denominador común es siempre el mismo: necesitamos predecir cómo se comporta la materia a escala nanométrica antes de ir al laboratorio.

El desafío central —como dice la slide— es que **ningún método único puede responder todas las preguntas relevantes**. La solución requiere una estrategia jerárquica.

---

## SLIDE 3 — The Foundation: Schrödinger Equation *(~1.5 min)*

Todo empieza acá.

*[Señalar la ecuación: Ĥ Ψ = E Ψ]*

La ecuación de Schrödinger contiene, en principio, toda la información física del universo. Si pudiéramos resolverla exactamente para cualquier sistema, no necesitaríamos ningún otro método. Sabríamos exactamente cómo se mueven los electrones, cuáles son las energías de interacción, qué geometría adopta cada molécula.

El problema es brutal: **es computacionalmente intratable para sistemas reales**.

Para un solo átomo de hidrógeno, funciona perfectamente. Para una molécula de glyphosate con 20 átomos, ya requiere aproximaciones. Para un poro de MOF con miles de átomos en contacto con un fluido, es directamente imposible.

Esto no es una limitación tecnológica que se va a resolver con computadoras más rápidas. Es una limitación matemática fundamental: el costo escala exponencialmente con el número de electrones.

Entonces, ¿qué hacemos? Construimos aproximaciones controladas. Cada nivel de la jerarquía sacrifica detalle para ganar escala. Y la clave es saber exactamente qué se pierde en cada aproximación.

---

## SLIDE 4 — The Scale Problem *(~1 min)*

Este gráfico lo dice todo.

*[Señalar el gráfico de costo computacional vs. tamaño del sistema]*

La mecánica cuántica exacta sube exponencialmente. Con 100 átomos ya es intratable. Con 1000, es imposible incluso para las supercomputadoras más grandes del mundo.

DFT —la aproximación que vamos a ver ahora— escala como N³. Eso nos permite llegar a sistemas de cientos a miles de átomos.

Monte Carlo y Dinámica Molecular escalan mucho mejor y nos permiten simular millones de átomos.

PNP —Poisson-Nernst-Planck— trata el sistema como un campo continuo y puede escalar a dispositivos de micrómetros.

La estrategia no es elegir el mejor método. Es usar **cada método para la pregunta correcta**.

---

## SLIDE 5 — The Solution: Hierarchy of Approximations *(~1 min)*

El flujo de información va de abajo hacia arriba.

*[Señalar el diagrama DFT → MC → Mol. Theory → PNP]*

DFT calcula energías de interacción y cargas parciales → esos parámetros alimentan Monte Carlo.

Monte Carlo calcula isotermas de adsorción y perfiles de densidad → esos resultados alimentan la Teoría Molecular.

La Teoría Molecular calcula perfiles de carga en función de pH y salinidad → esos perfiles alimentan PNP.

PNP predice curvas I-V, selectividad iónica, y comportamiento del dispositivo.

Cada nivel es validado experimentalmente de forma independiente. Esto es lo que hace que el ciclo sea científicamente robusto: no es una cadena de suposiciones, es una cadena de predicciones verificables.

---

## SLIDE 6 — Tabla: Methods Hierarchy *(~1 min)*

*[Leer brevemente las columnas sin detenerse demasiado]*

Esta tabla es la hoja de ruta de la charla. Siete niveles, siete ecuaciones, siete aproximaciones, siete preguntas de diseño.

Vamos a recorrer cada uno. Para cada nivel voy a mostrar: la ecuación fundamental, qué físicamente representa, qué aproximamos, y —lo más importante— un caso concreto de diseño de materiales donde ese método fue la clave.

Empecemos.

---

## SLIDE 7 — Sección: Quantum Level / DFT *(~20 seg)*

*[Pausa breve. Cambio de ritmo.]*

Primer nivel: la escala cuántica.

---

## SLIDE 8 — Many-Body Problem *(~2 min)*

La ecuación de Kohn-Sham:

*[Señalar: E₀ ≤ E[n(r)]]*

Los teoremas de Hohenberg-Kohn de 1964 son uno de los resultados más elegantes de la física teórica del siglo XX. Demuestran que toda la información química de un sistema —energías, geometrías, propiedades electrónicas— está contenida en una función de tres variables: la densidad electrónica ρ(r).

Eso reduce el problema de 3N dimensiones —donde N puede ser miles— a solo tres dimensiones de espacio.

¿Qué ganamos? Que podemos calcular geometrías moleculares, frecuencias vibracionales, cargas parciales, afinidades electrónicas, energías de interacción. Todo lo que necesitamos para parametrizar los niveles superiores.

¿Qué perdemos? El funcional de intercambio-correlación exacto no lo conocemos. B3LYP, PBE, M06 son aproximaciones empíricas. Funcionan muy bien para la mayoría de los sistemas, pero hay clases de problemas —correlación fuerte, estados excitados— donde fallan.

*[Señalar el diagrama wavefunction vs. electron density]*

A la izquierda: la función de onda. 3N dimensiones, escala exponencial. A la derecha: la densidad electrónica. 3 dimensiones, escala N³. Esta es la revolución de DFT.

---

## SLIDE 9 — Hohenberg-Kohn Theorems *(~1.5 min)*

*[Señalar el diagrama comparativo wavefunction vs. density]*

¿Qué parámetros concretos salen de DFT y alimentan el siguiente nivel?

Principalmente tres:
- **ε y σ** (parámetros Lennard-Jones): definen cómo interactúan las moléculas a corta distancia
- **Cargas parciales q**: definen las interacciones electrostáticas de largo alcance
- **Geometrías de equilibrio**: posiciones atómicas que minimizan la energía

Estos son los force fields. Sin DFT, usaríamos force fields experimentales —que existen, y son buenos. Con DFT, podemos construirlos desde cero para moléculas que nunca se han sintetizado.

Eso es diseño racional: antes de fabricar el material, sabemos con qué fuerza va a atraer al adsorbato de interés.

---

## SLIDE 10 — PROBLEMA: Atlas #3 — Glyphosate/Solvent *(~1.5 min)*

Primer caso concreto.

**¿Qué solvente maximiza la captura del herbicida glyphosate?**

El glyphosate es uno de los herbicidas más usados en el mundo, y es uno de los contaminantes de agua subterránea más problemáticos en países agrícolas como Argentina. Para diseñar un adsorbente eficiente, necesitamos saber en qué forma química existe la molécula en diferentes entornos.

El problema: el glyphosate tiene múltiples grupos ionizables —amina, fosfonato, carboxilato. Su estado de protonación —y por tanto su carga y su geometría— depende críticamente del solvente.

*[Señalar imagen de la estructura molecular]*

La pregunta de diseño es: ¿en qué forma está el glyphosate en agua, en acetona, en DMSO, en etanol? Porque eso determina qué arquitectura de adsorbente es óptima.

---

## SLIDE 11 — SOLUCIÓN: DFT Reveals the Zwitterionic State *(~1.5 min)*

La respuesta que dio DFT —funcional B3LYP con base 6-311++G(2d,2p) y modelos de solvatación implícita IEFPCM y SMD:

La especie dominante en solventes polares es la **forma zwitteriónica**: el grupo amino está protonado (+) y el fosfonato está deprotonado (-). Carga neta cero, pero con polos de carga muy definidos.

*[Señalar imágenes de los cálculos DFT]*

Esta geometría tiene consecuencias directas de diseño:

**Decisión de diseño**: Los adsorbentes deben tener arquitectura hidrofílica con sitios catiónicos para interactuar con el fosfonato negativo. Los solventes apolares producen una forma neutral diferente con menor afinidad. El diseño del adsorbente debe especificar el solvente de operación.

Esta información no se podía obtener experimentalmente de manera directa —los espectros RMN confirman la predicción, pero no podían dar la geometría tridimensional completa sin el cálculo.

---

## SLIDE 12 — PROBLEMA: Atlas #16 — Tautomerism/Antivirals *(~1 min)*

Segundo caso: el problema del tautomerismo en agentes antivirales.

¿Cómo predecir la reactividad biológica de un fármaco antiviral antes de sintetizarlo?

Los malononitriles insaturados presentan equilibrio tautomérico entre la forma nitrilo y la forma cetenimina. La forma activa —la que induce mutagénesis letal en virus— es la cetenimina.

*[Señalar imagen de la estructura]*

Pero en el laboratorio, ambas formas coexisten y son difíciles de distinguir experimentalmente.

---

## SLIDE 13 — SOLUCIÓN: Structure-Activity Correlation *(~1 min)*

DFT calculó las barreras de activación y las energías relativas de los tautómeros.

La correlación es directa: cuanto más estable es el tautómero cetenimina según DFT, mayor es la eficacia mutagénica observada experimentalmente en ensayos biológicos.

*[Señalar imágenes comparativas]*

**Decisión de diseño**: Los candidatos a fármaco antiviral pueden pre-filtrarse usando el cálculo de la barrera tautomérica. Solo los compuestos donde la cetenimina es termodinámicamente accesible merecen ser sintetizados. Reducción dramática del espacio de búsqueda experimental.

---

## SLIDE 14 — PROBLEMA: Atlas #17 — GOF Linkers *(~1 min)*

Tercer caso en el nivel cuántico.

¿Debemos diseñar linkers rígidos o flexibles en marcos orgánicos de grafeno (GOFs)?

Los GOFs son materiales porosos donde láminas de grafeno están conectadas por moléculas orgánicas —linkers— formando una red tridimensional. Son candidatos prometedores para almacenamiento de gas.

El debate: linkers rígidos dan poros bien definidos. Linkers flexibles podrían colapsar bajo presión. ¿Cuál es mejor?

*[Señalar imagen de la estructura GOF]*

---

## SLIDE 15 — SOLUCIÓN: Covalent Angled Model CA-GOF *(~1.5 min)*

La combinación DFT + difracción de neutrones resolvió el debate.

Los linkers DBA son flexibles, pero **no colapsan**. Rotan. Esta rotación tiene una energía de deformación pequeña comparada con la energía de adsorción, y permite que el material se **expanda monotónicamente** al adsorber gas.

El modelo CA-GOF —Covalent Angled GOF— describe exactamente este comportamiento y coincide cuantitativamente con los datos de difracción de neutrones.

*[Señalar imágenes MD/DFT]*

**Decisión de diseño**: No diseñar estructuras rígidas. La flexibilidad conformacional es el mecanismo clave del hinchamiento adaptativo. Los modelos de poros rígidos subestimarán sistemáticamente la capacidad real del material.

Este resultado cambió el paradigma de diseño en GOFs.

---

## SLIDE 16 — Limitation of Quantum Level *(~30 seg)*

DFT describe moléculas aisladas o pares moleculares en vacío.

Un reactor contiene del orden de 10²³ moléculas interactuando simultáneamente. Necesitamos promediar sobre el espacio de configuraciones.

Entra la termodinámica estadística.

---

## SLIDE 17 — Sección: Statistical Thermodynamics *(~20 seg)*

El puente entre lo microscópico y lo macroscópico.

---

## SLIDE 18 — Partition Function *(~2 min)*

*[Señalar: F = -k_B T ln Z]*

La función de partición Z es, en mi opinión, uno de los resultados más profundos de la física.

Z suma sobre todos los estados accesibles del sistema, ponderados por su factor de Boltzmann e^{-βE}. De Z derivan **todas** las cantidades termodinámicas: energía libre, entropía, presión, calor específico.

*[Señalar el gráfico del paisaje energético]*

Miren este diagrama. Tenemos un paisaje energético con mínimos a diferentes profundidades. El estado i=2 es el más estable —tiene el peso de Boltzmann más grande. Pero i=1 e i=3 también contribuyen, con pesos menores.

La función de partición es literalmente la suma de todos esos pesos. Y de esa suma emerge toda la termodinámica.

Lo que esto significa en práctica: para calcular cuántas moléculas de gas se adsorben en un poro a una presión dada y temperatura dada, no necesitamos resolver ecuaciones diferenciales. Necesitamos **muestrear el espacio de configuraciones** con la distribución de Boltzmann correcta.

Eso es exactamente lo que hace Monte Carlo.

---

## SLIDE 19 — Physical Intuition: Energies to Probabilities *(~1 min)*

*[Señalar el diagrama configuraciones → ensemble → isotherm]*

La isóterma de adsorción —la cantidad de moléculas adsorbidas como función de la presión— es un promedio de ensemble. Es el promedio del número de moléculas N sobre 10⁸ configuraciones del sistema.

El vínculo con DFT: las energías de interacción calculadas por DFT determinan los pesos e^{-βE}. Si DFT subestima la energía de interacción, Monte Carlo subestimará la adsorción. La calidad del muestreo estadístico depende de la calidad de los parámetros cuánticos.

La jerarquía no es opcional. Es estructural.

---

## SLIDE 20 — Sección: Monte Carlo / Adsorption *(~20 seg)*

Tercer nivel: Monte Carlo en el ensemble Gran Canónico.

---

## SLIDE 21 — Grand Canonical Ensemble *(~2 min)*

*[Señalar la ecuación de aceptación]*

En el ensemble Grand Canónico —μVT— el potencial químico μ, el volumen V y la temperatura T están fijos. El número de moléculas N fluctúa.

Esto replica exactamente lo que pasa en un experimento de adsorción: el poro está en contacto con un reservorio de gas a presión fija. Las moléculas entran y salen hasta alcanzar el equilibrio.

*[Señalar el diagrama reservoir-pore-output]*

El algoritmo tiene tres tipos de movimiento:
1. **Inserción**: intentamos colocar una molécula en una posición aleatoria. Se acepta si ΔU es favorable, con probabilidad dada por la ecuación que ven en pantalla.
2. **Eliminación**: intentamos remover una molécula aleatoria.
3. **Desplazamiento**: movemos una molécula a una nueva posición.

Cada movimiento satisface el balance detallado —condición necesaria para que la cadena de Markov converja a la distribución Grand Canónica correcta.

El resultado directo: la isóterma de adsorción ⟨N⟩ como función de la presión P.

---

## SLIDE 22 — Stochastic Sampling *(~1.5 min)*

*[Señalar el diagrama MC vs. MD]*

Comparemos Monte Carlo con Dinámica Molecular visualmente.

MC: puntos dispersos conectados por líneas discontinuas. No hay trayectoria física. Los movimientos son no-secuenciales. Pero el conjunto de puntos visitados, con la frecuencia correcta, reproduce la distribución estadística del sistema.

MD: trayectoria continua. Hay tiempo físico. Cada punto evoluciona desde el anterior según las ecuaciones de Newton.

**MC gana en**: isotermas, selectividad binaria, distribución espacial de moléculas en el poro. No requiere resolver ecuaciones diferenciales.

**MC pierde en**: coeficientes de difusión, espectros vibracionales, cualquier propiedad dependiente del tiempo. No hay dinámica real.

Los parámetros de entrada —los force fields— vienen directamente de DFT.

---

## SLIDE 23 — PROBLEMA: Atlas #1 — IAST Validation *(~1 min)*

Primera pregunta de diseño en Monte Carlo.

**¿Es confiable el diseño binario sobre carbón activado usando solo isotermas puras?**

La Teoría de Solución Adsorbida Ideal —IAST— permite predecir el equilibrio de mezclas binarias a partir de las isotermas de los componentes puros. Es mucho más barata computacionalmente que simular la mezcla directamente.

Pero su nombre lo dice: asume ideal. ¿Cuándo falla?

*[Señalar imagen del carbón activado]*

---

## SLIDE 24 — SOLUCIÓN: Ar/CH₄ Validation on Carbon *(~1 min)*

Comparamos IAST vs. GCMC explícito para mezclas Ar/CH₄ sobre grafito exfoliante.

*[Señalar imágenes de isotermas comparativas]*

En superficies relativamente homogéneas como el grafito exfoliado, IAST reproduce los resultados de GCMC con desviaciones por debajo del 5% en el rango industrialmente relevante.

**Decisión de diseño**: Para ciclos de separación industrial —PSA, VSA— se puede usar IAST para screening rápido cuando se conocen las isotermas puras. Reservar GCMC explícito para validación o cuando se sospecha no-idealidad —por ejemplo, en superficies fuertemente heterogéneas o con grupos funcionales polares.

Este es el "cero analítico" del laboratorio: el caso más simple posible, que establece la validez del marco teórico antes de aplicarlo a sistemas más complejos.

---

## SLIDE 25 — PROBLEMA: Atlas #10 — Activated Carbon *(~1 min)*

**¿Cómo afecta la heterogeneidad superficial los límites de capacidad en carbones activados?**

Los carbones activados son los adsorbentes más usados industrialmente. Pero son amorfos, con distribuciones de energía de sitios muy anchas. Los modelos de superficie homogénea —grafito puro— no reproducen su comportamiento.

¿Qué papel juegan los grupos funcionales oxigenados —carboxilos, furanos, lactonas— que quedan del proceso de activación?

*[Señalar imagen del modelo de clúster C-360]*

---

## SLIDE 26 — SOLUCIÓN: Oxygen Nucleation Sites *(~1.5 min)*

Usamos modelos de clústeres poliaromáticos C-360 con funcionalización controlada.

Los grupos carboxilo actúan como **núcleos de condensación** para especies polares como el agua y el metanol. Capturan moléculas a presiones mucho menores que las predichas para carbono puro.

*[Señalar imágenes de los resultados GCMC]*

El modelo de "imperfecciones aleatorias" en la superficie de clústeres reproduce fielmente las isotermas y los calores isostéricos de carbones activados reales.

**Decisión de diseño**: Funcionalizar el carbón activado con grupos oxigenados para maximizar la afinidad por especies polares. El grado de funcionalización debe calibrarse según la aplicación. Para gases apolares como N₂ o Ar, la funcionalización reduce la capacidad —el sitio oxigenado ocupa espacio sin aportar afinidad.

---

## SLIDE 27 — PROBLEMA: Atlas #21 — CO₂ on C72 *(~1 min)*

**¿Los materiales cristalinos bien definidos son superiores a los carbones activados amorfos para captura de CO₂?**

La captura de CO₂ post-combustión es uno de los problemas de materiales más urgentes del siglo XXI. Los carbones activados tienen alta capacidad pero son difíciles de regenerar —los calores de adsorción son demasiado altos y heterogéneos.

Los nuevos nanocarbonos cristalinos —nanoconos, macrociclos C72, rylene propellers— ofrecen sitios de adsorción geométricamente uniformes.

*[Señalar imagen de la estructura C72]*

¿Vale la pena la complejidad sintética?

---

## SLIDE 28 — SOLUCIÓN: Superiority of C72 Twisted *(~1.5 min)*

GCMC en geometrías cristalinas bien definidas mostró que el macrociclo **C72 Twisted** maximiza el volumen de microporos y ofrece calores de adsorción por debajo de 20 kJ/mol.

*[Señalar imágenes de isotermas y energías]*

¿Por qué importa el umbral de 20 kJ/mol? Porque determina la temperatura de regeneración. Por encima de 30-40 kJ/mol, necesitas calentar mucho para desorber el CO₂ —el costo energético del ciclo sube dramáticamente.

**Decisión de diseño**: Priorizar materiales cristalinos bien definidos para aplicaciones de captura a baja presión donde la selectividad inicial es crítica. Los carbones amorfos son preferibles para alta capacidad a presiones elevadas donde la uniformidad del sitio importa menos.

---

## SLIDE 29 — PROBLEMA: Atlas #22 — Pentane Isomers *(~1 min)*

**¿Qué funcionalización del MOF UiO-66 optimiza el número de octano en combustibles?**

La separación de isómeros de pentano —n-pentano, isopentano, neopentano— es crítica en la industria petroquímica. El neopentano tiene número de octano significativamente mayor y es el producto de mayor valor.

Los MOFs —Metal-Organic Frameworks— con geometría de poro controlada son candidatos naturales para esta separación. Pero ¿cuál funcionalización del linker es óptima?

*[Señalar imagen de la estructura UiO-66]*

---

## SLIDE 30 — SOLUCIÓN: UiO-66-NH₂ Shape and Polarity *(~1.5 min)*

GCMC + análisis de selectividad sobre variantes funcionales de UiO-66 mostró:

El grupo amino en UiO-66-NH₂ discrimina isómeros de pentano mediante una combinación de **impedimento estérico** e **interacciones polares preferenciales** con el isómero más ramificado —neopentano.

*[Señalar imágenes de isotermas por isómero]*

La selectividad del UiO-66-NH₂ es significativamente superior al UiO-66 nativo y a las variantes con otros grupos funcionales.

**Decisión de diseño**: El MOF con amino es el material óptimo para esta separación. Las variantes sin funcionalización amino —incluyendo UiO-66 nativo— son significativamente menos eficientes para este par de isómeros. La razón es tanto geométrica como electrostática: el amino "firma" la selectividad por forma.

---

*[FIN PARTE 1 — ~25 MINUTOS]*
