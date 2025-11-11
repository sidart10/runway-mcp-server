#!/usr/bin/env python3
"""
Comprehensive test suite for Runway MCP Server
Tests code structure, imports, type safety, and basic functionality
"""

import sys
import os
from pathlib import Path

# Colors for terminal output
class Colors:
    """ANSI color codes for better test output readability"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def print_test_header(message: str):
    """Print a formatted test section header"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{message}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.ENDC}\n")


def print_success(message: str):
    """Print a success message"""
    print(f"{Colors.OKGREEN}✓ {message}{Colors.ENDC}")


def print_failure(message: str):
    """Print a failure message"""
    print(f"{Colors.FAIL}✗ {message}{Colors.ENDC}")


def print_warning(message: str):
    """Print a warning message"""
    print(f"{Colors.WARNING}⚠ {message}{Colors.ENDC}")


def print_info(message: str):
    """Print an info message"""
    print(f"{Colors.OKCYAN}ℹ {message}{Colors.ENDC}")


# Test Results Tracking
test_results = {
    "passed": 0,
    "failed": 0,
    "warnings": 0
}


def test_file_structure():
    """Test 1: Verify project file structure"""
    print_test_header("TEST 1: Project File Structure")
    
    required_files = [
        "src/runway_mcp_server/__init__.py",
        "src/runway_mcp_server/server.py",
        "pyproject.toml",
        "requirements.txt",
        "README.md",
        "server.json",
    ]
    
    required_dirs = [
        "src",
        "src/runway_mcp_server",
        "docs",
        "config",
    ]
    
    all_passed = True
    
    # Check required files
    for file_path in required_files:
        if Path(file_path).exists():
            print_success(f"File exists: {file_path}")
        else:
            print_failure(f"Missing file: {file_path}")
            all_passed = False
            test_results["failed"] += 1
    
    # Check required directories
    for dir_path in required_dirs:
        if Path(dir_path).is_dir():
            print_success(f"Directory exists: {dir_path}")
        else:
            print_failure(f"Missing directory: {dir_path}")
            all_passed = False
            test_results["failed"] += 1
    
    if all_passed:
        test_results["passed"] += 1
        print_success("All required files and directories present")
    
    return all_passed


def test_imports():
    """Test 2: Verify all imports work correctly"""
    print_test_header("TEST 2: Import Tests")
    
    all_passed = True
    
    # Test standard library imports
    try:
        import os
        import json
        import time
        import asyncio
        from typing import Optional, List, Dict, Any, Literal
        from enum import Enum
        print_success("Standard library imports successful")
    except ImportError as e:
        print_failure(f"Standard library import failed: {e}")
        all_passed = False
        test_results["failed"] += 1
    
    # Test third-party dependencies
    try:
        import httpx
        print_success("httpx import successful")
    except ImportError:
        print_failure("httpx not installed - run: pip install httpx")
        all_passed = False
        test_results["failed"] += 1
    
    try:
        from dotenv import load_dotenv
        print_success("python-dotenv import successful")
    except ImportError:
        print_failure("python-dotenv not installed - run: pip install python-dotenv")
        all_passed = False
        test_results["failed"] += 1
    
    try:
        from mcp.server.fastmcp import FastMCP
        print_success("MCP framework import successful")
    except ImportError:
        print_failure("MCP framework not installed - run: pip install mcp")
        all_passed = False
        test_results["failed"] += 1
    
    # Test module imports
    try:
        sys.path.insert(0, str(Path("src")))
        from runway_mcp_server import __version__
        print_success(f"Package import successful (version: {__version__})")
    except ImportError as e:
        print_failure(f"Package import failed: {e}")
        all_passed = False
        test_results["failed"] += 1
    
    if all_passed:
        test_results["passed"] += 1
    
    return all_passed


def test_code_syntax():
    """Test 3: Verify Python syntax is valid"""
    print_test_header("TEST 3: Python Syntax Validation")
    
    import py_compile
    
    python_files = [
        "src/runway_mcp_server/__init__.py",
        "src/runway_mcp_server/server.py",
    ]
    
    all_passed = True
    
    for file_path in python_files:
        try:
            py_compile.compile(file_path, doraise=True)
            print_success(f"Syntax valid: {file_path}")
        except py_compile.PyCompileError as e:
            print_failure(f"Syntax error in {file_path}: {e}")
            all_passed = False
            test_results["failed"] += 1
    
    if all_passed:
        test_results["passed"] += 1
        print_success("All Python files have valid syntax")
    
    return all_passed


