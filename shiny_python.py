import re

from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.panel_title("File Upload and Validation"),
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_file("file", "Choose a file to upload:", multiple=True),
        ),
    
        ui.panel_main(
            ui.output_text_verbatim("fileStatus"),
        )
    )
)


def server(input, output, session):

    @output
    @render.text()        
    def fileStatus():
                # file_infos is a list of dicts; each dict represents one file. Example:
        # [
        #   {
        #     'name': 'data.csv',
        #     'size': 2601,
        #     'type': 'text/csv',
        #     'datapath': '/tmp/fileupload-1wnx_7c2/tmpga4x9mps/0.csv'
        #   }
        # ]
        
        file_infos = input.file()
        file_name = file_infos[0]['name']
        
        if validateFileName(file_name):
            return "File name is correct."
            
        # Invalid file name
        else:
            return "Invalid file name. File name should start with a LabID number and end with _raw.xlsx."
                
    # Function to validate the correctness of a file name
    def validateFileName(file_name):
        """
        Validate the correctness of a file name.
        Returns True if the file name is valid, False otherwise.
        """
        # File name pattern: starts with a LabId number and end with _raw.xlsx
        pattern = r'^\d.*_raw\.xlsx$'
        return re.match(pattern,file_name) is not None

app = App(app_ui, server)
