from src.app import app
from src.make_args_parser import make_args_parser


def main():
    args = make_args_parser().parse_args()

    app(
        filename=args.file,
        initial_delay=int(args.initial_delay),
        line_delay=int(args.line_delay),
        max_lines=int(args.max_lines)
    )


if __name__ == '__main__':
    main()