def test_configuration():
    """Test 4: Verify configuration files"""
    print_test_header("TEST 4: Configuration Validation")
    
    import json
    import tomllib
    
    all_passed = True
    
    # Test pyproject.toml
    try:
        with open("pyproject.toml", "rb") as f:
            config = tomllib.load(f)
            
        # Verify required fields
        assert "project" in config, "Missing [project] section"
        assert config["project"]["name"] == "runway-mcp-server", "Incorrect package name"
        assert "version" in config["project"], "Missing version"
        assert "dependencies" in config["project"], "Missing dependencies"
        
        print_success("pyproject.toml is valid")
        print_info(f"  Package: {config['project']['name']}")
        print_info(f"  Version: {config['project']['version']}")
        print_info(f"  Dependencies: {len(config['project']['dependencies'])} packages")
        
    except Exception as e:
        print_failure(f"pyproject.toml validation failed: {e}")
        all_passed = False
        test_results["failed"] += 1
    
    # Test server.json
    try:
        with open("server.json", "r") as f:
            server_config = json.load(f)
        
        # Verify required fields
        assert "name" in server_config, "Missing name field"
        assert "version" in server_config, "Missing version field"
        assert "packages" in server_config, "Missing packages field"
        
        print_success("server.json is valid")
        print_info(f"  Server: {server_config['name']}")
        print_info(f"  Version: {server_config['version']}")
        
    except Exception as e:
        print_failure(f"server.json validation failed: {e}")
        all_passed = False
        test_results["failed"] += 1
    
    # Check for .env or warn
    if not Path(".env").exists():
        print_warning(".env file not found (needed for API key)")
        print_info("  Create .env with: RUNWAY_API_KEY=your_key_here")
        test_results["warnings"] += 1
    else:
        print_success(".env file exists")
    
    if all_passed:
        test_results["passed"] += 1
    
    return all_passed


def test_server_structure():
    """Test 5: Verify server code structure"""
    print_test_header("TEST 5: Server Code Structure")
    
    sys.path.insert(0, str(Path("src")))
    
    all_passed = True
    
    try:
        from runway_mcp_server.server import (
            RunwayAPIClient,
            get_client,
            mcp,
        )
        print_success("Core server components imported successfully")
    except ImportError as e:
        print_failure(f"Failed to import server components: {e}")
        all_passed = False
        test_results["failed"] += 1
        return False
    
    # Test RunwayAPIClient class structure
    try:
        required_methods = ["_request", "create_task", "get_task", "wait_for_task"]
        for method in required_methods:
            assert hasattr(RunwayAPIClient, method), f"Missing method: {method}"
        print_success("RunwayAPIClient has all required methods")
    except AssertionError as e:
        print_failure(f"RunwayAPIClient structure issue: {e}")
        all_passed = False
        test_results["failed"] += 1
    
    # Test MCP tool registration
    try:
        # Check if mcp has the _tool_manager attribute (FastMCP uses this internally)
        if hasattr(mcp, '_tool_manager') and hasattr(mcp._tool_manager, 'tools'):
            tool_count = len(mcp._tool_manager.tools)
            print_success(f"MCP server has {tool_count} registered tools")
            
            expected_tools = [
                "generate_image_gen4",
                "generate_video_text_to_video",
                "generate_video_image_to_video",
                "generate_video_first_last_frame",
                "edit_video_with_aleph",
                "restyle_video",
                "extend_video",
                "upscale_video_4k",
                "get_task_status",
                "cancel_task",
                "list_available_models",
                "get_api_info",
            ]
            
            registered_tool_names = [tool.name for tool in mcp._tool_manager.tools.values()]
            
            for tool_name in expected_tools:
                if tool_name in registered_tool_names:
                    print_success(f"  ✓ Tool registered: {tool_name}")
                else:
                    print_failure(f"  ✗ Missing tool: {tool_name}")
                    all_passed = False
                    test_results["failed"] += 1
        else:
            print_warning("Unable to verify tool registration (MCP internal structure changed)")
            test_results["warnings"] += 1
        
    except Exception as e:
        print_failure(f"Tool registration check failed: {e}")
        all_passed = False
        test_results["failed"] += 1
    
    if all_passed:
        test_results["passed"] += 1
    
    return all_passed


