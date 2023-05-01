import unreal

# Set the project content directory
content_dir = "/Game/Content/"

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
material_edit_library = unreal.MaterialEditingLibrary
editor_asset_library = unreal.EditorAssetLibrary

#check that there is a Materials directory
materials_dir = content_dir + "Materials"
esc_path = repr(materials_dir).replace(" ", "")
print(materials_dir)

#if there is no materials directory, create one
if not editor_asset_library.does_directory_exist(materials_dir):
    editor_asset_library.make_directory(materials_dir)

# create a master material
master_material = asset_tools.create_asset("M_GenericMaterial", materials_dir, unreal.Material, unreal.MaterialFactoryNew())


