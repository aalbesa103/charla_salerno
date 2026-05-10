# GUION CHARLA SALERNO — PARTE 2
# Dinámica Molecular → Coarse-Grain → Teoría Molecular → Continuum → Cierre
# Tiempo estimado: ~25 min

---

## SLIDE 31 — Sección: Molecular Dynamics *(~20 seg)*

Cuarto nivel: Dinámica Molecular. Ahora sí hay tiempo.

---

## SLIDE 32 — Newton's Second Law *(~2 min)*

*[Señalar: m·d²r/dt² = -∇V]*

La diferencia fundamental con Monte Carlo: aquí integramos las ecuaciones de Newton paso a paso. Cada átomo siente la fuerza de sus vecinos y se mueve en consecuencia.

El potencial cuántico V(r) es reemplazado por force fields clásicos: resortes para enlaces, ángulos y torques, más términos Lennard-Jones y Coulomb para interacciones no-enlazantes.

El resultado: trayectorias completas. No solo dónde están las moléculas, sino cómo se mueven. Coeficientes de difusión, funciones de distribución radial, espectros vibracionales.

El costo: pasos de femtosegundo. Para ver microsegundos, necesitamos 10⁹ pasos. El tiempo de simulación es el cuello de botella.

---

## SLIDE 33 — The Temporal Limit *(~1.5 min)*

*[Señalar el diagrama de escalas de tiempo]*

MD puede ver vibración de enlaces, difusión en poros, relajación de polímeros. Todo hasta aproximadamente el microsegundo.

Más allá: plegamiento de proteínas, transiciones de fase, catálisis enzimática. Invisible para MD estándar.

¿Cuándo pasamos a Coarse-Grain? Cuando la pregunta requiere escalas de micrómetros o milisegundos.

---

## SLIDE 34 — PROBLEMA: Atlas #14 — Nanogel Antifouling *(~1 min)*

**¿Cómo evitar que las proteínas del plasma sanguíneo se peguen al nanogel cuando se calienta?**

Los nanogeles termorresponsivos de NIPAm colapsan por encima de su temperatura de transición —unos 32°C. Al colapsar, exponen regiones hidrofóbicas que atraen proteínas plasmáticas.

Si se cubren de proteínas antes de llegar al tumor, el nanovehículo es neutralizado por el sistema inmune.

*[Señalar imagen del nanogel]*

---

## SLIDE 35 — SOLUCIÓN: Janus Architecture *(~1.5 min)*

MD de copolímeros NIPAm-EG mostró que la distribución espacial del co-monómero EG es crítica.

Parches bien definidos de EG en la superficie —arquitectura Janus— forman una capa hidrofílica dinámica que repele estéricamente las proteínas, incluso cuando el núcleo NIPAm está colapsado.

*[Señalar imágenes MD]*

Distribución aleatoria de EG: no protege. La hidrofobicidad del NIPAm colapsado domina.

**Decisión de diseño**: Forzar síntesis de arquitectura Janus con parches de EG bien definidos. Distribuciones aleatorias de monómeros hidrofílicos no protegen el núcleo del nanovehículo contra la adsorción de proteínas.

---

## SLIDE 36 — PROBLEMA: Atlas #17-MD — GOF Swelling *(~1 min)*

El mismo sistema GOF del nivel cuántico, ahora con una pregunta diferente.

**¿Cómo se expande dinámicamente el material bajo presión de gas?**

DFT nos dio la estructura de equilibrio y las energías de deformación del linker. Pero ¿cómo evoluciona ese proceso en el tiempo? ¿Es reversible? ¿Es isótropo?

*[Señalar imagen MD del GOF]*

---

## SLIDE 37 — SOLUCIÓN: Dynamic Swelling *(~1.5 min)*

Las trayectorias MD muestran el proceso completo: rotación de linkers, expansión de la celda unitaria, redistribución de la densidad electrónica.

La dilatación es **anisótropa y dependiente de la presión**. El eje de expansión preferente está determinado por la geometría de los linkers DBA.

*[Señalar imágenes MD]*

**Decisión de diseño**: Incorporar la dilatación estructural en el diseño mecánico del dispositivo de contención. Ignorar el hinchamiento lleva a subestimar la capacidad real y a fallo mecánico en ciclos de carga/descarga.

---

## SLIDE 38 — Sección: Coarse-Grain *(~20 seg)*

Quinto nivel. Sacrificamos detalle atómico para ganar dos o tres órdenes de magnitud en escala.

---

