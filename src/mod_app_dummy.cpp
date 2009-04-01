#include "main.h"


/**************************************
	Interception module stuff
**************************************/
AppModule::AppModule(string command){
	init(command);
}

bool AppModule::init(string command){
	
	LOG("Created dummy AppModule! This shouldn't be used\n");
	return false;
}

bool AppModule::process(list<Instruction> &list){
		
	LOG("Dummy AppModule can't do stuff\n");
	return false;
}