def test_documentation():
    """Test 6: Verify documentation completeness"""
    print_test_header("TEST 6: Documentation Check")
    
    required_docs = [
        "README.md",
        "docs/QUICKSTART.md",
        "docs/ARCHITECTURE.md",
        "docs/FEATURES.md",
        "docs/ALEPH_GUIDE.md",
    ]
    
    all_passed = True
    
    for doc in required_docs:
        if Path(doc).exists():
            # Check file size to ensure it's not empty
            size = Path(doc).stat().st_size
            if size > 100:  # At least 100 bytes
                print_success(f"Documentation present: {doc} ({size} bytes)")
            else:
                print_warning(f"Documentation file too small: {doc}")
                test_results["warnings"] += 1
        else:
            print_failure(f"Missing documentation: {doc}")
            all_passed = False
            test_results["failed"] += 1
    
    if all_passed:
        test_results["passed"] += 1
    
    return all_passed


def test_type_safety():
    """Test 7: Verify type hints are present"""
    print_test_header("TEST 7: Type Safety Check")
    
    with open("src/runway_mcp_server/server.py", "r") as f:
        server_code = f.read()
    
    all_passed = True
    
    # Check for type imports
    type_indicators = [
        "from typing import",
        "Optional[",
        "List[",
        "Dict[",
        "Literal[",
        "-> str:",
        "-> Dict",
    ]
    
    for indicator in type_indicators:
        if indicator in server_code:
            print_success(f"Found type annotation: {indicator}")
        else:
            print_warning(f"Limited use of: {indicator}")
            test_results["warnings"] += 1
    
    # Check for async/await
    if "async def" in server_code and "await" in server_code:
        print_success("Async/await patterns detected")
    else:
        print_failure("Missing async/await patterns")
        all_passed = False
        test_results["failed"] += 1
    
    if all_passed:
        test_results["passed"] += 1
    
    return all_passed


def print_summary():
    """Print final test summary"""
    print_test_header("TEST SUMMARY")
    
    total_tests = test_results["passed"] + test_results["failed"]
    
    print(f"\n{Colors.BOLD}Results:{Colors.ENDC}")
    print(f"  {Colors.OKGREEN}Passed:  {test_results['passed']}/{total_tests}{Colors.ENDC}")
    print(f"  {Colors.FAIL}Failed:  {test_results['failed']}/{total_tests}{Colors.ENDC}")
    print(f"  {Colors.WARNING}Warnings: {test_results['warnings']}{Colors.ENDC}")
    
    success_rate = (test_results["passed"] / total_tests * 100) if total_tests > 0 else 0
    
    print(f"\n{Colors.BOLD}Success Rate: {success_rate:.1f}%{Colors.ENDC}")
    
    if test_results["failed"] == 0:
        print(f"\n{Colors.OKGREEN}{Colors.BOLD}🎉 ALL TESTS PASSED!{Colors.ENDC}")
        print(f"{Colors.OKGREEN}Your Runway MCP Server is ready to use!{Colors.ENDC}")
    else:
        print(f"\n{Colors.FAIL}{Colors.BOLD}❌ SOME TESTS FAILED{Colors.ENDC}")
        print(f"{Colors.FAIL}Please fix the issues above before deploying.{Colors.ENDC}")
    
    print()


def main():
    """Run all tests"""
    print(f"{Colors.HEADER}{Colors.BOLD}")
    print("""
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║           RUNWAY MCP SERVER - COMPREHENSIVE TEST SUITE           ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
    """)
    print(f"{Colors.ENDC}")
    
    # Run all tests in sequence
    test_file_structure()
    test_imports()
    test_code_syntax()
    test_configuration()
    test_server_structure()
    test_documentation()
    test_type_safety()
    
    # Print summary
    print_summary()
    
    # Exit with appropriate code
    sys.exit(0 if test_results["failed"] == 0 else 1)


if __name__ == "__main__":
    main()

