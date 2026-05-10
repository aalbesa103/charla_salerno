# GUION CHARLA SALERNO â€” 50 MINUTOS
# Alberto Albesa Â· INIFTA-CONICET-UNLP
# Parte 1: IntroducciÃ³n â†’ Monte Carlo (~25 min)

---

## â± DISTRIBUCIÃ“N DE TIEMPOS

| SecciÃ³n | Tiempo |
|---------|--------|
| IntroducciÃ³n + Tabla | 6 min |
| Nivel CuÃ¡ntico (DFT) | 8 min |
| Puente EstadÃ­stico | 3 min |
| Monte Carlo | 8 min |
| **Total Parte 1** | **25 min** |

---

## SLIDE 1 â€” TÃ­tulo: "Multiscale Integration" *(~1 min)*

*[Esperar a que el pÃºblico se acomode. Hablar con calma.]*

Buenos dÃ­as a todos. Gracias al Instituto Salerno por la invitaciÃ³n.

El tÃ­tulo de esta charla es "Multiscale Integration â€” Rational Design of Functional Materials". Pero podrÃ­a haber un subtÃ­tulo mÃ¡s honesto: **Â¿cÃ³mo diseÃ±amos materiales que todavÃ­a no existen, sin fabricar miles de prototipos?**

Esa es la pregunta que ha guiado veinte aÃ±os de mi trabajo. Y hoy quiero mostrarles cÃ³mo se responde usando una jerarquÃ­a de mÃ©todos computacionales que van desde los electrones hasta los dispositivos.

---

## SLIDE 2 â€” The Fundamental Question *(~1.5 min)*

Antes de entrar en mÃ©todos, tenemos que coincidir en la pregunta.

Â¿CÃ³mo diseÃ±amos materiales que separen, capturen o transporten molÃ©culas con precisiÃ³n y eficiencia?

Esta pregunta aparece en tres contextos muy distintos en mi trabajo:
- **AdsorciÃ³n de gases**: captura de COâ‚‚, separaciÃ³n de mezclas industriales
- **Hidrogeles responsivos**: secuestro de herbicidas, liberaciÃ³n controlada de fÃ¡rmacos
- **IontrÃ³nica**: nanoporos que rectifican corriente iÃ³nica como si fueran transistores moleculares

El denominador comÃºn es siempre el mismo: necesitamos predecir cÃ³mo se comporta la materia a escala nanomÃ©trica antes de ir al laboratorio.

El desafÃ­o central â€”como dice la slideâ€” es que **ningÃºn mÃ©todo Ãºnico puede responder todas las preguntas relevantes**. La soluciÃ³n requiere una estrategia jerÃ¡rquica.

---

## SLIDE 3 â€” The Foundation: SchrÃ¶dinger Equation *(~1.5 min)*

Todo empieza acÃ¡.

*[SeÃ±alar la ecuaciÃ³n: Ä¤ Î¨ = E Î¨]*

La ecuaciÃ³n de SchrÃ¶dinger contiene, en principio, toda la informaciÃ³n fÃ­sica del universo. Si pudiÃ©ramos resolverla exactamente para cualquier sistema, no necesitarÃ­amos ningÃºn otro mÃ©todo. SabrÃ­amos exactamente cÃ³mo se mueven los electrones, cuÃ¡les son las energÃ­as de interacciÃ³n, quÃ© geometrÃ­a adopta cada molÃ©cula.

El problema es brutal: **es computacionalmente intratable para sistemas reales**.

Para un solo Ã¡tomo de hidrÃ³geno, funciona perfectamente. Para una molÃ©cula de glyphosate con 20 Ã¡tomos, ya requiere aproximaciones. Para un poro de MOF con miles de Ã¡tomos en contacto con un fluido, es directamente imposible.

Esto no es una limitaciÃ³n tecnolÃ³gica que se va a resolver con computadoras mÃ¡s rÃ¡pidas. Es una limitaciÃ³n matemÃ¡tica fundamental: el costo escala exponencialmente con el nÃºmero de electrones.

Entonces, Â¿quÃ© hacemos? Construimos aproximaciones controladas. Cada nivel de la jerarquÃ­a sacrifica detalle para ganar escala. Y la clave es saber exactamente quÃ© se pierde en cada aproximaciÃ³n.

---

## SLIDE 4 â€” The Scale Problem *(~1 min)*

Este grÃ¡fico lo dice todo.

*[SeÃ±alar el grÃ¡fico de costo computacional vs. tamaÃ±o del sistema]*

La mecÃ¡nica cuÃ¡ntica exacta sube exponencialmente. Con 100 Ã¡tomos ya es intratable. Con 1000, es imposible incluso para las supercomputadoras mÃ¡s grandes del mundo.

DFT â€”la aproximaciÃ³n que vamos a ver ahoraâ€” escala como NÂ³. Eso nos permite llegar a sistemas de cientos a miles de Ã¡tomos.

Monte Carlo y DinÃ¡mica Molecular escalan mucho mejor y nos permiten simular millones de Ã¡tomos.

PNP â€”Poisson-Nernst-Planckâ€” trata el sistema como un campo continuo y puede escalar a dispositivos de micrÃ³metros.

La estrategia no es elegir el mejor mÃ©todo. Es usar **cada mÃ©todo para la pregunta correcta**.

---

## SLIDE 5 â€” The Solution: Hierarchy of Approximations *(~1 min)*

El flujo de informaciÃ³n va de abajo hacia arriba.

*[SeÃ±alar el diagrama DFT â†’ MC â†’ Mol. Theory â†’ PNP]*

DFT calcula energÃ­as de interacciÃ³n y cargas parciales â†’ esos parÃ¡metros alimentan Monte Carlo.

Monte Carlo calcula isotermas de adsorciÃ³n y perfiles de densidad â†’ esos resultados alimentan la TeorÃ­a Molecular.

La TeorÃ­a Molecular calcula perfiles de carga en funciÃ³n de pH y salinidad â†’ esos perfiles alimentan PNP.

PNP predice curvas I-V, selectividad iÃ³nica, y comportamiento del dispositivo.

Cada nivel es validado experimentalmente de forma independiente. Esto es lo que hace que el ciclo sea cientÃ­ficamente robusto: no es una cadena de suposiciones, es una cadena de predicciones verificables.

---

## SLIDE 6 â€” Tabla: Methods Hierarchy *(~1 min)*

*[Leer brevemente las columnas sin detenerse demasiado]*

Esta tabla es la hoja de ruta de la charla. Siete niveles, siete ecuaciones, siete aproximaciones, siete preguntas de diseÃ±o.

Vamos a recorrer cada uno. Para cada nivel voy a mostrar: la ecuaciÃ³n fundamental, quÃ© fÃ­sicamente representa, quÃ© aproximamos, y â€”lo mÃ¡s importanteâ€” un caso concreto de diseÃ±o de materiales donde ese mÃ©todo fue la clave.

Empecemos.

---

## SLIDE 7 â€” SecciÃ³n: Quantum Level / DFT *(~20 seg)*

*[Pausa breve. Cambio de ritmo.]*

Primer nivel: la escala cuÃ¡ntica.

---

## SLIDE 8 â€” Many-Body Problem *(~2 min)*

La ecuaciÃ³n de Kohn-Sham:

*[SeÃ±alar: Eâ‚€ â‰¤ E[n(r)]]*

Los teoremas de Hohenberg-Kohn de 1964 son uno de los resultados mÃ¡s elegantes de la fÃ­sica teÃ³rica del siglo XX. Demuestran que toda la informaciÃ³n quÃ­mica de un sistema â€”energÃ­as, geometrÃ­as, propiedades electrÃ³nicasâ€” estÃ¡ contenida en una funciÃ³n de tres variables: la densidad electrÃ³nica Ï(r).

Eso reduce el problema de 3N dimensiones â€”donde N puede ser milesâ€” a solo tres dimensiones de espacio.