## SLIDE 39 — Integration of Degrees of Freedom *(~2 min)*

*[Señalar: V_CG(R) ≈ -k_BT ln ∫ e^{-βV} dr]*

La idea es simple: agrupamos N átomos en un único "bead" CG. La dinámica interna del grupo se integra fuera — solo queda el potencial efectivo de interacción entre beads.

*[Señalar diagrama átomo → bead, mapeo 4:1]*

Con 4 átomos por bead, reducimos el número de partículas por un factor 4. Pero la ganancia en tiempo de simulación es mucho mayor —porque el paso de tiempo también puede ser mayor, y el potencial es más suave.

El resultado: acceso a escalas de micrómetros y milisegundos. Vesículas, micelas, redes de polímeros, morfología de ensamblado.

El precio: perdemos los sitios activos. No podemos calcular reacciones químicas ni reconocimiento molecular de alta precisión con CG.

---

## SLIDE 40 — Gain vs Loss *(~1 min)*

Regla práctica:

**Usar CG para**: morfología de auto-ensamblado, transporte bulk en materiales, conformaciones de cadenas poliméricas largas.

**Evitar CG para**: reconocimiento molecular específico, cálculos de selectividad en sitios activos, reacciones, interacciones de corto alcance que determinan afinidad.

**Protocolo óptimo**: CG para identificar configuraciones morfológicas relevantes, luego refinamiento con átomos explícitos en las regiones de interés.

---

## SLIDE 41 — PROBLEMA: Atlas #15 — Alkane CG *(~1 min)*

**¿Cuál es el límite del modelado simplificado bajo confinamiento extremo?**

Los alcanos largos en carbones activados son sistemas industrialmente relevantes —solventes, combustibles, refinación. La simulación atomística es costosa.

¿Podemos usar modelos CG 4:1 sin perder precisión?

*[Señalar imagen del modelo carbón-alcano]*

---

## SLIDE 42 — SOLUCIÓN: The Coarse-Grain Limit *(~1.5 min)*

El modelo CG reproduce fielmente el comportamiento de alcanos en **mesoporos** —poros de 2-50 nm.

Pero falla cuantitativamente en **microconfinamiento** —poros menores de 1 nm— donde el detalle atómico domina el empaquetamiento. La diferencia en isoterma puede superar el 30%.

*[Señalar imágenes comparativas]*

**Decisión de diseño**: Usar CG para modelado de transporte bulk y adsorción en mesoporos. Cambiar a representación átomo explícito cuando el poro es comparable al tamaño molecular o cuando el sitio activo específico determina el resultado.

Este es un resultado metodológico importante: establece cuándo el ahorro computacional de CG deja de ser válido.

---

## SLIDE 43 — Sección: Molecular Theory *(~20 seg)*

Sexto nivel. Aquí cambiamos de paradigma: en lugar de simular partículas, minimizamos un funcional termodinámico.

---

## SLIDE 44 — Free Energy Functional *(~2 min)*

*[Señalar: δΩ[ρ]/δρ = 0]*

La pregunta fundamental de campo medio: ¿cuál es el perfil de densidad ρ(r) que minimiza el potencial termodinámico grand Ω?

La respuesta es un sistema de ecuaciones de Euler-Lagrange acopladas. Una por cada especie química, incluyendo el polímero, los iones, el agua, y los grupos ionizables.

*[Señalar diagrama de perfiles de densidad en el poro]*

La ventaja revolucionaria frente a MC: podemos incorporar directamente el equilibrio químico —protonación/deprotonación— como variable termodinámica. El pH local dentro del gel emerge del cálculo, no se asume.

Una minimización funcional tarda segundos de CPU. Monte Carlo equivalente tomaría horas. Esto nos permite mapear sistemáticamente el espacio de parámetros de diseño: pH, salinidad, densidad de injerto, tipo de polímero.

---

## SLIDE 45 — Chemical Equilibria and Stimulus Response *(~1.5 min)*

La ventaja clave de la Teoría Molecular para sistemas responsivos: podemos calcular el estado de protonación de cada grupo funcional del polímero como función del pH local.

Ese pH local depende a su vez del perfil de densidad iónica. Y el perfil iónico depende del potencial electrostático. Es un sistema de ecuaciones acopladas que se resuelve iterativamente hasta autoconsistencia.

*[Señalar imagen del gel con los perfiles de densidad por pH]*

El resultado: predictibilidad cuantitativa del comportamiento de hidrogeles y nanogeles responsivos en función de variables de control externas.

---

