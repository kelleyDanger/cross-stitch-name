
import argparse

class BinaryCrossStich:
    def __init__(self):
        self.args = self.parse_args()
        self.name = self.args.name
        self.name_d = {}
        print(f"name: {self.name}")

    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('name', nargs="+", help='Name to create Binary cross-stich pattern.')
        args = parser.parse_args()
        args.name = ' '.join(args.name)
        return args

    def string_to_binary(self, name_s: str) -> list:
        # create name_d for debugging
        for letter in name_s:
            b = format(ord(letter), '08b')
            self.name_d[letter] = b

        binary_list = [format(ord(i), '08b') for i in name_s]
        return binary_list

    def cross_stitch_0(self):
       zero = """
         xx
        x  x
        x  x
        x  x
        x  x
        x  x
        x  x
         xx
       """
       return zero

    def cross_stitch_1(self):
       one = """
          x
         xx
       x  x
          x
          x
          x
          x
         xxx
       """
       return one
    
    def small_cross_stitch_0(self):
       zero = """
 xx 
x  x
x  x
x  x
 xx 
       """
       a = zero.split("\n")[1:-1]
        # [' xx', 'x  x', 'x  x', ' xx']
       return a

    def small_cross_stitch_1(self):
       one = """
 xx 
x x 
  x 
  x 
 xxx
       """
       a = one.split("\n")[1:-1]
       # [' xx', 'x x', '  x', 'xxx']
       return a

    def create_cross_stitch_name(self):
        # binary_list = self.string_to_binary(self.name)
        i = 0
        names = self.name.split()
        longest_name = max(names)

        # K D
        # 01001011 01000100
        #  xx    xx      xx
        # x  x    x     x  x
        #  xx    xxx     xx
        # e a
        # l n 
        # l g 
        # e e 
        # y r

        while i < len(longest_name): # loop through longest name 
            for col in range(len(names)):
                # K, '01001011' D, '01000100'
                letter = names[col][i]
                letter_binary = format(ord(letter), '08b')
                print(f"{letter}: {letter_binary}")

                # how ever tall the cross-stitch times, print off that binary x's
                # 4
                height = len(self.small_cross_stitch_0())
                for h in range(height):
                    for l in letter_binary: # 0
                        if l == "0":
                            # need h x's for zero
                            xs = self.small_cross_stitch_0()[h]
                        else:
                            # need h x's for one
                            xs = self.small_cross_stitch_1()[h]
                        print(xs, end="      ")
                    print("\n")
                # end of letter 'K'
            # end of K, D
            i += 1
                        
if __name__ == "__main__":
    # Uncomment the line below if running in an interactive environment or testing
    import sys; sys.argv.append("Kelley Danger")

    bcs = BinaryCrossStich()    
    bcs.create_cross_stitch_name()
