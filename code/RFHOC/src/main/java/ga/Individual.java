package ga;




import java.util.Arrays;
import java.util.LinkedHashMap;



public class Individual {
	static int defaultGeneLength = 50;   //x?????????
	//????????
	private double[] genes = new double[defaultGeneLength];
	//?????????
	private double fitness=0;

	public Individual clone(){
		Individual individual = new Individual();
		individual.setGenes(Arrays.copyOf(genes, genes.length));
		return individual;
	}
	public Individual(){

	}
	public Individual(double fit){
		fitness=fit;
	}
	//??????????????????
	public void generateIndividual() {

		do {
			for (int i = 0; i < defaultGeneLength; i++) {
				double gene = Math.random();
				genes[i] = gene;
			}
		} while (!isLegal(transfromGene()));
    }
	
	public double[] getGenes() {
		return genes;
	}
	public void setGenes(double[] genes) {
		this.genes = genes;
	}
	
	//????????fitness?
	public double getFitness(){
		if (fitness == 0) {
           //????????

			LinkedHashMap<String,String> parameter=transfromGene();
			
//			Iterator<Map.Entry<String, String>> iterator = parameter.entrySet().iterator();
//			while (iterator.hasNext()) {
//				Map.Entry<String, String> entry = iterator.next();
//				System.out.println(entry.getKey());
//				System.out.println(entry.getValue());
//			}
			
//			double memoryFraction= Double.parseDouble(parameter.get("spark.shuffle.memoryFraction"));
//			double safetyFraction=Double.parseDouble(parameter.get("spark.shuffle.safetyFraction"));
//			if(memoryFraction*safetyFraction<=0.45){
//
//				//�޸�Ϊ
////				WhatIfEstimate whatif=new WhatIfEstimate();
////				fitness=whatif.estimate(parameter,inputBytes,jarFileSize,exeMem,tasknums);
//			}else{
//				fitness=Double.MAX_VALUE;
//			}

			try {
				fitness = GAStarter.rt.predict(parameter);
			} catch (Exception e) {
				e.printStackTrace();
			}

		}
        return fitness;
	}
	
	public void setFitness(double fitness){
		this.fitness=fitness;
	}
	
	public double getGene(int index) {
        return genes[index];
    }

    public void setGene(int index, double value) {
        genes[index] = value;
        fitness = 0;
    }

    public static boolean isLegal(LinkedHashMap<String,String> parameters){
//		int cores = Integer.parseInt(parameters.get("spark.executor.cores"));
//		int mem = Integer.parseInt(parameters.get("spark.executor.memory"));
//		if(4 / cores * ((mem - 300) * ParameterUtils.ratio + 300) > ParameterUtils.maxMemory){
//			return false;
//		}
		return true;
	}

