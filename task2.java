import java.io.*;
import java.util.*;
public class task2{
//the main method of the class
	public static void main(String args[]) {
	if( args.length == 0 ||args.length > 6 ) 
    {
      System.out.println(" Give the arguments correctly ");
      System.out.println(" ERROR No of args should be between 1 and 6");
      System.exit(0);
//Exit the system on encountering wrong variables
     }
	double success = 1.0;
	double failure = 0.0;
    double probability_earthquake = 0.0;
	double probability_disaster = 1.0;
	 //assign boolean variables
	boolean given=false;
	boolean taken=true;
	boolean arg=false;
	//arraylist values declared here
	ArrayList<String> obn=new ArrayList<String>();
	ArrayList<String> val=new ArrayList<String>();
	ArrayList<String> observation=new ArrayList<String>();
	ArrayList<String> query=new ArrayList<String>();
	ArrayList<String> q1=new ArrayList<String>();
	for(int i =0;i<args.length;i++ )
	{
		if(args[i]=="taken")
		{
			System.exit(0);
		}
		if(args[i]=="arg")
		{
			System.exit(0);
		}
		if(args[i]=="given")
		{
			given=true;
			continue;
		}
		query.add(args[i]);
		if(given==true)
		{
			observation.add(args[i]);
		}
		
	}
	BayesianNetwork bnet=new BayesianNetwork();
	double num,denom;
	double n1,d1;
	double success_rate = 1.0;
	double failure_rate = 0.0;
	if(query.isEmpty()) {
		System.out.println("Invalid string as User Input");
	}
	else
	{
		num = bnet.different_patterns(bnet.find_values(query));
		  if(!observation.isEmpty()) {
			  denom=bnet.different_patterns(bnet.find_values(observation));
		  }
		  else
			  denom=1;
		  System.out.println("----------------------");
		  System.out.printf("Probability ===== %.9f",(num/denom));
	}
	
}}