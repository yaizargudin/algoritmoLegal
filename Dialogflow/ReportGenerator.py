from fpdf import FPDF

title = 'Informe de Evaluación'

class PDF(FPDF):
    """Clase que se encarga de generar el informe en pdf. Para generar el informe se le tiene que pasar un diccionario con las preguntas, las respuestas y las explicaciones"""


    def header(self):
        # Logo
        self.image('Algoritmo-Legal-logo.jpg', 10, 8, 60)

        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_draw_color(255, 255, 255)
        self.set_fill_color(255, 255, 255)
        self.set_text_color(0, 0, 0)
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Line break
        self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Página ' + str(self.page_no()), 0, 0, 'C')

    def question_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Pregunta %d :' % (num), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def question_body(self, text, answer, explanation):
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, text)
        # Line break
        self.ln()
        self.set_font('Times', 'B', 12)
        self.cell(0, 10, '  Respuesta: ' + str(answer), 0, 1, 'L')
        self.ln()
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, explanation)
        self.ln()

    def print_pregunta(self, num, title, text_pregunta, answer, explanation):
        self.question_title(num, title)
        self.question_body(text_pregunta, answer, explanation)

    def print_informe(self, preguntas, answers, explanations):
        self.set_title(title)
        self.set_author('Algoritmo Legal')
        self.add_page()

        # Bucle
        pregunta = 0
        for parameter in preguntas:
            pregunta += 1
            self.print_pregunta(pregunta, 'Pregunta ', preguntas[parameter]['pregunta'], "answer", "explanation")
        self.output('Informe.pdf', 'F')