## SLIDE 46 — PROBLEMA: Atlas #4 — Glyphosate Polymer *(~1 min)*

**¿Qué pH maximiza el secuestro de glifosato en polímeros responsivos de PAH?**

Tenemos una capa de polietilenimina injertada sobre una superficie. Queremos que capture glifosato del agua contaminada. El pH externo es una variable de control —podemos ajustarlo.

Pero el pH interno de la capa polimérica no es igual al externo. ¿Cuál es el pH óptimo de operación?

*[Señalar imagen del sistema polímero-herbicida]*

---

## SLIDE 47 — SOLUCIÓN: Charge Regulation by Local pH *(~1.5 min)*

La Teoría Molecular calculó los perfiles de pH y carga dentro de la capa polimérica.

El pH interno difiere del bulk hasta en 2 unidades, dependiendo de la densidad de injerto y la salinidad. La deprotonación del glifosato al entrar en la capa —donde el pH local es mayor— favorece activamente su adsorción.

*[Señalar imágenes con perfiles de densidad]*

**Decisión de diseño**: Ajustar la densidad de injerto del polímero para crear un microentorno interno de pH óptimo, independientemente del pH externo de la solución tratada. El material puede diseñarse para funcionar en un rango de pH externo amplio, manteniendo condiciones internas óptimas.

---

## SLIDE 48 — PROBLEMA: Atlas #8 — AMPA vs Glyphosate *(~1 min)*

**¿Cómo diseñar selectividad contra los productos de degradación del glifosato?**

El AMPA es el principal metabolito del glifosato y también un contaminante. Un adsorbente ideal capturaría glifosato pero no —o mucho menos— AMPA.

¿Por qué AMPA se adsorbe mucho menos? ¿Podemos explotar esta diferencia para diseño?

*[Señalar imagen de ambas moléculas]*

---

## SLIDE 49 — SOLUCIÓN: Ionic Competition *(~1.5 min)*

La Teoría Molecular con descripción explícita de conformaciones reveló el mecanismo:

El glifosato tiene tres grupos ionizables. El AMPA tiene uno. A pH neutro, el glifosato tiene carga efectiva significativamente mayor.

En la competencia por sitios catiónicos del polímero, el glifosato desplaza al AMPA por superioridad de carga efectiva. La energía libre de transferencia cuantifica esta diferencia.

**Decisión de diseño**: Maximizar la densidad de carga del adsorbente para explotar la diferencia de valencia entre glifosato y AMPA. A alta densidad de carga, la selectividad por el compuesto más cargado aumenta exponencialmente. El adsorbente está inherentemente optimizado para el contaminante sin diseño adicional.

---

## SLIDE 50 — PROBLEMA: Atlas #5 — Protein Loading *(~1 min)*

**¿Qué arquitectura de nanogel maximiza la carga de proteínas terapéuticas?**

Insulina, mioglobina, citocromo C —proteínas con cargas y tamaños diferentes. Queremos encapsularlas en nanogeles pH-responsivos para delivery controlado.

¿Distribución homogénea de grupos funcionales en el gel, o gradiente de carga?

*[Señalar imagen del nanogel con proteínas]*

---

## SLIDE 51 — SOLUCIÓN: Core-Shell Charge Gradient *(~1.5 min)*

La Teoría Molecular predijo que un gradiente de densidad de carga —núcleo altamente funcionalizado, corteza neutral— crea un potencial electrostático que atrae la proteína hacia el interior.

La proteína queda alejada del entorno externo potencialmente desnaturalizante. La carga interna simultáneamente atrae y protege.

*[Señalar imágenes comparativas de distribuciones de carga]*

**Decisión de diseño**: Diseñar nanogeles con núcleo altamente funcionalizado y corteza de baja carga. La arquitectura homogénea tiene carga ~3 veces menor que el gradiente óptimo. La distribución espacial de la funcionalización importa tanto como la cantidad total.

---

## SLIDE 52 — PROBLEMA: Atlas #9 — Salt Anomaly *(~1 min)*

**¿Cuál es la ventana de salinidad para la respuesta coloidal del nanogel?**

El comportamiento de hinchamiento como función de la concentración de sal es contra-intuitivo: el gel primero se expande, luego colapsa, y a salinidad muy alta puede re-expandirse.

Este comportamiento no-monótono —la anomalía del sal añadida— es crítico para aplicaciones biomédicas donde la salinidad fisiológica es fija en ~150 mM NaCl.

*[Señalar imagen del nanogel en diferentes condiciones]*