Â¿QuÃ© ganamos? Que podemos calcular geometrÃ­as moleculares, frecuencias vibracionales, cargas parciales, afinidades electrÃ³nicas, energÃ­as de interacciÃ³n. Todo lo que necesitamos para parametrizar los niveles superiores.

Â¿QuÃ© perdemos? El funcional de intercambio-correlaciÃ³n exacto no lo conocemos. B3LYP, PBE, M06 son aproximaciones empÃ­ricas. Funcionan muy bien para la mayorÃ­a de los sistemas, pero hay clases de problemas â€”correlaciÃ³n fuerte, estados excitadosâ€” donde fallan.

*[SeÃ±alar el diagrama wavefunction vs. electron density]*

A la izquierda: la funciÃ³n de onda. 3N dimensiones, escala exponencial. A la derecha: la densidad electrÃ³nica. 3 dimensiones, escala NÂ³. Esta es la revoluciÃ³n de DFT.

---

## SLIDE 9 â€” Hohenberg-Kohn Theorems *(~1.5 min)*

*[SeÃ±alar el diagrama comparativo wavefunction vs. density]*

Â¿QuÃ© parÃ¡metros concretos salen de DFT y alimentan el siguiente nivel?

Principalmente tres:
- **Îµ y Ïƒ** (parÃ¡metros Lennard-Jones): definen cÃ³mo interactÃºan las molÃ©culas a corta distancia
- **Cargas parciales q**: definen las interacciones electrostÃ¡ticas de largo alcance
- **GeometrÃ­as de equilibrio**: posiciones atÃ³micas que minimizan la energÃ­a

Estos son los force fields. Sin DFT, usarÃ­amos force fields experimentales â€”que existen, y son buenos. Con DFT, podemos construirlos desde cero para molÃ©culas que nunca se han sintetizado.

Eso es diseÃ±o racional: antes de fabricar el material, sabemos con quÃ© fuerza va a atraer al adsorbato de interÃ©s.

---

## SLIDE 10 â€” PROBLEMA: Atlas #3 â€” Glyphosate/Solvent *(~1.5 min)*

Primer caso concreto.

**Â¿QuÃ© solvente maximiza la captura del herbicida glyphosate?**

El glyphosate es uno de los herbicidas mÃ¡s usados en el mundo, y es uno de los contaminantes de agua subterrÃ¡nea mÃ¡s problemÃ¡ticos en paÃ­ses agrÃ­colas como Argentina. Para diseÃ±ar un adsorbente eficiente, necesitamos saber en quÃ© forma quÃ­mica existe la molÃ©cula en diferentes entornos.

El problema: el glyphosate tiene mÃºltiples grupos ionizables â€”amina, fosfonato, carboxilato. Su estado de protonaciÃ³n â€”y por tanto su carga y su geometrÃ­aâ€” depende crÃ­ticamente del solvente.

*[SeÃ±alar imagen de la estructura molecular]*

La pregunta de diseÃ±o es: Â¿en quÃ© forma estÃ¡ el glyphosate en agua, en acetona, en DMSO, en etanol? Porque eso determina quÃ© arquitectura de adsorbente es Ã³ptima.

---

## SLIDE 11 â€” SOLUCIÃ“N: DFT Reveals the Zwitterionic State *(~1.5 min)*

La respuesta que dio DFT â€”funcional B3LYP con base 6-311++G(2d,2p) y modelos de solvataciÃ³n implÃ­cita IEFPCM y SMD:

La especie dominante en solventes polares es la **forma zwitteriÃ³nica**: el grupo amino estÃ¡ protonado (+) y el fosfonato estÃ¡ deprotonado (-). Carga neta cero, pero con polos de carga muy definidos.

*[SeÃ±alar imÃ¡genes de los cÃ¡lculos DFT]*

Esta geometrÃ­a tiene consecuencias directas de diseÃ±o:

**DecisiÃ³n de diseÃ±o**: Los adsorbentes deben tener arquitectura hidrofÃ­lica con sitios catiÃ³nicos para interactuar con el fosfonato negativo. Los solventes apolares producen una forma neutral diferente con menor afinidad. El diseÃ±o del adsorbente debe especificar el solvente de operaciÃ³n.

Esta informaciÃ³n no se podÃ­a obtener experimentalmente de manera directa â€”los espectros RMN confirman la predicciÃ³n, pero no podÃ­an dar la geometrÃ­a tridimensional completa sin el cÃ¡lculo.

---

## SLIDE 12 â€” PROBLEMA: Atlas #16 â€” Tautomerism/Antivirals *(~1 min)*

Segundo caso: el problema del tautomerismo en agentes antivirales.

Â¿CÃ³mo predecir la reactividad biolÃ³gica de un fÃ¡rmaco antiviral antes de sintetizarlo?

Los malononitriles insaturados presentan equilibrio tautomÃ©rico entre la forma nitrilo y la forma cetenimina. La forma activa â€”la que induce mutagÃ©nesis letal en virusâ€” es la cetenimina.

*[SeÃ±alar imagen de la estructura]*

Pero en el laboratorio, ambas formas coexisten y son difÃ­ciles de distinguir experimentalmente.

---

## SLIDE 13 â€” SOLUCIÃ“N: Structure-Activity Correlation *(~1 min)*

DFT calculÃ³ las barreras de activaciÃ³n y las energÃ­as relativas de los tautÃ³meros.

La correlaciÃ³n es directa: cuanto mÃ¡s estable es el tautÃ³mero cetenimina segÃºn DFT, mayor es la eficacia mutagÃ©nica observada experimentalmente en ensayos biolÃ³gicos.

*[SeÃ±alar imÃ¡genes comparativas]*

**DecisiÃ³n de diseÃ±o**: Los candidatos a fÃ¡rmaco antiviral pueden pre-filtrarse usando el cÃ¡lculo de la barrera tautomÃ©rica. Solo los compuestos donde la cetenimina es termodinÃ¡micamente accesible merecen ser sintetizados. ReducciÃ³n dramÃ¡tica del espacio de bÃºsqueda experimental.

---

## SLIDE 14 â€” PROBLEMA: Atlas #17 â€” GOF Linkers *(~1 min)*

Tercer caso en el nivel cuÃ¡ntico.

Â¿Debemos diseÃ±ar linkers rÃ­gidos o flexibles en marcos orgÃ¡nicos de grafeno (GOFs)?

Los GOFs son materiales porosos donde lÃ¡minas de grafeno estÃ¡n conectadas por molÃ©culas orgÃ¡nicas â€”linkersâ€” formando una red tridimensional. Son candidatos prometedores para almacenamiento de gas.

El debate: linkers rÃ­gidos dan poros bien definidos. Linkers flexibles podrÃ­an colapsar bajo presiÃ³n. Â¿CuÃ¡l es mejor?

*[SeÃ±alar imagen de la estructura GOF]*

---

## SLIDE 15 â€” SOLUCIÃ“N: Covalent Angled Model CA-GOF *(~1.5 min)*

La combinaciÃ³n DFT + difracciÃ³n de neutrones resolviÃ³ el debate.

Los linkers DBA son flexibles, pero **no colapsan**. Rotan. Esta rotaciÃ³n tiene una energÃ­a de deformaciÃ³n pequeÃ±a comparada con la energÃ­a de adsorciÃ³n, y permite que el material se **expanda monotÃ³nicamente** al adsorber gas.

El modelo CA-GOF â€”Covalent Angled GOFâ€” describe exactamente este comportamiento y coincide cuantitativamente con los datos de difracciÃ³n de neutrones.

*[SeÃ±alar imÃ¡genes MD/DFT]*

**DecisiÃ³n de diseÃ±o**: No diseÃ±ar estructuras rÃ­gidas. La flexibilidad conformacional es el mecanismo clave del hinchamiento adaptativo. Los modelos de poros rÃ­gidos subestimarÃ¡n sistemÃ¡ticamente la capacidad real del material.

