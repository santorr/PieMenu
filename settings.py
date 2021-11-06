import bpy


class PIE_PT_setting_pie(bpy.types.AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        layout = self.layout
        layout.label(text='Information about the pie menu', icon='ERROR')
        layout.label(text='By default, the shortcut to use this pie menu is the space bar.')
