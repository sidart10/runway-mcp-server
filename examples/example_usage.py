"""
Example usage script for Runway MCP Server
Demonstrates all major features including Aleph video editing
"""

import asyncio
import json
from runway_mcp_server import (
    generate_image_gen4,
    generate_video_text_to_video,
    generate_video_image_to_video,
    edit_video_with_aleph,
    restyle_video,
    extend_video,
    upscale_video_4k,
    list_available_models,
    get_api_info
)


async def example_server_info():
    """Check server configuration and capabilities"""
    print("=" * 60)
    print("RUNWAY MCP SERVER INFO")
    print("=" * 60)
    
    info = await get_api_info()
    print(info)
    print()


async def example_list_models():
    """List all available models"""
    print("=" * 60)
    print("AVAILABLE MODELS")
    print("=" * 60)
    
    models = await list_available_models()
    print(models)
    print()


async def example_gen4_image():
    """Generate image with Gen-4"""
    print("=" * 60)
    print("EXAMPLE: Gen-4 Image Generation")
    print("=" * 60)
    
    result = await generate_image_gen4(
        prompt_text="A futuristic cityscape at sunset with flying cars and neon lights, cyberpunk aesthetic",
        ratio="1920:1080",
        wait_for_completion=False  # Don't wait for demo purposes
    )
    
    print(result)
    print()


async def example_gen4_image_with_reference():
    """Generate image with reference images for consistent characters"""
    print("=" * 60)
    print("EXAMPLE: Gen-4 Image with Reference")
    print("=" * 60)
    
    # Note: Replace with actual image URLs
    result = await generate_image_gen4(
        prompt_text="@Hero standing on a mountain peak at sunrise, epic hero pose",
        reference_images=[
            {
                "uri": "https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_(cropped).jpg",
                "tag": "Hero"
            }
        ],
        wait_for_completion=False
    )
    
    print(result)
    print()


async def example_text_to_video():
    """Generate video from text"""
    print("=" * 60)
    print("EXAMPLE: Text-to-Video")
    print("=" * 60)
    
    result = await generate_video_text_to_video(
        prompt_text="A majestic eagle soaring over snow-capped mountains at golden hour, cinematic drone shot with smooth camera movement",
        model="gen4_turbo",
        duration=5,
        ratio="1280:768",
        wait_for_completion=False
    )
    
    print(result)
    print()


async def example_image_to_video():
    """Animate an image"""
    print("=" * 60)
    print("EXAMPLE: Image-to-Video")
    print("=" * 60)
    
    result = await generate_video_image_to_video(
        prompt_image="https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_(cropped).jpg",
        prompt_text="Timelapse of clouds moving across the sky with changing light",
        keyframe_position="first",
        duration=5,
        wait_for_completion=False
    )
    
    print(result)
    print()


async def example_aleph_remove_object():
    """ALEPH: Remove objects from video"""
    print("=" * 60)
    print("EXAMPLE: Aleph - Remove Object")
    print("=" * 60)
    print("NOTE: This is the revolutionary video editing feature!")
    print()
    
    # Note: Replace with actual video URL
    result = await edit_video_with_aleph(
        input_video="https://example.com/your-video.mp4",
        prompt_text="Remove all people from the background of the scene",
        wait_for_completion=False
    )
    
    print(result)
    print()


async def example_aleph_add_object():
    """ALEPH: Add objects to video"""
    print("=" * 60)
    print("EXAMPLE: Aleph - Add Objects")
    print("=" * 60)
    
    result = await edit_video_with_aleph(
        input_video="https://example.com/your-video.mp4",
        prompt_text="Add spectacular fireworks exploding in the night sky",
        wait_for_completion=False
    )
    
    print(result)
    print()


async def example_aleph_change_camera():
    """ALEPH: Generate new camera angle"""
    print("=" * 60)
    print("EXAMPLE: Aleph - Change Camera Angle")
    print("=" * 60)
    
    result = await edit_video_with_aleph(
        input_video="https://example.com/your-video.mp4",
        prompt_text="Generate a reverse angle shot showing the opposite perspective",
        wait_for_completion=False
    )
    
    print(result)
    print()