Este resultado cambiÃ³ el paradigma de diseÃ±o en GOFs.

---

## SLIDE 16 â€” Limitation of Quantum Level *(~30 seg)*

DFT describe molÃ©culas aisladas o pares moleculares en vacÃ­o.

Un reactor contiene del orden de 10Â²Â³ molÃ©culas interactuando simultÃ¡neamente. Necesitamos promediar sobre el espacio de configuraciones.

Entra la termodinÃ¡mica estadÃ­stica.

---

## SLIDE 17 â€” SecciÃ³n: Statistical Thermodynamics *(~20 seg)*

El puente entre lo microscÃ³pico y lo macroscÃ³pico.

---

## SLIDE 18 â€” Partition Function *(~2 min)*

*[SeÃ±alar: F = -k_B T ln Z]*

La funciÃ³n de particiÃ³n Z es, en mi opiniÃ³n, uno de los resultados mÃ¡s profundos de la fÃ­sica.

Z suma sobre todos los estados accesibles del sistema, ponderados por su factor de Boltzmann e^{-Î²E}. De Z derivan **todas** las cantidades termodinÃ¡micas: energÃ­a libre, entropÃ­a, presiÃ³n, calor especÃ­fico.

*[SeÃ±alar el grÃ¡fico del paisaje energÃ©tico]*

Miren este diagrama. Tenemos un paisaje energÃ©tico con mÃ­nimos a diferentes profundidades. El estado i=2 es el mÃ¡s estable â€”tiene el peso de Boltzmann mÃ¡s grande. Pero i=1 e i=3 tambiÃ©n contribuyen, con pesos menores.

La funciÃ³n de particiÃ³n es literalmente la suma de todos esos pesos. Y de esa suma emerge toda la termodinÃ¡mica.

Lo que esto significa en prÃ¡ctica: para calcular cuÃ¡ntas molÃ©culas de gas se adsorben en un poro a una presiÃ³n dada y temperatura dada, no necesitamos resolver ecuaciones diferenciales. Necesitamos **muestrear el espacio de configuraciones** con la distribuciÃ³n de Boltzmann correcta.

Eso es exactamente lo que hace Monte Carlo.

---

## SLIDE 19 â€” Physical Intuition: Energies to Probabilities *(~1 min)*

*[SeÃ±alar el diagrama configuraciones â†’ ensemble â†’ isotherm]*

La isÃ³terma de adsorciÃ³n â€”la cantidad de molÃ©culas adsorbidas como funciÃ³n de la presiÃ³nâ€” es un promedio de ensemble. Es el promedio del nÃºmero de molÃ©culas N sobre 10â¸ configuraciones del sistema.

El vÃ­nculo con DFT: las energÃ­as de interacciÃ³n calculadas por DFT determinan los pesos e^{-Î²E}. Si DFT subestima la energÃ­a de interacciÃ³n, Monte Carlo subestimarÃ¡ la adsorciÃ³n. La calidad del muestreo estadÃ­stico depende de la calidad de los parÃ¡metros cuÃ¡nticos.

La jerarquÃ­a no es opcional. Es estructural.

---

## SLIDE 20 â€” SecciÃ³n: Monte Carlo / Adsorption *(~20 seg)*

Tercer nivel: Monte Carlo en el ensemble Gran CanÃ³nico.

---

## SLIDE 21 â€” Grand Canonical Ensemble *(~2 min)*

*[SeÃ±alar la ecuaciÃ³n de aceptaciÃ³n]*

En el ensemble Grand CanÃ³nico â€”Î¼VTâ€” el potencial quÃ­mico Î¼, el volumen V y la temperatura T estÃ¡n fijos. El nÃºmero de molÃ©culas N fluctÃºa.

Esto replica exactamente lo que pasa en un experimento de adsorciÃ³n: el poro estÃ¡ en contacto con un reservorio de gas a presiÃ³n fija. Las molÃ©culas entran y salen hasta alcanzar el equilibrio.

*[SeÃ±alar el diagrama reservoir-pore-output]*

El algoritmo tiene tres tipos de movimiento:
1. **InserciÃ³n**: intentamos colocar una molÃ©cula en una posiciÃ³n aleatoria. Se acepta si Î”U es favorable, con probabilidad dada por la ecuaciÃ³n que ven en pantalla.
2. **EliminaciÃ³n**: intentamos remover una molÃ©cula aleatoria.
3. **Desplazamiento**: movemos una molÃ©cula a una nueva posiciÃ³n.

Cada movimiento satisface el balance detallado â€”condiciÃ³n necesaria para que la cadena de Markov converja a la distribuciÃ³n Grand CanÃ³nica correcta.

El resultado directo: la isÃ³terma de adsorciÃ³n âŸ¨NâŸ© como funciÃ³n de la presiÃ³n P.

---

## SLIDE 22 â€” Stochastic Sampling *(~1.5 min)*

*[SeÃ±alar el diagrama MC vs. MD]*

Comparemos Monte Carlo con DinÃ¡mica Molecular visualmente.

MC: puntos dispersos conectados por lÃ­neas discontinuas. No hay trayectoria fÃ­sica. Los movimientos son no-secuenciales. Pero el conjunto de puntos visitados, con la frecuencia correcta, reproduce la distribuciÃ³n estadÃ­stica del sistema.

MD: trayectoria continua. Hay tiempo fÃ­sico. Cada punto evoluciona desde el anterior segÃºn las ecuaciones de Newton.

**MC gana en**: isotermas, selectividad binaria, distribuciÃ³n espacial de molÃ©culas en el poro. No requiere resolver ecuaciones diferenciales.

**MC pierde en**: coeficientes de difusiÃ³n, espectros vibracionales, cualquier propiedad dependiente del tiempo. No hay dinÃ¡mica real.

Los parÃ¡metros de entrada â€”los force fieldsâ€” vienen directamente de DFT.

---

## SLIDE 23 â€” PROBLEMA: Atlas #1 â€” IAST Validation *(~1 min)*

Primera pregunta de diseÃ±o en Monte Carlo.

**Â¿Es confiable el diseÃ±o binario sobre carbÃ³n activado usando solo isotermas puras?**

La TeorÃ­a de SoluciÃ³n Adsorbida Ideal â€”IASTâ€” permite predecir el equilibrio de mezclas binarias a partir de las isotermas de los componentes puros. Es mucho mÃ¡s barata computacionalmente que simular la mezcla directamente.

Pero su nombre lo dice: asume ideal. Â¿CuÃ¡ndo falla?

*[SeÃ±alar imagen del carbÃ³n activado]*

---

## SLIDE 24 â€” SOLUCIÃ“N: Ar/CHâ‚„ Validation on Carbon *(~1 min)*

Comparamos IAST vs. GCMC explÃ­cito para mezclas Ar/CHâ‚„ sobre grafito exfoliante.

*[SeÃ±alar imÃ¡genes de isotermas comparativas]*

En superficies relativamente homogÃ©neas como el grafito exfoliado, IAST reproduce los resultados de GCMC con desviaciones por debajo del 5% en el rango industrialmente relevante.

**DecisiÃ³n de diseÃ±o**: Para ciclos de separaciÃ³n industrial â€”PSA, VSAâ€” se puede usar IAST para screening rÃ¡pido cuando se conocen las isotermas puras. Reservar GCMC explÃ­cito para validaciÃ³n o cuando se sospecha no-idealidad â€”por ejemplo, en superficies fuertemente heterogÃ©neas o con grupos funcionales polares.

Este es el "cero analÃ­tico" del laboratorio: el caso mÃ¡s simple posible, que establece la validez del marco teÃ³rico antes de aplicarlo a sistemas mÃ¡s complejos.

---

## SLIDE 25 â€” PROBLEMA: Atlas #10 â€” Activated Carbon *(~1 min)*