---

## SLIDE 53 — SOLUCIÓN: Physiological Trigger *(~1.5 min)*

La Teoría Termodinámica de Donnan predijo el mecanismo completo:

A baja sal: la presión osmótica de los contra-iones maniene el gel expandido. A sal fisiológica: la neutralización de carga induce colapso. A muy alta sal: el efecto salting-out puede re-expandirlo.

La teoría predice exactamente el mínimo de hinchamiento y la salinidad de transición.

*[Señalar imágenes con curvas de swelling]*

**Decisión de diseño**: Calibrar la densidad de red y la densidad de grupos ionizables para que el colapso máximo ocurra exactamente a 150 mM NaCl —la concentración fisiológica del citoplasma tumoral. El gel libera el fármaco precisamente en el microentorno tumoral.

---

## SLIDE 54 — PROBLEMA: Atlas #20 — Doxorubicin Release *(~1 min)*

**¿Podemos usar poliaminas tumorales como llave química para liberar doxorubicina?**

Las biopoliaminas —putrescina, espermina— están sobre-expresadas en tejido tumoral. Si pudiéramos usar esta señal química como gatillo de liberación, tendríamos un sistema de delivery intrínsecamente selectivo.

*[Señalar imagen del sistema polímero-doxorubicina-poliaminas]*

---

## SLIDE 55 — SOLUCIÓN: Ion Exchange Triggered by Polyamines *(~1.5 min)*

La Teoría Molecular demostró el mecanismo de intercambio iónico:

Las biopoliaminas —altamente cargadas— desplazan a la doxorubicina —positiva— de los sitios aniónicos del polímero portador por superioridad de afinidad electroestática competitiva.

El gatillo funciona: la doxorubicina solo se libera cuando hay biopoliaminas presentes a concentraciones suficientes.

*[Señalar imágenes del mecanismo]*

**Decisión de diseño**: Usar polímeros aniónicos con afinidad calibrada por biopoliaminas como plataforma de liberación tumor-selectiva. La concentración umbral de biopoliaminas para el gatillo puede ajustarse modificando la densidad de carga del portador.

---

## SLIDE 56 — Sección: Continuum / PNP *(~20 seg)*

Último nivel de simulación. Aquí la discretización molecular desaparece completamente.

---

## SLIDE 57 — Poisson-Nernst-Planck Equations *(~2 min)*

*[Señalar: ∇·(D∇c + zμc∇φ) = 0]*

El flujo iónico tiene dos componentes: difusivo —proporcional al gradiente de concentración— y electromigración —proporcional al campo eléctrico local.

La ecuación de Poisson acopla el campo eléctrico con la densidad de carga libre de los iones. El sistema PNP completo determina los perfiles de concentración y potencial en el poro a escala de dispositivo.

*[Señalar diagrama de perfiles c(z) y φ(z)]*

¿Qué ganamos? Podemos predecir curvas I-V completas, rectificación iónica, selectividad a escala de micrómetros. Podemos explorar geometrías de poro, funcionalización de superficies, condiciones de operación —todo sin síntesis.

¿Qué perdemos? La discretización molecular. Cada ion es una densidad continua, no una partícula. Los efectos de correlación iónica de corto alcance —importantes a concentraciones muy altas— quedan fuera.

---

## SLIDE 58 — The Device Scale: IAST and PNP *(~1.5 min)*

A nivel continuo, dos herramientas complementarias:

**PNP para transporte iónico**: nanoporos funcionalizados, iontrónica, membranas de separación iónica. El input principal son los perfiles de carga superficial —que vienen de la Teoría Molecular del nivel anterior.

**IAST para separación de mezclas**: predicción del equilibrio de mezclas de gases a partir de isotermas puras. Útil para diseño de ciclos industriales PSA/VSA, donde simular mezclas explícitas es prohibitivo.

*[Señalar diagrama del loop completo DFT → MC → Theory → PNP]*

El loop completo está cerrado. Cada nivel valida y alimenta al siguiente.

---

## SLIDE 59 — PROBLEMA: Atlas #2 — Blue Energy *(~1 min)*

**¿Qué geometría de poro maximiza la energía osmótica extraíble en la desembocadura río-mar?**

La diferencia de salinidad entre el río y el mar representa una enorme fuente de energía renovable —energía azul. Un nanoporo selectivo puede convertir ese gradiente en corriente eléctrica.

La geometría del poro importa: un poro cilíndrico, cónico, o con forma de bala producen potencias muy diferentes.

