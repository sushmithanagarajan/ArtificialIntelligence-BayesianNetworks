import java.util.ArrayList;

public class BayesianNetwork {
 
    double values_display()
	{
	double num,denom;
	double n1,d1;
	double success_rate = 1.0;
	double failure_rate = 0.0;
	return success_rate;
	}
	ArrayList<String> find_values(ArrayList<String> variables)
	{
		ArrayList<String> final_val=new ArrayList<String>(10);
		if(variables.contains("Bt"))
			final_val.add(0,"true");
		else if(variables.contains("Bf"))
			final_val.add(0,"false");
		else
			final_val.add(null);
		if(variables.contains("Et"))
			final_val.add(1,"true");
		else if(variables.contains("Ef"))
			final_val.add(1,"false");
		else
			final_val.add(null);
		if(variables.contains("At"))
			final_val.add(2,"true");
		else if(variables.contains("Af"))
			final_val.add(2,"false");
		else
			final_val.add(2,null);
		
		if(variables.contains("Jt"))
			final_val.add(3,"true");
		else if(variables.contains("Jf"))
			final_val.add(3,"false");
		else
			final_val.add(3,null);
		
		if(variables.contains("Mt"))
			final_val.add(4,"true");
		else if(variables.contains("Mf"))
			final_val.add(4,"false");
		else
			final_val.add(4,null);
		return final_val;
	}

	double different_patterns(ArrayList<String> variables)
	{
			ArrayList<String> new_variables=new ArrayList<String>();
			int noneId;
			if(!variables.contains(null)) {
				
				return find_prob(variables.get(0),variables.get(1),variables.get(2),variables.get(3),variables.get(4));
			}
			else {
				noneId=variables.indexOf(null);
				
				for(int i1=0;i1<variables.size();i1++)
				{
					new_variables.add(i1,variables.get(i1));
				}
				new_variables.set(noneId,"true");
			
				double val1=different_patterns(new_variables);
				new_variables.set(noneId,"false");
				
				double val2=different_patterns(new_variables);
				return (val1+val2);
			}
	}
	double find_prob(String b, String e, String a, String j, String m) {
		double final_val=(Prob("B",b,null,null)*Prob("E",e,null,null)*Prob("A|B,E",a,b,e)*Prob("J|A",j,a,null)*Prob("M|A",m,a,null));
		double res=(Prob("B",b,null,null)*Prob("A|B,E",a,b,e)*Prob("J|A",j,a,null)*Prob("M|A",m,a,null)*Prob("E",e,null,null));
		return final_val;
	}
	
	double calc_estimate(String b, String e, String a, String j, String m)
	{
		double res=(Prob("B",b,null,null)*Prob("A|B,E",a,b,e)*Prob("J|A",j,a,null)*Prob("M|A",m,a,null)*Prob("E",e,null,null));
		return res;
	}

	double Prob(String q, String var1, String var2, String var3) {
		
		if(q.equalsIgnoreCase("A|B,E")) {
			double temp=0.0;
			if(var2.equals("true") && var3.equals("true")) {
				temp=0.95;
			}
			else if(var2.equals("true") && var3.equals("false")) {
				temp=0.94;
			}
			else if(var2.equals("false") && var3.equals("true")) {
				temp=0.29;
			}
			else if(var2.equals("false") && var3.equals("false")) {
				temp=0.001;
			}
			if(var1.equals("true")) {
				return temp;
			}
			else
				return (1-temp);
		}
		if(q.equalsIgnoreCase("B"))
		{
			if(var1.equalsIgnoreCase("True"))
				return (0.001);
			else
				return (0.999);
		}
		
		if(q.equalsIgnoreCase("M|A")) {
			double temp=0.0;
			if(var2.equalsIgnoreCase("true"))
				temp=0.70;
			else 
				temp=0.01;
			if(var1.equalsIgnoreCase("true"))
				return temp;
			else
				return (1-temp);
		}
		
		if(q.equalsIgnoreCase("J|A")) {
			double temp=0.0;
			if(var2.equalsIgnoreCase("true")) {
				temp=0.90;
			}
			else 
				temp=0.05;
			if(var1.equalsIgnoreCase("true"))
				return temp;
			else
				return (1-temp);
			}
		
		if(q.equalsIgnoreCase("E"))
		{
			if(var1.equalsIgnoreCase("True"))
				return (0.002);
			else
				return (0.998);
		}
		return -1;
	}
}
