import argparse

def print_string(print_this):
	return print_this

def main(print_this):
	print(print_string(print_this))
	
	
def test_print():
	assert print_string("hi")=="hi"

if __name__=='__main__':
	parser=argparse.ArgumentParser()
	parser.add_argument('--print_this', required=True, help='string to display')
	args=parser.parse_args()
	main(args.print_this)