**Â¿CÃ³mo afecta la heterogeneidad superficial los lÃ­mites de capacidad en carbones activados?**

Los carbones activados son los adsorbentes mÃ¡s usados industrialmente. Pero son amorfos, con distribuciones de energÃ­a de sitios muy anchas. Los modelos de superficie homogÃ©nea â€”grafito puroâ€” no reproducen su comportamiento.

Â¿QuÃ© papel juegan los grupos funcionales oxigenados â€”carboxilos, furanos, lactonasâ€” que quedan del proceso de activaciÃ³n?

*[SeÃ±alar imagen del modelo de clÃºster C-360]*

---

## SLIDE 26 â€” SOLUCIÃ“N: Oxygen Nucleation Sites *(~1.5 min)*

Usamos modelos de clÃºsteres poliaromÃ¡ticos C-360 con funcionalizaciÃ³n controlada.

Los grupos carboxilo actÃºan como **nÃºcleos de condensaciÃ³n** para especies polares como el agua y el metanol. Capturan molÃ©culas a presiones mucho menores que las predichas para carbono puro.

*[SeÃ±alar imÃ¡genes de los resultados GCMC]*

El modelo de "imperfecciones aleatorias" en la superficie de clÃºsteres reproduce fielmente las isotermas y los calores isostÃ©ricos de carbones activados reales.

**DecisiÃ³n de diseÃ±o**: Funcionalizar el carbÃ³n activado con grupos oxigenados para maximizar la afinidad por especies polares. El grado de funcionalizaciÃ³n debe calibrarse segÃºn la aplicaciÃ³n. Para gases apolares como Nâ‚‚ o Ar, la funcionalizaciÃ³n reduce la capacidad â€”el sitio oxigenado ocupa espacio sin aportar afinidad.

---

## SLIDE 27 â€” PROBLEMA: Atlas #21 â€” COâ‚‚ on C72 *(~1 min)*

**Â¿Los materiales cristalinos bien definidos son superiores a los carbones activados amorfos para captura de COâ‚‚?**

La captura de COâ‚‚ post-combustiÃ³n es uno de los problemas de materiales mÃ¡s urgentes del siglo XXI. Los carbones activados tienen alta capacidad pero son difÃ­ciles de regenerar â€”los calores de adsorciÃ³n son demasiado altos y heterogÃ©neos.

Los nuevos nanocarbonos cristalinos â€”nanoconos, macrociclos C72, rylene propellersâ€” ofrecen sitios de adsorciÃ³n geomÃ©tricamente uniformes.

*[SeÃ±alar imagen de la estructura C72]*

Â¿Vale la pena la complejidad sintÃ©tica?

---

## SLIDE 28 â€” SOLUCIÃ“N: Superiority of C72 Twisted *(~1.5 min)*

GCMC en geometrÃ­as cristalinas bien definidas mostrÃ³ que el macrociclo **C72 Twisted** maximiza el volumen de microporos y ofrece calores de adsorciÃ³n por debajo de 20 kJ/mol.

*[SeÃ±alar imÃ¡genes de isotermas y energÃ­as]*

Â¿Por quÃ© importa el umbral de 20 kJ/mol? Porque determina la temperatura de regeneraciÃ³n. Por encima de 30-40 kJ/mol, necesitas calentar mucho para desorber el COâ‚‚ â€”el costo energÃ©tico del ciclo sube dramÃ¡ticamente.

**DecisiÃ³n de diseÃ±o**: Priorizar materiales cristalinos bien definidos para aplicaciones de captura a baja presiÃ³n donde la selectividad inicial es crÃ­tica. Los carbones amorfos son preferibles para alta capacidad a presiones elevadas donde la uniformidad del sitio importa menos.

---

## SLIDE 29 â€” PROBLEMA: Atlas #22 â€” Pentane Isomers *(~1 min)*

**Â¿QuÃ© funcionalizaciÃ³n del MOF UiO-66 optimiza el nÃºmero de octano en combustibles?**

La separaciÃ³n de isÃ³meros de pentano â€”n-pentano, isopentano, neopentanoâ€” es crÃ­tica en la industria petroquÃ­mica. El neopentano tiene nÃºmero de octano significativamente mayor y es el producto de mayor valor.

Los MOFs â€”Metal-Organic Frameworksâ€” con geometrÃ­a de poro controlada son candidatos naturales para esta separaciÃ³n. Pero Â¿cuÃ¡l funcionalizaciÃ³n del linker es Ã³ptima?

*[SeÃ±alar imagen de la estructura UiO-66]*

---

## SLIDE 30 â€” SOLUCIÃ“N: UiO-66-NHâ‚‚ Shape and Polarity *(~1.5 min)*

GCMC + anÃ¡lisis de selectividad sobre variantes funcionales de UiO-66 mostrÃ³:

El grupo amino en UiO-66-NHâ‚‚ discrimina isÃ³meros de pentano mediante una combinaciÃ³n de **impedimento estÃ©rico** e **interacciones polares preferenciales** con el isÃ³mero mÃ¡s ramificado â€”neopentano.

*[SeÃ±alar imÃ¡genes de isotermas por isÃ³mero]*

La selectividad del UiO-66-NHâ‚‚ es significativamente superior al UiO-66 nativo y a las variantes con otros grupos funcionales.

**DecisiÃ³n de diseÃ±o**: El MOF con amino es el material Ã³ptimo para esta separaciÃ³n. Las variantes sin funcionalizaciÃ³n amino â€”incluyendo UiO-66 nativoâ€” son significativamente menos eficientes para este par de isÃ³meros. La razÃ³n es tanto geomÃ©trica como electrostÃ¡tica: el amino "firma" la selectividad por forma.

---

*[FIN PARTE 1 â€” ~25 MINUTOS]*

---

## SLIDE 31 â€” SecciÃ³n: Molecular Dynamics *(~20 seg)*

Cuarto nivel: DinÃ¡mica Molecular. Ahora sÃ­ hay tiempo.

---

## SLIDE 32 â€” Newton's Second Law *(~2 min)*

*[SeÃ±alar: mÂ·dÂ²r/dtÂ² = -âˆ‡V]*

La diferencia fundamental con Monte Carlo: aquÃ­ integramos las ecuaciones de Newton paso a paso. Cada Ã¡tomo siente la fuerza de sus vecinos y se mueve en consecuencia.

El potencial cuÃ¡ntico V(r) es reemplazado por force fields clÃ¡sicos: resortes para enlaces, Ã¡ngulos y torques, mÃ¡s tÃ©rminos Lennard-Jones y Coulomb para interacciones no-enlazantes.

El resultado: trayectorias completas. No solo dÃ³nde estÃ¡n las molÃ©culas, sino cÃ³mo se mueven. Coeficientes de difusiÃ³n, funciones de distribuciÃ³n radial, espectros vibracionales.

El costo: pasos de femtosegundo. Para ver microsegundos, necesitamos 10â¹ pasos. El tiempo de simulaciÃ³n es el cuello de botella.

---

## SLIDE 33 â€” The Temporal Limit *(~1.5 min)*

*[SeÃ±alar el diagrama de escalas de tiempo]*

MD puede ver vibraciÃ³n de enlaces, difusiÃ³n en poros, relajaciÃ³n de polÃ­meros. Todo hasta aproximadamente el microsegundo.

MÃ¡s allÃ¡: plegamiento de proteÃ­nas, transiciones de fase, catÃ¡lisis enzimÃ¡tica. Invisible para MD estÃ¡ndar.

Â¿CuÃ¡ndo pasamos a Coarse-Grain? Cuando la pregunta requiere escalas de micrÃ³metros o milisegundos.

---

## SLIDE 34 â€” PROBLEMA: Atlas #14 â€” Nanogel Antifouling *(~1 min)*

