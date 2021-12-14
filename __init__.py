bl_info = {
    'name': 'Pie Menu',
    'description': 'A pie menu to help production',
    'author': 'Jeremy Duchesne',
    'version': (1, 0),
    'blender': (2, 93, 1),
    'location': 'Space bar on your Viewport',
    'wiki_url': "https://github.com/santorr/PieMenu",
    'tracker_url': "https://github.com/santorr/PieMenu/issues",
    'support': "COMMUNITY",
    'category': 'Custom',
}

import bpy

from .settings import PIE_PT_setting_pie
from .pie_menu import PIE_OT_SnapTarget, \
    PIE_OT_SnapElement, \
    PIE_MT_view, \
    PIE_MT_snap, \
    PIE_MT_transform, \
    PIE_MT_edit, \
    PIE_MT_object, \
    PIE_MT_create, \
    PIE_MT_overlay, \
    PIE_MT_pie
from .pie_pivot_point import CUSTOMPIE_OT_pivot_point
from .pie_clean_normals import CUSTOMPIE_OT_clean_normals
from .pie_object_vertex_color import CUSTOMPIE_OT_vertex_color


modules_class = [
    PIE_OT_SnapTarget,
    PIE_OT_SnapElement,
    PIE_MT_view,
    PIE_MT_snap,
    PIE_MT_transform,
    PIE_MT_edit,
    PIE_MT_object,
    PIE_MT_create,
    PIE_MT_overlay,
    PIE_MT_pie,
    PIE_PT_setting_pie,
    CUSTOMPIE_OT_pivot_point,
    CUSTOMPIE_OT_clean_normals,
    CUSTOMPIE_OT_vertex_color
]

modulesNames = ['pie_menu', 'settings']
addonKeymap = []


def register():
    for cls in modules_class:
        bpy.utils.register_class(cls)

    # Keymap setup
    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        km = wm.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY')
        kmi = km.keymap_items.new(idname='wm.call_menu_pie', type='SPACE', value='PRESS', ctrl=False, shift=False)
        kmi.properties.name = 'PIE_MT_pie'
        addonKeymap.append((km, kmi))


def unregister():
    for cls in modules_class:
        bpy.utils.unregister_class(cls)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        for km, kmi in addonKeymap:
            km.keymap_items.remove(kmi)
    addonKeymap.clear()


if __name__ == "__main__":
    register()

    bpy.ops.wm.call_menu_pie(name='PIE_MT_pie')
