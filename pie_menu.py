import bpy


class PIE_OT_SnapTarget(bpy.types.Operator):
    bl_idname = 'object.snaptargetvariable'
    bl_label = 'Snap Target Variable'
    variable: bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        context.scene.tool_settings.snap_target = self.variable
        return {'FINISHED'}


class PIE_OT_SnapElement(bpy.types.Operator):
    bl_idname = 'object.snapelementvariable'
    bl_label = 'Snap Element Variable'
    variable: bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        context.scene.tool_settings.snap_elements = self.variable
        return {'FINISHED'}


# MODIFIER
class PIE_MT_modifier(bpy.types.Menu):
    bl_label = 'Modifier'

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.operator('object.modifier_add', text='Weighted normal', icon='MOD_NORMALEDIT').type = 'WEIGHTED_NORMAL'
        pie.operator('object.modifier_add', text='Bevel', icon='MOD_BEVEL').type = 'BEVEL'
        pie.operator('object.modifier_add', text='Mirror', icon='MOD_MIRROR').type = 'MIRROR'
        pie.operator('object.modifier_add', text='Boolean', icon='MOD_BOOLEAN').type = 'BOOLEAN'
        pie.operator('object.modifier_add', text='Array', icon='MOD_ARRAY').type = 'ARRAY'


# VIEW
class PIE_MT_view(bpy.types.Menu):
    bl_label = 'View'

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.operator('view3d.view_axis', text='Left', icon='TRIA_LEFT').type = 'LEFT'
        pie.operator('view3d.view_axis', text='Right', icon='TRIA_RIGHT').type = 'RIGHT'
        pie.operator('view3d.view_axis', text='Bottom', icon='TRIA_DOWN').type = 'BOTTOM'
        pie.operator('view3d.view_axis', text='Top', icon='TRIA_UP').type = 'TOP'
        pie.operator('view3d.view_axis', text='Front').type = 'FRONT'
        pie.operator('view3d.view_axis', text='Back').type = 'BACK'


# SNAP
class PIE_MT_snap(bpy.types.Menu):
    bl_label = 'Snap'

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        col = pie.column()
        col.separator()
        col.label(text='SNAP TO :')
        col.prop(context.tool_settings, 'snap_elements', expand=True)

        col = pie.column()
        col.separator()
        col.label(text='SNAP WITH :')
        col.prop(context.tool_settings, 'snap_target', expand=True)
        pie.prop(context.tool_settings, 'use_snap')


# TRANSFORM ORIENTATION
class PIE_MT_transform(bpy.types.Menu):
    bl_label = 'Transform orientation'

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator_context = 'EXEC_DEFAULT'
        pie.operator('transform.select_orientation', text='World', icon='ORIENTATION_GLOBAL').orientation = 'GLOBAL'
        pie.operator('transform.select_orientation', text='Local', icon='ORIENTATION_LOCAL').orientation = 'LOCAL'
        pie.operator('transform.select_orientation', text='Normal', icon='ORIENTATION_NORMAL').orientation = 'NORMAL'
        pie.operator('transform.select_orientation', text='Gimbal', icon='ORIENTATION_GIMBAL').orientation = 'GIMBAL'
        pie.operator('transform.select_orientation', text='View', icon='ORIENTATION_VIEW').orientation = 'VIEW'
        pie.operator('transform.select_orientation', text='Cursor', icon='ORIENTATION_CURSOR').orientation = 'CURSOR'


class PIE_MT_object(bpy.types.Menu):
    bl_label = 'Object'

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        ''' Set pivot point '''
        pie.operator('custom_pie.pivot', text='Set pivot point', icon='VERTEXSEL')
        pie.operator('custom_pie.clean_normals', text='Clean normals', icon='VERTEXSEL')