**Â¿CÃ³mo evitar que las proteÃ­nas del plasma sanguÃ­neo se peguen al nanogel cuando se calienta?**

Los nanogeles termorresponsivos de NIPAm colapsan por encima de su temperatura de transiciÃ³n â€”unos 32Â°C. Al colapsar, exponen regiones hidrofÃ³bicas que atraen proteÃ­nas plasmÃ¡ticas.

Si se cubren de proteÃ­nas antes de llegar al tumor, el nanovehÃ­culo es neutralizado por el sistema inmune.

*[SeÃ±alar imagen del nanogel]*

---

## SLIDE 35 â€” SOLUCIÃ“N: Janus Architecture *(~1.5 min)*

MD de copolÃ­meros NIPAm-EG mostrÃ³ que la distribuciÃ³n espacial del co-monÃ³mero EG es crÃ­tica.

Parches bien definidos de EG en la superficie â€”arquitectura Janusâ€” forman una capa hidrofÃ­lica dinÃ¡mica que repele estÃ©ricamente las proteÃ­nas, incluso cuando el nÃºcleo NIPAm estÃ¡ colapsado.

*[SeÃ±alar imÃ¡genes MD]*

DistribuciÃ³n aleatoria de EG: no protege. La hidrofobicidad del NIPAm colapsado domina.

**DecisiÃ³n de diseÃ±o**: Forzar sÃ­ntesis de arquitectura Janus con parches de EG bien definidos. Distribuciones aleatorias de monÃ³meros hidrofÃ­licos no protegen el nÃºcleo del nanovehÃ­culo contra la adsorciÃ³n de proteÃ­nas.

---

## SLIDE 36 â€” PROBLEMA: Atlas #17-MD â€” GOF Swelling *(~1 min)*

El mismo sistema GOF del nivel cuÃ¡ntico, ahora con una pregunta diferente.

**Â¿CÃ³mo se expande dinÃ¡micamente el material bajo presiÃ³n de gas?**

DFT nos dio la estructura de equilibrio y las energÃ­as de deformaciÃ³n del linker. Pero Â¿cÃ³mo evoluciona ese proceso en el tiempo? Â¿Es reversible? Â¿Es isÃ³tropo?

*[SeÃ±alar imagen MD del GOF]*

---

## SLIDE 37 â€” SOLUCIÃ“N: Dynamic Swelling *(~1.5 min)*

Las trayectorias MD muestran el proceso completo: rotaciÃ³n de linkers, expansiÃ³n de la celda unitaria, redistribuciÃ³n de la densidad electrÃ³nica.

La dilataciÃ³n es **anisÃ³tropa y dependiente de la presiÃ³n**. El eje de expansiÃ³n preferente estÃ¡ determinado por la geometrÃ­a de los linkers DBA.

*[SeÃ±alar imÃ¡genes MD]*

**DecisiÃ³n de diseÃ±o**: Incorporar la dilataciÃ³n estructural en el diseÃ±o mecÃ¡nico del dispositivo de contenciÃ³n. Ignorar el hinchamiento lleva a subestimar la capacidad real y a fallo mecÃ¡nico en ciclos de carga/descarga.

---

## SLIDE 38 â€” SecciÃ³n: Coarse-Grain *(~20 seg)*

Quinto nivel. Sacrificamos detalle atÃ³mico para ganar dos o tres Ã³rdenes de magnitud en escala.

---

## SLIDE 39 â€” Integration of Degrees of Freedom *(~2 min)*

*[SeÃ±alar: V_CG(R) â‰ˆ -k_BT ln âˆ« e^{-Î²V} dr]*

La idea es simple: agrupamos N Ã¡tomos en un Ãºnico "bead" CG. La dinÃ¡mica interna del grupo se integra fuera â€” solo queda el potencial efectivo de interacciÃ³n entre beads.

*[SeÃ±alar diagrama Ã¡tomo â†’ bead, mapeo 4:1]*

Con 4 Ã¡tomos por bead, reducimos el nÃºmero de partÃ­culas por un factor 4. Pero la ganancia en tiempo de simulaciÃ³n es mucho mayor â€”porque el paso de tiempo tambiÃ©n puede ser mayor, y el potencial es mÃ¡s suave.

El resultado: acceso a escalas de micrÃ³metros y milisegundos. VesÃ­culas, micelas, redes de polÃ­meros, morfologÃ­a de ensamblado.

El precio: perdemos los sitios activos. No podemos calcular reacciones quÃ­micas ni reconocimiento molecular de alta precisiÃ³n con CG.

---

## SLIDE 40 â€” Gain vs Loss *(~1 min)*

Regla prÃ¡ctica:

**Usar CG para**: morfologÃ­a de auto-ensamblado, transporte bulk en materiales, conformaciones de cadenas polimÃ©ricas largas.

**Evitar CG para**: reconocimiento molecular especÃ­fico, cÃ¡lculos de selectividad en sitios activos, reacciones, interacciones de corto alcance que determinan afinidad.

**Protocolo Ã³ptimo**: CG para identificar configuraciones morfolÃ³gicas relevantes, luego refinamiento con Ã¡tomos explÃ­citos en las regiones de interÃ©s.

---

## SLIDE 41 â€” PROBLEMA: Atlas #15 â€” Alkane CG *(~1 min)*

**Â¿CuÃ¡l es el lÃ­mite del modelado simplificado bajo confinamiento extremo?**

Los alcanos largos en carbones activados son sistemas industrialmente relevantes â€”solventes, combustibles, refinaciÃ³n. La simulaciÃ³n atomÃ­stica es costosa.

Â¿Podemos usar modelos CG 4:1 sin perder precisiÃ³n?

*[SeÃ±alar imagen del modelo carbÃ³n-alcano]*

---

## SLIDE 42 â€” SOLUCIÃ“N: The Coarse-Grain Limit *(~1.5 min)*

El modelo CG reproduce fielmente el comportamiento de alcanos en **mesoporos** â€”poros de 2-50 nm.

Pero falla cuantitativamente en **microconfinamiento** â€”poros menores de 1 nmâ€” donde el detalle atÃ³mico domina el empaquetamiento. La diferencia en isoterma puede superar el 30%.

*[SeÃ±alar imÃ¡genes comparativas]*

**DecisiÃ³n de diseÃ±o**: Usar CG para modelado de transporte bulk y adsorciÃ³n en mesoporos. Cambiar a representaciÃ³n Ã¡tomo explÃ­cito cuando el poro es comparable al tamaÃ±o molecular o cuando el sitio activo especÃ­fico determina el resultado.

Este es un resultado metodolÃ³gico importante: establece cuÃ¡ndo el ahorro computacional de CG deja de ser vÃ¡lido.

---

## SLIDE 43 â€” SecciÃ³n: Molecular Theory *(~20 seg)*

Sexto nivel. AquÃ­ cambiamos de paradigma: en lugar de simular partÃ­culas, minimizamos un funcional termodinÃ¡mico.

---

## SLIDE 44 â€” Free Energy Functional *(~2 min)*

*[SeÃ±alar: Î´Î©[Ï]/Î´Ï = 0]*

La pregunta fundamental de campo medio: Â¿cuÃ¡l es el perfil de densidad Ï(r) que minimiza el potencial termodinÃ¡mico grand Î©?

La respuesta es un sistema de ecuaciones de Euler-Lagrange acopladas. Una por cada especie quÃ­mica, incluyendo el polÃ­mero, los iones, el agua, y los grupos ionizables.

*[SeÃ±alar diagrama de perfiles de densidad en el poro]*

La ventaja revolucionaria frente a MC: podemos incorporar directamente el equilibrio quÃ­mico â€”protonaciÃ³n/deprotonaciÃ³nâ€” como variable termodinÃ¡mica. El pH local dentro del gel emerge del cÃ¡lculo, no se asume.