*[Señalar imagen de las geometrías de poro]*

---

## SLIDE 60 — SOLUCIÓN: Bullet-Shaped Pore *(~1.5 min)*

PNP en geometrías asimétricas reveló que el **poro tipo bala** triplica la potencia osmótica extraíble respecto al poro cilíndrico.

El mecanismo: la forma de bala reduce drásticamente la resistencia iónica de acceso en el extremo estrecho, donde el campo eléctrico es más intenso. El gradiente de concentración se convierte en corriente con mínimas pérdidas resistivas.

El poro cónico —la alternativa intuitiva— tiene menor rendimiento por su gradiente de campo más suave.

*[Señalar imágenes con curvas I-V y mapas de campo]*

**Decisión de diseño**: Fabricar poros asimétricos tipo bala para aplicaciones de energía osmótica. Los poros cónicos son subóptimos. Esta geometría —80 pW por canal individual— es el valor más alto reportado para un canal único sin modificar.

---

## SLIDE 61 — PROBLEMA: Atlas #7 — Phosphate Diode *(~1 min)*

**¿Cómo crear un diodo iónico sensible específicamente al fosfato?**

El fosfato es un biomarcador importante —sobreexpresado en varios contextos patológicos. Detectarlo a concentraciones fisiológicas requiere un transductor con alta relación señal-ruido.

Los nanoporos con PAH —polietilenimina— tienen carga positiva. ¿Podemos usar la unión específica fosfato-PAH para cambiar el estado del diodo?

*[Señalar imagen del nanoporo con PAH]*

---

## SLIDE 62 — SOLUCIÓN: Rectification Inversion *(~1.5 min)*

PNP acoplado con MC mostró el mecanismo completo:

La unión de fosfato al PAH invierte la carga superficial del nanoporo de positiva a negativa. Esa inversión de carga invierte la dirección de la rectificación iónica.

El modelo predice cuantitativamente el umbral de concentración de fosfato que desencadena el cambio. Validado experimentalmente.

*[Señalar imágenes de las curvas I-V antes/después]*

**Decisión de diseño**: Usar PAH como capa de funcionalización en nanoporos para biosensado de fosfato con alta SNR. La inversión de rectificación provee una señal binaria robusta, fácilmente detectable electrónicamente. Imita funcionalmente los canales biológicos SLC34.

---

## SLIDE 63 — PROBLEMA: Atlas #18 — Three-State Switch *(~1 min)*

**¿Cómo diseñar un interruptor iónico con tres estados estables?**

Los circuitos iónicos —iontrónica— necesitan elementos de lógica más allá del simple on/off. Un interruptor de tres estados abriría posibilidades de lógica ternaria.

El mecanismo debe ser físicamente robusto —el tercer estado no puede revertirse espontáneamente.

*[Señalar imagen del nanoporo asimétrico]*

---

## SLIDE 64 — SOLUCIÓN: Three-Level Iontronic Logic *(~1.5 min)*

PNP en régimen no-lineal, combinado con experimentos de KClO₄, descubrió el mecanismo:

La **nanoprecipitación** de una sal poco soluble dentro del poro crea un estado de baja conductancia que no se revierte espontáneamente. Este es el tercer estado —inactivo.

PNP predice que este estado requiere operar cerca del límite de solubilidad del producto de precipitación en el lumen del poro.

*[Señalar imágenes con los tres estados I-V]*

**Decisión de diseño**: Diseñar poros funcionalizados asimétricos para operar bajo condiciones donde la concentración local del producto iónico esté próxima al Ksp del precipitado objetivo. La asimetría del poro es esencial para localizar la precipitación en la zona estrecha.

---

## SLIDE 65 — Multiscale Integration: The Complete Loop *(~2 min)*

*[Señalar el diagrama vertical DFT → MC → Theory → PNP]*

Ahora podemos ver el loop completo.

DFT calcula energías de interacción y cargas → esos parámetros alimentan los force fields.

Monte Carlo y Dinámica Molecular calculan isotermas, perfiles de densidad molecular, coeficientes de difusión → esa información caracteriza el material estadísticamente.

La Teoría Molecular optimiza la respuesta colectiva en función de variables de control pH, salinidad, temperatura → entrega perfiles de carga.

PNP traduce esos perfiles en curvas I-V y selectividad a escala de dispositivo.

Cada nivel tiene su validación experimental independiente. Eso es lo que hace al loop robusto. Si hay discrepancia con el experimento, podemos identificar en qué escala se origina el problema.