# EDIT MENU
class PIE_MT_edit(bpy.types.Menu):
    bl_label = 'Edit'

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        col = pie.column()
        col.separator()
        col.label(text='MERGE')
        col.operator('mesh.merge', text='Merge at center', icon='VERTEXSEL').type = 'CENTER'
        col.operator('mesh.remove_doubles', text='Merge by distance', icon='VERTEXSEL')

        col = pie.column()
        col.separator()
        col.label(text='SEAM')
        col.operator('mesh.mark_seam', text='Mark seam', icon='MOD_EDGESPLIT').clear = False
        col.operator('mesh.mark_seam', text='Clear seam', icon='MOD_EDGESPLIT').clear = True

        col = pie.column()
        col.separator()
        col.label(text='SHARP')
        col.operator('mesh.mark_sharp', text='Mark sharp', icon='MOD_EDGESPLIT').clear = False
        col.operator('mesh.mark_sharp', text='Clear sharp', icon='MOD_EDGESPLIT').clear = True

        col = pie.column()
        col.separator()
        col.label(text='NORMALS')
        col.operator('mesh.flip_normals', text='Flip normals', icon='NORMALS_FACE')
        col.operator('mesh.normals_make_consistent', text='Recalculate outside', icon='NORMALS_FACE').inside = False
        col.operator('mesh.normals_make_consistent', text='Recalculate inside', icon='NORMALS_FACE').inside = True

        col = pie.column()
        col.separator()
        col.label(text='MODELING')
        col.operator('mesh.loopcut_slide', text='Edge loop', icon='OVERLAY')
        col.operator('mesh.bridge_edge_loops', text='Bridge faces', icon='OVERLAY')

        col = pie.column()
        col.separator()
        col.label(text='SELECT')
        col.operator('mesh.loop_multi_select', text='Select loop', icon='SELECT_SET').ring = False
        col.operator('mesh.loop_multi_select', text='Select ring', icon='SELECT_SET').ring = True


class PIE_MT_create(bpy.types.Menu):
    """ Create primitive objects """
    bl_label = 'Create'

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        col = pie.column()
        col.separator()
        col.label(text='Meshes')
        col.operator("mesh.primitive_plane_add", text='Plane', icon='MESH_PLANE')  # Plane
        col.operator("mesh.primitive_cube_add", text='Cube', icon='MESH_CUBE')  # Cube
        col.operator("mesh.primitive_uv_sphere_add", text='Sphere', icon='MESH_CIRCLE')    # Sphere
        col.operator("mesh.primitive_cylinder_add", text='Cylinder', icon='MESH_CYLINDER')   # Cylinder
        col.operator("mesh.primitive_cone_add", text='Cone', icon='MESH_CONE')   # Cone
        col.operator("mesh.primitive_torus_add", text='Torus', icon='MESH_TORUS')   # Torus


# VISUALIZATION MENU
class PIE_MT_overlay(bpy.types.Menu):
    bl_label = 'Overlay'

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.prop(context.space_data.overlay, 'show_extra_edge_length', icon='CURVE_PATH')
        pie.prop(context.space_data.overlay, 'show_face_orientation', icon='SNAP_VOLUME')
        pie.prop(context.space_data.overlay, 'show_wireframes', icon='SHADING_WIRE')
        pie.separator()


# MAIN PIE MENU
class PIE_MT_pie(bpy.types.Menu):
    bl_label = 'main menu'

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        column = pie.column()
        column.operator('wm.call_menu_pie', text='Edit Mode', icon='CUBE').name = 'PIE_MT_edit'
        column.operator('wm.call_menu_pie', text='Object Mode', icon='CUBE').name = 'PIE_MT_object'

        pie.operator('wm.call_menu_pie', text='View', icon='VIEW_CAMERA').name = 'PIE_MT_view'
        pie.operator('wm.call_menu_pie', text='Modifier', icon='MODIFIER_ON').name = 'PIE_MT_modifier'
        pie.operator('wm.call_menu_pie', text='Overlay', icon='OVERLAY').name = 'PIE_MT_overlay'
        pie.operator('wm.call_menu_pie', text='Create', icon='MATCUBE').name = 'PIE_MT_create'
        pie.operator('wm.call_menu_pie', text='Snap', icon='SNAP_ON').name = 'PIE_MT_snap'
        pie.operator('wm.call_menu_pie', text='Transform', icon='EMPTY_AXIS').name = 'PIE_MT_transform'