Una minimizaciÃ³n funcional tarda segundos de CPU. Monte Carlo equivalente tomarÃ­a horas. Esto nos permite mapear sistemÃ¡ticamente el espacio de parÃ¡metros de diseÃ±o: pH, salinidad, densidad de injerto, tipo de polÃ­mero.

---

## SLIDE 45 â€” Chemical Equilibria and Stimulus Response *(~1.5 min)*

La ventaja clave de la TeorÃ­a Molecular para sistemas responsivos: podemos calcular el estado de protonaciÃ³n de cada grupo funcional del polÃ­mero como funciÃ³n del pH local.

Ese pH local depende a su vez del perfil de densidad iÃ³nica. Y el perfil iÃ³nico depende del potencial electrostÃ¡tico. Es un sistema de ecuaciones acopladas que se resuelve iterativamente hasta autoconsistencia.

*[SeÃ±alar imagen del gel con los perfiles de densidad por pH]*

El resultado: predictibilidad cuantitativa del comportamiento de hidrogeles y nanogeles responsivos en funciÃ³n de variables de control externas.

---

## SLIDE 46 â€” PROBLEMA: Atlas #4 â€” Glyphosate Polymer *(~1 min)*

**Â¿QuÃ© pH maximiza el secuestro de glifosato en polÃ­meros responsivos de PAH?**

Tenemos una capa de polietilenimina injertada sobre una superficie. Queremos que capture glifosato del agua contaminada. El pH externo es una variable de control â€”podemos ajustarlo.

Pero el pH interno de la capa polimÃ©rica no es igual al externo. Â¿CuÃ¡l es el pH Ã³ptimo de operaciÃ³n?

*[SeÃ±alar imagen del sistema polÃ­mero-herbicida]*

---

## SLIDE 47 â€” SOLUCIÃ“N: Charge Regulation by Local pH *(~1.5 min)*

La TeorÃ­a Molecular calculÃ³ los perfiles de pH y carga dentro de la capa polimÃ©rica.

El pH interno difiere del bulk hasta en 2 unidades, dependiendo de la densidad de injerto y la salinidad. La deprotonaciÃ³n del glifosato al entrar en la capa â€”donde el pH local es mayorâ€” favorece activamente su adsorciÃ³n.

*[SeÃ±alar imÃ¡genes con perfiles de densidad]*

**DecisiÃ³n de diseÃ±o**: Ajustar la densidad de injerto del polÃ­mero para crear un microentorno interno de pH Ã³ptimo, independientemente del pH externo de la soluciÃ³n tratada. El material puede diseÃ±arse para funcionar en un rango de pH externo amplio, manteniendo condiciones internas Ã³ptimas.

---

## SLIDE 48 â€” PROBLEMA: Atlas #8 â€” AMPA vs Glyphosate *(~1 min)*

**Â¿CÃ³mo diseÃ±ar selectividad contra los productos de degradaciÃ³n del glifosato?**

El AMPA es el principal metabolito del glifosato y tambiÃ©n un contaminante. Un adsorbente ideal capturarÃ­a glifosato pero no â€”o mucho menosâ€” AMPA.

Â¿Por quÃ© AMPA se adsorbe mucho menos? Â¿Podemos explotar esta diferencia para diseÃ±o?

*[SeÃ±alar imagen de ambas molÃ©culas]*

---

## SLIDE 49 â€” SOLUCIÃ“N: Ionic Competition *(~1.5 min)*

La TeorÃ­a Molecular con descripciÃ³n explÃ­cita de conformaciones revelÃ³ el mecanismo:

El glifosato tiene tres grupos ionizables. El AMPA tiene uno. A pH neutro, el glifosato tiene carga efectiva significativamente mayor.

En la competencia por sitios catiÃ³nicos del polÃ­mero, el glifosato desplaza al AMPA por superioridad de carga efectiva. La energÃ­a libre de transferencia cuantifica esta diferencia.

**DecisiÃ³n de diseÃ±o**: Maximizar la densidad de carga del adsorbente para explotar la diferencia de valencia entre glifosato y AMPA. A alta densidad de carga, la selectividad por el compuesto mÃ¡s cargado aumenta exponencialmente. El adsorbente estÃ¡ inherentemente optimizado para el contaminante sin diseÃ±o adicional.

---

## SLIDE 50 â€” PROBLEMA: Atlas #5 â€” Protein Loading *(~1 min)*

**Â¿QuÃ© arquitectura de nanogel maximiza la carga de proteÃ­nas terapÃ©uticas?**

Insulina, mioglobina, citocromo C â€”proteÃ­nas con cargas y tamaÃ±os diferentes. Queremos encapsularlas en nanogeles pH-responsivos para delivery controlado.

Â¿DistribuciÃ³n homogÃ©nea de grupos funcionales en el gel, o gradiente de carga?

*[SeÃ±alar imagen del nanogel con proteÃ­nas]*

---

## SLIDE 51 â€” SOLUCIÃ“N: Core-Shell Charge Gradient *(~1.5 min)*

La TeorÃ­a Molecular predijo que un gradiente de densidad de carga â€”nÃºcleo altamente funcionalizado, corteza neutralâ€” crea un potencial electrostÃ¡tico que atrae la proteÃ­na hacia el interior.

La proteÃ­na queda alejada del entorno externo potencialmente desnaturalizante. La carga interna simultÃ¡neamente atrae y protege.

*[SeÃ±alar imÃ¡genes comparativas de distribuciones de carga]*

**DecisiÃ³n de diseÃ±o**: DiseÃ±ar nanogeles con nÃºcleo altamente funcionalizado y corteza de baja carga. La arquitectura homogÃ©nea tiene carga ~3 veces menor que el gradiente Ã³ptimo. La distribuciÃ³n espacial de la funcionalizaciÃ³n importa tanto como la cantidad total.

---

## SLIDE 52 â€” PROBLEMA: Atlas #9 â€” Salt Anomaly *(~1 min)*

**Â¿CuÃ¡l es la ventana de salinidad para la respuesta coloidal del nanogel?**

El comportamiento de hinchamiento como funciÃ³n de la concentraciÃ³n de sal es contra-intuitivo: el gel primero se expande, luego colapsa, y a salinidad muy alta puede re-expandirse.

Este comportamiento no-monÃ³tono â€”la anomalÃ­a del sal aÃ±adidaâ€” es crÃ­tico para aplicaciones biomÃ©dicas donde la salinidad fisiolÃ³gica es fija en ~150 mM NaCl.

*[SeÃ±alar imagen del nanogel en diferentes condiciones]*

---

## SLIDE 53 â€” SOLUCIÃ“N: Physiological Trigger *(~1.5 min)*

La TeorÃ­a TermodinÃ¡mica de Donnan predijo el mecanismo completo:

A baja sal: la presiÃ³n osmÃ³tica de los contra-iones maniene el gel expandido. A sal fisiolÃ³gica: la neutralizaciÃ³n de carga induce colapso. A muy alta sal: el efecto salting-out puede re-expandirlo.

La teorÃ­a predice exactamente el mÃ­nimo de hinchamiento y la salinidad de transiciÃ³n.

*[SeÃ±alar imÃ¡genes con curvas de swelling]*

**DecisiÃ³n de diseÃ±o**: Calibrar la densidad de red y la densidad de grupos ionizables para que el colapso mÃ¡ximo ocurra exactamente a 150 mM NaCl â€”la concentraciÃ³n fisiolÃ³gica del citoplasma tumoral. El gel libera el fÃ¡rmaco precisamente en el microentorno tumoral.

---

## SLIDE 54 â€” PROBLEMA: Atlas #20 â€” Doxorubicin Release *(~1 min)*

**Â¿Podemos usar poliaminas tumorales como llave quÃ­mica para liberar doxorubicina?**

Las biopoliaminas â€”putrescina, esperminaâ€” estÃ¡n sobre-expresadas en tejido tumoral. Si pudiÃ©ramos usar esta seÃ±al quÃ­mica como gatillo de liberaciÃ³n, tendrÃ­amos un sistema de delivery intrÃ­nsecamente selectivo.

