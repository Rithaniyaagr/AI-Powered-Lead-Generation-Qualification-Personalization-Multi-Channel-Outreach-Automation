"""
IncuBrix Option 3 Runner (Root Wrapper)
Executes Option 3 AEO, SEO & GEO Visibility Engine from root.
"""

import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from option_3_aeo_seo_geo.run_visibility_tracker import run_pipeline, ContentBriefGenerator

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="IncuBrix Option 3 Visibility Engine")
    parser.add_argument("--scale", type=int, default=100, help="Number of questions to audit")
    parser.add_argument("--brief", type=str, help="Generate brief for a query")
    args = parser.parse_args()

    if args.brief:
        print(ContentBriefGenerator.generate_brief(args.brief))
    else:
        run_pipeline(scale=args.scale)
