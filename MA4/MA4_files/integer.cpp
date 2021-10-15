#include <cstdlib>
// Integer class

class Integer{
	public:
		Integer(int);
		int get();
		int fib();
		void set(int);
	private:
		int val;
		int fib_c(int);
	};
Integer::Integer(int n){
	val = n;
	}
int Integer::get(){
	return val;
	}
void Integer::set(int n){
	val = n;
	}
int Integer::fib_c(int n){
	if( n<=1)
		return n;
	else
		return (fib_c(n-1)+fib_c(n-2));
}
int Integer::fib(){
	return fib_c(val);
}
extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_get(Integer* integer) {return integer->get();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	int Integer_fib(Integer* integer){return integer->fib();}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}
