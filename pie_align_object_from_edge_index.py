import bpy
import math

class CUSTOMPIE_OT_align_object_from_edge_index(bpy.types.Operator):
    bl_idname = "custom_pie.align_object_from_edge_index"
    bl_label = "Align object form edge index"
    bl_description = "You can align the object rotation based on an edge index."
    bl_options = {'REGISTER', 'UNDO'}

    edge_index: bpy.props.IntProperty(default=1, min=0, name='Edge index')

    @classmethod
    def poll(cls, context):
        return context.active_object != None and len(bpy.context.selected_objects) > 0

    def initialize_selection(self, active_object, selected_objects):
        for ob in selected_objects:
            ob.select_set(True)
        bpy.context.view_layer.objects.active = active_object

    def execute(self, context):
        selected_objects = bpy.context.selected_objects

        for ob in selected_objects:
            data = ob.data
            """ Get edges and vertices data for this object """
            edges = data.edges
            verts = data.vertices
            """ Get both vertices connected to this edge """
            edge_vertices = edges[self.edge_index].vertices
            """ Store vertices as variable """
            pos_vert_0 = verts[edge_vertices[0]].co
            pos_vert_1 = verts[edge_vertices[1]].co

            rad_angle = math.atan2(-(pos_vert_0[1] - pos_vert_1[1]), (pos_vert_0[0] - pos_vert_1[0]))
            ob.rotation_euler[2] = rad_angle

        return {'FINISHED'}

##############################
#   REGISTRATION
##############################


def register():
    bpy.utils.register_class(CUSTOMPIE_OT_align_object_from_edge_index)


def unregister():
    bpy.utils.unregister_class(CUSTOMPIE_OT_align_object_from_edge_index)
