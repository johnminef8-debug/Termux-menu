#!/usr/bin/env python3
"""
HamsterLin - Termux Graphical Desktop Environment
Main entry point for the application
"""

import sys
import os
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent))

from src.ui.desktop import HamsterLinDesktop

def main():
    """Main application entry point"""
    app = HamsterLinDesktop()
    sys.exit(app.run())

if __name__ == "__main__":
    main()
