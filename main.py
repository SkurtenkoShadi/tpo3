from module import MathOperations, TextOperation
import sys
def main():
        
        math = sys.argv[0]
        text = sys.argv[1]

        squared_value = math.square()
        cubed_value = math.cube()
        quad_value = math._quad()
        word_count = text.count_words()
        symbols_count = text.symbols_count()
        up = text._up()
        
        print(f"Squared value: {squared_value}")
        print(f"Cubed value: {cubed_value}")
        print(f"Word count: {word_count}")
        print(f"Quad value: {quad_value}")
        print(f"Symbols count: {symbols_count}")
        print(f"Up!: {up}")
if __name__ == "__main__":
    main()