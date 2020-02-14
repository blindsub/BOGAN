package ga;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import weka.classifiers.Evaluation;
import weka.classifiers.trees.RandomForest;
import weka.core.DenseInstance;
import weka.core.Instance;
import weka.core.Instances;
import weka.core.converters.CSVLoader;

import java.io.File;
import java.io.FileWriter;
import java.util.*;

/**
 * Author: cwz
 * Time: 2017/11/12
 * Description:
 */
class CompareClass{
    Instance in;
    double value;
    public CompareClass(Instance i,double v){
        in = i;
        value = v;
    }
}

public class RT {
    private static final Logger logger = LoggerFactory.getLogger(RT.class);
    private static RandomForest randomForest = new RandomForest();
    private Instances instances;
    public RT(String filePath){
        try {
            CSVLoader loader = new CSVLoader();
            loader.setSource(new File(filePath));
            instances = loader.getDataSet();
            instances.setClassIndex(instances.numAttributes() - 1);
//            randomForest = new RandomForest();
            Evaluation eval=new Evaluation(instances);
            eval.crossValidateModel(randomForest, instances, 10, new Random(1));
            logger.info("model rae: {}", eval.relativeAbsoluteError());
            logger.info("instances size rae: {}", eval.numInstances());
            randomForest = new RandomForest();
            randomForest.buildClassifier(instances);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public double predict(LinkedHashMap<String, String> param)throws Exception{
        Instance inst = new DenseInstance(param.size());
        inst.setDataset(instances);
        int i = 0;
        for(String value : param.values()) {
            if (instances.attribute(i).type() == 0) {
                inst.setValue(i++, Double.parseDouble(value));
            } else {
                inst.setValue(i++, value);
            }
        }
        double value = randomForest.classifyInstance(inst);
        return value;
    }

//    /**
//     * 选择150个配置参数，50个用来测试，100个作为训练样本池，依次从1个样本开始计算模型的准确性，画如下所示的图：
//     * @throws Exception
//     */
//    public static void graph1() throws Exception {
//        for(int trainNum =10;trainNum<101;trainNum+=10){
////            int trainNum = 99;
//            System.out.println(trainNum+"*****************");
//            CSVLoader loader = new CSVLoader();
//            loader.setSource(new File("1500.csv"));
//            Instances instances = loader.getDataSet();
//            instances.randomize(new Random(System.currentTimeMillis()));
//            Instances testins = new Instances(instances);
//
//
//            instances.setClassIndex(instances.numAttributes() - 1);
//            Iterator<Instance> testit = testins.iterator();
//            for(int i=0;i<100;i++){
//                testit.next();
//                testit.remove();
//            }
//            Instances testAns = new Instances(testins);
//            testins.deleteAttributeAt(11);
//
//            Iterator<Instance> it = instances.iterator();
//            for(int i=0;i<trainNum;i++){
//                it.next();
//            }
//            while(it.hasNext()){
//                it.remove();
//                it.next();
//            }
//
//
//
//            Evaluation eval = new Evaluation(instances);
//
////            randomForest.setBatchSize("100");
////            randomForest.setNumIterations(500);
//            randomForest.setMaxDepth(10);
//            randomForest.setCalcOutOfBag(true);
////            randomForest.setNumFeatures(8);
//            eval.crossValidateModel(randomForest, instances, 10, new Random(1));
////            System.out.println(eval.toSummaryString());
//            randomForest = new RandomForest();
//            randomForest.buildClassifier(instances);
//            double error = 0;
//            int count =0;
//
////        double value = randomForest.classifyInstance(i);
//            List<CompareClass> predictList = new ArrayList<>();
//            for(int i=0;i<testins.size(); i++){
//                Instance in = testins.get(i);
//                in.setDataset(instances);
//                double value = randomForest.classifyInstance(in);
//                double turevalue = testAns.get(i).value(11);
////                System.out.println("truevalue" + turevalue+" value "+value);
//                predictList.add(new CompareClass(testAns.get(i),value));
//                error = error + Math.abs(value-turevalue)/turevalue;
//                count++;
//            }
//
//            Collections.sort(testAns, new Comparator<Instance>() {
//                @Override
//                public int compare(Instance o1, Instance o2) {
//                    return o1.value(11)>o2.value(11)?-1:1;
//                }
//            });
//            System.out.println("true*****************");
//            for(int i=0;i<10;i++){
//                System.out.println(testAns.get(i).toString());
//            }
//
//            Collections.sort(predictList, new Comparator<CompareClass>() {
//                @Override
//                public int compare(CompareClass o1, CompareClass o2) {
//                    return o1.value>o2.value?-1:1;
//                }
//            });
//
//            System.out.println("predict*****************");
//            for(int i=0;i<10;i++){
//                System.out.println(predictList.get(i).in.toString());
//            }
//            double sum=0;
//            for(int i=0;i<10;i++){
//               Instance in =  testAns.get(i);
//               int predictIndex = findIndex(predictList,in);
////                System.out.println(i+" "+predictIndex);
//                sum+= Math.abs(i-predictIndex);
//            }
//            System.out.println(sum/10);
//            System.out.println(trainNum+" "+(1-error/count));
//
//        }
//
//    }
//    public static int findIndex(Instances ins ,Instance in){
//        for(int i=0;i<ins.size();i++){
//            if(ins.get(i)==in){
//                return i;
//            }
//        }
//        return -1;
//    }
//    public static int findIndex(List<CompareClass> ins ,Instance in){
//        for(int i=0;i<ins.size();i++){
////            System.out.println("findindex");
////            System.out.println(ins.get(i).in.toString());
////            System.out.println(in.toString());
////            System.out.println(in.toString().equals(ins.get(i).in.toString()));
//            if(in.toString().equals(ins.get(i).in.toString())){
//                return i;
//            }
//        }
//        return -1;
//    }
//
//
//    /**
//     *   令k=20，b=10，即从50个测试样本中每次随机拿出20个，拿100组（放回采样），然后用预测模型取其中的前10个
//     *   （只对前10个结果进行rank计算），然后计算100个排序nDCG的取值，画图
//     * @throws Exception
//     */
//    public static void graph2_2() throws Exception {
//        /**
//         * 训练集数据从1-100
//         */
//        for(int trainNum =1;trainNum<100;trainNum++){
//            CSVLoader loader = new CSVLoader();
//            loader.setSource(new File("150.csv"));
//            Instances instances = loader.getDataSet();
//            /**
//             * 剔除前100个数据,选择后50个作为测试样本
//             */
//            Instances testins = new Instances(instances);
//            instances.setClassIndex(instances.numAttributes() - 1);
//            Iterator<Instance> testit = testins.iterator();
//            for(int i=0;i<100;i++){
//                testit.next();
//                testit.remove();
//            }
//            /**
//             * 选择训练集数据
//             */
//            Iterator<Instance> it = instances.iterator();
//            for(int i=0;i<trainNum+1;i++){
//                it.next();
//            }
//            while(it.hasNext()){
//                it.remove();
//                it.next();
//            }
//            double avgDcg = 0;
//            /**
//             * 从50个测试集中,选择100次,每次选择20组数据
//             */
//            for(int turnIndex =0;turnIndex<100;turnIndex++){
//                Collections.shuffle(testins);
//                List<Instance> test20= new ArrayList<>();
//                List<Node> top = new ArrayList<>();
//                //从50组中随机选取20个
//                for(int i=0;i<20;i++){
//                    test20.add(testins.get(i));
//                }
//                Evaluation eval = new Evaluation(instances);
//                randomForest = new RandomForest();
//                eval.crossValidateModel(randomForest, instances, 10<trainNum?10:trainNum+1, new Random(1));
//                randomForest.buildClassifier(instances);
//
//                //对20个进行预测
//                for(Instance in : test20){
//                    Instance inst = new DenseInstance(in.numAttributes()-1);
//                    inst.setDataset(instances);
//                    int i = 0;
//                    for(;i<in.numAttributes()-1 ;i++) {
//                        inst.setValue(i, in.value(i));
//                    }
//                    double value = randomForest.classifyInstance(inst);
//                    top.add(new Node(in,value));
//                }
//                //取前10个
//                Collections.sort(top, new Comparator<Node>() {
//                    @Override
//                    public int compare(Node o1, Node o2) {
//                        return o1.value>o2.value?-1:1;
//                    }
//                });
//                List<Instance> test10= new ArrayList<>();
//                for(int i=0;i<10;i++){
//                    test10.add(top.get(i).in);
//                }
//
//                Collections.sort(test10, new Comparator<Instance>() {
//                    @Override
//                    public int compare(Instance o1, Instance o2) {
//                        return o1.value(11)>o2.value(11)?-1:1;
//                    }
//                });
//                /**
//                 * 计算DCGr(dcg) ,DCGr*(dcgr)
//                 */
//                double dcg = DCG.computeDCG(test10,top.subList(0,10));
//                double dcgr = DCG.computeDCGr(test10);
////                System.out.println(dcg);
//                avgDcg= avgDcg + dcg/dcgr;
//            }
//            System.out.println(trainNum+1 +" "+avgDcg/100);
//        }
//
//    }
//
//    /**
//     * 令k=b=50，即对50个测试结果进行全排序，计算nDCG
//     * @throws Exception
//     */
//    public static void graph2_1() throws Exception {
//        for(int trainNum =1;trainNum<100;trainNum++){
//            CSVLoader loader = new CSVLoader();
//            loader.setSource(new File("150.csv"));
//            Instances instances = loader.getDataSet();
//            //测试样本带结果50
//            Instances testins = new Instances(instances);
//            instances.setClassIndex(instances.numAttributes() - 1);
//            Iterator<Instance> testit = testins.iterator();
//            for(int i=0;i<100;i++){
//                testit.next();
//                testit.remove();
//            }
//            //训练样本不带结果
//            Iterator<Instance> it = instances.iterator();
//            for(int i=0;i<trainNum+1;i++){
//                it.next();
//            }
//            while(it.hasNext()){
//                it.remove();
//                it.next();
//            }
//
//            List<Instance> test50= new ArrayList<>();
//            List<Node> top = new ArrayList<>();
//
//            for(int i=0;i<50;i++){
//                test50.add(testins.get(i));
//            }
//            Evaluation eval = new Evaluation(instances);
//            randomForest = new RandomForest();
//            eval.crossValidateModel(randomForest, instances, 10<trainNum?10:trainNum+1, new Random(1));
//            randomForest.buildClassifier(instances);
//
//            //对20个进行预测
//            for(Instance in : test50){
//                Instance inst = new DenseInstance(in.numAttributes()-1);
//                inst.setDataset(instances);
//                int i = 0;
//                for(;i<in.numAttributes()-1 ;i++) {
//                    inst.setValue(i, in.value(i));
//                }
//                double value = randomForest.classifyInstance(inst);
//                top.add(new Node(in,value));
//            }
//            //取前10个
//            Collections.sort(top, new Comparator<Node>() {
//                @Override
//                public int compare(Node o1, Node o2) {
//                    return o1.value>o2.value?-1:1;
//                }
//            });
//
//            //instance从大到小排序
//            Collections.sort(test50, new Comparator<Instance>() {
//                @Override
//                public int compare(Instance o1, Instance o2) {
//                    return o1.value(11)>o2.value(11)?-1:1;
//                }
//            });
//            double dcg = DCG.computeDCG(test50,top);
//            double dcgr = DCG.computeDCGr(test50);
//            System.out.println(trainNum+1 +" "+dcg/dcgr);
//        }
//    }
//    public static void graph3_1() throws Exception {
//        CSVLoader loader = new CSVLoader();
//        loader.setSource(new File("log.csv"));//150.csv
//        Instances instances = loader.getDataSet();
//        instances.randomize(new Random());
//        List<List<String>> ans = new ArrayList<List<String>>();
//        for(int i=0;i<100;i++){
//            for(int j=0;j<100;j++){
//                if(i!=j){
//                    List<String> l = new ArrayList<>();
//                    Instance n1 = instances.get(i);
//                    Instance n2 = instances.get(j);
//                    for(int at=0;at<n1.numAttributes()-1;at++){
//                        l.add(n1.value(at)+"");
//                    }
//                    for(int at=0;at<n2.numAttributes()-1;at++){
//                        l.add(n2.value(at)+"");
//                    }
//                    if(n1.value(n1.numAttributes()-1)>n2.value(n2.numAttributes()-1)){
//                        l.add("1");
//                    }else{
//                        l.add("0");
//                    }
//                    ans.add(l);
//                }
//            }
//        }
////        System.out.println(instances.size());
//        for(int i=100;i<150;i++){
//            for(int j=100;j<150;j++){
//                if(i!=j){
//                    List<String> l = new ArrayList<>();
//                    Instance n1 = instances.get(i);
//                    Instance n2 = instances.get(j);
//                    for(int at=0;at<n1.numAttributes()-1;at++){
//
//                        l.add(n1.value(at)+"");
//                    }
//                    for(int at=0;at<n2.numAttributes()-1;at++){
//                        l.add(n2.value(at)+"");
//                    }
//                    if(n1.value(n1.numAttributes()-1)>n2.value(n2.numAttributes()-1)){
//                        l.add("1");
//                    }else{
//                        l.add("0");
//                    }
//                    ans.add(l);
//                }
//            }
//        }
//        File f = new File("./random.csv");
//        if(f.exists()){
//            f.delete();
//        }
//        FileWriter fw = new FileWriter(f);
//        fw.write("num.network.threads,num.io.threads,queued.max.requests,num.replica.fetchers," +
//                "socket.receive.buffer.bytes,socket.send.buffer.bytes,socket.request.max.bytes," +
//                "buffer.memory,batch.size,linger.ms,compression.type,num.network.threads1,num.io.threads1,queued.max.requests1," +
//                "num.replica.fetchers1,socket.receive.buffer.bytes1,socket.send.buffer.bytes1,socket.request.max.bytes1,buffer.memory1," +
//                "batch.size1,linger.ms1,compression.type1,T\r\n");
//        for(List<String> t : ans){
//            for(int i=0;i<t.size()-1;i++){
//                fw.write(t.get(i)+",");
//            }
//            fw.write(t.get(t.size()-1));
//            fw.write("\r\n");
//        }
//        fw.close();
//    }
//    public static void graph3_2() throws Exception {
//        CSVLoader loader = new CSVLoader();
//        loader.setSource(new File("random.csv"));
//        Instances instances = loader.getDataSet();
////        instances.randomize(new Random());
//        Instances test = new Instances(instances);
//        instances.setClassIndex(instances.numAttributes() - 1);
//        Iterator<Instance> it = test.iterator();
//        //删除前9900个,留下测试集
//        for(int i=0;i<9900;i++){
//            it.next();
//            it.remove();
//        }
//        //留下训练集
//        Iterator<Instance> trainIt = instances.iterator();
//        List<Instance> test9900= new ArrayList<>();
////        System.out.println(instances.size()-2450);
//        for(int i=0;i<800;i++){
//            Instance in = trainIt.next();
//            test9900.add(in);
//        }
//        while(trainIt.hasNext()){
//            trainIt.remove();
//            trainIt.next();
//        }
//        List<Instance> test2450= new ArrayList<>();
//
//
//        for(int i=0;i<test.size();i++){
//            test2450.add(test.get(i));
//        }
//        Evaluation eval = new Evaluation(instances);
//        randomForest = new RandomForest();
//        eval.crossValidateModel(randomForest, instances, 10, new Random(1));
////        CVParameterSelection ps = new CVParameterSelection();
////        ps.setClassifier(randomForest);
////        ps.setNumFolds(5);
////        ps.buildClassifier(instances);
//        randomForest.setBatchSize("100");
//        randomForest.setNumIterations(500);
//        randomForest.setMaxDepth(5);
//        randomForest.setCalcOutOfBag(true);
//        randomForest.setNumFeatures(8);
////        randomForest.set
//        randomForest.buildClassifier(instances);
//        List<Long> predictTrain = new ArrayList<>();
//        List<Double> predictDoubleTrain = new ArrayList<>();
//        for(Instance in : test9900){
//            Instance inst = new DenseInstance(in.numAttributes()-1);
//            inst.setDataset(instances);
//            int i = 0;
//            for(;i<in.numAttributes()-1 ;i++) {
//                inst.setValue(i, in.value(i));
//            }
//            double value = randomForest.classifyInstance(inst);
//            predictDoubleTrain.add(value);
//            predictTrain.add(Math.round(value));
//        }
//        List<Long> predict = new ArrayList<>();
//        List<Double> predictDouble = new ArrayList<>();
//        for(Instance in : test2450){
//            Instance inst = new DenseInstance(in.numAttributes()-1);
//            inst.setDataset(instances);
//            int i = 0;
//            for(;i<in.numAttributes()-1 ;i++) {
//                inst.setValue(i, in.value(i));
//            }
//            double value = randomForest.classifyInstance(inst);
//            predictDouble.add(value);
//            predict.add(Math.round(value));
//        }
//        int count1=0;
//        int count2=0;
//        int targetIndex = instances.numAttributes() - 1;
//        int tn =0;//实际负:->预测负
//        int tp =0;//实际正:->预测正
//        int fn =0;//实际负:->预测正
//        int fp =0;//实际正:->预测负
//        double precesion =0; //查准率 TP/(TP+FP) 即在检索后返回的结果中，真正正确的个数占整个结果的比例。
//        double recall = 0;//查全率 recall = TP/(TP+FN) 即在检索结果中真正正确的个数 占整个数据集（检索到的和未检索到的）中真正正确个数的比例。
//        for (int i = 0; i < predict.size(); i++) {
//            if(Math.round(test2450.get(i).value(targetIndex)) == predict.get(i)){
//                if(predict.get(i)==0){
//                    tn++;
//                }else{
//                    tp++;
//                }
////                System.out.println(test2450.get(i).value(targetIndex) +" --- " + predict.get(i) +" --- "+predictDouble.get(i));
//                count1++;
//            }else if(Math.round(test2450.get(i).value(targetIndex))==0){
//                fn++;
//            }else{
//                fp++;
//            }
//        }
//        for (int i = 0; i < predictTrain.size(); i++) {
//            if(Math.round(test9900.get(i).value(targetIndex)) == predictTrain.get(i)){
//                if(predictTrain.get(i)==0){
//                    tn++;
//                }else{
//                    tp++;
//                }
//                count2++;
//            }else if(Math.round(test9900.get(i).value(targetIndex))==0){
//                fn++;
//            }else{
//                fp++;
//            }
//        }
////        System.out.println(tn);
////        System.out.println(tp);
////        System.out.println(fn);
////        System.out.println(fp);
////        precesion = 1.0*tp/(tp+fp);
////        recall = 1.0*tp/(tp+fn);
////        System.out.println(precesion);
////        System.out.println(recall);
//        System.out.println(1.0*count1/test2450.size());
////        System.out.println(1.0*count2/test9900.size());
//
//
//    }
//
//    public static void pr() throws Exception {
//        int trainNum = 100;
//        CSVLoader loader = new CSVLoader();
//        loader.setSource(new File("1500.csv"));
//        Instances instances = loader.getDataSet();
//        instances.randomize(new Random(System.currentTimeMillis()));
//        Instances testins = new Instances(instances);
//
//
//        instances.setClassIndex(instances.numAttributes() - 1);
//        Iterator<Instance> testit = testins.iterator();
//        for(int i=0;i<100;i++){
//            testit.next();
//            testit.remove();
//        }
//        Instances testAns = new Instances(testins);
//        testins.deleteAttributeAt(11);
//
//        Iterator<Instance> it = instances.iterator();
//        for(int i=0;i<trainNum;i++){
//            it.next();
//        }
//        while(it.hasNext()){
//            it.remove();
//            it.next();
//        }
//
//
//
//        Evaluation eval = new Evaluation(instances);
//
////            randomForest.setBatchSize("100");
////            randomForest.setNumIterations(500);
//        randomForest.setMaxDepth(10);
//        randomForest.setCalcOutOfBag(true);
////            randomForest.setNumFeatures(8);
//        eval.crossValidateModel(randomForest, instances, 10, new Random(1));
////            System.out.println(eval.toSummaryString());
//        randomForest = new RandomForest();
//        randomForest.buildClassifier(instances);
//        double error = 0;
//        int count =0;
//
////        double value = randomForest.classifyInstance(i);
//        List<CompareClass> predictList = new ArrayList<>();
//        for(int i=0;i<testins.size(); i++){
//            Instance in = testins.get(i);
//            in.setDataset(instances);
//            double value = randomForest.classifyInstance(in);
//            double turevalue = testAns.get(i).value(11);
////                System.out.println("truevalue" + turevalue+" value "+value);
//            predictList.add(new CompareClass(testAns.get(i),value));
//            error = error + Math.abs(value-turevalue)/turevalue;
//            count++;
//        }

//    }
//    public static void main(String[] args) throws Exception {
//      graph1();
////      graph2_2();
////      graph2_1();
////        for(int i=0;i<1;i++){
//////            graph1();
////            graph3_1();
////            graph3_2();
////        }
//
//
//    }

}
