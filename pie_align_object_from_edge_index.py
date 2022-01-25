import bpy


class CUSTOMPIE_OT_align_object_from_edge_index(bpy.types.Operator):
    bl_idname = "custom_pie.align_object_from_edge_index"
    bl_label = "Align object form edge index"
    bl_description = "You can align the object rotation based on an edge index."
    bl_options = {'REGISTER', 'UNDO'}

    move_to_world: bpy.props.IntProperty(default=1, name='Edge index')

    def initialize_selection(self, active_object, selected_objects):
        for ob in selected_objects:
            ob.select_set(True)
        bpy.context.view_layer.objects.active = active_object

    def execute(self, context):

        return {'FINISHED'}

##############################
#   REGISTRATION
##############################


def register():
    bpy.utils.register_class(CUSTOMPIE_OT_align_object_from_edge_index)


def unregister():
    bpy.utils.unregister_class(CUSTOMPIE_OT_align_object_from_edge_index)
