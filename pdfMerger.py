import os
import PyPDF2

def merge_pdfs(folder_path, output_filename):
    pdf_merger = PyPDF2.PdfMerger()
    
    # Listar archivos en la carpeta del script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_list = [file for file in os.listdir(script_dir) if file.lower().endswith(".pdf")]
    
    # Ordenar archivos
    file_list.sort()
    
    # Agregar cada PDF a pdf_merger
    for file in file_list:
        file_path = os.path.join(script_dir, file)
        pdf_merger.append(file_path)
    
    # Guardarlo en un nuevo archivo
    with open(output_filename, "wb") as output_file:
        pdf_merger.write(output_file)

if __name__ == "__main__":
    output_filename = "resultado.pdf"   # Nombre del archivo PDF resultante
    
    merge_pdfs("", output_filename)
