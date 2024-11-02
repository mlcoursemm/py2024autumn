import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', '-e', help='Number of training epochs', type=int, default=100, required=True)
    parser.add_argument('--opt', help='Optimizer algorithm', type=str, choices=['sgd', 'adam'])
    parser.add_argument('--learning-rate', help='Learning rate', type=float, default=1e-3)
    args = parser.parse_args()

    print(f"Epochs number: {args.epochs}")
    print(f"Optimizer: {args.opt}")
    print(f"Learning rate: {args.learning_rate}")

if __name__ == '__main__':
    main()
