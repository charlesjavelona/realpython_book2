
import pdb

def add_one_hundred():
    again = 'yes'
    while again == 'yes':
        number = input('Enter a number between 1 and 10: ')
        new_number = (int(number) + 100)
        print('{} plus 100 is {}!'.format(number, new_number))
        again = input('Another round, my friend? (`yes` or `no`) ')
    print("Goodbye!")



def main():
	pdb.set_trace()
	add_one_hundred()

if __name__ == '__main__':
	main()