import os

def is_ignored(path, names):
    ignored_dirs = {
        'node_modules', '.next', '.git', '.vscode', '.idea', 'dist', 'build', 'coverage', 
        '.pnpm-store', 'media', 'public', '.cursor', 'generated', 'swagger'
    }
    ignored_files = {
        'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml', 'payload-types.ts', 
        'next-env.d.ts', 'tsconfig.tsbuildinfo', '.DS_Store', 'Api.ts'
    }
    
    # Check if the path itself is in ignored_dirs (for top-level checks)
    if os.path.basename(path) in ignored_dirs:
        return True
        
    return False

def should_count_file(filename):
    extensions = {
        '.ts', '.tsx', '.js', '.jsx', '.css', '.scss', '.py', '.html', '.json'
    }
    # Exclude specific files
    if filename in {'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml', 'payload-types.ts', 'next-env.d.ts', 'tsconfig.tsbuildinfo', 'Api.ts'}:
        return False
        
    _, ext = os.path.splitext(filename)
    return ext in extensions

def count_lines_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return sum(1 for _ in f)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return 0

def count_code(root_dir):
    """
    Counts lines of code in the given directory, excluding auto-generated and non-code files.
    
    Exclusions:
    - Directories: node_modules, .next, .git, .vscode, .idea, dist, build, coverage, .pnpm-store, media, public, .cursor, generated, swagger
    - Files: package-lock.json, yarn.lock, pnpm-lock.yaml, payload-types.ts, next-env.d.ts, tsconfig.tsbuildinfo, .DS_Store, Api.ts
    - Extensions: Only counts .ts, .tsx, .js, .jsx, .css, .scss, .py, .html, .json
    """
    total_lines = 0
    file_counts = {}
    
    print(f"Scanning {root_dir}...")
    
    for root, dirs, files in os.walk(root_dir):
        # Modify dirs in-place to skip ignored directories
        dirs[:] = [d for d in dirs if d not in {
            'node_modules', '.next', '.git', '.vscode', '.idea', 'dist', 'build', 'coverage', 
            '.pnpm-store', 'media', '.cursor', 'generated', 'swagger'
        }]
        
        for file in files:
            if should_count_file(file):
                filepath = os.path.join(root, file)
                lines = count_lines_in_file(filepath)
                total_lines += lines
                file_counts[filepath] = lines
                # print(f"{filepath}: {lines}")

    return total_lines, file_counts

def main():
    root_dirs = ['lunarety-v2', 'lunarety-v2-website']
    # Get the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to find the project root
    base_path = os.path.abspath(os.path.join(script_dir, '..'))
    
    grand_total = 0
    
    for d in root_dirs:
        path = os.path.join(base_path, d)
        if os.path.exists(path):
            lines, _ = count_code(path)
            print(f"Total lines in {d}: {lines}")
            grand_total += lines
        else:
            print(f"Directory {d} not found.")
            
    print(f"\nGrand Total Lines of Code: {grand_total}")

if __name__ == "__main__":
    main()