---

## SLIDE 66 — Philosophy *(~1.5 min)*

Quiero cerrar con algo que va más allá de los métodos.

El principio fundamental de este trabajo es: **pregunta primero, método después**.

El error más común en simulación computacional es elegir el método por familiaridad —"usamos DFT porque sabemos DFT"— en lugar de por adecuación a la pregunta.

Si la pregunta es "¿cómo interactúan estos dos átomos?", la respuesta es DFT.
Si la pregunta es "¿cuánto gas cabe en este poro a esta presión?", la respuesta es Monte Carlo.
Si la pregunta es "¿cómo responde este gel al pH fisiológico?", la respuesta es Teoría Molecular.
Si la pregunta es "¿qué corriente produce este nanoporo bajo 100 mV?", la respuesta es PNP.

Usar el nivel equivocado puede dar una respuesta correcta a la pregunta incorrecta.

---

## SLIDE 67 — Impact *(~1.5 min)*

El diseño racional de materiales tiene consecuencias prácticas concretas.

El tiempo de desarrollo de un nuevo material pasa de décadas a años cuando la búsqueda está guiada por predicción computacional en lugar de prueba y error experimental.

Los casos que presenté hoy cubren tres áreas de impacto:

**Ambiente**: captura de CO₂, secuestro de herbicidas en agua contaminada, separación de mezclas industriales.

**Salud**: nanogeles para delivery controlado de quimioterápicos, biosensores de fosfato, nanovehículos antifouling.

**Energía**: cosecha de energía osmótica, separación de isómeros para mejorar combustibles.

El denominador común: diseñar antes de fabricar. Simular antes de sintetizar.

---

## SLIDE 68 — Future *(~1.5 min)*

¿Hacia dónde va el campo?

La frontera más interesante, en mi opinión, es la integración entre el loop multiescala y el aprendizaje automático.

Los modelos de lenguaje y las redes neuronales entrenadas sobre datos de simulación multiescala pueden reemplazar los cálculos cuánticos más costosos en búsquedas a gran escala de materiales.

Pero —y esto es crítico— **la física no desaparece**. Los mejores modelos de ML en ciencia de materiales son los que respetan las leyes de conservación, las simetrías del sistema, y los límites físicos conocidos.

El ML no reemplaza la física. La acelera. Y para acelerarla bien, primero hay que entenderla bien.

Eso es exactamente lo que este programa de investigación ha construido durante veinte años.

---

## SLIDE 69 — The Power of Integration *(~1 min)*

*[Pausa. Mirar al público.]*

Empezamos con la ecuación de Schrödinger —intratable para sistemas reales.

Terminamos con dispositivos iónicos a escala de micrómetros, nanogeles que responden al microentorno tumoral, y materiales que separan isómeros con selectividad de forma.

El camino entre esos dos extremos es la jerarquía de aproximaciones que recorrimos hoy.

Cada método sacrifica algo. Pero lo que gana —en escala, en velocidad, en diseñabilidad— es lo que hace posible la ciencia de materiales computacional.

Muchas gracias.

*[Esperar aplausos. Preparar para preguntas.]*

---

## PREGUNTAS FRECUENTES — Respuestas preparadas

**P: ¿Cuánto tiempo toma un ciclo completo DFT→PNP para un material nuevo?**
R: Para un sistema bien caracterizado, de días a semanas. El cuello de botella suele ser el GCMC o la parametrización del force field. Una vez el force field está validado, explorar variantes tarda horas.

**P: ¿Cómo se valida que el force field de DFT es transferible?**
R: Comparamos propiedades de bulto —densidad, presión de vapor, calor de vaporización— con datos experimentales antes de usar el force field para adsorción. Si reproduce esas propiedades, confiamos en su transferibilidad.

**P: ¿Cuándo falla el modelo PNP?**
R: PNP falla a concentraciones iónicas muy altas (>1M) donde las correlaciones iónicas de corto alcance son importantes. También falla si los iones son muy asimétricos en tamaño. Para esos casos usamos modelos de correlación iónica o MC explícito.

**P: ¿Tienen datos experimentales propios o todo es predicción?**
R: La mayoría de los trabajos tienen componente experimental. El grupo colabora con experimentalistas —en Argentina y en el exterior— que sintetizan los materiales y miden las propiedades. La teoría predice; el experimento valida; el loop se cierra.

---

*FIN DEL GUION — Tiempo total estimado: 50 minutos*
*Slides 1-30: ~25 min | Slides 31-69: ~25 min*