    //�����������
    public LinkedHashMap<String,String> transfromGene(){

		LinkedHashMap<String,String> parameters = new LinkedHashMap<>();


//		int cores = (int)Math.ceil(genes[0] * 4);
//		int testMaxMem = (EnvConfigs.maxMemory - 300)/ EnvConfigs.ratio + 300;
//		int mem = (int)(Math.floor(genes[1] * (testMaxMem - 540)) + 540);
//
//
//		double memory = genes[2] * 0.8 + 0.1;
//		double storageFrac = genes[3] * 0.8 + 0.1;
//
//
//		//spark.executor.cores ȡֵ��Χ(1,2,4)
//    	int parallelism = (int)Math.ceil(genes[4] * 81) + 19;
//
//
//		String shuffleCompress = genes[5] < 0.5 ? "true" : "false";
//		String shuffleSpillCompress = genes[6] < 0.5 ? "true" : "false";
//		String broadcastCompress = genes[7] < 0.5 ? "true" : "false";
//		String rddCompress = genes[8] < 0.5 ? "true" : "false";
//		String codec="";
//		if(genes[9]<1.0/3){
//			codec="lz4";
//		}
//		else{
//			if(genes[9]<2.0/3){
//				codec="lzf";
//			}
//			else{
//				codec="snappy";
//			}
//		}
//		double sizeInFlight = Math.floor(genes[10] * 89) + 8;
//		double fileBuffer = Math.floor(genes[11] * 57) + 8;

//		int sort_buffer_size = (int) (Math.ceil(genes[0]*3968)+128);
//		int join_buffer_size = (int) (Math.ceil(genes[1]*1920)+128);
//		int table_open_cache = (int) (Math.ceil(genes[2]*1920)+128);
//		int thread_cache_size = (int) (Math.ceil(genes[3]*120)+8);
//		int query_cache_limit = (int) (Math.ceil(genes[4]*2048)+1024);
//		int max_allowed_packet = (int) (Math.ceil(genes[5]*14336)+2048);
//		int max_connect_errors = (int) Math.ceil(genes[6]*2000);
//		int tmp_table_size = (int) (Math.ceil(genes[7]*120*1024)+8192);
//		int max_heap_table_size = (int) (Math.ceil(genes[8]*120*1024)+2048);
//		int innodb_autoextend_increment = (int) (Math.ceil(genes[9]*504*1024)+8192);
//		int innodb_buffer_pool_size = (int) Math.ceil(genes[10]*8192);
//		int innodb_additional_mem_pool_size = (int) (Math.ceil(genes[11]*1024*19)+1024);
//		int innodb_log_buffer_size = (int) (Math.ceil(genes[12]*1024*28)+4*1024);
//
//		parameters.put("sort_buffer_size", String.valueOf(sort_buffer_size));
//		parameters.put("join_buffer_size",String.valueOf(join_buffer_size));
//		parameters.put("table_open_cache",String.valueOf(table_open_cache));
//		parameters.put("thread_cache_size",String.valueOf(thread_cache_size));
//		parameters.put("query_cache_limit",String.valueOf(query_cache_limit));
//		parameters.put("max_allowed_packet", String.valueOf(max_allowed_packet));
//		parameters.put("max_connect_errors", String.valueOf(max_connect_errors));
//		parameters.put("tmp_table_size",String.valueOf(tmp_table_size));
//		parameters.put("max_heap_table_size",String.valueOf(max_heap_table_size));
//		parameters.put("innodb_autoextend_increment", String.valueOf(innodb_autoextend_increment));
//		parameters.put("innodb_buffer_pool_size", String.valueOf(innodb_buffer_pool_size));
//		parameters.put("innodb_additional_mem_pool_size",String.valueOf(innodb_additional_mem_pool_size));
//		parameters.put("innodb_log_buffer_size", String.valueOf(innodb_log_buffer_size));

		// spark.serializer
//		String serializer =  genes[12] < 0.5 ? "org.apache.spark.serializer.JavaSerializer" : "org.apache.spark.serializer.KryoSerializer";
//		parameters.put("spark.executor.cores", String.valueOf(cores));
//		parameters.put("spark.executor.memory", String.valueOf(mem));
//		parameters.put("spark.memory.fraction", String.valueOf(memory));
//		parameters.put("spark.memory.storageFraction", String.valueOf(storageFrac));
//		parameters.put("spark.default.parallelism", String.valueOf(parallelism));
//		parameters.put("spark.shuffle.compress", String.valueOf(shuffleCompress));
//		parameters.put("spark.shuffle.spill.compress", String.valueOf(shuffleSpillCompress));
//		parameters.put("spark.broadcast.compress", String.valueOf(broadcastCompress));
//		parameters.put("spark.rdd.compress", String.valueOf(rddCompress));
//		parameters.put("spark.io.compression.codec", String.valueOf(codec));
//		parameters.put("spark.reducer.maxSizeInFlight", String.valueOf(sizeInFlight));
//		parameters.put("spark.shuffle.file.buffer", String.valueOf(fileBuffer));
//		parameters.put("spark.serializer", String.valueOf(serializer));

		double range = 5.12;
		double x1 = Math.ceil(genes[0] * 2 * range) - range;
		double x2 = Math.ceil(genes[1] * 2 * range) - range;
		double x3 = Math.ceil(genes[2] * 2 * range) - range;
		double x4 = Math.ceil(genes[3] * 2 * range) - range;
		double x5 = Math.ceil(genes[4] * 2 * range) - range;
		double x6 = Math.ceil(genes[5] * 2 * range) - range;
		double x7 = Math.ceil(genes[6] * 2 * range) - range;
		double x8 = Math.ceil(genes[7] * 2 * range) - range;
		double x9 = Math.ceil(genes[8] * 2 * range) - range;
		double x10 = Math.ceil(genes[9] * 2 * range) - range;
		double x11 = Math.ceil(genes[10] * 2 * range) - range;
		double x12 = Math.ceil(genes[11] * 2 * range) - range;
		double x13 = Math.ceil(genes[12] * 2 * range) - range;
		double x14 = Math.ceil(genes[13] * 2 * range) - range;
		double x15 = Math.ceil(genes[14] * 2 * range) - range;
		double x16 = Math.ceil(genes[15] * 2 * range) - range;
		double x17 = Math.ceil(genes[16] * 2 * range) - range;
		double x18 = Math.ceil(genes[17] * 2 * range) - range;
		double x19 = Math.ceil(genes[18] * 2 * range) - range;
		double x20 = Math.ceil(genes[19] * 2 * range) - range;
		double x21 = Math.ceil(genes[20] * 2 * range) - range;
		double x22 = Math.ceil(genes[21] * 2 * range) - range;
		double x23 = Math.ceil(genes[22] * 2 * range) - range;
		double x24 = Math.ceil(genes[23] * 2 * range) - range;
		double x25 = Math.ceil(genes[24] * 2 * range) - range;
		double x26 = Math.ceil(genes[25] * 2 * range) - range;
		double x27 = Math.ceil(genes[26] * 2 * range) - range;
		double x28 = Math.ceil(genes[27] * 2 * range) - range;
		double x29 = Math.ceil(genes[28] * 2 * range) - range;
		double x30 = Math.ceil(genes[29] * 2 * range) - range;
		double x31 = Math.ceil(genes[30] * 2 * range) - range;
		double x32 = Math.ceil(genes[31] * 2 * range) - range;
		double x33 = Math.ceil(genes[32] * 2 * range) - range;
		double x34 = Math.ceil(genes[33] * 2 * range) - range;
		double x35 = Math.ceil(genes[34] * 2 * range) - range;
		double x36 = Math.ceil(genes[35] * 2 * range) - range;
		double x37 = Math.ceil(genes[36] * 2 * range) - range;
		double x38 = Math.ceil(genes[37] * 2 * range) - range;
		double x39 = Math.ceil(genes[38] * 2 * range) - range;
		double x40 = Math.ceil(genes[39] * 2 * range) - range;
		double x41 = Math.ceil(genes[40] * 2 * range) - range;
		double x42 = Math.ceil(genes[41] * 2 * range) - range;
		double x43 = Math.ceil(genes[42] * 2 * range) - range;
		double x44 = Math.ceil(genes[43] * 2 * range) - range;
		double x45 = Math.ceil(genes[44] * 2 * range) - range;
		double x46 = Math.ceil(genes[45] * 2 * range) - range;
		double x47 = Math.ceil(genes[46] * 2 * range) - range;
		double x48 = Math.ceil(genes[47] * 2 * range) - range;
		double x49 = Math.ceil(genes[48] * 2 * range) - range;
		double x50 = Math.ceil(genes[49] * 2 * range) - range;


		parameters.put("x1", String.valueOf(x1));
		parameters.put("x2", String.valueOf(x2));
		parameters.put("x3", String.valueOf(x3));
		parameters.put("x4", String.valueOf(x4));
		parameters.put("x5", String.valueOf(x5));
		parameters.put("x6", String.valueOf(x6));
		parameters.put("x7", String.valueOf(x7));
		parameters.put("x8", String.valueOf(x8));
		parameters.put("x9", String.valueOf(x9));
		parameters.put("x10", String.valueOf(x10));
		parameters.put("x11", String.valueOf(x11));
		parameters.put("x12", String.valueOf(x12));
		parameters.put("x13", String.valueOf(x13));
		parameters.put("x14", String.valueOf(x14));
		parameters.put("x15", String.valueOf(x15));
		parameters.put("x16", String.valueOf(x16));
		parameters.put("x17", String.valueOf(x17));
		parameters.put("x18", String.valueOf(x18));
		parameters.put("x19", String.valueOf(x19));
		parameters.put("x20", String.valueOf(x20));
		parameters.put("x21", String.valueOf(x21));
		parameters.put("x22", String.valueOf(x22));
		parameters.put("x23", String.valueOf(x23));
		parameters.put("x24", String.valueOf(x24));
		parameters.put("x25", String.valueOf(x25));
		parameters.put("x26", String.valueOf(x26));
		parameters.put("x27", String.valueOf(x27));
		parameters.put("x28", String.valueOf(x28));
		parameters.put("x29", String.valueOf(x29));
		parameters.put("x30", String.valueOf(x30));
		parameters.put("x31", String.valueOf(x31));
		parameters.put("x32", String.valueOf(x32));
		parameters.put("x33", String.valueOf(x33));
		parameters.put("x34", String.valueOf(x34));
		parameters.put("x35", String.valueOf(x35));
		parameters.put("x36", String.valueOf(x36));
		parameters.put("x37", String.valueOf(x37));
		parameters.put("x38", String.valueOf(x38));
		parameters.put("x39", String.valueOf(x39));
		parameters.put("x40", String.valueOf(x40));
		parameters.put("x41", String.valueOf(x41));
		parameters.put("x42", String.valueOf(x42));
		parameters.put("x43", String.valueOf(x43));
		parameters.put("x44", String.valueOf(x44));
		parameters.put("x45", String.valueOf(x45));
		parameters.put("x46", String.valueOf(x46));
		parameters.put("x47", String.valueOf(x47));
		parameters.put("x48", String.valueOf(x48));
		parameters.put("x49", String.valueOf(x49));
		parameters.put("x50", String.valueOf(x50));

    	return parameters;
    }

	public static void main(String[] args) {
	}

}
