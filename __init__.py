
# -*- coding: utf8 -*-
# python
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

bl_info = {"name": "Blend Modes Pie",
           "author": "CDMJ",
           "version": (1, 0, 0),
           "blender": (2, 80, 0),
           "location": "",
           "description": "Assistant to help toggle blend modes in Texture Paint",
           "warning": "Alpha version",
           "category": "3D View"}


import bpy
from bpy.types import Menu

#operators
class VIEW3D_OT_add_multiply(bpy.types.Operator):
    """Toggle Add Multiply"""
    bl_idname = "object.toggle_add_multiply"

    bl_label = "Toggle Add Multiply"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene
        #new code
        #brush = bpy.context.tool_settings.image_paint.brush.blend
        if bpy.context.tool_settings.image_paint.brush.blend != 'MUL':
            bpy.context.tool_settings.image_paint.brush.blend = 'MUL'
        else:
            bpy.context.tool_settings.image_paint.brush.blend = 'ADD'

        return {'FINISHED'}

class VIEW3D_OT_screen_mix(bpy.types.Operator):
    """Toggle Screen Mix"""
    bl_idname = "object.toggle_screen_mix"

    bl_label = "Toggle Screen Mix"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene
        #new code
        #brush = bpy.context.tool_settings.image_paint.brush.blend
        bpy.context.tool_settings.image_paint.brush.blend
        if bpy.context.tool_settings.image_paint.brush.blend != 'MIX':
            bpy.context.tool_settings.image_paint.brush.blend = 'MIX'
        else:
            bpy.context.tool_settings.image_paint.brush.blend = 'SCREEN'

        return {'FINISHED'}

class VIEW3D_OT_color_overlay(bpy.types.Operator):
    """Toggle Color Overaly"""
    bl_idname = "object.toggle_color_overlay"

    bl_label = "Toggle Color Overlay"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene
        #new code
        #brush = bpy.context.tool_settings.image_paint.brush.blend
        if bpy.context.tool_settings.image_paint.brush.blend != 'OVERLAY':
            bpy.context.tool_settings.image_paint.brush.blend= 'OVERLAY'
        else:
            bpy.context.tool_settings.image_paint.brush.blend = 'COLOR'

        return {'FINISHED'}

class VIEW3D_OT_add_erase_alpha(bpy.types.Operator):
    """Toggle Add/Erase Alpha"""
    bl_idname = "object.toggle_add_erase_alpha"

    bl_label = "Toggle Add/Erase Alpha"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene
        #new code
        #brush = bpy.context.tool_settings.image_paint.brush.blend
        if bpy.context.tool_settings.image_paint.brush.blend != 'ERASE_ALPHA':
            bpy.context.tool_settings.image_paint.brush.blend = 'ERASE_ALPHA'
        else:
            bpy.context.tool_settings.image_paint.brush.blend = 'ADD_ALPHA'

        return {'FINISHED'}

class VIEW3D_OT_hard_soft_light(bpy.types.Operator):
    """Toggle Hard/Soft Light"""
    bl_idname = "object.toggle_hard_soft_light"

    bl_label = "Toggle Hard/Soft Light"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene
        #new code
        #brush = bpy.context.tool_settings.image_paint.brush.blend
        if bpy.context.tool_settings.image_paint.brush.blend != 'HARDLIGHT':
            bpy.context.tool_settings.image_paint.brush.blend = 'HARDLIGHT'
        else:
            bpy.context.tool_settings.image_paint.brush.blend = 'SOFTLIGHT'

        return {'FINISHED'}

class VIEW3D_PIE_blendmode(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "Blend Mode"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()


        pie.operator("object.toggle_add_multiply", text='ADD/MULTIPLY',
            icon='RENDERLAYERS')
        pie.operator("object.toggle_screen_mix", text='SCREEN/MIX',
            icon='RENDERLAYERS')
        pie.operator("object.toggle_color_overlay", text='COLOR/OVERLAY',
            icon='RENDERLAYERS')
        pie.operator("object.toggle_add_erase_alpha", text='ADD/ERASE ALPHA',
            icon='RENDERLAYERS')
        pie.operator("object.toggle_hard_soft_light", text='HARD/SOFT LIGHT',
            icon='RENDERLAYERS')

_CLASSES = (
    VIEW3D_OT_add_multiply,
    VIEW3D_OT_screen_mix,
    VIEW3D_OT_color_overlay,
    VIEW3D_OT_add_erase_alpha,
    VIEW3D_OT_hard_soft_light
)


def register():
    for cls in _CLASSES:
        bpy.utils.register_class(cls)

    km_list = ['3D View']
    for i in km_list:
        sm = bpy.context.window_manager
        km = sm.keyconfigs.default.keymaps[i]
        kmi = km.keymap_items.new('wm.call_menu_pie', 'G', 'PRESS', shift=True)
        kmi.properties.name = "VIEW3D_PIE_blendmode"

def unregister():
    for cls in _CLASSES:
        bpy.utils.unregister_class(cls)

    km_list = ['3D View']
    for i in km_list:
        sm = bpy.context.window_manager
        km = sm.keyconfigs.default.keymaps[i]
        for kmi in (kmi for kmi in km.keymap_items \
                            if (kmi.idname == "VIEW3D_PIE_blendmode")):
            km.keymap_items.remove(kmi)
