##########################
# NIVELES DE IMPORTANCIA #
##########################

MUY_ALTA = 1.0
ALTA     = 1.0
MEDIA    = 0.6
BAJA     = 0.25

#############
# PREGUNTAS #
#############

evaluar = {
	'Roboadvisors_1': {
		'pregunta': '¿Ha implementado medidas para evaluar y verificar continuamente la calidad de los datos de entrada a su sistema de IA (por ejemplo, es capaz de detectar cuando los datos son insuficientes para el cumplimiento de una tarea o cuando los datos de entrada son erróneos, incorrectos o inexactos)?',
		'importancia': ALTA
		},
	'Roboadvisors_2': {
		'pregunta': '¿Ha implementado procesos para monitorizar la presencia de posibles sesgos durante el ciclo de vida del sistema de IA, como por ejemplo, los sesgos generados por limitaciones derivadas de la composición del conjunto de datos utilizados (falta de diversidad, no representatividad, etc.)?',
		'importancia': ALTA
		},
	'Roboadvisors_3': {
		'pregunta': 'En los casos que exista una persona responsable de la privacidad y protección de los datos en su organización (por ejemplo, un Delegado de Protección de Datos o DPO), ¿lo han implicado en el diseño del sistema de IA desde la fase inicial del proceso?',
		'importancia': ALTA
		},
	'Roboadvisors_4': {
		'pregunta': '¿Ha diseñado su sistema de IA teniendo en cuenta las recomendaciones establecidas en los estándares internacionales (por ejemplo, las ISO de la Organización Internacional de Normalización o las recomendaciones del Instituto de Ingenieros Eléctricos y Electrónicos) y lo estipulado por el Reglamento General de Protección de Datos (protección de datos desde el diseño y por defecto, respeto de los derechos del interesado, licitud del tratamiento de los datos, etc.)?',
		'importancia': MUY_ALTA
		},
	'Roboadvisors_5': {
		'pregunta': '¿Ha establecido mecanismos para facilitar la auditabilidad del sistema de IA por parte de agentes internos y de externos independientes?',
		'importancia': ALTA
		},
	'Roboadvisors_6': {
		'pregunta': '¿Implicó o consultó durante la fase de diseño y desarrollo de su sistema de IA a personas con algún tipo de discapacidad?',
		'importancia': MEDIA
		},
	'Roboadvisors_7': {
		'pregunta': '¿Ha considerado la posibilidad de crear una "junta de revisión ética de la IA" (u otro sistema similar) en su organización con el fin de revisar las prácticas éticas y realizar una rendición de cuentas de sus sistemas de IA?',
		'importancia': BAJA
		},
	'Roboadvisors_8': {
		'pregunta': '¿Ha proporcionado claramente la información necesaria a las partes interesadas en los casos de que exista algún riesgo para la integridad física y/o psicológica de las personas derivado del uso de la IA en su modelo de negocio?',
		'importancia': ALTA
		},
	'Roboadvisors_9': {
		'pregunta': '¿Ha estudiado la posibilidad de contratar una póliza de seguro de responsabilidad civil para hacer frente a los posibles daños que pudiera provocar su sistema de IA?',
		'importancia': BAJA
		},
	'Roboadvisors_10': {
		'pregunta': '¿Ha establecido mecanismos para medir el impacto ambiental del desarrollo, despliegue y utilización del sistema de IA, por ejemplo, la energía consumida?',
		'importancia': BAJA
		},
	'Roboadvisors_11': {
		'pregunta': 'Si el sistema de IA integrado en el robo-advisor está realizando o ha realizado predicciones incorrectas o recomendaciones erróneas de inversión: ¿Ha establecido algún protocolo gestionado por seres humanos para subsanar dicho problema?',
		'importancia': ALTA
		},
	'Roboadvisors_12': {
		'pregunta': '¿Ha adoptado medidas para evitar los daños que se ocasionarían si el sistema de IA integrado en el robo-advisor realiza predicciones incorrectas y/o formula recomendaciones de inversión erróneas que no se ajustan al perfil de inversión del cliente?',
		'importancia': MUY_ALTA
		},
	'Roboadvisors_13': {
		'pregunta': '¿Ha establecido mecanismos que faciliten la auditabilidad del sistema de IA del robo-advisor (por ejemplo, la trazabilidad del proceso de desarrollo del robo-advisor, la obtención de los datos de entrenamiento y el registro de los procesos, el impacto positivo y negativo del sistema de IA y los resultados generados) por terceros independientes?',
		'importancia': ALTA
		},
	'Roboadvisors_14': {
		'pregunta': '¿Evaluó si la interfaz de usuario del sistema de IA del robo-advisor es utilizable también por personas con necesidades especiales o discapacidades y/o personas en riesgo de exclusión? Es decir: ¿Se aseguró de que el sistema de IA tiene en cuenta los principios de "accesibilidad universal" durante cada fase del proceso de planificación y desarrollo, si corresponde?',
		'importancia': MEDIA
		},
	'Roboadvisors_15': {
		'pregunta': '¿Los usuarios finales humanos son conocedores de que están interactuando con un sistema de IA en vez de un humano en el proceso de asesoramiento financiero personalizado?',
		'importancia': MUY_ALTA
		},
	'Roboadvisors_16': {
		'pregunta': '¿Se ha asegurado de que el robo-advisor indica claramente que su interacción social es simulada y que no tiene capacidad para "entender" ni "sentir"?',
		'importancia': ALTA
		},
	'Roboadvisors_17': {
		'pregunta': '¿Realiza encuestas a los usuarios con la finalidad de verificar si comprenden las decisiones adoptadas por el robo-advisor?',
		'importancia': MEDIA
		},
	'Roboadvisors_18': {
		'pregunta': '¿Se ha asegurado de introducir un "botón de parada o freno" o ha establecido algún procedimiento para abortar de modo seguro una operación del robo-advisor, cuando ello fuera necesario?',
		'importancia': BAJA
		},
	'Roboadvisors_19': {
		'pregunta': '¿Se ha asegurado de que los trabajadores que operan en el mismo entorno del robo-advisor comprenden como funciona el sistema de IA y cuáles son sus capacidades y limitaciones?',
		'importancia': MEDIA
		},



	'Trading_1': {
		'pregunta': '¿Ha implementado medidas para evaluar y verificar continuamente la calidad de los datos de entrada a su sistema de IA (por ejemplo, es capaz de detectar cuando los datos son insuficientes para el cumplimiento de una tarea o cuando los datos de entrada son erróneos, incorrectos o inexactos)?',
		'importancia': ALTA
		},
	'Trading_2': {
		'pregunta': '¿Ha implementado procesos para monitorizar la presencia de posibles sesgos durante el ciclo de vida del sistema de IA, como por ejemplo, los sesgos generados por limitaciones derivadas de la composición del conjunto de datos utilizados (falta de diversidad, no representatividad, etc.)?',
		'importancia': ALTA
		},
	'Trading_3': {
		'pregunta': 'En los casos que exista una persona responsable de la privacidad y protección de los datos en su organización (por ejemplo, un Delegado de Protección de Datos o DPO), ¿lo han implicado en el diseño del sistema de IA desde la fase inicial del proceso?',
		'importancia': ALTA
		},
	'Trading_4': {
		'pregunta': '¿Ha diseñado su sistema de IA teniendo en cuenta las recomendaciones establecidas en los estándares internacionales (por ejemplo, las ISO de la Organización Internacional de Normalización o las recomendaciones del Instituto de Ingenieros Eléctricos y Electrónicos) y lo estipulado por el Reglamento General de Protección de Datos (protección de datos desde el diseño y por defecto, respeto de los derechos del interesado, licitud del tratamiento de los datos, etc.)?',
		'importancia': MUY_ALTA
		},
	'Trading_5': {
		'pregunta': '¿Ha establecido mecanismos para facilitar la auditabilidad del sistema de IA por parte de agentes internos y de externos independientes?',
		'importancia': ALTA
		},
	'Trading_6': {
		'pregunta': '¿Implicó o consultó durante la fase de diseño y desarrollo de su sistema de IA a personas con algún tipo de discapacidad?',
		'importancia': MEDIA
		},
	'Trading_7': {
		'pregunta': '¿Ha considerado la posibilidad de crear una "junta de revisión ética de la IA" (u otro sistema similar) en su organización con el fin de revisar las prácticas éticas y realizar una rendición de cuentas de sus sistemas de IA?',
		'importancia': BAJA
		},
	'Trading_8': {
		'pregunta': '¿Ha proporcionado claramente la información necesaria a las partes interesadas en los casos de que exista algún riesgo para la integridad física y/o psicológica de las personas derivado del uso de la IA en su modelo de negocio?',
		'importancia': ALTA
		},
	'Trading_9': {
		'pregunta': '¿Ha estudiado la posibilidad de contratar una póliza de seguro de responsabilidad civil para hacer frente a los posibles daños que pudiera provocar su sistema de IA?',
		'importancia': BAJA
		},
	'Trading_10': {
		'pregunta': '¿Ha establecido mecanismos para medir el impacto ambiental del desarrollo, despliegue y utilización del sistema de IA, por ejemplo, la energía consumida?',
		'importancia': BAJA
		},
	'Trading_11': {
		'pregunta': '¿Ha anticipado los daños que se ocasionarían si el sistema de IA ejecuta operaciones de compra y venta de instrumentos financieros que no se ajustan a lo que necesita el cliente?',
		'importancia': ALTA
		},
	'Trading_12': {
		'pregunta': '¿Ha adoptado medidas que puedan garantizar la trazabilidad del algoritmo y, en concreto, que documenten el método de programación del algoritmo y que exliquen cómo funciona el algoritmo que ejecuta de manera automática órdenes de compra y venta de instrumentos financieros?',
		'importancia': MUY_ALTA
		},
	'Trading_13': {
		'pregunta': '¿Ha establecido mecanismos y adoptado medidas que garanticen la posibilidad de que las decisiones sobre compra y venta de instrumentos financieros automatizadas con algoritmos, puedan tomarse bajo la responsabilidad exclusiva de seres humanos?',
		'importancia': ALTA
		},
	'Trading_14': {
		'pregunta': '¿El sistema de IA que sustenta el trading algorítmico utilizado por la empresa cumple con estándares de ciberseguridad que minimicen el riesgo de ciberataques?',
		'importancia': MEDIA
		},



	'CreditScoring_1': {
		'pregunta': '¿Ha implementado medidas para evaluar y verificar continuamente la calidad de los datos de entrada a su sistema de IA (por ejemplo, es capaz de detectar cuando los datos son insuficientes para el cumplimiento de una tarea o cuando los datos de entrada son erróneos, incorrectos o inexactos)?',
		'importancia': ALTA
		},
	'CreditScoring_2': {
		'pregunta': '¿Ha implementado procesos para monitorizar la presencia de posibles sesgos durante el ciclo de vida del sistema de IA, como por ejemplo, los sesgos generados por limitaciones derivadas de la composición del conjunto de datos utilizados (falta de diversidad, no representatividad, etc.)?',
		'importancia': ALTA
		},
	'CreditScoring_3': {
		'pregunta': 'En los casos que exista una persona responsable de la privacidad y protección de los datos en su organización (por ejemplo, un Delegado de Protección de Datos o DPO), ¿lo han implicado en el diseño del sistema de IA desde la fase inicial del proceso?',
		'importancia': ALTA
		},
	'CreditScoring_4': {
		'pregunta': '¿Ha diseñado su sistema de IA teniendo en cuenta las recomendaciones establecidas en los estándares internacionales (por ejemplo, las ISO de la Organización Internacional de Normalización o las recomendaciones del Instituto de Ingenieros Eléctricos y Electrónicos) y lo estipulado por el Reglamento General de Protección de Datos (protección de datos desde el diseño y por defecto, respeto de los derechos del interesado, licitud del tratamiento de los datos, etc.)?',
		'importancia': MUY_ALTA
		},
	'CreditScoring_5': {
		'pregunta': '¿Ha establecido mecanismos para facilitar la auditabilidad del sistema de IA por parte de agentes internos y de externos independientes?',
		'importancia': ALTA
		},
	'CreditScoring_6': {
		'pregunta': '¿Implicó o consultó durante la fase de diseño y desarrollo de su sistema de IA a personas con algún tipo de discapacidad?',
		'importancia': MEDIA
		},
	'CreditScoring_7': {
		'pregunta': '¿Ha considerado la posibilidad de crear una "junta de revisión ética de la IA" (u otro sistema similar) en su organización con el fin de revisar las prácticas éticas y realizar una rendición de cuentas de sus sistemas de IA?',
		'importancia': BAJA
		},
	'CreditScoring_8': {
		'pregunta': '¿Ha proporcionado claramente la información necesaria a las partes interesadas en los casos de que exista algún riesgo para la integridad física y/o psicológica de las personas derivado del uso de la IA en su modelo de negocio?',
		'importancia': ALTA
		},
	'CreditScoring_9': {
		'pregunta': '¿Ha estudiado la posibilidad de contratar una póliza de seguro de responsabilidad civil para hacer frente a los posibles daños que pudiera provocar su sistema de IA?',
		'importancia': BAJA
		},
	'CreditScoring_10': {
		'pregunta': '¿Ha establecido mecanismos para medir el impacto ambiental del desarrollo, despliegue y utilización del sistema de IA, por ejemplo, la energía consumida?',
		'importancia': BAJA
		},
	'CreditScoring_11': {
		'pregunta': '¿Ha adoptado medidas para garantizar que los datos utilizados por el sistema de IA para evaluar el historial crediticio de un individuo sean correctos y actualizados?',
		'importancia': ALTA
		},
	'CreditScoring_12': {
		'pregunta': '¿Ha estimado el efecto probable de un fallo de su sistema de IA, que provoque que el sistema ofrezca resultados erróneos y/o discriminatorios al momento de pronunciarse sobre la solvencia de un cliente?',
		'importancia': MUY_ALTA
		},
	'CreditScoring_13': {
		'pregunta': '¿Se informa claramente a los usuarios que la decisión de conceder o no un crédito es fruto de una decisión "algorítmica" adoptada por un sistema de IA?',
		'importancia': ALTA
		},
	'CreditScoring_14': {
		'pregunta': '¿Tienen sus clientes la posibilidad de expresar sus puntos de vista, impugnar ante la empresa la decisión adoptada por el sistema de "scoring crediticio" y recibir una respuesta e intervención humanas por parte del responsable del sistema de IA?',
		'importancia': ALTA
		},
	'CreditScoring_15': {
		'pregunta': '¿Ha introducido mecanismos de aviso y control sobre los datos personales que trata de sus clientes en función del caso de uso (como, por ejemplo, verificación del consentimiento válido y la posibilidad de revocar el uso de dichos datos, cuando proceda)?',
		'importancia': MUY_ALTA
		},



	'Onboarding_1': {
		'pregunta': '¿Ha implementado medidas para evaluar y verificar continuamente la calidad de los datos de entrada a su sistema de IA (por ejemplo, es capaz de detectar cuando los datos son insuficientes para el cumplimiento de una tarea o cuando los datos de entrada son erróneos, incorrectos o inexactos)?',
		'importancia': ALTA
		},
	'Onboarding_2': {
		'pregunta': '¿Ha implementado procesos para monitorizar la presencia de posibles sesgos durante el ciclo de vida del sistema de IA, como por ejemplo, los sesgos generados por limitaciones derivadas de la composición del conjunto de datos utilizados (falta de diversidad, no representatividad, etc.)?',
		'importancia': ALTA
		},
	'Onboarding_3': {
		'pregunta': 'En los casos que exista una persona responsable de la privacidad y protección de los datos en su organización (por ejemplo, un Delegado de Protección de Datos o DPO), ¿lo han implicado en el diseño del sistema de IA desde la fase inicial del proceso?',
		'importancia': ALTA
		},
	'Onboarding_4': {
		'pregunta': '¿Ha diseñado su sistema de IA teniendo en cuenta las recomendaciones establecidas en los estándares internacionales (por ejemplo, las ISO de la Organización Internacional de Normalización o las recomendaciones del Instituto de Ingenieros Eléctricos y Electrónicos) y lo estipulado por el Reglamento General de Protección de Datos (protección de datos desde el diseño y por defecto, respeto de los derechos del interesado, licitud del tratamiento de los datos, etc.)?',
		'importancia': MUY_ALTA
		},
	'Onboarding_5': {
		'pregunta': '¿Ha establecido mecanismos para facilitar la auditabilidad del sistema de IA por parte de agentes internos y de externos independientes?',
		'importancia': ALTA
		},
	'Onboarding_6': {
		'pregunta': '¿Implicó o consultó durante la fase de diseño y desarrollo de su sistema de IA a personas con algún tipo de discapacidad?',
		'importancia': MEDIA
		},
	'Onboarding_7': {
		'pregunta': '¿Ha considerado la posibilidad de crear una "junta de revisión ética de la IA" (u otro sistema similar) en su organización con el fin de revisar las prácticas éticas y realizar una rendición de cuentas de sus sistemas de IA?',
		'importancia': BAJA
		},
	'Onboarding_8': {
		'pregunta': '¿Ha proporcionado claramente la información necesaria a las partes interesadas en los casos de que exista algún riesgo para la integridad física y/o psicológica de las personas derivado del uso de la IA en su modelo de negocio?',
		'importancia': ALTA
		},
	'Onboarding_9': {
		'pregunta': '¿Ha estudiado la posibilidad de contratar una póliza de seguro de responsabilidad civil para hacer frente a los posibles daños que pudiera provocar su sistema de IA?',
		'importancia': BAJA
		},
	'Onboarding_10': {
		'pregunta': '¿Ha establecido mecanismos para medir el impacto ambiental del desarrollo, despliegue y utilización del sistema de IA, por ejemplo, la energía consumida?',
		'importancia': BAJA
		},
	'Onboarding_11': {
		'pregunta': '¿Ha informado al usuario si es necesario tener en cuenta algún contexto o una condición particular para garantizar la reproducibilidad y uso del sistema de IA empleado en el proceso de onboarding (por ejemplo, determinado sistema operativo y navegador, uso de webcam, etc.)?',
		'importancia': MEDIA
		},
	'Onboarding_12': {
		'pregunta': '¿Ha establecido un protocolo y mecanismos que permitan notificar problemas y riesgos relacionados con la privacidad y la protección de datos  personales en los procesos de recopilación de datos y verificación de la identidad de los usuarios en el onboarding financiero?',
		'importancia': MUY_ALTA
		},
	'Onboarding_13': {
		'pregunta': '¿Ha evaluado si las personas con discapacidad, con necesidades especiales o en riesgo de exclusión pueden utilizar su sistema de onboarding basado en IA?',
		'importancia': MEDIA
		},



	'GestionRiesgos_1': {
		'pregunta': '¿Ha implementado medidas para evaluar y verificar continuamente la calidad de los datos de entrada a su sistema de IA (por ejemplo, es capaz de detectar cuando los datos son insuficientes para el cumplimiento de una tarea o cuando los datos de entrada son erróneos, incorrectos o inexactos)?',
		'importancia': ALTA
		},
	'GestionRiesgos_2': {
		'pregunta': '¿Ha implementado procesos para monitorizar la presencia de posibles sesgos durante el ciclo de vida del sistema de IA, como por ejemplo, los sesgos generados por limitaciones derivadas de la composición del conjunto de datos utilizados (falta de diversidad, no representatividad, etc.)?',
		'importancia': ALTA
		},
	'GestionRiesgos_3': {
		'pregunta': 'En los casos que exista una persona responsable de la privacidad y protección de los datos en su organización (por ejemplo, un Delegado de Protección de Datos o DPO), ¿lo han implicado en el diseño del sistema de IA desde la fase inicial del proceso?',
		'importancia': ALTA
		},
	'GestionRiesgos_4': {
		'pregunta': '¿Ha diseñado su sistema de IA teniendo en cuenta las recomendaciones establecidas en los estándares internacionales (por ejemplo, las ISO de la Organización Internacional de Normalización o las recomendaciones del Instituto de Ingenieros Eléctricos y Electrónicos) y lo estipulado por el Reglamento General de Protección de Datos (protección de datos desde el diseño y por defecto, respeto de los derechos del interesado, licitud del tratamiento de los datos, etc.)?',
		'importancia': MUY_ALTA
		},
	'GestionRiesgos_5': {
		'pregunta': '¿Ha establecido mecanismos para facilitar la auditabilidad del sistema de IA por parte de agentes internos y de externos independientes?',
		'importancia': ALTA
		},
	'GestionRiesgos_6': {
		'pregunta': '¿Implicó o consultó durante la fase de diseño y desarrollo de su sistema de IA a personas con algún tipo de discapacidad?',
		'importancia': MEDIA
		},
	'GestionRiesgos_7': {
		'pregunta': '¿Ha considerado la posibilidad de crear una "junta de revisión ética de la IA" (u otro sistema similar) en su organización con el fin de revisar las prácticas éticas y realizar una rendición de cuentas de sus sistemas de IA?',
		'importancia': BAJA
		},
	'GestionRiesgos_8': {
		'pregunta': '¿Ha proporcionado claramente la información necesaria a las partes interesadas en los casos de que exista algún riesgo para la integridad física y/o psicológica de las personas derivado del uso de la IA en su modelo de negocio?',
		'importancia': ALTA
		},
	'GestionRiesgos_9': {
		'pregunta': '¿Ha estudiado la posibilidad de contratar una póliza de seguro de responsabilidad civil para hacer frente a los posibles daños que pudiera provocar su sistema de IA?',
		'importancia': BAJA
		},
	'GestionRiesgos_10': {
		'pregunta': '¿Ha establecido mecanismos para medir el impacto ambiental del desarrollo, despliegue y utilización del sistema de IA, por ejemplo, la energía consumida?',
		'importancia': BAJA
		},
	'GestionRiesgos_11': {
		'pregunta': '¿Ha estudiado la posibilidad de contratar una póliza de seguro para hacer frente a los posibles daños que provoque el sistema de IA que predicen y automatizan los procesos de gestión de riesgos en su organización?',
		'importancia': MEDIA
		},
	'GestionRiesgos_12': {
		'pregunta': '¿Ha evaluado si existe un riesgo de pérdida de puestos de trabajo o de descualificación de la mano de obra dentro de su empresa, debido a la implantación de algoritmos para la gestión de riesgos financieros? Por ejemplo, para el supuesto de que se esté utilizando un algoritmo de IA para predecir, analizar riesgos financieros y tomar decisiones que antes eran realizados por una persona humana.',
		'importancia': MEDIA
		},
	'GestionRiesgos_13': {
		'pregunta': '¿Ha evaluado en qué medida la predicción del sistema algorítmico sobre la existencia (o no) de un posible riesgo financiero influye en la toma de decisiones de su organización?',
		'importancia': ALTA
		},
	'GestionRiesgos_14': {
		'pregunta': '¿Se ha asegurado de que sus sistemas de gestión de riesgos basados en IA cuentan con un plan idóneo para hacer frente a un ciberataque o una brecha de seguridad?',
		'importancia': MUY_ALTA
		},



	'Compliance_1': {
		'pregunta': '¿Ha implementado medidas para evaluar y verificar continuamente la calidad de los datos de entrada a su sistema de IA (por ejemplo, es capaz de detectar cuando los datos son insuficientes para el cumplimiento de una tarea o cuando los datos de entrada son erróneos, incorrectos o inexactos)?',
		'importancia': ALTA
		},
	'Compliance_2': {
		'pregunta': '¿Ha implementado procesos para monitorizar la presencia de posibles sesgos durante el ciclo de vida del sistema de IA, como por ejemplo, los sesgos generados por limitaciones derivadas de la composición del conjunto de datos utilizados (falta de diversidad, no representatividad, etc.)?',
		'importancia': ALTA
		},
	'Compliance_3': {
		'pregunta': 'En los casos que exista una persona responsable de la privacidad y protección de los datos en su organización (por ejemplo, un Delegado de Protección de Datos o DPO), ¿lo han implicado en el diseño del sistema de IA desde la fase inicial del proceso?',
		'importancia': ALTA
		},
	'Compliance_4': {
		'pregunta': '¿Ha diseñado su sistema de IA teniendo en cuenta las recomendaciones establecidas en los estándares internacionales (por ejemplo, las ISO de la Organización Internacional de Normalización o las recomendaciones del Instituto de Ingenieros Eléctricos y Electrónicos) y lo estipulado por el Reglamento General de Protección de Datos (protección de datos desde el diseño y por defecto, respeto de los derechos del interesado, licitud del tratamiento de los datos, etc.)?',
		'importancia': MUY_ALTA
		},
	'Compliance_5': {
		'pregunta': '¿Ha establecido mecanismos para facilitar la auditabilidad del sistema de IA por parte de agentes internos y de externos independientes?',
		'importancia': ALTA
		},
	'Compliance_6': {
		'pregunta': '¿Implicó o consultó durante la fase de diseño y desarrollo de su sistema de IA a personas con algún tipo de discapacidad?',
		'importancia': MEDIA
		},
	'Compliance_7': {
		'pregunta': '¿Ha considerado la posibilidad de crear una "junta de revisión ética de la IA" (u otro sistema similar) en su organización con el fin de revisar las prácticas éticas y realizar una rendición de cuentas de sus sistemas de IA?',
		'importancia': BAJA
		},
	'Compliance_8': {
		'pregunta': '¿Ha proporcionado claramente la información necesaria a las partes interesadas en los casos de que exista algún riesgo para la integridad física y/o psicológica de las personas derivado del uso de la IA en su modelo de negocio?',
		'importancia': ALTA
		},
	'Compliance_9': {
		'pregunta': '¿Ha estudiado la posibilidad de contratar una póliza de seguro de responsabilidad civil para hacer frente a los posibles daños que pudiera provocar su sistema de IA?',
		'importancia': BAJA
		},
	'Compliance_10': {
		'pregunta': '¿Ha establecido mecanismos para medir el impacto ambiental del desarrollo, despliegue y utilización del sistema de IA, por ejemplo, la energía consumida?',
		'importancia': BAJA
		},
	'Compliance_11': {
		'pregunta': '¿Se han introducido en los procedimientos para detectar patrones de prevención de blanqueo de capitales métodos de verificación que permitan garantizar la fiabilidad de los datos personales utilizados?',
		'importancia': MUY_ALTA
		},
	'Compliance_12': {
		'pregunta': '¿Ha analizado la naturaleza y los diferentes tipos de las vulnerabilidades del sistema de IA, como la contaminación de los datos relativos a transacciones presuntamente sospechosas?',
		'importancia': MUY_ALTA
		},
	'Compliance_13': {
		'pregunta': '¿Ha adoptado en sus sistemas de compliance basados en IA medidas para mejorar la privacidad, a través de procesos como el encriptado, la anonimización o la agregación de datos?',
		'importancia': ALTA
		},

}