import bpy


class CUSTOMPIE_OT_clean_scene_materials(bpy.types.Operator):
    """ When you import a model as .fbx in a scene, you also import its materials. Then with multiples import
     you can stack a lot of materials, with increment (e.g : roof.001, roof.002, roof.003 ...).
     This operator will clean all materials on objects and scene. """

    bl_idname = "custom_pie.clean_scene_materials"
    bl_label = "Clean scene materials"
    bl_description = "Replace and remove all materials with '.' in his name."
    bl_options = {'REGISTER', 'UNDO'}

    def ShowMessageBox(self, message="", title="title", icon='INFO'):
        """ Display a message box """
        def draw(self, context):
            self.layout.label(text=message)
        bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)

    def get_search_material(self, search_name):
        """ Loop over all materials in the scene, and return a material by name, else return None """
        for material in bpy.data.materials:
            if material.name == search_name:
                return material
        return None

    def delete_materials(self):
        """ Delete all materials in the scene that contains '.' in its name and return the list of materials. """
        return [bpy.data.materials.remove(material) for material in bpy.data.materials if "." in material.name]

    def execute(self, context):
        num_created_materials = 0
        num_switch_materials = 0
        objects = [ob for ob in bpy.data.objects if ob.type == 'MESH']
        for ob in objects:
            object_materials = ob.material_slots
            for i in range(len(object_materials)):
                if "." in object_materials[i].name:
                    search_name = object_materials[i].name.split(".")[0]
                    find_material = self.get_search_material(search_name)
                    if find_material is not None:
                        object_materials[i].material = find_material
                        num_switch_materials += 1
                    else:
                        new_material = bpy.data.materials.new(name=search_name)
                        object_materials[i].material = new_material
                        num_created_materials += 1

        num_deleted_materials = len(self.delete_materials())

        self.ShowMessageBox(message=f"{num_created_materials} material(s) created, "
                                    f"{num_switch_materials} material(s) changed, "
                                    f"{num_deleted_materials} material(s) deleted.",
                            title="Clean materials")
        return {'FINISHED'}

##############################
#   REGISTRATION
##############################


def register():
    bpy.utils.register_class(CUSTOMPIE_OT_clean_scene_materials)


def unregister():
    bpy.utils.unregister_class(CUSTOMPIE_OT_clean_scene_materials)
