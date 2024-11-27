import bpy


class MeshGenProperties(bpy.types.PropertyGroup):
    __annotations__ = {
        "prompt": bpy.props.StringProperty(
            name="Prompt",
            description="Prompt for the mesh generation.",
            default="Create a 3D obj file using the following description: a desk",
        ),
        "is_running": bpy.props.BoolProperty(
            name="Is Running",
            description="Whether the mesh generation is running.",
            default=False,
        ),
        "generated_text": bpy.props.StringProperty(
            name="Generated Text",
            description="The generated text.",
            default="",
        ),
        "cancelled": bpy.props.BoolProperty(
            name="Cancelled",
            description="Whether the mesh generation was cancelled.",
            default=False,
        ),
        "temperature": bpy.props.FloatProperty(
            name="Temperature",
            description="The temperature for the mesh generation.",
            default=0.9,
            min=0.0,
            max=1.0,
        ),
        "max_new_tokens": bpy.props.IntProperty(
            name="Max New Tokens",
            description="The maximum number of new tokens to generate.",
            default=4096,
            min=1024,
            max=16384,
        ),
        "vertices_generated": bpy.props.IntProperty(
            name="Vertices Generated",
            description="The number of vertices generated.",
            default=0,
        ),
        "faces_generated": bpy.props.IntProperty(
            name="Faces Generated",
            description="The number of faces generated.",
            default=0,
        ),
        "show_developer_options": bpy.props.BoolProperty(
            name="Show Developer Options",
            description="Whether to show developer options.",
            default=False,
        ),
    }
