import bpy

# bpy.ops.mesh.primitive_cube_add(location=(0,0,0))

Obj = bpy.context.active_object

bpy.ops.object.editmode_toggle()

bpy.ops.mesh.select_mode(type="FACE")
bpy.ops.mesh.select_all(action= 'SELECT')

bpy.ops.mesh.inset(thickness=.1, use_individual=True,)
bpy.ops.mesh.inset(thickness=.1, use_individual=True, depth= -.5)

bpy.ops.object.editmode_toggle()

mod3 = Obj.modifiers.new("Wireframe","WIREFRAME")
mod3.thickness = 0.1

mod = Obj.modifiers.new("Subsurf", 'SUBSURF')

mod.levels = 2
bpy.ops.object.shade_smooth()

mod1 = Obj.modifiers.new("Array", 'ARRAY')
mod1.count=8

mod2 = Obj.modifiers.new("Array", 'ARRAY')
mod2.relative_offset_displace[0]=0
mod2.relative_offset_displace[1]=1.1
mod2.count=8

mod3 = Obj.modifiers.new("Array", 'ARRAY')
mod3.relative_offset_displace[0]=0
mod3.relative_offset_displace[1]=0
mod3.relative_offset_displace[2]=1.2
mod3.count=8

# mod1 = Obj.modifiers.new("Array", 'ARRAY')
# mod1.count=8
#
# mod2 = Obj.modifiers.new("Array", 'ARRAY')
# mod2.relative_offset_displace[0]=0
# mod2.relative_offset_displace[1]=1
# mod2.count=8
#
# bpy.ops.object.modifier_apply(modifier="Array.001")
# bpy.ops.object.modifier_apply(modifier="Array")
#
# bpy.ops.object.editmode_toggle()
# bpy.ops.mesh.separate(type="LOOSE")
# bpy.ops.object.editmode_toggle()
#
# bpy.ops.object.randomize_transform(loc=(0, 0, 2))
#
# bpy.ops.object.editmode_toggle()
#
#
#
# #