async def example_aleph_restyle():
    """ALEPH: Transform video style with reference"""
    print("=" * 60)
    print("EXAMPLE: Aleph - Style Transfer")
    print("=" * 60)
    
    result = await edit_video_with_aleph(
        input_video="https://example.com/your-video.mp4",
        prompt_text="Restyle the video using the color palette and mood from the reference image",
        reference_image="https://example.com/style-reference.jpg",
        wait_for_completion=False
    )
    
    print(result)
    print()


async def example_aleph_lighting():
    """ALEPH: Change lighting"""
    print("=" * 60)
    print("EXAMPLE: Aleph - Change Lighting")
    print("=" * 60)
    
    result = await edit_video_with_aleph(
        input_video="https://example.com/your-video.mp4",
        prompt_text="Change to dramatic nighttime lighting with neon accents and shadows",
        wait_for_completion=False
    )
    
    print(result)
    print()


async def example_style_transfer():
    """Apply style to existing video"""
    print("=" * 60)
    print("EXAMPLE: Video Style Transfer")
    print("=" * 60)
    
    result = await restyle_video(
        input_video="https://example.com/your-video.mp4",
        style_prompt="Transform into a vibrant watercolor painting with impressionist brush strokes",
        structure_transformation=0.3,
        wait_for_completion=False
    )
    
    print(result)
    print()


async def example_extend_video():
    """Extend video duration"""
    print("=" * 60)
    print("EXAMPLE: Extend Video")
    print("=" * 60)
    
    result = await extend_video(
        input_video="https://example.com/your-video.mp4",
        extension_duration=10,
        prompt_text="Continue the character's walk through the forest",
        wait_for_completion=False
    )
    
    print(result)
    print()


async def example_upscale_4k():
    """Upscale video to 4K"""
    print("=" * 60)
    print("EXAMPLE: Upscale to 4K")
    print("=" * 60)
    
    result = await upscale_video_4k(
        input_video="https://example.com/your-video.mp4",
        wait_for_completion=False
    )
    
    print(result)
    print()


async def main():
    """Run all examples"""
    print("\n" + "=" * 60)
    print("RUNWAY MCP SERVER - EXAMPLE DEMONSTRATIONS")
    print("=" * 60 + "\n")
    
    try:
        # Server info
        await example_server_info()
        
        # List models
        await example_list_models()
        
        # Image generation
        await example_gen4_image()
        await example_gen4_image_with_reference()
        
        # Video generation
        await example_text_to_video()
        await example_image_to_video()
        
        # ALEPH VIDEO EDITING (Featured!)
        print("\n" + "🌟" * 30)
        print("   ALEPH VIDEO EDITING EXAMPLES")
        print("   (Revolutionary Video-to-Video Features!)")
        print("🌟" * 30 + "\n")
        
        await example_aleph_remove_object()
        await example_aleph_add_object()
        await example_aleph_change_camera()
        await example_aleph_restyle()
        await example_aleph_lighting()
        
        # Other video features
        await example_style_transfer()
        await example_extend_video()
        await example_upscale_4k()
        
        print("\n" + "=" * 60)
        print("EXAMPLES COMPLETE")
        print("=" * 60)
        print("\nNote: All examples used wait_for_completion=False")
        print("In production, set wait_for_completion=True to get final results")
        print("\nReplace example URLs with your actual video/image URLs")
        print("Make sure RUNWAY_API_KEY environment variable is set")
        
    except ValueError as e:
        print(f"\n❌ ERROR: {e}")
        print("\nPlease set your RUNWAY_API_KEY environment variable:")
        print("export RUNWAY_API_KEY='your_api_key_here'")
        print("\nGet your API key at: https://dev.runwayml.com")
    
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("Check your API key and internet connection")


if __name__ == "__main__":
    asyncio.run(main())