*[SeÃ±alar imagen del sistema polÃ­mero-doxorubicina-poliaminas]*

---

## SLIDE 55 â€” SOLUCIÃ“N: Ion Exchange Triggered by Polyamines *(~1.5 min)*

La TeorÃ­a Molecular demostrÃ³ el mecanismo de intercambio iÃ³nico:

Las biopoliaminas â€”altamente cargadasâ€” desplazan a la doxorubicina â€”positivaâ€” de los sitios aniÃ³nicos del polÃ­mero portador por superioridad de afinidad electroestÃ¡tica competitiva.

El gatillo funciona: la doxorubicina solo se libera cuando hay biopoliaminas presentes a concentraciones suficientes.

*[SeÃ±alar imÃ¡genes del mecanismo]*

**DecisiÃ³n de diseÃ±o**: Usar polÃ­meros aniÃ³nicos con afinidad calibrada por biopoliaminas como plataforma de liberaciÃ³n tumor-selectiva. La concentraciÃ³n umbral de biopoliaminas para el gatillo puede ajustarse modificando la densidad de carga del portador.

---

## SLIDE 56 â€” SecciÃ³n: Continuum / PNP *(~20 seg)*

Ãšltimo nivel de simulaciÃ³n. AquÃ­ la discretizaciÃ³n molecular desaparece completamente.

---

## SLIDE 57 â€” Poisson-Nernst-Planck Equations *(~2 min)*

*[SeÃ±alar: âˆ‡Â·(Dâˆ‡c + zÎ¼câˆ‡Ï†) = 0]*

El flujo iÃ³nico tiene dos componentes: difusivo â€”proporcional al gradiente de concentraciÃ³nâ€” y electromigraciÃ³n â€”proporcional al campo elÃ©ctrico local.

La ecuaciÃ³n de Poisson acopla el campo elÃ©ctrico con la densidad de carga libre de los iones. El sistema PNP completo determina los perfiles de concentraciÃ³n y potencial en el poro a escala de dispositivo.

*[SeÃ±alar diagrama de perfiles c(z) y Ï†(z)]*

Â¿QuÃ© ganamos? Podemos predecir curvas I-V completas, rectificaciÃ³n iÃ³nica, selectividad a escala de micrÃ³metros. Podemos explorar geometrÃ­as de poro, funcionalizaciÃ³n de superficies, condiciones de operaciÃ³n â€”todo sin sÃ­ntesis.

Â¿QuÃ© perdemos? La discretizaciÃ³n molecular. Cada ion es una densidad continua, no una partÃ­cula. Los efectos de correlaciÃ³n iÃ³nica de corto alcance â€”importantes a concentraciones muy altasâ€” quedan fuera.

---

## SLIDE 58 â€” The Device Scale: IAST and PNP *(~1.5 min)*

A nivel continuo, dos herramientas complementarias:

**PNP para transporte iÃ³nico**: nanoporos funcionalizados, iontrÃ³nica, membranas de separaciÃ³n iÃ³nica. El input principal son los perfiles de carga superficial â€”que vienen de la TeorÃ­a Molecular del nivel anterior.

**IAST para separaciÃ³n de mezclas**: predicciÃ³n del equilibrio de mezclas de gases a partir de isotermas puras. Ãštil para diseÃ±o de ciclos industriales PSA/VSA, donde simular mezclas explÃ­citas es prohibitivo.

*[SeÃ±alar diagrama del loop completo DFT â†’ MC â†’ Theory â†’ PNP]*

El loop completo estÃ¡ cerrado. Cada nivel valida y alimenta al siguiente.

---

## SLIDE 59 â€” PROBLEMA: Atlas #2 â€” Blue Energy *(~1 min)*

**Â¿QuÃ© geometrÃ­a de poro maximiza la energÃ­a osmÃ³tica extraÃ­ble en la desembocadura rÃ­o-mar?**

La diferencia de salinidad entre el rÃ­o y el mar representa una enorme fuente de energÃ­a renovable â€”energÃ­a azul. Un nanoporo selectivo puede convertir ese gradiente en corriente elÃ©ctrica.

La geometrÃ­a del poro importa: un poro cilÃ­ndrico, cÃ³nico, o con forma de bala producen potencias muy diferentes.

*[SeÃ±alar imagen de las geometrÃ­as de poro]*

---

## SLIDE 60 â€” SOLUCIÃ“N: Bullet-Shaped Pore *(~1.5 min)*

PNP en geometrÃ­as asimÃ©tricas revelÃ³ que el **poro tipo bala** triplica la potencia osmÃ³tica extraÃ­ble respecto al poro cilÃ­ndrico.

El mecanismo: la forma de bala reduce drÃ¡sticamente la resistencia iÃ³nica de acceso en el extremo estrecho, donde el campo elÃ©ctrico es mÃ¡s intenso. El gradiente de concentraciÃ³n se convierte en corriente con mÃ­nimas pÃ©rdidas resistivas.

El poro cÃ³nico â€”la alternativa intuitivaâ€” tiene menor rendimiento por su gradiente de campo mÃ¡s suave.

*[SeÃ±alar imÃ¡genes con curvas I-V y mapas de campo]*

**DecisiÃ³n de diseÃ±o**: Fabricar poros asimÃ©tricos tipo bala para aplicaciones de energÃ­a osmÃ³tica. Los poros cÃ³nicos son subÃ³ptimos. Esta geometrÃ­a â€”80 pW por canal individualâ€” es el valor mÃ¡s alto reportado para un canal Ãºnico sin modificar.

---

## SLIDE 61 â€” PROBLEMA: Atlas #7 â€” Phosphate Diode *(~1 min)*

**Â¿CÃ³mo crear un diodo iÃ³nico sensible especÃ­ficamente al fosfato?**

El fosfato es un biomarcador importante â€”sobreexpresado en varios contextos patolÃ³gicos. Detectarlo a concentraciones fisiolÃ³gicas requiere un transductor con alta relaciÃ³n seÃ±al-ruido.

Los nanoporos con PAH â€”polietileniminaâ€” tienen carga positiva. Â¿Podemos usar la uniÃ³n especÃ­fica fosfato-PAH para cambiar el estado del diodo?

*[SeÃ±alar imagen del nanoporo con PAH]*

---

## SLIDE 62 â€” SOLUCIÃ“N: Rectification Inversion *(~1.5 min)*

PNP acoplado con MC mostrÃ³ el mecanismo completo:

La uniÃ³n de fosfato al PAH invierte la carga superficial del nanoporo de positiva a negativa. Esa inversiÃ³n de carga invierte la direcciÃ³n de la rectificaciÃ³n iÃ³nica.

El modelo predice cuantitativamente el umbral de concentraciÃ³n de fosfato que desencadena el cambio. Validado experimentalmente.

*[SeÃ±alar imÃ¡genes de las curvas I-V antes/despuÃ©s]*

**DecisiÃ³n de diseÃ±o**: Usar PAH como capa de funcionalizaciÃ³n en nanoporos para biosensado de fosfato con alta SNR. La inversiÃ³n de rectificaciÃ³n provee una seÃ±al binaria robusta, fÃ¡cilmente detectable electrÃ³nicamente. Imita funcionalmente los canales biolÃ³gicos SLC34.

---

## SLIDE 63 â€” PROBLEMA: Atlas #18 â€” Three-State Switch *(~1 min)*

**Â¿CÃ³mo diseÃ±ar un interruptor iÃ³nico con tres estados estables?**

Los circuitos iÃ³nicos â€”iontrÃ³nicaâ€” necesitan elementos de lÃ³gica mÃ¡s allÃ¡ del simple on/off. Un interruptor de tres estados abrirÃ­a posibilidades de lÃ³gica ternaria.

