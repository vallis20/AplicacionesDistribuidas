from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
from datetime import datetime

def generate_pdf_report(content, filename):
    buffer = BytesIO()

    # Create the PDF object, using BytesIO as its file
    pdf = canvas.Canvas(buffer, pagesize=letter)

    # Title
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawCentredString(300, 750, "Statistics Report")

    # Content
    pdf.setFont("Helvetica", 12)
    y_position = 700
    for line in content:
        pdf.drawString(50, y_position, line)
        y_position -= 20

    # Save the PDF to the buffer
    pdf.save()

    # Move the buffer's cursor to the beginning
    buffer.seek(0)

    # Save the PDF to a file
    with open(filename, "wb") as pdf_file:
        pdf_file.write(buffer.read())

def generate_general_report(db):
    streaming_query = """
    SELECT
        COUNT(*) AS total_streams,
        SUM(duration) AS total_duration,
        AVG(duration) AS average_duration
    FROM
        Streaming;
    """

    streaming_stats = db.execute_query(streaming_query)[0]

    audio_query = """
    SELECT
        COUNT(*) AS total_audios,
        SUM(duration) AS total_duration,
        AVG(duration) AS average_duration
    FROM
        Audio;
    """

    audio_stats = db.execute_query(audio_query)[0]

    download_query = """
    SELECT
        COUNT(*) AS total_downloads,
        MIN(fecha_descarga) AS earliest_download,
        MAX(fecha_descarga) AS latest_download
    FROM
        Descargas;
    """

    download_stats = db.execute_query(download_query)[0]

    # Format the statistics into lines for the PDF
    content = [
        f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "Streaming Statistics:",
        f"Total Streams: {streaming_stats.total_streams}",
        f"Total Duration: {streaming_stats.total_duration} seconds",
        f"Average Duration: {streaming_stats.average_duration:.2f} seconds",
        "",
        "Audio Statistics:",
        f"Total Audios: {audio_stats.total_audios}",
        f"Total Duration: {audio_stats.total_duration} seconds",
        f"Average Duration: {audio_stats.average_duration:.2f} seconds",
        "",
        "Download Statistics:",
        f"Total Downloads: {download_stats.total_downloads}",
        f"Earliest Download: {download_stats.earliest_download}",
        f"Latest Download: {download_stats.latest_download}",
    ]


    # Genera el informe PDF
    generate_pdf_report(content, "General_Statistics_Report.pdf")

def generate_billing_report(db):
    billing_query = """
    SELECT
        u.username AS user_username,
        f.factura_id,
        f.fecha_factura,
        f.total_amount,
        f.descripcion
    FROM
        Facturacion f
    JOIN
        Usuarios u ON f.usuario_id = u.usr_id;
    """

    billing_stats = db.execute_query(billing_query)

    # Format the billing statistics into lines for the PDF
    content = [
        f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "Billing Statistics:",
    ]

    for billing_record in billing_stats:
        content.append(f"User: {billing_record.user_username}")
        content.append(f"   Invoice ID: {billing_record.factura_id}")
        content.append(f"   Invoice Date: {billing_record.fecha_factura}")
        content.append(f"   Total Amount: {billing_record.total_amount}")
        content.append(f"   Description: {billing_record.descripcion}")
        content.append("")  # Add a blank line between entries

    # Generate the PDF report
    generate_pdf_report(content, "Billing_Statistics_Report.pdf")