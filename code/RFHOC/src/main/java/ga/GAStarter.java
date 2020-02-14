package ga;



import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;


public class GAStarter {
	public static RT rt = null;
	public static void main(String[] args) {
		long startTime=System.currentTimeMillis();

		rt = new RT("rs_rastrigins50_300.csv");
		Population myPop = new Population(100, true);    //��Ⱥ��
		Individual fittestIndividual=new Individual(Double.MAX_VALUE);//根据实际需求选择最大或最小 todo
//	    for(int i=0;i<5;i++){
//			Individual individual=myPop.getIndividual(i);
//			System.out.println(individual.getFitness());
//			for(int j=0;j<individual.defaultGeneLength;j++){
//				System.out.print(individual.getGene(j)+" ");
//			}
//			System.out.println();
//		}
		
		int generationCount=0;
		for(generationCount=0;generationCount<10000;generationCount++){    //��������
			if(generationCount%100==0){
				System.out.println("generationCount:"+generationCount);
			}
//			System.out.print("Generation: " + generationCount + " Fittest: "
//					+ myPop.getFittest().getFitness());
			//TODO
			 if(myPop.getFittest().getFitness()<fittestIndividual.getFitness()){
		        	fittestIndividual.setGenes(myPop.getFittest().getGenes());
		        	fittestIndividual.setFitness(myPop.getFittest().getFitness());
//		        	fittestIndividual.setGenes(fittestIndividual.getGenes());
//		        	fittestIndividual.setFitness(fittestIndividual.getFitness());
		        }
//			System.out.println(" "+fittestIndividual.getFitness()); 
			myPop = Algorithm.evolvePopulation(myPop);
//			for(int i=0;i<5;i++){
//				Individual individual=myPop.getIndividual(i);
//				System.out.println(individual.getFitness());
//				for(int j=0;j<individual.defaultGeneLength;j++){
//					System.out.print(individual.getGene(j)+" ");
//				}
//				System.out.println();
//			}
		}
		double x[]=fittestIndividual.getGenes();
		double y=fittestIndividual.getFitness();
//		System.out.println(y);
//		for(int j=0;j<x.length;j++){
//			System.out.print(x[j]+"��");
//		}
		HashMap<String,String> fitParameter=new HashMap<String,String>();
		fitParameter=fittestIndividual.transfromGene();
		
		FileWriter writer=null;
		String fileName="./result.txt";
		try{
			writer=new FileWriter(fileName);
			writer.write("genetic algorithm:\r\n");
			writer.write("parameters:\r\n");
			Iterator<Map.Entry<String, String>> iterator = fitParameter.entrySet().iterator();
			while (iterator.hasNext()) {
				Map.Entry<String, String> entry = iterator.next();
//				System.out.println(entry.getKey());
//				System.out.println(entry.getValue());
//				writer.write(entry.getKey()+":");
				writer.write(entry.getValue()+", ");
			}
//			writer.write("\r\n");
//			writer.write("fitness\r\n");
			writer.write(String.valueOf(y)+"\r\n");
			writer.write("parameters:\r\n");
			for(int i=0;i<x.length;i++)
				writer.write(String.valueOf(x[i])+" ");
			writer.write("\r\n");
			
		}catch (IOException e){
			e.printStackTrace();
		}finally{
			try{
				if(writer!=null){
					writer.close();
				}
			}catch (IOException e){
				e.printStackTrace();
			}
		}
        long endTime=System.currentTimeMillis();
        System.out.println(endTime - startTime);
	}

}