El mecanismo debe ser fÃ­sicamente robusto â€”el tercer estado no puede revertirse espontÃ¡neamente.

*[SeÃ±alar imagen del nanoporo asimÃ©trico]*

---

## SLIDE 64 â€” SOLUCIÃ“N: Three-Level Iontronic Logic *(~1.5 min)*

PNP en rÃ©gimen no-lineal, combinado con experimentos de KClOâ‚„, descubriÃ³ el mecanismo:

La **nanoprecipitaciÃ³n** de una sal poco soluble dentro del poro crea un estado de baja conductancia que no se revierte espontÃ¡neamente. Este es el tercer estado â€”inactivo.

PNP predice que este estado requiere operar cerca del lÃ­mite de solubilidad del producto de precipitaciÃ³n en el lumen del poro.

*[SeÃ±alar imÃ¡genes con los tres estados I-V]*

**DecisiÃ³n de diseÃ±o**: DiseÃ±ar poros funcionalizados asimÃ©tricos para operar bajo condiciones donde la concentraciÃ³n local del producto iÃ³nico estÃ© prÃ³xima al Ksp del precipitado objetivo. La asimetrÃ­a del poro es esencial para localizar la precipitaciÃ³n en la zona estrecha.

---

## SLIDE 65 â€” Multiscale Integration: The Complete Loop *(~2 min)*

*[SeÃ±alar el diagrama vertical DFT â†’ MC â†’ Theory â†’ PNP]*

Ahora podemos ver el loop completo.

DFT calcula energÃ­as de interacciÃ³n y cargas â†’ esos parÃ¡metros alimentan los force fields.

Monte Carlo y DinÃ¡mica Molecular calculan isotermas, perfiles de densidad molecular, coeficientes de difusiÃ³n â†’ esa informaciÃ³n caracteriza el material estadÃ­sticamente.

La TeorÃ­a Molecular optimiza la respuesta colectiva en funciÃ³n de variables de control pH, salinidad, temperatura â†’ entrega perfiles de carga.

PNP traduce esos perfiles en curvas I-V y selectividad a escala de dispositivo.

Cada nivel tiene su validaciÃ³n experimental independiente. Eso es lo que hace al loop robusto. Si hay discrepancia con el experimento, podemos identificar en quÃ© escala se origina el problema.

---

## SLIDE 66 â€” Philosophy *(~1.5 min)*

Quiero cerrar con algo que va mÃ¡s allÃ¡ de los mÃ©todos.

El principio fundamental de este trabajo es: **pregunta primero, mÃ©todo despuÃ©s**.

El error mÃ¡s comÃºn en simulaciÃ³n computacional es elegir el mÃ©todo por familiaridad â€”"usamos DFT porque sabemos DFT"â€” en lugar de por adecuaciÃ³n a la pregunta.

Si la pregunta es "Â¿cÃ³mo interactÃºan estos dos Ã¡tomos?", la respuesta es DFT.
Si la pregunta es "Â¿cuÃ¡nto gas cabe en este poro a esta presiÃ³n?", la respuesta es Monte Carlo.
Si la pregunta es "Â¿cÃ³mo responde este gel al pH fisiolÃ³gico?", la respuesta es TeorÃ­a Molecular.
Si la pregunta es "Â¿quÃ© corriente produce este nanoporo bajo 100 mV?", la respuesta es PNP.

Usar el nivel equivocado puede dar una respuesta correcta a la pregunta incorrecta.

---

## SLIDE 67 â€” Impact *(~1.5 min)*

El diseÃ±o racional de materiales tiene consecuencias prÃ¡cticas concretas.

El tiempo de desarrollo de un nuevo material pasa de dÃ©cadas a aÃ±os cuando la bÃºsqueda estÃ¡ guiada por predicciÃ³n computacional en lugar de prueba y error experimental.

Los casos que presentÃ© hoy cubren tres Ã¡reas de impacto:

**Ambiente**: captura de COâ‚‚, secuestro de herbicidas en agua contaminada, separaciÃ³n de mezclas industriales.

**Salud**: nanogeles para delivery controlado de quimioterÃ¡picos, biosensores de fosfato, nanovehÃ­culos antifouling.

**EnergÃ­a**: cosecha de energÃ­a osmÃ³tica, separaciÃ³n de isÃ³meros para mejorar combustibles.

El denominador comÃºn: diseÃ±ar antes de fabricar. Simular antes de sintetizar.

---

## SLIDE 68 â€” Future *(~1.5 min)*

Â¿Hacia dÃ³nde va el campo?

La frontera mÃ¡s interesante, en mi opiniÃ³n, es la integraciÃ³n entre el loop multiescala y el aprendizaje automÃ¡tico.

Los modelos de lenguaje y las redes neuronales entrenadas sobre datos de simulaciÃ³n multiescala pueden reemplazar los cÃ¡lculos cuÃ¡nticos mÃ¡s costosos en bÃºsquedas a gran escala de materiales.

Pero â€”y esto es crÃ­ticoâ€” **la fÃ­sica no desaparece**. Los mejores modelos de ML en ciencia de materiales son los que respetan las leyes de conservaciÃ³n, las simetrÃ­as del sistema, y los lÃ­mites fÃ­sicos conocidos.

El ML no reemplaza la fÃ­sica. La acelera. Y para acelerarla bien, primero hay que entenderla bien.

Eso es exactamente lo que este programa de investigaciÃ³n ha construido durante veinte aÃ±os.

---

## SLIDE 69 â€” The Power of Integration *(~1 min)*

*[Pausa. Mirar al pÃºblico.]*

Empezamos con la ecuaciÃ³n de SchrÃ¶dinger â€”intratable para sistemas reales.

Terminamos con dispositivos iÃ³nicos a escala de micrÃ³metros, nanogeles que responden al microentorno tumoral, y materiales que separan isÃ³meros con selectividad de forma.

El camino entre esos dos extremos es la jerarquÃ­a de aproximaciones que recorrimos hoy.

Cada mÃ©todo sacrifica algo. Pero lo que gana â€”en escala, en velocidad, en diseÃ±abilidadâ€” es lo que hace posible la ciencia de materiales computacional.

Muchas gracias.

*[Esperar aplausos. Preparar para preguntas.]*

---

## PREGUNTAS FRECUENTES â€” Respuestas preparadas

**P: Â¿CuÃ¡nto tiempo toma un ciclo completo DFTâ†’PNP para un material nuevo?**
R: Para un sistema bien caracterizado, de dÃ­as a semanas. El cuello de botella suele ser el GCMC o la parametrizaciÃ³n del force field. Una vez el force field estÃ¡ validado, explorar variantes tarda horas.

**P: Â¿CÃ³mo se valida que el force field de DFT es transferible?**
R: Comparamos propiedades de bulto â€”densidad, presiÃ³n de vapor, calor de vaporizaciÃ³nâ€” con datos experimentales antes de usar el force field para adsorciÃ³n. Si reproduce esas propiedades, confiamos en su transferibilidad.

**P: Â¿CuÃ¡ndo falla el modelo PNP?**
R: PNP falla a concentraciones iÃ³nicas muy altas (>1M) donde las correlaciones iÃ³nicas de corto alcance son importantes. TambiÃ©n falla si los iones son muy asimÃ©tricos en tamaÃ±o. Para esos casos usamos modelos de correlaciÃ³n iÃ³nica o MC explÃ­cito.

**P: Â¿Tienen datos experimentales propios o todo es predicciÃ³n?**
R: La mayorÃ­a de los trabajos tienen componente experimental. El grupo colabora con experimentalistas â€”en Argentina y en el exteriorâ€” que sintetizan los materiales y miden las propiedades. La teorÃ­a predice; el experimento valida; el loop se cierra.

---

*FIN DEL GUION â€” Tiempo total estimado: 50 minutos*
*Slides 1-30: ~25 min | Slides 31-69: ~25 min*

