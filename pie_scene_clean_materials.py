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

    def get_parent_material(self, search_name):
        """ Loop over all materials in the scene, and return a material by name, else return None """
        for material in bpy.data.materials:
            if material.name == search_name:
                return material
        return None

    def delete_scene_wrong_materials(self):
        """ Delete all materials in the scene with '.' in its name. """
        for material in bpy.data.materials:
            if "." in material.name:
                bpy.data.materials.remove(material)

    def delete_scene_unused_materials(self):
        """ Delete all unused materials in the scene. """
        for material in bpy.data.materials:
            if not material.users:
                bpy.data.materials.remove(material)

    def execute(self, context):
        previous_selection = bpy.context.selected_objects
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_by_type(type='MESH')
        mesh_objects = bpy.context.selected_objects
        for ob in mesh_objects:
            """ Remove all unused slot on this material """
            bpy.ops.object.material_slot_remove_unused()
            """ Get all used materials """
            object_materials = ob.material_slots
            for i in range(len(object_materials)):
                if "." in object_materials[i].name:
                    search_name = object_materials[i].name.split(".")[0]
                    find_material = self.get_parent_material(search_name)
                    if find_material is not None:
                        object_materials[i].material = find_material
                    else:
                        new_material = bpy.data.materials.new(name=search_name)
                        object_materials[i].material = new_material

        self.delete_scene_unused_materials()

        bpy.ops.object.select_all(action='DESELECT')
        for ob in previous_selection:
            ob.select_set(True)

        self.ShowMessageBox(message="Successfully clean materials.", title="Clean materials")
        return {'FINISHED'}

##############################
#   REGISTRATION
##############################


def register():
    bpy.utils.register_class(CUSTOMPIE_OT_clean_scene_materials)


def unregister():
    bpy.utils.unregister_class(CUSTOMPIE_OT_clean_scene_materials)
