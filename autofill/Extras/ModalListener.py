import bpy


class ListenerAttempt1(bpy.types.Operator):
    """My First Modal Operator"""
    bl_idname = 'wm.listener_attempt'
    bl_label = 'First Try at Listening'

    def modal(self, context, event):

        if event.type == 'MOUSEMOVE':
            print(f"MOUSEMOVE: {event.mouse_x}, {event.mouse_y}")

        elif event.type == 'LEFTMOUSE':
            print(f"LEFT {event.value} at {event.mouse_x}, {event.mouse_y}")

        elif event.type in {'ESC'}:
            print(f"{event.type} {event.value} -- STOPPING")
            return {'FINISHED'}

        return {'PASS_THROUGH'}

    def execute(self, context):
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}


def menu_func(self, context):
    self.layout.operator(ModalTimerOperator.bl_idname, text=ModalTimerOperator.bl_label)


def register():
    bpy.utils.register_class(ListenerAttempt1)
    bpy.types.VIEW3D_MT_view.append(menu_func)


# Register and add to the "view" menu (required to also use F3 search "Modal Timer Operator" for quick access)
def unregister():
    bpy.utils.unregister_class(ListenerAttempt1)
    bpy.types.VIEW3D_MT_view.remove(menu_func)


if __name__ == "__main__":
    register()
