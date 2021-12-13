import bpy


class CUSTOMPIE_OT_pivot_point(bpy.types.Operator):
    bl_idname = "custom_pie.pivot"
    bl_label = "Pivot point"
    bl_description = "Set the pivot point to the desired location."
    bl_options = {'REGISTER', 'UNDO'}

    forward_axis: bpy.props.EnumProperty(
        items=(('x', "x", ""),
               ('y', "y", "")
               ), default='x', name='Forward axis')
    pivot_location: bpy.props.EnumProperty(
        items=(('center/center', "center/center", ""),
               ('center/back', "center/back", ""),
               ('center/bottom', "center/bottom", "")
               ), default='center/center', name='Pivot location')
    move_to_world: bpy.props.BoolProperty(default=False, name='Move object to world')

    def initialize_selection(self, active_object, selected_objects):
        for ob in selected_objects:
            ob.select_set(True)
        bpy.context.view_layer.objects.active = active_object

    def execute(self, context):
        active_object = context.view_layer.objects.active
        selected_objects = context.selected_objects

        """ Loop over all selected objects """
        for ob in selected_objects:
            """ Only process if the object is a visible mesh """
            if ob.type == 'MESH' and not ob.hide_get():
                ob.select_set(state=True)
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')

                """ Set the cursor location to the center/bottom of the object """
                if self.pivot_location == "center/bottom":
                    bpy.context.scene.cursor.location = (ob.location.x, ob.location.y, ob.location.z - ob.dimensions.z/2)

                """ Set the cursor location to the center/back of the object """
                if self.pivot_location == 'center/back':
                    if self.forward_axis == 'x':
                        bpy.context.scene.cursor.location = (ob.location.x - ob.dimensions.x / 2, ob.location.y, ob.location.z)
                    elif self.forward_axis == 'y':
                        bpy.context.scene.cursor.location = (ob.location.x, ob.location.y - ob.dimensions.x / 2, ob.location.z)

                """ Set the cursor location to the center of the object """
                if self.pivot_location == "center/center":
                    bpy.context.scene.cursor.location = (ob.location.x, ob.location.y, ob.location.z)

                """ Set the pivot point for this object at the cursor location """
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

                """ Set the object position to 0, 0, 0 """
                if self.move_to_world:
                    ob.location[0] = 0
                    ob.location[1] = 0
                    ob.location[2] = 0

                """ Deselect the current object """
                ob.select_set(state=False)

        self.initialize_selection(active_object=active_object, selected_objects=selected_objects)
        return {'FINISHED'}

##############################
#   REGISTRATION
##############################


def register():
    bpy.utils.register_class(CUSTOMPIE_OT_pivot_point)


def unregister():
    bpy.utils.unregister_class(CUSTOMPIE_OT_pivot_point)
