#!/usr/bin/env python3
"""
Roboflow Dataset Uploader for Edge AI M1 & M2.

This script uploads the local Roboflow YOLO dataset (datasets/Roboflow_M1_M2_V3)
directly to your Roboflow workspace and updates project configuration links.
"""

import os
import sys
import argparse
from roboflow import Roboflow

def upload_dataset(api_key, workspace_name, project_name):
    print(f"Connecting to Roboflow workspace '{workspace_name}'...")
    rf = Roboflow(api_key=api_key)
    workspace = rf.workspace(workspace_name)
    
    dataset_path = os.path.abspath("Roboflow_M1_M2_V3_Dataset.zip")
    if not os.path.exists(dataset_path):
        dataset_path = os.path.abspath("datasets/Roboflow_M1_M2_V3")

    print(f"Uploading dataset from: {dataset_path}")
    print(f"Target project: {project_name}")

    try:
        result = workspace.upload_dataset(
            dataset_path=dataset_path,
            project_name=project_name,
            dataset_format="yolov8",
            project_type="object-detection",
            num_workers=8,
            wait=True
        )
        print("Upload completed successfully!")
        project_url = f"https://app.roboflow.com/{workspace_name}/{project_name}"
        print(f"Roboflow Project URL: {project_url}")
        return project_url
    except Exception as e:
        print(f"Upload failed: {e}")
        return None

def update_repo_links(workspace_name, project_name, version="1"):
    old_urls = [
        "https://app.roboflow.com/satheesh-s-workspace/m1_m2/3",
        "https://app.roboflow.com/jaishanth-s-workspace/m1_m2/3",
        "satheesh-s-workspace/m1_m2",
        "satheesh-s-workspace"
    ]
    new_url = f"https://app.roboflow.com/{workspace_name}/{project_name}/{version}"
    new_proj = f"{workspace_name}/{project_name}"
    
    print(f"Updating repository references to {new_url}...")
    for root, dirs, files in os.walk('.'):
        if '.git' in dirs: dirs.remove('.git')
        for f in files:
            if f.endswith(('.md', '.yaml', '.txt')):
                p = os.path.join(root, f)
                try:
                    with open(p, 'r', encoding='utf-8') as fp:
                        content = fp.read()
                    updated = content
                    updated = updated.replace("https://app.roboflow.com/satheesh-s-workspace/m1_m2/3", new_url)
                    updated = updated.replace("satheesh-s-workspace/m1_m2", new_proj)
                    updated = updated.replace("satheesh-s-workspace", workspace_name)
                    if updated != content:
                        with open(p, 'w', encoding='utf-8') as fp:
                            fp.write(updated)
                        print(f"  Updated: {p}")
                except Exception as e:
                    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Upload dataset to Roboflow")
    parser.add_argument("--api-key", default=os.getenv("ROBOFLOW_API_KEY"), help="Roboflow API key")
    parser.add_argument("--workspace", default="satheesh-b-4hbyc", help="Roboflow workspace name")
    parser.add_argument("--project", default="edge_ai_m1_m2", help="Roboflow project name")
    parser.add_argument("--version", default="1", help="Roboflow dataset version")
    args = parser.parse_args()

    if not args.api_key:
        print("Error: Roboflow API key is required.")
        print("Usage: python upload_to_roboflow.py --api-key <YOUR_ROBOFLOW_API_KEY> [--workspace <WORKSPACE>] [--project <PROJECT>]")
        sys.exit(1)

    url = upload_dataset(args.api_key, args.workspace, args.project)
    if url:
        update_repo_links(args.workspace, args.project, args.version)
        print("\nAll repository references have been successfully updated.")
