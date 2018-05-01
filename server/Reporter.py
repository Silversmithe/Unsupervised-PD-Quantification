"""
REPORTER

Class responsible for taking the result of the system and
outputting valuable information from the data section
in a pdf
"""
import os
import datetime
from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.pdfgen import canvas

PATIENT_SCORE = {
    'name': 'patient-1',
    'ftap':  [0.0, 0.0],
    'htap':  [0.0, 0.0],
    'ptrem': [0.0, 0.0],
    'ktrem': [0.0, 0.0],
    'rtrem': [0.0, 0.0],
    'crest': [0.0, 0.0]
}


class Reporter(object):

    POINT = 1
    INCH = 72
    FILENAME = "score.pdf"
    REPORT = "UPDAReport.pdf"

    def __init__(self):
        pass

    def generate_report(self, patient_path):
        """

        :param patient_path:
        :return:
        """
        self.__generate_score(patient_path=patient_path)
        self.__merge_reports(patient_path=patient_path)

    def __generate_score(self, patient_path):
        """

        :param patient_path:
        ex: ./data/patient-1

        :return:
        """

        if not os.path.exists(path=patient_path):
            print("error: {} does not exist, cannot generate report".format(patient_path))
            return

        c = canvas.Canvas("{}/score.pdf".format(patient_path), pagesize=(8.5*self.INCH, 11*self.INCH))
        c.setStrokeColorRGB(0, 0, 0)
        c.setFillColorRGB(0, 0, 0)
        c.setFont("Helvetica", 12 * self.POINT)

        # generate patient name
        v = 10 * self.INCH
        c.drawString(7 * self.INCH, v, PATIENT_SCORE['name'])
        # generate datetime
        v = 10 * self.INCH
        v -= 12 * 4 * self.POINT
        c.drawString(3.25 * self.INCH, v, str(datetime.datetime.now()))
        # generate finger tap scores
        v = 10 * self.INCH
        v -= 12 * 12.5 * self.POINT
        c.drawString(4.25 * self.INCH, v, "{}%".format(PATIENT_SCORE['ftap'][0]))
        c.drawString(6.40 * self.INCH, v, "{}".format(PATIENT_SCORE['ftap'][1]))
        # generate hand movement scores
        v = 10 * self.INCH
        v -= 12 * 14.75 * self.POINT
        c.drawString(4.25 * self.INCH, v, "{}%".format(PATIENT_SCORE['htap'][0]))
        c.drawString(6.40 * self.INCH, v, "{}".format(PATIENT_SCORE['htap'][1]))
        # generate postural tremor scores
        v = 10 * self.INCH
        v -= 12 * 17 * self.POINT
        c.drawString(4.25 * self.INCH, v, "{}%".format(PATIENT_SCORE['ptrem'][0]))
        c.drawString(6.40 * self.INCH, v, "{}".format(PATIENT_SCORE['ptrem'][1]))
        # generate kinetic tremor scores
        v = 10 * self.INCH
        v -= 12 * 19.25 * self.POINT
        c.drawString(4.25 * self.INCH, v, "{}%".format(PATIENT_SCORE['ktrem'][0]))
        c.drawString(6.40 * self.INCH, v, "{}".format(PATIENT_SCORE['ktrem'][1]))
        # generate rest tremor scores
        v = 10 * self.INCH
        v -= 12 * 21.5 * self.POINT
        c.drawString(4.25 * self.INCH, v, "{}%".format(PATIENT_SCORE['rtrem'][0]))
        c.drawString(6.40 * self.INCH, v, "{}".format(PATIENT_SCORE['rtrem'][1]))
        # generate consistency of rest scores
        v = 10 * self.INCH
        v -= 12 * 23.75 * self.POINT
        c.drawString(4.25 * self.INCH, v, "{}%".format(PATIENT_SCORE['crest'][0]))
        c.drawString(6.40 * self.INCH, v, "{}".format(PATIENT_SCORE['crest'][1]))

        c.showPage()
        c.save()

    def __merge_reports(self, patient_path):
        """

        :param patient_path:
        ex: ./data/patient-1

        :return:
        """
        output = PdfFileWriter()

        head = PdfFileReader(open("./resources/HeadScore.pdf", "rb"))
        head_page = head.getPage(0)

        score = PdfFileReader(open("{}/{}".format(patient_path, self.FILENAME), "rb"))
        head_page.mergePage(score.getPage(0))

        output.addPage(head_page)
        output_stream = open("./data/{}/{}".format(patient_path, self.REPORT), "wb")
        output.write(output_stream)
