import unreal

# Set the project content directory
content_dir = "/Game/Content/"

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
material_edit_library = unreal.MaterialEditingLibrary
editor_asset_library = unreal.EditorAssetLibrary

#define the materials directory
materials_dir = content_dir + "Materials"
esc_path = repr(materials_dir).replace(" ", "")
print(materials_dir)

#if there is no materials directory, create one
if not editor_asset_library.does_directory_exist(materials_dir):
    editor_asset_library.make_directory(materials_dir)

# create a master material
master_material = asset_tools.create_asset("M_GenericMaterial", materials_dir, unreal.Material, unreal.MaterialFactoryNew())

#create the base color parameter and connect it to the base color property
base_color_param = material_edit_library.create_material_expression(master_material, unreal.MaterialExpressionTextureSampleParameter,-384, -200)
material_edit_library.connect_material_property(base_color_param, "RGB", unreal.MaterialProperty.MP_BASE_COLOR)

#create a scalar parameter for emissive and connect it to the emissive property
emissive_param = material_edit_library.create_material_expression(master_material, unreal.MaterialExpressionScalarParameter, -584, 200)
material_edit_library.connect_material_property(emissive_param, "", unreal.MaterialProperty.MP_EMISSIVE_COLOR)

#create the normal parameter and connect it to the normal property
normal_param = material_edit_library.create_material_expression(master_material, unreal.MaterialExpressionTextureSampleParameter, -384, 50)
material_edit_library.connect_material_property(normal_param, "RGB", unreal.MaterialProperty.MP_NORMAL)

#create the ORM parameter and connect it to the ORM properties
orm_param = material_edit_library.create_material_expression(master_material, unreal.MaterialExpressionTextureSampleParameter, -384, 300)
material_edit_library.connect_material_property(orm_param, "R", unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)
material_edit_library.connect_material_property(orm_param, "G", unreal.MaterialProperty.MP_ROUGHNESS)
material_edit_library.connect_material_property(orm_param, "B", unreal.MaterialProperty.MP_METALLIC)

#set the parameter names
base_color_param.set_editor_property("parameter_name", "Base Color")
normal_param.set_editor_property("parameter_name", "Normal")
orm_param.set_editor_property("parameter_name", "ORM")
emissive_param.set_editor_property("parameter_name", "Emissive Intensity")

#set the parameter values
emissive_param.set_editor_property("default_value", 1.0)

#create a material instance
material_instance = asset_tools.create_asset("MI_GenericMaterial", materials_dir, unreal.MaterialInstanceConstant, unreal.MaterialInstanceConstantFactoryNew())

#set the parent material
material_instance.set_editor_property("parent", master_material)


