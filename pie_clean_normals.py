import math
import bpy


class CUSTOMPIE_OT_clean_normals(bpy.types.Operator):
    bl_idname = "custom_pie.clean_normals"
    bl_label = "Clean normals"
    bl_description = "Clean normals for all selected objects"
    bl_options = {'REGISTER', 'UNDO'}

    smooth_angle: bpy.props.IntProperty(default=30, min=0, max=180, name='Smooth angle')

    def initialize_selection(self, active_object, selected_objects):
        for ob in selected_objects:
            ob.select_set(True)
        bpy.context.view_layer.objects.active = active_object

    def execute(self, context):
        active_object = context.view_layer.objects.active
        selected_objects = bpy.context.selected_objects

        """ Loop over all selected objects """
        for ob in selected_objects:
            """ Only process if the object is a visible mesh """
            if ob.type == 'MESH' and not ob.hide_get():
                ob.select_set(state=True)
                """ You need to set this object as active object """
                if ob != context.view_layer.objects.active:
                    context.view_layer.objects.active = ob
                """ Clear existing normals """
                bpy.ops.mesh.customdata_custom_splitnormals_clear()
                """ Enable smooth shade """
                bpy.ops.object.shade_smooth()
                """ Enable auto smooth """
                ob.data.use_auto_smooth = True
                """ Set auto smooth value """
                ob.data.auto_smooth_angle = math.radians(self.smooth_angle)
                """ Get all modifiers of type (WEIGHTED_NORMAL) on this object """
                current_modifiers = [modifier for modifier in bpy.context.object.modifiers if modifier.type == 'WEIGHTED_NORMAL']
                """ If no modifier found, create one """
                if len(current_modifiers) == 0:
                    bpy.ops.object.modifier_add(type='WEIGHTED_NORMAL')
                    bpy.context.object.modifiers["WeightedNormal"].keep_sharp = True
                """ If one modifier found, update it """
                if len(current_modifiers) == 1:
                    bpy.context.object.modifiers[current_modifiers[0].name].keep_sharp = True
                else:
                    """ If more than one modifier found, delete all and create a new one """
                    for modifier in bpy.context.object.modifiers:
                        if modifier.type == 'WEIGHTED_NORMAL':
                            bpy.ops.object.modifier_remove(modifier=modifier.name)
                    bpy.ops.object.modifier_add(type='WEIGHTED_NORMAL')
                    bpy.context.object.modifiers["WeightedNormal"].keep_sharp = True

                """ Deselect the current object """
                ob.select_set(state=False)

        self.initialize_selection(active_object=active_object, selected_objects=selected_objects)
        return {'FINISHED'}

##############################
#   REGISTRATION
##############################


def register():
    bpy.utils.register_class(CUSTOMPIE_OT_clean_normals)


def unregister():
    bpy.utils.unregister_class(CUSTOMPIE_OT_clean_normals)
