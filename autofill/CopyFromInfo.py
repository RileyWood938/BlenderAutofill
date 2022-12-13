import bpy

import pyperclip as pc


def ProcessClipboard():
    writeFile = open(r'testwritefile.py', 'w')
    a = pc.paste()
    b = a.split('\r\n')

    writeFile.write('import bpy \n'
                    '\n'
                    'def ExecuteCopiedCode(): \n'
                    '\n')

    lineNumberOfFirstBreak = 0

    for i in range(len(b)):
        currentLine = b[-(i + 1)]
        print('line ' + str(i) + ' = ' + str(currentLine))
        if currentLine in ['bpy.ops.text.run_script()', 'bpy.ops.object.editmode_toggle()']:
            lineNumberOfFirstBreak = i + 1
            break
    print(-lineNumberOfFirstBreak)
    print(b[-lineNumberOfFirstBreak])

    if lineNumberOfFirstBreak in [0,1]:
        writeFile.write('   ' + 'pass' + '\n')
    else:
        for i in range(lineNumberOfFirstBreak):
            if i != 0:
                writeFile.write('   ' + b[-lineNumberOfFirstBreak + i] + '\n')

    writeFile.close()


class INFO_OT_CopyFromInfo(bpy.types.Operator):  # Declare my class
    """Copy All Entries From Info"""
    bl_idname = "info.makereplayable"  # Create an ID so that Blender can find the class
    bl_label = "CopyInfoToFile"

    def execute(self, context):  # Create an Execute function for my class, used when blender's UI calls it
        for window in bpy.context.window_manager.windows:
            screen = window.screen
            for area in screen.areas:
                if area.type == 'INFO':
                    override = {'window': window, 'screen': screen, 'area': area}
                    bpy.ops.info.select_all(override, action='SELECT')
                    bpy.ops.info.report_copy(override)
                    break

        # Write what is in the clipboard from the last script run or mode toggle on down

        ProcessClipboard()

        # tell Blender we are done
        return {"FINISHED"}


# Create register and unregister functions, these allow blender to know where my class is

def register():
    bpy.utils.register_class(INFO_OT_CopyFromInfo)


def unregister():
    bpy.utils.unregister_class(INFO_OT_CopyFromInfo)


if __name__ == '__main__':
    register()





