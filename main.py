
import os 

from pathlib import Path
import click 
import subprocess

@click.command()
@click.option(
    '-p',
    '--path',
    'path',
    type=click.Path(exists=True),
    required=True,
    help='ppt file path or directory which contains ppt files',
)
@click.option(
    '-o',
    '--output',
    'output',
    type=click.Path(),
    required=True,
    help='output directory',
)
def cli(path, output):
    
    def convert(source_fn, output_fn):
        subprocess.run(['./bin/extractor', '--path', source_fn, '--output', output_fn])
        
    os.makedirs(output, exist_ok=True)
    if not os.path.isdir(path):
        basename = os.path.basename(path)
        output_fn = os.path.join(output, f'{basename}.txt')
        convert(path, output_fn)
    else:
        for fn in Path(path).glob('*.ppt'):
            file_name = os.path.basename(fn)
            output_fn = os.path.join(output, f'{file_name}.txt')
            convert(str(fn), output_fn)


if __name__ == '__main__':
    cli()

