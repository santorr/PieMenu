import bpy
import bmesh


class CUSTOMPIE_OT_transpose_uvs_to_geometry(bpy.types.Operator):
    bl_idname = "custom_pie.transpose_uvs_to_geometry"
    bl_label = "Transpose uvs to geometry"
    bl_description = "Get the position of each vertex in uvs space and transpose it to world space to modify " \
                     "the geometry."
    bl_options = {'REGISTER', 'UNDO'}

    forward_axis: bpy.props.EnumProperty(
        items=(('x', "x", ""),
               ('y', "y", "")
               ), default='x', name='Forward axis')

    @staticmethod
    def initialize_selection(active_object, selected_objects):
        for ob in selected_objects:
            ob.select_set(True)
        bpy.context.view_layer.objects.active = active_object

    @staticmethod
    def get_uvs(obj):
        dictionary = []
        mesh_loops = obj.data.loops
        for i, mesh_loop in enumerate(mesh_loops):
            mesh_uv_loop = obj.data.uv_layers[0].data[i]
            index = mesh_loop.vertex_index
            pos_x, pos_y = (mesh_uv_loop.uv[0], mesh_uv_loop.uv[1])
            dictionary.append({"index": index, "uvs_x": pos_x, "uvs_y": pos_y})
        return dictionary

    def edit_geometry(self, data, obj):
        bm = bmesh.new()
        bm.from_mesh(obj.data)
        bm.verts.ensure_lookup_table()

        min_x = min(data, key=lambda x: x["uvs_x"])["uvs_x"]
        max_x = max(data, key=lambda x: x["uvs_x"])["uvs_x"]

        min_y = min(data, key=lambda y: y["uvs_y"])["uvs_y"]
        max_y = max(data, key=lambda y: y["uvs_y"])["uvs_y"]

        center = ((max_x - min_x)/2, (max_y - min_y)/2)

        offset = (min_x + center[0], min_y + center[1])

        for vertex in data:
            index = vertex["index"]
            x = vertex["uvs_x"]
            y = vertex["uvs_y"]
            world_pos = (0, x - offset[0], y - offset[1]) if self.forward_axis == 'x' else (x - offset[0], 0, y - offset[1])
            bm.verts[index].co = world_pos
        bm.to_mesh(obj.data)

    def execute(self, context):
        obj = context.view_layer.objects.active

        uvs_data = self.get_uvs(obj)
        self.edit_geometry(uvs_data, obj)

        return {'FINISHED'}
