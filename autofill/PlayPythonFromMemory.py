import bpy

import sys
import os


class VEIW3D_PT_PlayCommandsFromMemory(bpy.types.Operator):  # Declare my class
    """Play Commands Saved in Memory File"""
    bl_idname = "veiw3d.playfrommemory"  # Create an ID so that Blender can find the class
    bl_label = "PlayFromMemory"

    def execute(self, context):  # Create an Execute function for my class, used when blender's UI calls it
        dir = os.path.dirname(bpy.data.filepath)
        if not dir in sys.path:
            sys.path.append(dir)

        import testwritefile

        # this next part forces a reload in case you edit the source after you first start the blender session
        import imp
        imp.reload(testwritefile)

        testwritefile.ExecuteCopiedCode()

        # tell Blender we are done
        return {"FINISHED"}


# Create register and unregister functions, these allow blender to know where my class is

def register():
    bpy.utils.register_class(VEIW3D_PT_PlayCommandsFromMemory)


def unregister():
    bpy.utils.unregister_class(VEIW3D_PT_PlayCommandsFromMemory)


if __name__ == '__main__':
    register()
