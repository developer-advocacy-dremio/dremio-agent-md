import os

def generate_index(root_dir):
    with open(os.path.join(root_dir, 'README.md'), 'w') as f:
        f.write("# Dremioframe Documentation Index\n\n")
        
        for dirpath, dirnames, filenames in os.walk(root_dir):
            # Skip the root README itself to avoid self-reference loop or weirdness
            if dirpath == root_dir:
                rel_path = ""
            else:
                rel_path = os.path.relpath(dirpath, root_dir)
                f.write(f"\n## {rel_path.replace(os.sep, ' / ').title()}\n\n")
            
            for filename in sorted(filenames):
                if filename == 'README.md' and dirpath == root_dir:
                    continue
                if not filename.endswith('.md'):
                    continue
                    
                file_rel_path = os.path.join(rel_path, filename)
                title = filename.replace('.md', '').replace('_', ' ').title()
                f.write(f"- [{title}]({file_rel_path})\n")

if __name__ == "__main__":
    generate_index("dremio_sitemaps/dremioframe")
