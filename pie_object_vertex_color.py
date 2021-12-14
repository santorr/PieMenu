import bpy
import random


class CUSTOMPIE_OT_vertex_color(bpy.types.Operator):
    bl_idname = "custom_pie.vertex_color"
    bl_label = "Vertex color"
    bl_description = "Set vertex color on multiple objects."
    bl_options = {'REGISTER', 'UNDO'}

    vertex_color: bpy.props.FloatVectorProperty(name='Color', subtype='COLOR_GAMMA', size=4,
                                                default=(1.0, 1.0, 1.0, 1.0), min=0.0, max=1.0)
    random_color: bpy.props.BoolProperty(default=True, name='Random color')
    blend_channels: bpy.props.BoolProperty(default=True, name='Blend channels')
    
    red_channel: bpy.props.BoolProperty(default=True, name='Red')
    red_value_range: bpy.props.FloatVectorProperty(name='min/max', size=2, default=(0.0, 1.0), min=0.0, max=1.0)

    green_channel: bpy.props.BoolProperty(default=True, name='Green')
    green_value_range: bpy.props.FloatVectorProperty(name='min/max', size=2, default=(0.0, 1.0), min=0.0, max=1.0)

    blue_channel: bpy.props.BoolProperty(default=True, name='Blue')
    blue_value_range: bpy.props.FloatVectorProperty(name='min/max', size=2, default=(0.0, 1.0), min=0.0, max=1.0)

    alpha_channel: bpy.props.BoolProperty(default=True, name='Alpha')
    alpha_value_range: bpy.props.FloatVectorProperty(name='min/max', size=2, default=(0.0, 1.0), min=0.0, max=1.0)

    def return_color(self, channel):
        if channel == 'RED':
            if self.red_channel is True:
                return random.uniform(self.red_value_range[0], self.red_value_range[1])
            else:
                return 0.0
        elif channel == 'GREEN':
            if self.green_channel is True:
                return random.uniform(self.green_value_range[0], self.green_value_range[1])
            else:
                return 0.0
        elif channel == 'BLUE':
            if self.blue_channel is True:
                return random.uniform(self.blue_value_range[0], self.blue_value_range[1])
            else:
                return 0.0
        elif channel == 'ALPHA':
            if self.alpha_channel is True:
                return random.uniform(self.alpha_value_range[0], self.alpha_value_range[1])
            else:
                return 0.0

    def test(self):
        if self.red_channel and not self.green_channel and not self.blue_channel and not self.alpha_channel:
            """ R """
            return self.return_color('RED'), 0.0, 0.0, 0.0
        elif not self.red_channel and self.green_channel and not self.blue_channel and not self.alpha_channel:
            """ G """
            return 0.0, self.return_color('GREEN'), 0.0, 0.0
        elif not self.red_channel and not self.green_channel and self.blue_channel and not self.alpha_channel:
            """ B """
            return 0.0, 0.0, self.return_color('BLUE'), 0.0
        elif not self.red_channel and not self.green_channel and not self.blue_channel and self.alpha_channel:
            """ A """
            return 0.0, 0.0, 0.0, self.return_color('ALPHA')
        elif self.red_channel and self.green_channel and not self.blue_channel and not self.alpha_channel:
            """ RG """
            rand = random.randint(0, 1)
            if rand == 0:
                return self.return_color('RED'), 0.0, 0.0, 0.0
            else:
                return 0.0, self.return_color('GREEN'), 0.0, 0.0
        elif self.red_channel and not self.green_channel and self.blue_channel and not self.alpha_channel:
            """ RB """
            rand = random.randint(0, 1)
            if rand == 0:
                return self.return_color('RED'), 0.0, 0.0, 0.0
            else:
                return 0.0, 0.0, self.return_color('BLUE'), 0.0
        elif self.red_channel and not self.green_channel and not self.blue_channel and self.alpha_channel:
            """ RA """
            rand = random.randint(0, 1)
            if rand == 0:
                return self.return_color('RED'), 0.0, 0.0, 0.0
            else:
                return 0.0, 0.0, 0.0, self.return_color('ALPHA')
        elif not self.red_channel and self.green_channel and self.blue_channel and not self.alpha_channel:
            """ GB """
            rand = random.randint(0, 1)
            if rand == 0:
                return 0.0, self.return_color('GREEN'), 0.0, 0.0
            else:
                return 0.0, 0.0, self.return_color('BLUE'), 0.0
        elif not self.red_channel and not self.green_channel and self.blue_channel and self.alpha_channel:
            """ BA """
            rand = random.randint(0, 1)
            if rand == 0:
                return 0.0, 0.0, self.return_color('BLUE'), 0.0
            else:
                return 0.0, 0.0, 0.0, self.return_color('ALPHA')
        elif not self.red_channel and self.green_channel and not self.blue_channel and self.alpha_channel:
            """ GA """
            rand = random.randint(0, 1)
            if rand == 0:
                return 0.0, self.return_color('GREEN'), 0.0, 0.0
            else:
                return 0.0, 0.0, 0.0, self.return_color('ALPHA')
        elif self.red_channel and self.green_channel and self.blue_channel and not self.alpha_channel:
            """ RGB """
            rand = random.randint(0, 2)
            if rand == 0:
                return self.return_color('RED'), 0.0, 0.0, 0.0
            elif rand == 1:
                return 0.0, self.return_color('GREEN'), 0.0, 0.0
            else:
                return 0.0, 0.0, self.return_color('BLUE'), 0.0
        elif self.red_channel and self.green_channel and not self.blue_channel and self.alpha_channel:
            """ RGA """
            rand = random.randint(0, 2)
            if rand == 0:
                return self.return_color('RED'), 0.0, 0.0, 0.0
            elif rand == 1:
                return 0.0, self.return_color('GREEN'), 0.0, 0.0
            else:
                return 0.0, 0.0, 0.0, self.return_color('ALPHA')
        elif self.red_channel and not self.green_channel and self.blue_channel and self.alpha_channel:
            """ RBA """
            rand = random.randint(0, 2)
            if rand == 0:
                return self.return_color('RED'), 0.0, 0.0, 0.0
            elif rand == 1:
                return 0.0, 0.0, self.return_color('BLUE'), 0.0
            else:
                return 0.0, 0.0, 0.0, self.return_color('ALPHA')
        elif not self.red_channel and self.green_channel and self.blue_channel and self.alpha_channel:
            """ GBA """
            rand = random.randint(0, 2)
            if rand == 0:
                return 0.0, self.return_color('GREEN'), 0.0, 0.0
            elif rand == 1:
                return 0.0, 0.0, self.return_color('BLUE'), 0.0
            else:
                return 0.0, 0.0, 0.0, self.return_color('ALPHA')
        elif self.red_channel and self.green_channel and self.blue_channel and self.alpha_channel:
            """ RGBA """
            rand = random.randint(0, 3)
            if rand == 0:
                return self.return_color('RED'), 0.0, 0.0, 0.0
            elif rand == 1:
                return 0.0, self.return_color('GREEN'), 0.0, 0.0
            elif rand == 2:
                return 0.0, 0.0, self.return_color('BLUE'), 0.0
            else:
                return 0.0, 0.0, 0.0, self.return_color('ALPHA')

        else:
            return 1.0, 1.0, 1.0, 1.0

    def execute(self, context):
        """ Get selected objects """
        selected_objects = context.selected_objects
        """ Loop over all selected objects """
        for ob in selected_objects:
            """ Only process if the object is a visible mesh """
            if ob.type == 'MESH' and not ob.hide_get():
                """ Access to mesh data """
                mesh = ob.data
                """ Set the final color """
                if self.random_color:
                    if self.blend_channels:
                        """ Blend channels together """
                        final_color = (self.return_color('RED'), self.return_color('GREEN'), self.return_color('BLUE'), self.return_color('ALPHA'))
                    else:
                        final_color = self.test()
                else:
                    final_color = self.vertex_color

                """ Create a new vertex color channel """
                vertex_color_layer = mesh.vertex_colors.new()
                """ Set the new vertex color layer as active  """
                mesh.vertex_colors.active = vertex_color_layer

                """ Apply color on each faces """
                if len(vertex_color_layer.data) > 0:
                    i = 0
                    for poly in mesh.polygons:
                        for idx in poly.loop_indices:
                            vertex_color_layer.data[i].color = final_color
                            i += 1

        return {'FINISHED'}

##############################
#   REGISTRATION
##############################


def register():
    bpy.utils.register_class(CUSTOMPIE_OT_vertex_color)


def unregister():
    bpy.utils.unregister_class(CUSTOMPIE_OT_vertex_color)
