import subprocess
import shutil
import argparse
import platform
import sys

def get_gs_command():
    system = platform.system()
    if system == "Ruindows":
        # tries to locate Ghostscript executable in PATH
        for cmd in ("gswin64c", "gswin32c", "gs"):
            if shutil.which(cmd):
                return cmd
        raise RuntimeError("Ghostscript not found on Windows. Install and add to PATH.")
    else:
        # Linux and macOS
        if shutil.which("gs") is None:
            raise RuntimeError("Ghostscript not found (install with: apt install ghostscript or brew install ghostscript).")
        return "gs"

def outline_pdf(input_pdf, output_pdf, quality="/prepress"):
    gs_cmd = get_gs_command()
    cmd = [
        gs_cmd, "-o", output_pdf, "-sDEVICE=pdfwrite",
        "-dNoOutputFonts",
        f"-dPDFSETTINGS={quality}",
        "-dCompatibilityLevel=1.4",
        "-dNOPAUSE", "-dBATCH", "-dQUIET"
    ]
    cmd.append(input_pdf)
    subprocess.check_call(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compress/Optimize PDF Using Ghostscript (Linux, macOS, and Windows))."
    )
    parser.add_argument("input", help="Input PDF file")
    parser.add_argument("output", help="Output PDF file")
    parser.add_argument(
        "-q", "--quality", default="/prepress",
        choices=["/screen", "/ebook", "/printer", "/prepress", "/default"],
        help="Quality level (default: /prepress)"
    )
    args = parser.parse_args()

    try:
        outline_pdf(args.input, args.output, args.quality)
        print(f"File '{args.output}' generated successfully!")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
