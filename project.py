# Import the DaVinci Resolve Script module
from pydavinci import davinci

# Connect to the DaVinci Resolve application

def export_projects(export_folder):
    # Connect to the DaVinci Resolve application
    resolve = davinci.Resolve()

    # Get the project manager
    project_manager = resolve.project_manager

    # Get a list of all the projects in the database
    projects = project_manager.projects

    # Iterate through the projects and export each one
    for project in projects:
        export_folder_2 = export_folder + project
        project_manager.export_project(project, export_folder_2)

    print("All projects have been exported to the specified folder.")

# Set the export folder path
export_folder = '/Users/johnrogers/Desktop/resolvepy/'

# Export all the projects
export_projects(export_folder)