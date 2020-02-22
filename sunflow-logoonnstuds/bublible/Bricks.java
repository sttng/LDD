package bublible;

import java.io.FileNotFoundException;
import static java.lang.Float.parseFloat;
import static java.lang.Integer.parseInt;
import java.util.Arrays;
import org.sunflow.SunflowAPI;
import org.sunflow.core.Modifier;
import org.sunflow.core.parser.SCParser;
import org.sunflow.core.tesselatable.FileMesh;
import org.sunflow.math.MathUtils;
import org.sunflow.math.Matrix4;

// Brick manipulating methods
public final class Bricks {

    private Utils q;
    private final FileMesh los = new FileMesh();
    private int logoonstuds = 0;

    private Matrix4 m = new Matrix4();
    private float wz05 = 0.988f;
    private float wz1 = 0.992f;
    private float wz2 = 0.993f;
    private float wz3 = 0.996f;
    private float wz4 = 0.997f;
    private float wz5 = 0.998f;
    private float wz6 = 0.9985f;
    private float wz7 = 0.99855f;
    private float wz8 = 0.9986f;
    private float wz9 = 0.99865f;
    private float wz10 = 0.998f;
    private float wz11 = 0.998725f;
    private float wz12 = 0.99875f;
    private float wz13 = 0.9988f;
    private float wz14 = 0.99885f;
    private float wz15 = 0.99889f;
    private float wz16 = 0.9992f;
    private float wz18 = 0.9993f;
    private float wz24 = 0.9994f;
    private float wz28 = 0.9995f;
    private float wz34 = 0.9996f;
    private float h0_1 = 0.97f;
    private float h0_2 = 0.99f;
    private float h1 = 0.99f;
    private float h1_1 = 0.99125f;
    private float h1_2 = 0.9915f;
    private float h2 = 0.9945f;
    private float h2_1 = 0.99465f;
    private float h2_2 = 0.99485f;
    private float h3 = 0.9966f;
    private float h3_1 = 0.996633f;
    private float h3_2 = 0.996666f;
    private float h4 = 0.9967f;
    private float h4_2 = 0.9971f;
    private float h5 = 0.9975f;
    private float h5_2 = 0.9978f;
    private float h6 = 0.998f;
    private float h6_1 = 0.9981f;
    private float h7 = 0.99825f;
    private float h8 = 0.9985f;
    private float h9 = 0.9986f;
    private float h10 = 0.99875f;
    private float h11_2 = 0.9990f;
    private float h12 = 0.9992f;
    private float h16 = 0.9995f;

    // --------------------------- BRICK SIZE GROUPS (BRICK SEAMS) ---------------------------
    private final String[] g_0_5x2x0_2 = {"41677"};
    private final String[] g_0_5x2x2 = {"4346"};
    private final String[] g_0_5x3x0_2 = {"6632"};
    private final String[] g_0_5x3x1_2 = {"6575"};
    private final String[] g_0_5x3x2_1 = {"32056", "32249"};
    private final String[] g_0_5x4x0_2 = {"32449"};
    private final String[] g_0_5x4x2_1 = {"2905", "99773"};
    private final String[] g_0_5x4x3_2 = {"44374"};
    private final String[] g_0_5x5x0_2 = {"11478", "32017"};
    private final String[] g_0_5x5x2_1 = {"32250"};
    private final String[] g_0_5x6x0_2 = {"32063"};
    private final String[] g_0_5x7x0_2 = {"32065"};
    private final String[] g_0_5x7x4 = {"32251"};
    private final String[] g_1x1x0_1 = {"3070", "3024", "6141", "98138", "85861"};
    private final String[] g_1x1x0_2 = {"50746", "2555", "12825", "15712"};
    private final String[] g_1x1x1 = {"3005", "3062", "4589", "6188", "59900",
        "4070", "87087", "47905", "2921", "60475",
        "60476", "4733", "6541"};
    private final String[] g_1x1x2 = {"15444"};
    private final String[] g_1x1x3 = {"14716", "60583"};
    private final String[] g_1x1x5 = {"2453"};
    private final String[] g_1x2x0_1 = {"3023", "3069", "3794", "2412", "4085",
        "60897", "32028", "49668", "15208"};
    private final String[] g_1x2x0_2 = {"85984", "11477", "99780", "99781", "92280",
        "30383", "4081", "6019", "3614", "61409",
        "3937", "3938"};
    private final String[] g_1x2x1 = {"2877", "3004", "3065", "30136", "98283",
        "3134", "4216", "11211", "30364", "30365",
        "30540", "30541", "52107", "76385", "30237",
        "95820", "30236", "30386", "47975", "32000",
        "2458", "32064", "3700", "30526", "3665",
        "3040", "92946", "15571", "3048", "3044",
        "6091", "2432", "11458", "3830", "3831"};
    private final String[] g_1x2x1_1 = {"32529", "32530"};
    private final String[] g_1x2x1_2 = {"99207", "44728"};
    private final String[] g_1x2x2 = {"3245", "60481", "2342", "4175", "73081"};
    private final String[] g_1x2x3 = {"2449", "4460"};
    private final String[] g_1x2x5 = {"2454", "88393"};
    private final String[] g_1x3x0_1 = {"3623", "63864", "4275", "4276", "60478",
        "44301", "63868", "4531", "2429", "2430"};
    private final String[] g_1x3x0_2 = {"14418", "14419", "44300"};
    private final String[] g_1x3x1 = {"3622", "4286", "18759", "2341", "4287", "4490",
        "50950", "4595"};
    private final String[] g_1x3x2 = {"6005", "92903", "33243", "88292"};
    private final String[] g_1x3x2_1 = {"60484"};
    private final String[] g_1x3x3 = {"6044", "13965"};
    private final String[] g_1x3x5 = {"3755"};
    private final String[] g_1x4x0_1 = {"3710", "2431", "92593", "4315", "18649"};
    private final String[] g_1x4x0_2 = {"93273", "2436", "10201", "4625", "44522",
        "95120", "32006"};
    private final String[] g_1x4x1 = {"3010", "3066", "15533", "30137", "2653",
        "30414", "30387", "3701", "60477", "6191",
        "10314", "11153", "61678", "3659", "13547",
        "18624", "4590", "3633"};
    private final String[] g_1x4x1_2 = {"93274", "32140", "3187", "14520", "3186"};
    private final String[] g_1x4x2 = {"2743", "6182", "6187", "3185", "33303",
        "15332", "30055"};
    private final String[] g_1x4x6 = {"10304", "30164", "42447"};
    private final String[] g_1x5x0_1 = {"32124"};
    private final String[] g_1x5x0_2 = {"50947"};
    private final String[] g_1x5x1 = {"40996", "61072"};
    private final String[] g_1x5x3 = {"2340"};
    private final String[] g_1x5x2_1 = {"32526"};
    private final String[] g_1x5x4 = {"2339", "14395", "30099", "76768"};
    private final String[] g_1x6x0_1 = {"3666", "6636"};
    private final String[] g_1x6x1 = {"3009", "3067", "3894", "52501", "3455",
        "92950", "41763", "41762"};
    private final String[] g_1x6x2 = {"2744", "3307", "6183", "15254", "30077",
        "6583"};
    private final String[] g_1x6x2_2 = {"32348"};
    private final String[] g_1x6x3 = {"32333", "15967", "6060"};
    private final String[] g_1x6x5 = {"3754", "30249", "64448"};
    private final String[] g_1x6x10 = {"64449"};
    private final String[] g_1x7x0_2 = {"32524"};
    private final String[] g_1x8x0_1 = {"3460", "4162", "4510"};
    private final String[] g_1x8x1 = {"3008", "3702"};
    private final String[] g_1x8x1_1 = {"50967"};
    private final String[] g_1x8x2 = {"3308", "16577"};
    private final String[] g_1x8x2_1 = {"32271"};
    private final String[] g_1x8x2_2 = {"6629", "6079"};
    private final String[] g_1x8x3 = {"2583"};
    private final String[] g_1x9x0_2 = {"40490"};
    private final String[] g_1x9x4 = {"32009"};
    private final String[] g_1x10x0_1 = {"4477"};
    private final String[] g_1x10x1 = {"6111", "2730", "13731", "85970"};
    private final String[] g_1x11x0_2 = {"32525"};
    private final String[] g_1x12x0_1 = {"60479"};
    private final String[] g_1x12x1 = {"6112", "3895"};
    private final String[] g_1x12x3 = {"6108", "14707", "18838"};
    private final String[] g_1x12x5 = {"6184"};
    private final String[] g_1x13x0_2 = {"41239"};
    private final String[] g_1x14x1 = {"4217", "32018"};
    private final String[] g_1x15x0_2 = {"32278"};
    private final String[] g_1x16x1 = {"2465", "3703"};
    private final String[] g_2x2x0_1 = {"3022", "3068", "87580", "2420", "14719",
        "4150", "14769", "15535", "4032", "2654",
        "4740", "11203", "2452", "2540", "48336",
        "44567", "60471", "3679", "3680"};
    private final String[] g_2x2x0_2 = {"3300", "15068", "99206", "92582",
        "11476", "60470", "14704", "14417", "43857",
        "41855", "47457"};
    private final String[] g_2x2x1 = {"2357", "3003", "98100", "3067", "85080",
        "87620", "6143", "17485", "30367", "92947",
        "90258", "40902", "30389", "4729", "3660",
        "3676", "3039", "3045", "3046", "3043",
        "3049", "13548", "30165", "74698", "2376",
        "2460", "2476", "15092", "88072", "4623",
        "2444", "2817", "10247", "44675", "30602",
        "30603", "4588"};
    private final String[] g_2x2x1_1 = {"50943"};
    private final String[] g_2x2x1_2 = {"2563", "30106"};
    private final String[] g_2x2x2 = {"30151", "3942", "30361", "6039", "41533",
        "4792", "3678", "3688", "2489", "4345",
        "3940", "61780", "4079", "4591", "3956"};
    private final String[] g_2x2x3 = {"30145", "3685", "30499"};
    private final String[] g_2x2x5 = {"30256", "98549"};
    private final String[] g_2x2x7 = {"2039", "11062", "6253"};
    private final String[] g_2x2x10 = {"57893", "58827", "95347"};
    private final String[] g_2x2x16 = {"91176"};
    private final String[] g_2x3x0_1 = {"3021", "43722", "43723", "3176", "3839"};
    private final String[] g_2x3x0_2 = {"63082", "3730", "3729", "15456", "32523"};
    private final String[] g_2x3x1 = {"3002", "6564", "6565", "48169", "62712",
        "92013", "57909", "48171", "48170", "6232",
        "3298", "3747", "3038", "3042", "6215",
        "85943"};
    private final String[] g_2x3x1_1 = {"91996"};
    private final String[] g_2x3x2 = {"4532", "92410", "3957", "50946", "44661"};
    private final String[] g_2x4x0_1 = {"3020", "87079", "41769", "41770", "51739",
        "3709", "2873", "44569", "92092", "44568",
        "4596"};
    private final String[] g_2x4x0_2 = {"3299", "88930", "3787", "3788", "30350",
        "3184", "61068", "47456", "50949", "60212"};
    private final String[] g_2x4x1 = {"3001", "41767", "41768", "48172", "17114",
        "57908", "47452", "6249", "30000", "3041",
        "3037", "30363", "4871", "43710", "43711",
        "43720", "43721", "47759", "6081", "6192",
        "93606", "30043", "3183", "98263", "4739",
        "41862", "93590", "41854", "88289"};
    private final String[] g_2x4x1_2 = {"4229"};
    private final String[] g_2x4x2 = {"6061", "2434", "30592", "6216", "4744",
        "4598", "2439", "92926", "30601", "93598",
        "3479", "55205", "4209"};
    private final String[] g_2x4x3 = {"30144", "97492", "30209", "44572", "15091",
        "47990"};
    private final String[] g_2x4x4 = {"30535"};
    private final String[] g_2x4x6 = {"47847"};
    private final String[] g_2x5x0_2 = {"32316"};
    private final String[] g_2x5x1 = {"98285", "98286"};
    private final String[] g_2x5x1_1 = {"11215"};
    private final String[] g_2x5x1_2 = {"6070", "3639"};
    private final String[] g_2x5x2 = {"4868", "4746"};
    private final String[] g_2x5x2_1 = {"6087", "76766"};
    private final String[] g_2x5x2_2 = {"30358"};
    private final String[] g_2x5x3_1 = {"3587"};
    private final String[] g_2x5x5 = {"4476"};
    private final String[] g_2x6x0_1 = {"3795", "32001"};
    private final String[] g_2x6x0_2 = {"87609"};
    private final String[] g_2x6x1 = {"44237", "47432", "47454", "2875", "41747",
        "41748", "41764", "41765", "44126"};
    private final String[] g_2x6x1_2 = {"3640"};
    private final String[] g_2x6x2 = {"2904", "2336"};
    private final String[] g_2x6x3 = {"6213"};
    private final String[] g_2x6x3_1 = {"6239"};
    private final String[] g_2x6x6 = {"6236"};
    private final String[] g_2x8x0_1 = {"3034", "3738", "30586"};
    private final String[] g_2x8x1 = {"3007", "93888", "4445"};
    private final String[] g_2x8x1_1 = {"4732"};
    private final String[] g_2x8x2 = {"11290", "11301", "41766"};
    private final String[] g_2x10x0_1 = {"3832"};
    private final String[] g_2x10x1 = {"3006"};
    private final String[] g_2x10x2 = {"30180"};
    private final String[] g_2x12x0_1 = {"2445"};
    private final String[] g_2x12x5 = {"87614"};
    private final String[] g_2x12x6 = {"30272", "30110"};
    private final String[] g_2x14x0_1 = {"91988"};
    private final String[] g_2x14x8 = {"54094"};
    private final String[] g_2x16x0_1 = {"4282", "62743"};
    private final String[] g_2x16x1 = {"30382"};
    private final String[] g_2x16x1_1 = {"57779"};
    private final String[] g_3x2x3 = {"30274"};
    private final String[] g_3x2x4 = {"2422"};
    private final String[] g_3x3x0_1 = {"11212", "15397", "2450", "30357"};
    private final String[] g_3x3x0_2 = {"43898"};
    private final String[] g_3x3x1 = {"2462", "30505", "3675", "4161", "99301",
        "3963"};
    private final String[] g_3x3x2 = {"88293", "6233", "2463", "2464"};
    private final String[] g_3x3x3 = {"4222"};
    private final String[] g_3x4x0_1 = {"88646", "48183", "90194", "92692"};
    private final String[] g_3x4x0_2 = {"50948", "11291", "93604"};
    private final String[] g_3x4x1 = {"3297", "4861", "64225", "44674", "3475",
        "98302", "98282"};
    private final String[] g_3x4x1_1 = {"93597", "47755"};
    private final String[] g_3x4x1_2 = {"30150", "93587", "98835", "50745"};
    private final String[] g_3x4x6 = {"30163"};
    private final String[] g_3x6x0_1 = {"54383", "54384", "2419"};
    private final String[] g_3x6x1 = {"3939", "58181"};
    private final String[] g_3x6x2_2 = {"93168"};
    private final String[] g_3x6x5 = {"30613", "30366"};
    private final String[] g_3x6x10 = {"57792"};
    private final String[] g_3x8x0_1 = {"50304", "50305"};
    private final String[] g_3x8x1 = {"2397"};
    private final String[] g_3x8x2 = {"41749", "41750"};
    private final String[] g_3x8x7 = {"6083"};
    private final String[] g_3x10x1 = {"50955", "50956"};
    private final String[] g_3x12x0_1 = {"47397", "47398"};
    private final String[] g_3x12x1 = {"42060", "42061"};
    private final String[] g_3x14x2_1 = {"30296"};
    private final String[] g_4x3x3 = {"98287"};
    private final String[] g_4x3x3_2 = {"2717"};
    private final String[] g_4x4x0_1 = {"3031", "6179", "64799", "2639", "3960",
        "3935", "3936", "11833", "30503", "30565",
        "60474", "43719", "2349", "4213", "30094",
        "75937", "30033", "44570", "30516", "3403"};
    private final String[] g_4x4x0_2 = {"45677"};
    private final String[] g_4x4x1 = {"2399", "50373", "2577", "6222", "14413",
        "48092", "87081", "86500", "32324", "4854",
        "72454", "30390", "15647", "47753", "4857",
        "4855", "4858", "13349", "48933", "93348",
        "43708", "44571", "98284", "64867", "47757",
        "3404", "30658"};
    private final String[] g_4x4x1_1 = {"47758", "87750", "93589"};
    private final String[] g_4x4x1_2 = {"30208", "13754", "30286", "30342", "30294",
        "64951", "4424", "6067"};
    private final String[] g_4x4x2 = {"4742", "3943", "61487", "30056"};
    private final String[] g_4x4x3_1 = {"11598"};
    private final String[] g_4x4x3_2 = {"30139"};
    private final String[] g_4x4x4 = {"2435", "6064"};
    private final String[] g_4x4x5 = {"2680"};
    private final String[] g_4x4x6 = {"3470"};
    private final String[] g_4x4x6_1 = {"3471"};
    private final String[] g_4x4x9 = {"4844"};
    private final String[] g_4x4x11_2 = {"30338"};
    private final String[] g_4x4x12 = {"3778"};
    private final String[] g_4x5x0_1 = {"15706", "32125"};
    private final String[] g_4x5x0_2 = {"30042", "11399", "47998", "4211"};
    private final String[] g_4x5x3 = {"43121"};
    private final String[] g_4x6x0_1 = {"3032", "6180", "32059", "47407", "92099"};
    private final String[] g_4x6x0_2 = {"52031", "98281"};
    private final String[] g_4x6x1 = {"44042", "32531", "30183", "32083", "60219",
        "13269", "4856", "6153", "43712", "43713"};
    private final String[] g_4x6x1_1 = {"93591"};
    private final String[] g_4x6x1_2 = {"4238", "87612"};
    private final String[] g_4x6x2_2 = {"4237"};
    private final String[] g_4x6x8 = {"47543"};
    private final String[] g_4x7x0_2 = {"2441"};
    private final String[] g_4x7x3 = {"30250"};
    private final String[] g_4x8x0_1 = {"3035", "6576", "3933", "3934", "3474"};
    private final String[] g_4x8x0_2 = {"15625"};
    private final String[] g_4x8x1 = {"47974"};
    private final String[] g_4x8x1_1 = {"87561"};
    private final String[] g_4x8x2 = {"6066"};
    private final String[] g_4x8x2_1 = {"6066"};
    private final String[] g_4x8x3 = {"30118"};
    private final String[] g_4x9x0_1 = {"2413", "14181"};
    private final String[] g_4x10x0_1 = {"3030"};
    private final String[] g_4x10x0_2 = {"4212"};
    private final String[] g_4x10x1 = {"6212", "30181", "30076"};
    private final String[] g_4x10x2 = {"47846"};
    private final String[] g_4x10x6 = {"6082"};
    private final String[] g_4x11x1_2 = {"6007"};
    private final String[] g_4x11x2 = {"6058"};
    private final String[] g_4x12x0_1 = {"3029"};
    private final String[] g_4x12x1 = {"60033"};
    private final String[] g_4x12x3 = {"52041"};
    private final String[] g_4x16x1 = {"45301"};
    private final String[] g_4x16x16 = {"2635", "92086"};
    private final String[] g_4x18x1 = {"30400"};
    private final String[] g_5x2x0_1 = {"2508"};
    private final String[] g_5x5x1 = {"32555"};
    private final String[] g_5x5x1_1 = {"2512"};
    private final String[] g_5x5x3 = {"6065"};
    private final String[] g_5x5x3_2 = {"6040"};
    private final String[] g_5x6x2 = {"4228", "61484", "30149"};
    private final String[] g_5x9x2 = {"14455", "4080"};
    private final String[] g_6x6x0_1 = {"3958", "10202", "4285", "44375", "6003",
        "6106", "11213", "30062", "64566", "6881"};
    private final String[] g_6x6x0_2 = {"30303"};
    private final String[] g_6x6x1 = {"95188", "4509", "2876", "2626"};
    private final String[] g_6x6x1_1 = {"92547", "4597"};
    private final String[] g_6x6x2 = {"87559", "30373", "47507"};
    private final String[] g_6x6x3_1 = {"30131"};
    private final String[] g_6x8x0_1 = {"3036", "2539", "92107", "30041"};
    private final String[] g_6x8x0_2 = {"30036"};
    private final String[] g_6x8x1 = {"32532", "4515", "32084", "11295"};
    private final String[] g_6x8x2 = {"41751", "41761"};
    private final String[] g_6x8x4 = {"11293"};
    private final String[] g_6x10x0_1 = {"3033"};
    private final String[] g_6x10x1 = {"87611", "87615"};
    private final String[] g_6x10x2 = {"45705", "47406"};
    private final String[] g_6x10x4 = {"87613", "87616"};
    private final String[] g_6x12x0_1 = {"3028", "6178", "30355", "30356"};
    private final String[] g_6x12x1_1 = {"30263", "30248"};
    private final String[] g_6x12x6 = {"94531"};
    private final String[] g_6x14x0_1 = {"3456"};
    private final String[] g_6x16x0_1 = {"3027", "6205"};
    private final String[] g_6x24x0_1 = {"3026"};
    private final String[] g_6x24x0_2 = {"92340", "6584"};
    private final String[] g_6x28x0_2 = {"4093"};
    private final String[] g_6x34x2 = {"2972"};
    private final String[] g_7x4x6 = {"30134"};
    private final String[] g_7x6x0_1 = {"2625", "50303"};
    private final String[] g_7x7x2_1 = {"6072"};
    private final String[] g_7x12x0_1 = {"3585", "3586"};
    private final String[] g_8x6x2 = {"45410", "45411"};
    private final String[] g_8x8x0_1 = {"41539", "30504", "6177", "3961", "6104",
        "4152"};
    private final String[] g_8x8x0_2 = {"15624"};
    private final String[] g_8x8x1 = {"43802"};
    private final String[] g_8x8x2 = {"54091", "54095", "54096"};
    private final String[] g_8x10x1 = {"2622"};
    private final String[] g_8x12x3_1 = {"30300"};
    private final String[] g_8x12x4_2 = {"90109"};
    private final String[] g_8x16x0_1 = {"92438", "90498", "48288"};
    private final String[] g_8x16x1 = {"44041"};
    private final String[] g_8x16x2 = {"54090"};
    private final String[] g_8x16x5 = {"54923"};
    private final String[] g_8x16x7 = {"54654"};
    private final String[] g_8x24x5_2 = {"57781"};
    private final String[] g_9x10x0_1 = {"2621"};
    private final String[] g_10x10x0_1 = {"2401", "6063", "89523", "92584", "50990"};
    private final String[] g_10x10x1 = {"58846"};
    private final String[] g_10x10x2 = {"30320", "30201"};
    private final String[] g_12x8x0_1 = {"47405"};
    private final String[] g_12x12x1 = {"6162", "52040"};
    private final String[] g_12x24x1 = {"30072"};
    private final String[] g_16x14x0_1 = {"6219"};
    private final String[] g_16x16x0_1 = {"91405"};
    private final String[] g_16x16x0_2 = {"15623"};
    private final String[] g_bigwing = {"54093"};
    private final String[] g_mf_h1_2 = {"41879", "16709", "76382", "84638", "63208",
        "12896", "97149", "10677", "11938", "16478"};
    private final String[] g_mf_h2 = {"73200", "10679", "84637", "95351", "87749",
        "85863"};
    private final String[] g_mf_h2_1 = {"98376", "99778"};
    private final String[] g_mf_h3_1 = {"51345"};

    // -------------------------- STUDS COUNT GROUPS (LOGO-ON-STUD) ---------------------------
    private final String[] s_1x1x0_1 = {"3024", "6091", "6141", "4085", "60897",
        "6019", "61252", "4081", "92280", "30383",
        "15070", "6252", "4094", "4595", "4346",
        "11458", "3960"};
    private final String[] s_1x1x1 = {"3005", "4070", "87087", "47905", "2921",
        "60475", "60476", "3040", "4286", "60477",
        "3665", "4287", "76385", "3045", "3676",
        "3675", "2341", "18759", "3821", "3822",
        "3741", "6255", "4599"};
    private final String[] s_1x1x2 = {"6005", "92903", "88293", "3188", "3189",
        "3581", "3186", "60481"};
    private final String[] s_1x1x3 = {"14716", "3190"};
    private final String[] s_1x1x4 = {"30099", "3193", "3194", "3195"};
    private final String[] s_1x1x5 = {"73194", "47899"};
    private final String[] s_1x1x6 = {"12818"};
    private final String[] s_1x2x0_1 = {"85970", "13731", "3023", "44302", "44301",
        "88072", "4623", "32028", "60478", "2452",
        "63868", "2540", "48336", "60471", "99780",
        "60470", "11476", "44567", "99781", "92692",
        "3839", "4590", "99207", "2508", "18624",
        "44728", "2436", "10201", "4596", "42445",
        "93274", "15208", "4175", "3475", "98302",
        "11291", "4079", "15540", "50967", "2430",
        "2429", "51858", "15440", "93587", "18649"};
    private final String[] s_1x2x1 = {"2877", "3004", "3065", "30136", "98283",
        "3747", "3039", "3660", "30363", "3134", "4216",
        "11211", "52107", "30364", "30365", "30540",
        "30541", "2458", "30526", "30237", "95820",
        "30236", "47975", "30386", "41762", "4861",
        "14520", "40996", "50949", "4222", "47457",
        "41855", "47456", "3963", "74880", "50946",
        "98835", "93597", "3830", "3831", "3298",
        "41747", "41748"};
    private final String[] s_1x2x2 = {"3245", "6183", "2377", "3678"};
    private final String[] s_1x2x3 = {"6060", "15967"};
    private final String[] s_1x3x0_1 = {"3623", "43722", "43723"};
    private final String[] s_1x3x1 = {"3622", "4161", "3038", "6564", "6565", "4490"};
    private final String[] s_1x3x2 = {"88292"};
    private final String[] s_1x3x3 = {"13965"};
    private final String[] s_1x4x0_1 = {"6081", "3710", "41770", "41769", "44568",
        "4315", "3184", "30043", "3183", "2349",
        "98263", "30407", "30022", "92593"};
    private final String[] s_1x4x0_2 = {"61072"};
    private final String[] s_1x4x1 = {"3010", "3066", "30137", "15533", "3037",
        "3297", "4858", "30414", "30387", "41767", "41768",
        "3659", "41763", "6195", "4739", "52031"};
    private final String[] s_1x4x2 = {"4863", "61484", "30149", "2578"};
    private final String[] s_1x4x6 = {"11267"};
    private final String[] s_1x6x0_1 = {"3666", "6583", "57906", "62361"};
    private final String[] s_1x6x1 = {"3009", "3067", "30388", "3455", "3939",
        "58181"};
    private final String[] s_1x6x2 = {"30077"};
    private final String[] s_1x8x0_1 = {"3460", "4510", "30586"};
    private final String[] s_1x8x1 = {"3008", "4445"};
    private final String[] s_1x10x0_1 = {"4477"};
    private final String[] s_1x10x1 = {"6111"};
    private final String[] s_1x12x0_1 = {"60479"};
    private final String[] s_1x12x1 = {"6112"};
    private final String[] s_1x14x1 = {"4217"};
    private final String[] s_1x16x1 = {"2465"};
    private final String[] s_2x1x0_1 = {"92582", "6070", "93604", "50948", "11112",
        "11111", "11110", "11113", "11122", "15074",
        "45677"};
    private final String[] s_2x1x1 = {"92474", "64867", "47757", "47758", "30536",
        "96874", "93591", "6007"};
    private final String[] s_2x1x2 = {};
    private final String[] s_2x2x0_1 = {"2420", "3022", "4032", "90194", "48183",
        "43719", "51739", "6177", "4285", "63082",
        "3730", "15456", "3729", "3176", "3787",
        "98284", "75937", "30033", "30094", "2422",
        "4598", "62743", "99206", "4600", "6157",
        "47720", "44674", "41862", "41854", "93590",
        "4424", "2512", "3956", "3679", "98285",
        "4871", "3961"};
    private final String[] s_2x2x1 = {"30000", "6232", "57908", "17114", "57909",
        "30389", "62712", "92013", "40902", "92947",
        "6143", "3003", "6215", "2357", "3046",
        "87620", "85080", "3063", "15469", "4488",
        "10313", "98281", "30286", "30293", "98282",
        "50745", "6040", "6065", "30078", "15647",
        "30390", "6248"};
    private final String[] s_2x2x2 = {"3943", "6233", "92580", "92579", "2418",
        "4591", "54923", "4744"};
    private final String[] s_2x2x3 = {"30145", "6037"};
    private final String[] s_2x2x5 = {"74573"};
    private final String[] s_2x2x9 = {"6002"};
    private final String[] s_2x2x11 = {"75347"};
    private final String[] s_2x3x0_1 = {"3021", "3587", "30150", "98286"};
    private final String[] s_2x3x1 = {"3002", "91996"};
    private final String[] s_2x3x2 = {"4532"};
    private final String[] s_2x4x0_1 = {"3020", "3709", "98287", "3788", "30157",
        "60212", "4237", "47755", "3639", "3640", "4854", "72454", "30592"};
    private final String[] s_2x4x1 = {"3001"};
    private final String[] s_2x4x2 = {"55205", "4209"};
    private final String[] s_2x4x3 = {"30144", "97492", "30485", "4132"};
    private final String[] s_2x4x5 = {"4130"};
    private final String[] s_2x5x1 = {"11215"};
    private final String[] s_2x5x2 = {"6087", "76766"};
    private final String[] s_2x6x0_1 = {"3795", "32001", "54383", "54384", "87609",
        "93140", "90201"};
    private final String[] s_2x6x1 = {"4509", "44237"};
    private final String[] s_2x6x2 = {"2336", "17454", "4238"};
    private final String[] s_2x6x3 = {"6213"};
    private final String[] s_2x6x6 = {"6236"};
    private final String[] s_2x6x9 = {"2572"};
    private final String[] s_2x7x0_1 = {"2397"};
    private final String[] s_2x8x0_1 = {"3034", "3738"};
    private final String[] s_2x8x1 = {"3007", "93888", "4732"};
    private final String[] s_2x10x0_1 = {"3832"};
    private final String[] s_2x10x1 = {"3006"};
    private final String[] s_2x12x0_1 = {"2445"};
    private final String[] s_2x12x2 = {"30296"};
    private final String[] s_2x14x0_1 = {"91988", "15626"};
    private final String[] s_2x16x0_1 = {"4282", "45301"};
    private final String[] s_3x3x0_1 = {"11212", "15397", "2450", "30357"};
    private final String[] s_3x3x1 = {"99301", "30505", "2462"};
    private final String[] s_3x3x11 = {"2409"};
    private final String[] s_3x4x0_1 = {"88646", "3935", "3936", "4213", "44570"};
    private final String[] s_3x6x0_1 = {"2419"};
    private final String[] s_3x6x11 = {"2408"};
    private final String[] s_3x8x0_1 = {"3933", "3934", "50304", "50305", "3474"};
    private final String[] s_3x12x0_1 = {"47397", "47398"};
    private final String[] s_4x1x0_1 = {"62694", "30497", "93589", "52501"};
    private final String[] s_4x1x1 = {"15536"};
    private final String[] s_4x1x2 = {"13252", "15455", "4474"};
    private final String[] s_4x1x3 = {"32086"};
    private final String[] s_4x1x7 = {"55768"};
    private final String[] s_4x2x1 = {"46413", "47843"};
    private final String[] s_4x2x2 = {"76033"};
    private final String[] s_4x2x4 = {"87613", "11293"};
    private final String[] s_4x3x0_1 = {"44571", "87616"};
    private final String[] s_4x3x1 = {"2399", "50373"};
    private final String[] s_4x4x0_1 = {"3031", "6179", "64799", "2639", "30565",
        "60474", "30503", "11833", "47407", "15706",
        "47998", "11399", "6067", "30300", "3404",
        "30658", "60219", "4844"};
    private final String[] s_4x4x1 = {"32083", "87081", "2577", "48092", "14413"};
    private final String[] s_4x4x3 = {"4447", "60806"};
    private final String[] s_4x5x0_1 = {"30042", "4211"};
    private final String[] s_4x6x0_1 = {"3032", "6180", "32059", "92099"};
    private final String[] s_4x6x1 = {"44042"};
    private final String[] s_4x6x9 = {"2635"};
    private final String[] s_4x7x0_1 = {"2441"};
    private final String[] s_4x7x3 = {"30250"};
    private final String[] s_4x8x0_1 = {"3035", "6576", "30118"};
    private final String[] s_4x8x1 = {"47974"};
    private final String[] s_4x8x2 = {"6066"};
    private final String[] s_4x9x0_1 = {"2413", "14181"};
    private final String[] s_4x9x1 = {"87615"};
    private final String[] s_4x10x0_1 = {"30029", "4212", "3030"};
    private final String[] s_4x10x1 = {"6212", "30181"};
    private final String[] s_4x12x0_1 = {"3029", "52036"};
    private final String[] s_4x12x1 = {"60033"};
    private final String[] s_4x18x1 = {"30400"};
    private final String[] s_4x22x1 = {"2549", "30644"};
    private final String[] s_5x5x1 = {"6107"};
    private final String[] s_6x2x2 = {"30180"};
    private final String[] s_6x4x1 = {"30183"};
    private final String[] s_6x6x0_1 = {"3958", "6003", "6106", "11213", "30062",
        "2539", "30303"};
    private final String[] s_6x6x1 = {"95188", "4597", "92547"};
    private final String[] s_6x6x2 = {"87559", "47507"};
    private final String[] s_6x7x0_1 = {"2625", "50303"};
    private final String[] s_6x8x0_1 = {"3036", "6104", "92107", "30041"};
    private final String[] s_6x9x0_1 = {"90109"};
    private final String[] s_6x10x0_1 = {"3033", "30263", "30248"};
    private final String[] s_6x12x0_1 = {"3028", "6178", "30355", "30356", "30018"};
    private final String[] s_6x14x0_1 = {"3456"};
    private final String[] s_6x16x0_1 = {"3027", "6205", "52037"};
    private final String[] s_6x24x0_1 = {"3026"};
    private final String[] s_7x4x6 = {"30134"};
    private final String[] s_7x7x2 = {"6072"};
    private final String[] s_7x12x0_1 = {"3585", "3586"};
    private final String[] s_8x8x0_1 = {"41539", "30504", "4151"};
    private final String[] s_8x8x1 = {"43802", "2618"};
    private final String[] s_8x16x0_1 = {"92438"};
    private final String[] s_8x16x1 = {"44041"};
    private final String[] s_10x9x0_1 = {"2621"};
    private final String[] s_10x10x0_1 = {"6063", "89523", "2401", "92584"};
    private final String[] s_10x10x1 = {"58846"};
    private final String[] s_12x8x0_1 = {"47405"};
    private final String[] s_12x12x1 = {"6162", "52040"};
    private final String[] s_12x14x5 = {"54654"};
    private final String[] s_12x24x1 = {"30072"};
    private final String[] s_16x14x0_1 = {"6219"};
    private final String[] s_16x16x0_1 = {"91405"};
    private final String[] s_56x20x0_1 = {"54093"};
    private final String[] s_bp_8x16 = {"3865"};
    private final String[] s_bp_16x16 = {"6098", "51595"};
    private final String[] s_bp_16x32 = {"2748"};
    private final String[] s_bp_32x32 = {"3811", "30225", "44336", "44341", "44342",
        "44343", "3947"};
    private final String[] s_bp_48x48 = {"4186"};

    // ------------------------------ GRAIN ------------------------------------
    private final String[] grainySlopes = {"2449", "3039", "3040", "3045", "3046",
        "3297", "3298", "3660", "3676", "4286",
        "4460", "92946", "44336", "44341", "44342",
        "44343", "30225", "60477", "3665", "3038",
        "3037", "30363", "52501", "4871", "4161",
        "3675", "99301", "2875", "30499", "3685",
        "4445", "4861", "18759", "2341", "4854",
        "15647", "30390", "3044", "3048", "15571",
        "3300", "3043", "3049", "3299", "3747",
        "4287", "3042", "72454", "30183", "32083",
        "60219", "30249", "4509", "3947", "4858"};
    private final String[] grainyBP32x32 = {"44336", "44341", "44342", "44343",
        "30225"};
    private final String[] grainyBP16x16 = {"51595"};

    // ------------------------------ RUBBER -----------------------------------
    private final String[] rubberParts = {"3641", "87414", "42611", "92409", "50861",
        "2815", "4084", "61254", "3483", "11209",
        "87697", "6015", "4288", "56890", "30648",
        "89201", "56897", "2346", "6578", "30391",
        "58090", "92402", "3634", "2696", "56891",
        "56898", "55978", "44308", "44309", "15413",
        "6581", "6579", "32019", "55976", "41897",
        "2902", "43903", "71372", "53992", "61480",
        "44771", "88516", "11957", "2995", "45982",
        "18450", "92912", "54120", "45590"};

    /**
     * This method creates simple brick seams by shrinking individual brick
     * types.
     *
     * @param api
     * @param geoname brick's name
     * @param m4 brick's original transformation matrix
     * @param i additional float value to shrink or wide the gap more
     * @return mixture color output between color and texture
     * @throws java.io.FileNotFoundException
     */
    public Matrix4 SimpleBrickSeams(SunflowAPI api, String geoname, Matrix4 m4, float i) throws FileNotFoundException {

        float overallAdjust = i - 0.000025f;
        float LV = 0.9f;
        float HV = 0.9999f;

        wz05 = MathUtils.clamp(wz05 + (overallAdjust / 0.5f), LV, HV);
        wz1 = MathUtils.clamp(wz1 + (overallAdjust / 1f), LV, HV);
        wz2 = MathUtils.clamp(wz2 + (overallAdjust / 2f), LV, HV);
        wz3 = MathUtils.clamp(wz3 + (overallAdjust / 3f), LV, HV);
        wz4 = MathUtils.clamp(wz4 + (overallAdjust / 4f), LV, HV);
        wz5 = MathUtils.clamp(wz5 + (overallAdjust / 5f), LV, HV);
        wz6 = MathUtils.clamp(wz6 + (overallAdjust / 6f), LV, HV);
        wz7 = MathUtils.clamp(wz7 + (overallAdjust / 7f), LV, HV);
        wz8 = MathUtils.clamp(wz8 + (overallAdjust / 8f), LV, HV);
        wz9 = MathUtils.clamp(wz9 + (overallAdjust / 9f), LV, HV);
        wz10 = MathUtils.clamp(wz10 + (overallAdjust / 10f), LV, HV);
        wz11 = MathUtils.clamp(wz11 + (overallAdjust / 11f), LV, HV);
        wz12 = MathUtils.clamp(wz12 + (overallAdjust / 12f), LV, HV);
        wz13 = MathUtils.clamp(wz13 + (overallAdjust / 13f), LV, HV);
        wz14 = MathUtils.clamp(wz14 + (overallAdjust / 14f), LV, HV);
        wz15 = MathUtils.clamp(wz15 + (overallAdjust / 15f), LV, HV);
        wz16 = MathUtils.clamp(wz16 + (overallAdjust / 16f), LV, HV);
        wz18 = MathUtils.clamp(wz18 + (overallAdjust / 18f), LV, HV);
        wz24 = MathUtils.clamp(wz24 + (overallAdjust / 24f), LV, HV);
        wz28 = MathUtils.clamp(wz28 + (overallAdjust / 28f), LV, HV);
        wz34 = MathUtils.clamp(wz34 + (overallAdjust / 34f), LV, HV);
        h0_1 = MathUtils.clamp(h0_1 + (overallAdjust / 0.1f), LV, HV);
        h0_2 = MathUtils.clamp(h0_2 + (overallAdjust / 0.2f), LV, HV);
        h1 = MathUtils.clamp(h1 + (overallAdjust / 1f), LV, HV);
        h1_1 = MathUtils.clamp(h1_1 + (overallAdjust / 1.1f), LV, HV);
        h1_2 = MathUtils.clamp(h1_2 + (overallAdjust / 1.2f), LV, HV);
        h2 = MathUtils.clamp(h2 + (overallAdjust / 2f), LV, HV);
        h2_1 = MathUtils.clamp(h2_1 + (overallAdjust / 2.1f), LV, HV);
        h2_2 = MathUtils.clamp(h2_2 + (overallAdjust / 2.2f), LV, HV);
        h3 = MathUtils.clamp(h3 + (overallAdjust / 3f), LV, HV);
        h3_1 = MathUtils.clamp(h3_1 + (overallAdjust / 3.1f), LV, HV);
        h3_2 = MathUtils.clamp(h3_2 + (overallAdjust / 3.2f), LV, HV);
        h4 = MathUtils.clamp(h4 + (overallAdjust / 4f), LV, HV);
        h4_2 = MathUtils.clamp(h4_2 + (overallAdjust / 4.2f), LV, HV);
        h5 = MathUtils.clamp(h5 + (overallAdjust / 5f), LV, HV);
        h5_2 = MathUtils.clamp(h5_2 + (overallAdjust / 5.2f), LV, HV);
        h6 = MathUtils.clamp(h6 + (overallAdjust / 6f), LV, HV);
        h6_1 = MathUtils.clamp(h6_1 + (overallAdjust / 6.1f), LV, HV);
        h7 = MathUtils.clamp(h7 + (overallAdjust / 7f), LV, HV);
        h8 = MathUtils.clamp(h8 + (overallAdjust / 8f), LV, HV);
        h9 = MathUtils.clamp(h9 + (overallAdjust / 8f), LV, HV);
        h10 = MathUtils.clamp(h10 + (overallAdjust / 10f), LV, HV);
        h11_2 = MathUtils.clamp(h11_2 + (overallAdjust / 11.2f), LV, HV);
        h12 = MathUtils.clamp(h12 + (overallAdjust / 12f), LV, HV);
        h16 = MathUtils.clamp(h16 + (overallAdjust / 16f), LV, HV);

        String g = geoname.split("_")[0];
        if (g.matches("[0-9]+") && g.length() >= 4) {

            if (Arrays.asList(g_0_5x2x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h0_2, wz05));
            } else if (Arrays.asList(g_0_5x2x2).contains(g)) {
                if (g.equals("4346")) {
                    m = m4.multiply(Matrix4.scale(wz2, h2, wz05 - 0.001f)).multiply(Matrix4.translation(0f, 0f, 0.015f));
                } else {
                    m = m4.multiply(Matrix4.scale(wz2, h2, wz05));
                }
            } else if (Arrays.asList(g_0_5x3x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz3, h0_2, wz05));
            } else if (Arrays.asList(g_0_5x3x1_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz3, h1_2, wz05));
            } else if (Arrays.asList(g_0_5x3x2_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz3, h2_1, wz05));
            } else if (Arrays.asList(g_0_5x4x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h0_2, wz05));
            } else if (Arrays.asList(g_0_5x4x2_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h2_1, wz05));
            } else if (Arrays.asList(g_0_5x4x3_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h3_2, wz05));
            } else if (Arrays.asList(g_0_5x5x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h0_2, wz05));
            } else if (Arrays.asList(g_0_5x5x2_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h2_1, wz05));
            } else if (Arrays.asList(g_0_5x6x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h0_2, wz05));
            } else if (Arrays.asList(g_0_5x7x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz7, h0_2, wz05));
            } else if (Arrays.asList(g_0_5x7x4).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz7, h4, wz05));
            } else if (Arrays.asList(g_1x1x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz1, h0_1, wz1));
            } else if (Arrays.asList(g_1x1x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz1, h0_2, wz1));
            } else if (Arrays.asList(g_1x1x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz1, h1, wz1));
            } else if (Arrays.asList(g_1x1x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz1, h2, wz1));
            } else if (Arrays.asList(g_1x1x3).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz1, h3, wz1));
            } else if (Arrays.asList(g_1x1x5).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz1, h5, wz1));
            } else if (Arrays.asList(g_1x2x0_1).contains(g)) {
                if (g.equals("49668")) {
                    m = m4.multiply(Matrix4.scale(wz1, h0_1, wz2));
                } else {
                    m = m4.multiply(Matrix4.scale(wz2, h0_1, wz1));
                }
            } else if (Arrays.asList(g_1x2x0_2).contains(g)) {
                if (g.equals("61409")) {
                    m = m4.multiply(Matrix4.scale(wz1, h0_2, wz2));
                } else {
                    m = m4.multiply(Matrix4.scale(wz2, h0_2, wz1));
                }
            } else if (Arrays.asList(g_1x2x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h1, wz1));
            } else if (Arrays.asList(g_1x2x1_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h1_1, wz1));
            } else if (Arrays.asList(g_1x2x1_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h1_2, wz1));
            } else if (Arrays.asList(g_1x2x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h2, wz1));
            } else if (Arrays.asList(g_1x2x3).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h3, wz1));
            } else if (Arrays.asList(g_1x2x5).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h5, wz1));
            } else if (Arrays.asList(g_1x3x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz3, h0_1, wz1));
            } else if (Arrays.asList(g_1x3x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz3, h0_2, wz1));
            } else if (Arrays.asList(g_1x3x1).contains(g)) {
                if (g.equals("4286")) {
                    m = m4.multiply(Matrix4.scale(0.990f, h1, 0.996f));
                } else {
                    m = m4.multiply(Matrix4.scale(wz3, h1, wz1));
                }
            } else if (Arrays.asList(g_1x3x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz3, h2, wz1));
            } else if (Arrays.asList(g_1x3x2_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz3, h2_1, wz1));
            } else if (Arrays.asList(g_1x3x3).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz3, h3, wz1));
            } else if (Arrays.asList(g_1x3x5).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz3, h5, wz1));
            } else if (Arrays.asList(g_1x4x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h0_1, wz1));
            } else if (Arrays.asList(g_1x4x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h0_2, wz1));
            } else if (Arrays.asList(g_1x4x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h1, wz1));
            } else if (Arrays.asList(g_1x4x1_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h1_2, wz1));
            } else if (Arrays.asList(g_1x4x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h2, wz1));
            } else if (Arrays.asList(g_1x4x6).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h6, wz1));
            } else if (Arrays.asList(g_1x5x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h0_1, wz1));
            } else if (Arrays.asList(g_1x5x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h0_2, wz1));
            } else if (Arrays.asList(g_1x5x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h1, wz1));
            } else if (Arrays.asList(g_1x5x3).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h3, wz1));
            } else if (Arrays.asList(g_1x5x2_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h2_1, wz1));
            } else if (Arrays.asList(g_1x5x4).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h4, wz1));
            } else if (Arrays.asList(g_1x6x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h0_1, wz1));
            } else if (Arrays.asList(g_1x6x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h1, wz1));
            } else if (Arrays.asList(g_1x6x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h2, wz1));
            } else if (Arrays.asList(g_1x6x2_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h2_2, wz1));
            } else if (Arrays.asList(g_1x6x3).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h3, wz1));
            } else if (Arrays.asList(g_1x6x5).contains(g)) {
                if (g.equals("30249")) {
                    m = m4.multiply(Matrix4.scale(wz1, h5, wz6));
                } else {
                    m = m4.multiply(Matrix4.scale(wz6, h5, wz1));
                }
            } else if (Arrays.asList(g_1x6x10).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h10, wz1));
            } else if (Arrays.asList(g_1x7x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz7, h0_2, wz1));
            } else if (Arrays.asList(g_1x8x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h0_1, wz1));
            } else if (Arrays.asList(g_1x8x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h1, wz1));
            } else if (Arrays.asList(g_1x8x1_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h1_1, wz1));
            } else if (Arrays.asList(g_1x8x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h2, wz1));
            } else if (Arrays.asList(g_1x8x2_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h2_1, wz1));
            } else if (Arrays.asList(g_1x8x2_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h2_2, wz1));
            } else if (Arrays.asList(g_1x8x3).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h3, wz1));
            } else if (Arrays.asList(g_1x9x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz9, h0_2, wz1));
            } else if (Arrays.asList(g_1x9x4).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz9, h4, wz1));
            } else if (Arrays.asList(g_1x10x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h0_1, wz1));
            } else if (Arrays.asList(g_1x10x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h1, wz1));
            } else if (Arrays.asList(g_1x11x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz11, h0_2, wz1));
            } else if (Arrays.asList(g_1x12x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz12, h0_1, wz1));
            } else if (Arrays.asList(g_1x12x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz12, h1, wz1));
            } else if (Arrays.asList(g_1x12x3).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz12, h3, wz1));
            } else if (Arrays.asList(g_1x12x5).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz12, h5, wz1));
            } else if (Arrays.asList(g_1x13x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz13, h0_2, wz1));
            } else if (Arrays.asList(g_1x14x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz14, h1, wz1));
            } else if (Arrays.asList(g_1x15x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz15, h0_2, wz1));
            } else if (Arrays.asList(g_1x16x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz16, h1, wz1));
            } else if (Arrays.asList(g_2x2x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h0_1, wz2));
            } else if (Arrays.asList(g_2x2x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h0_2, wz2));
            } else if (Arrays.asList(g_2x2x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h1, wz2));
            } else if (Arrays.asList(g_2x2x1_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h1_1, wz2));
            } else if (Arrays.asList(g_2x2x1_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h1_2, wz2));
            } else if (Arrays.asList(g_2x2x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h2, wz2));
            } else if (Arrays.asList(g_2x2x3).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h3, wz2));
            } else if (Arrays.asList(g_2x2x5).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h5, wz2));
            } else if (Arrays.asList(g_2x2x7).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h7, wz2));
            } else if (Arrays.asList(g_2x2x10).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h10, wz2));
            } else if (Arrays.asList(g_2x2x16).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h16, wz2));
            } else if (Arrays.asList(g_2x3x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz3, h0_1, wz2));
            } else if (Arrays.asList(g_2x3x0_2).contains(g)) {
                if (g.equals("3729") || g.equals("15456")) {
                    m = m4.multiply(Matrix4.scale(wz2, h0_2, wz3));
                } else {
                    m = m4.multiply(Matrix4.scale(wz3, h0_2, wz2));
                }
            } else if (Arrays.asList(g_2x3x1).contains(g)) {
                if (g.equals("85943")) {
                    m = m4.multiply(Matrix4.scale(wz2, h1, wz3));
                } else {
                    m = m4.multiply(Matrix4.scale(wz3, h1, wz2));
                }
            } else if (Arrays.asList(g_2x3x1_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz3, h1_1, wz2));
            } else if (Arrays.asList(g_2x3x2).contains(g)) {
                if (g.equals("3957") || g.equals("50946")) {
                    m = m4.multiply(Matrix4.scale(wz2, h2, wz3));
                } else {
                    m = m4.multiply(Matrix4.scale(wz3, h2, wz2));
                }
            } else if (Arrays.asList(g_2x4x0_1).contains(g)) {
                if (g.equals("4596")) {
                    m = m4.multiply(Matrix4.scale(wz2, h0_1, wz4));
                } else {
                    m = m4.multiply(Matrix4.scale(wz4, h0_1, wz2));
                }
            } else if (Arrays.asList(g_2x4x0_2).contains(g)) {
                if (g.equals("47456")) {
                    m = m4.multiply(Matrix4.scale(wz2, h0_2, wz4));
                } else {
                    m = m4.multiply(Matrix4.scale(wz4, h0_2, wz2));
                }
            } else if (Arrays.asList(g_2x4x1).contains(g)) {
                if (g.equals("30363")) {
                    m = m4.multiply(Matrix4.scale(wz2, h1, wz4));
                } else {
                    m = m4.multiply(Matrix4.scale(wz4, h1, wz2));
                }
            } else if (Arrays.asList(g_2x4x1_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h1_2, wz4));
            } else if (Arrays.asList(g_2x4x2).contains(g)) {
                if (g.equals("4598")) {
                    m = m4.multiply(Matrix4.scale(wz2, h2, wz4));
                } else {
                    m = m4.multiply(Matrix4.scale(wz4, h2, wz2));
                }
            } else if (Arrays.asList(g_2x4x3).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h3, wz2));
            } else if (Arrays.asList(g_2x4x4).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h4, wz2));
            } else if (Arrays.asList(g_2x4x6).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h6, wz2));
            } else if (Arrays.asList(g_2x5x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h2, wz2));
            } else if (Arrays.asList(g_2x5x2_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h2_1, wz2));
            } else if (Arrays.asList(g_2x5x2_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h2_2, wz2));
            } else if (Arrays.asList(g_2x5x3_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h3_1, wz2));
            } else if (Arrays.asList(g_2x5x5).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h5, wz2));
            } else if (Arrays.asList(g_2x5x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h0_2, wz2));
            } else if (Arrays.asList(g_2x5x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h1, wz2));
            } else if (Arrays.asList(g_2x5x1_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h1_1, wz2));
            } else if (Arrays.asList(g_2x5x1_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h1_2, wz2));
            } else if (Arrays.asList(g_2x6x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h0_1, wz2));
            } else if (Arrays.asList(g_2x6x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h0_2, wz2));
            } else if (Arrays.asList(g_2x6x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h1, wz2));
            } else if (Arrays.asList(g_2x6x1_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h1_2, wz2));
            } else if (Arrays.asList(g_2x6x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h2, wz2));
            } else if (Arrays.asList(g_2x6x3).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h3, wz2));
            } else if (Arrays.asList(g_2x6x3_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h3_1, wz2));
            } else if (Arrays.asList(g_2x6x6).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h6, wz2));
            } else if (Arrays.asList(g_2x8x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h0_1, wz2));
            } else if (Arrays.asList(g_2x8x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h1, wz2));
            } else if (Arrays.asList(g_2x8x1_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h1_1, wz2));
            } else if (Arrays.asList(g_2x8x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h2, wz2));
            } else if (Arrays.asList(g_2x10x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h0_1, wz2));
            } else if (Arrays.asList(g_2x10x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h1, wz2));
            } else if (Arrays.asList(g_2x10x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h2, wz1));
            } else if (Arrays.asList(g_2x12x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz12, h0_1, wz2));
            } else if (Arrays.asList(g_2x12x5).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz12, h5, wz2));
            } else if (Arrays.asList(g_2x12x6).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz12, h6, wz2));
            } else if (Arrays.asList(g_2x14x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz14, h0_1, wz2));
            } else if (Arrays.asList(g_2x14x8).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz14, h8, wz2));
            } else if (Arrays.asList(g_2x16x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz16, h0_1, wz2));
            } else if (Arrays.asList(g_2x16x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz16, h1, wz2));
            } else if (Arrays.asList(g_2x16x1_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz16, h1_1, wz2));
            } else if (Arrays.asList(g_3x2x3).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h3, wz3));
            } else if (Arrays.asList(g_3x2x4).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h4, wz3));
            } else if (Arrays.asList(g_3x3x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz3, h0_1, wz3));
            } else if (Arrays.asList(g_3x3x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz3, h0_2, wz3));
            } else if (Arrays.asList(g_3x3x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz3, h1, wz3));
            } else if (Arrays.asList(g_3x3x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz3, h2, wz3));
            } else if (Arrays.asList(g_3x3x3).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz3, h3, wz3));
            } else if (Arrays.asList(g_3x4x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h0_1, wz3));
            } else if (Arrays.asList(g_3x4x0_2).contains(g)) {
                if (g.equals("93604")) {
                    m = m4.multiply(Matrix4.scale(wz3, h0_2, wz4));
                } else {
                    m = m4.multiply(Matrix4.scale(wz4, h0_2, wz3));
                }
            } else if (Arrays.asList(g_3x4x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h1, wz3));
            } else if (Arrays.asList(g_3x4x1_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h1_1, wz3));
            } else if (Arrays.asList(g_3x4x1_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h1_2, wz3));
            } else if (Arrays.asList(g_3x4x6).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h6, wz3));
            } else if (Arrays.asList(g_3x6x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h0_1, wz3));
            } else if (Arrays.asList(g_3x6x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h1, wz3));
            } else if (Arrays.asList(g_3x6x2_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h2_2, wz3));
            } else if (Arrays.asList(g_3x6x5).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h5, wz3));
            } else if (Arrays.asList(g_3x6x10).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h10, wz3));
            } else if (Arrays.asList(g_3x8x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h0_1, wz3));
            } else if (Arrays.asList(g_3x8x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h1, wz3));
            } else if (Arrays.asList(g_3x8x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h2, wz3));
            } else if (Arrays.asList(g_3x8x7).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h7, wz3));
            } else if (Arrays.asList(g_3x10x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h1, wz3));
            } else if (Arrays.asList(g_3x12x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz12, h0_1, wz3));
            } else if (Arrays.asList(g_3x12x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz12, h1, wz3));
            } else if (Arrays.asList(g_3x14x2_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz14, h2_1, wz3));
            } else if (Arrays.asList(g_4x3x3).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz3, h3, wz4));
            } else if (Arrays.asList(g_4x3x3_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz3, h3_2, wz4));
            } else if (Arrays.asList(g_4x4x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h0_1, wz4));
            } else if (Arrays.asList(g_4x4x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h0_2, wz4));
            } else if (Arrays.asList(g_4x4x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h1, wz4));
            } else if (Arrays.asList(g_4x4x1_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h1_2, wz4));
            } else if (Arrays.asList(g_4x4x1_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h1_1, wz4));
            } else if (Arrays.asList(g_4x4x3_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h3_1, wz4));
            } else if (Arrays.asList(g_4x4x3_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h3_2, wz4));
            } else if (Arrays.asList(g_4x4x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h2, wz4));
            } else if (Arrays.asList(g_4x4x4).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h4, wz4));
            } else if (Arrays.asList(g_4x4x5).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h5, wz4));
            } else if (Arrays.asList(g_4x4x6).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h6, wz4));
            } else if (Arrays.asList(g_4x4x6_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h6_1, wz4));
            } else if (Arrays.asList(g_4x4x9).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h9, wz4));
            } else if (Arrays.asList(g_4x4x11_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h11_2, wz4));
            } else if (Arrays.asList(g_4x4x12).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h12, wz4));
            } else if (Arrays.asList(g_4x5x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h0_1, wz4));
            } else if (Arrays.asList(g_4x5x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h0_2, wz4));
            } else if (Arrays.asList(g_4x5x3).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h3, wz4));
            } else if (Arrays.asList(g_4x6x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h0_1, wz4));
            } else if (Arrays.asList(g_4x6x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h0_2, wz4));
            } else if (Arrays.asList(g_4x6x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h1, wz4));
            } else if (Arrays.asList(g_4x6x1_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h1_1, wz4));
            } else if (Arrays.asList(g_4x6x1_2).contains(g)) {
                if (g.equals("87612")) {
                    m = m4.multiply(Matrix4.scale(wz4, h1_2, wz6));
                } else {
                    m = m4.multiply(Matrix4.scale(wz6, h1_2, wz4));
                }
            } else if (Arrays.asList(g_4x6x2_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h2_2, wz4));
            } else if (Arrays.asList(g_4x6x8).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h8, wz4));
            } else if (Arrays.asList(g_4x7x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz7, h0_2, wz4));
            } else if (Arrays.asList(g_4x7x3).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz7, h3, wz4));
            } else if (Arrays.asList(g_4x8x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h0_1, wz4));
            } else if (Arrays.asList(g_4x8x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h0_2, wz4));
            } else if (Arrays.asList(g_4x8x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h1, wz4));
            } else if (Arrays.asList(g_4x8x1_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h1_1, wz4));
            } else if (Arrays.asList(g_4x8x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h2, wz4));
            } else if (Arrays.asList(g_4x8x2_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h2_1, wz4));
            } else if (Arrays.asList(g_4x8x3).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h3, wz4));
            } else if (Arrays.asList(g_4x9x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz9, h0_1, wz4));
            } else if (Arrays.asList(g_4x10x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h0_1, wz4));
            } else if (Arrays.asList(g_4x10x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h0_2, wz4));
            } else if (Arrays.asList(g_4x10x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h1, wz4));
            } else if (Arrays.asList(g_4x10x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h2, wz4));
            } else if (Arrays.asList(g_4x10x6).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h6, wz4));
            } else if (Arrays.asList(g_4x11x1_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz11, h1_2, wz4));
            } else if (Arrays.asList(g_4x11x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz11, h2, wz4));
            } else if (Arrays.asList(g_4x12x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz12, h0_1, wz4));
            } else if (Arrays.asList(g_4x12x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz12, h1, wz4));
            } else if (Arrays.asList(g_4x12x3).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz12, h3, wz4));
            } else if (Arrays.asList(g_4x16x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz16, h1, wz4));
            } else if (Arrays.asList(g_4x16x16).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz16, h16, wz4));
            } else if (Arrays.asList(g_4x18x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz18, h1, wz4));
            } else if (Arrays.asList(g_5x2x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz2, h0_1, wz5));
            } else if (Arrays.asList(g_5x5x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h1, wz5));
            } else if (Arrays.asList(g_5x5x1_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h1_1, wz5));
            } else if (Arrays.asList(g_5x5x3).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h3, wz5));
            } else if (Arrays.asList(g_5x5x3_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz5, h3_2, wz5));
            } else if (Arrays.asList(g_5x6x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h2, wz5));
            } else if (Arrays.asList(g_5x9x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz9, h2, wz5));
            } else if (Arrays.asList(g_6x6x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h0_1, wz6));
            } else if (Arrays.asList(g_6x6x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h0_2, wz6));
            } else if (Arrays.asList(g_6x6x1_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h1_1, wz6));
            } else if (Arrays.asList(g_6x6x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h1, wz6));
            } else if (Arrays.asList(g_6x6x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h2, wz6));
            } else if (Arrays.asList(g_6x6x3_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h3_1, wz6));
            } else if (Arrays.asList(g_6x8x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h0_1, wz6));
            } else if (Arrays.asList(g_6x8x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h0_2, wz6));
            } else if (Arrays.asList(g_6x8x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h1, wz6));
            } else if (Arrays.asList(g_6x8x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h2, wz6));
            } else if (Arrays.asList(g_6x8x4).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h4, wz6));
            } else if (Arrays.asList(g_6x10x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h0_1, wz6));
            } else if (Arrays.asList(g_6x10x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h1, wz6));
            } else if (Arrays.asList(g_6x10x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h2, wz6));
            } else if (Arrays.asList(g_6x10x4).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h4, wz6));
            } else if (Arrays.asList(g_6x12x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz12, h0_1, wz6));
            } else if (Arrays.asList(g_6x12x1_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz12, h1_1, wz6));
            } else if (Arrays.asList(g_6x12x6).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz12, h6, wz6));
            } else if (Arrays.asList(g_6x14x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz14, h0_1, wz6));
            } else if (Arrays.asList(g_6x16x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz16, h0_1, wz6));
            } else if (Arrays.asList(g_6x24x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz24, h0_1, wz6));
            } else if (Arrays.asList(g_6x24x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz24, h0_2, wz6));
            } else if (Arrays.asList(g_6x28x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz28, h0_2, wz6));
            } else if (Arrays.asList(g_6x34x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz34, h2, wz6));
            } else if (Arrays.asList(g_7x4x6).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz4, h6, wz7));
            } else if (Arrays.asList(g_7x6x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h0_1, wz7));
            } else if (Arrays.asList(g_7x7x2_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz7, h2_1, wz7));
            } else if (Arrays.asList(g_7x12x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz12, h0_1, wz7));
            } else if (Arrays.asList(g_8x6x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz6, h2, wz8));
            } else if (Arrays.asList(g_8x8x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h0_1, wz8));
            } else if (Arrays.asList(g_8x8x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h0_2, wz8));
            } else if (Arrays.asList(g_8x8x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h1, wz8));
            } else if (Arrays.asList(g_8x8x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h2, wz8));
            } else if (Arrays.asList(g_8x10x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h1, wz8));
            } else if (Arrays.asList(g_8x12x3_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz12, h3_1, wz8));
            } else if (Arrays.asList(g_8x12x4_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz12, h4_2, wz8));
            } else if (Arrays.asList(g_8x16x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz16, h0_1, wz8));
            } else if (Arrays.asList(g_8x16x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz16, h1, wz8));
            } else if (Arrays.asList(g_8x16x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz16, h2, wz8));
            } else if (Arrays.asList(g_8x16x5).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz16, h5, wz8));
            } else if (Arrays.asList(g_8x16x7).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz16, h7, wz8));
            } else if (Arrays.asList(g_8x24x5_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz24, h5_2, wz8));
            } else if (Arrays.asList(g_9x10x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h0_1, wz9));
            } else if (Arrays.asList(g_10x10x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h0_1, wz10));
            } else if (Arrays.asList(g_10x10x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h1, wz10));
            } else if (Arrays.asList(g_10x10x2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz10, h2, wz10));
            } else if (Arrays.asList(g_12x8x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz8, h0_1, wz12));
            } else if (Arrays.asList(g_12x12x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz12, h1, wz12));
            } else if (Arrays.asList(g_12x24x1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz24, h1, wz12));
            } else if (Arrays.asList(g_16x14x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz14, h0_1, wz16));
            } else if (Arrays.asList(g_16x16x0_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz16, h0_1, wz16));
            } else if (Arrays.asList(g_16x16x0_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(wz16, h0_2, wz16));
            } else if (Arrays.asList(g_bigwing).contains(g)) {
                m = m4.multiply(Matrix4.scale(1f, h0_2, 1f));
            } else if (Arrays.asList(g_mf_h1_2).contains(g)) {
                m = m4.multiply(Matrix4.scale(1f, h1_2, 1f));
            } else if (Arrays.asList(g_mf_h2).contains(g)) {
                m = m4.multiply(Matrix4.scale(1f, h2, 1f));
            } else if (Arrays.asList(g_mf_h2_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(1f, h2_1, 1f));
            } else if (Arrays.asList(g_mf_h3_1).contains(g)) {
                m = m4.multiply(Matrix4.scale(1f, h3_1, 1f));

                // OTHER OBJECTS ARE NOT MODIFIED
            } else {
                m = m4;
            }

            // RETURNS NEW MATRIX + BRICK SHIFTED A TINY BIT ON X & Z AXES
            float shiftX = 0.003f;
            float shiftY = 0.0f;
            float shiftZ = 0.003f;

            if (g.equals("2817")) {
                return m.multiply(Matrix4.translation(shiftX, shiftY - 0.004f, shiftZ));
            } else {
                return m.multiply(Matrix4.translation(shiftX, shiftY, shiftZ));
            }

        } else {
            // anything else will return original matrix back
            return m4;
        }
    }

    /**
     * Adds word "LEGO" to every brick stud.
     *
     * @param api
     * @param geoname used geometry
     * @param shdr used shader
     * @param mLDD brick matrix
     * @param i
     */
    public void LogoOnStuds(SunflowAPI api, String geoname, String shdr, Matrix4 mLDD, float i) {
        String g = geoname.split("_")[0];
        if (g.matches("[0-9]+") && g.length() >= 4) {

            if (Arrays.asList(s_1x1x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x1x0.1", i, mLDD);
            } else if (Arrays.asList(s_1x1x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x1x1", i, mLDD);
            } else if (Arrays.asList(s_1x1x2).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x1x2", i, mLDD);
            } else if (Arrays.asList(s_1x1x3).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x1x3", i, mLDD);
            } else if (Arrays.asList(s_1x1x4).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x1x4", i, mLDD);
            } else if (Arrays.asList(s_1x1x5).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x1x5", i, mLDD);
            } else if (Arrays.asList(s_1x1x6).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x1x6", i, mLDD);
            } else if (Arrays.asList(s_1x2x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x2x0.1", i, mLDD);
            } else if (Arrays.asList(s_1x2x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x2x1", i, mLDD);
            } else if (Arrays.asList(s_1x2x2).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x2x2", i, mLDD);
            } else if (Arrays.asList(s_1x2x3).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x2x3", i, mLDD);
            } else if (Arrays.asList(s_1x3x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x3x0.1", i, mLDD);
            } else if (Arrays.asList(s_1x3x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x3x1", i, mLDD);
            } else if (Arrays.asList(s_1x3x2).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x3x2", i, mLDD);
            } else if (Arrays.asList(s_1x3x3).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x3x3", i, mLDD);
            } else if (Arrays.asList(s_1x4x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x4x0.1", i, mLDD);
            } else if (Arrays.asList(s_1x4x0_2).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x4x0.2", i, mLDD);
            } else if (Arrays.asList(s_1x4x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x4x1", i, mLDD);
            } else if (Arrays.asList(s_1x4x2).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x4x2", i, mLDD);
            } else if (Arrays.asList(s_1x4x6).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x4x6", i, mLDD);
            } else if (Arrays.asList(s_1x6x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x6x0.1", i, mLDD);
            } else if (Arrays.asList(s_1x6x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x6x1", i, mLDD);
            } else if (Arrays.asList(s_1x6x2).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x6x2", i, mLDD);
            } else if (Arrays.asList(s_1x8x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x8x0.1", i, mLDD);
            } else if (Arrays.asList(s_1x8x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x8x1", i, mLDD);
            } else if (Arrays.asList(s_1x10x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x10x0.1", i, mLDD);
            } else if (Arrays.asList(s_1x10x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x10x1", i, mLDD);
            } else if (Arrays.asList(s_1x12x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x12x0.1", i, mLDD);
            } else if (Arrays.asList(s_1x12x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x12x1", i, mLDD);
            } else if (Arrays.asList(s_1x14x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x14x1", i, mLDD);
            } else if (Arrays.asList(s_1x16x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "1x16x1", i, mLDD);
            } else if (Arrays.asList(s_2x1x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x1x0.1", i, mLDD);
            } else if (Arrays.asList(s_2x1x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x1x1", i, mLDD);
            } else if (Arrays.asList(s_2x1x2).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x1x2", i, mLDD);
            } else if (Arrays.asList(s_2x2x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x2x0.1", i, mLDD);
            } else if (Arrays.asList(s_2x2x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x2x1", i, mLDD);
            } else if (Arrays.asList(s_2x2x2).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x2x2", i, mLDD);
            } else if (Arrays.asList(s_2x2x3).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x2x3", i, mLDD);
            } else if (Arrays.asList(s_2x2x5).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x2x5", i, mLDD);
            } else if (Arrays.asList(s_2x2x9).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x2x9", i, mLDD);
            } else if (Arrays.asList(s_2x2x11).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x2x11", i, mLDD);
            } else if (Arrays.asList(s_2x3x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x3x0.1", i, mLDD);
            } else if (Arrays.asList(s_2x3x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x3x1", i, mLDD);
            } else if (Arrays.asList(s_2x3x2).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x3x2", i, mLDD);
            } else if (Arrays.asList(s_2x4x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x4x0.1", i, mLDD);
            } else if (Arrays.asList(s_2x4x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x4x1", i, mLDD);
            } else if (Arrays.asList(s_2x4x2).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x4x2", i, mLDD);
            } else if (Arrays.asList(s_2x4x3).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x4x3", i, mLDD);
            } else if (Arrays.asList(s_2x4x5).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x4x5", i, mLDD);
            } else if (Arrays.asList(s_2x5x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x5x1", i, mLDD);
            } else if (Arrays.asList(s_2x5x2).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x5x2", i, mLDD);
            } else if (Arrays.asList(s_2x6x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x6x0.1", i, mLDD);
            } else if (Arrays.asList(s_2x6x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x6x1", i, mLDD);
            } else if (Arrays.asList(s_2x6x2).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x6x2", i, mLDD);
            } else if (Arrays.asList(s_2x6x3).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x6x3", i, mLDD);
            } else if (Arrays.asList(s_2x6x6).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x6x6", i, mLDD);
            } else if (Arrays.asList(s_2x6x9).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x6x9", i, mLDD);
            } else if (Arrays.asList(s_2x7x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x7x0.1", i, mLDD);
            } else if (Arrays.asList(s_2x8x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x8x0.1", i, mLDD);
            } else if (Arrays.asList(s_2x8x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x8x1", i, mLDD);
            } else if (Arrays.asList(s_2x10x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x10x0.1", i, mLDD);
            } else if (Arrays.asList(s_2x10x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x10x1", i, mLDD);
            } else if (Arrays.asList(s_2x12x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x12x0.1", i, mLDD);
            } else if (Arrays.asList(s_2x12x2).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x12x2", i, mLDD);
            } else if (Arrays.asList(s_2x14x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x14x0.1", i, mLDD);
            } else if (Arrays.asList(s_2x16x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "2x16x0.1", i, mLDD);
            } else if (Arrays.asList(s_3x3x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "3x3x0.1", i, mLDD);
            } else if (Arrays.asList(s_3x3x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "3x3x1", i, mLDD);
            } else if (Arrays.asList(s_3x3x11).contains(g)) {
                LOSloop(api, shdr, geoname, g, "3x3x11", i, mLDD);
            } else if (Arrays.asList(s_3x4x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "3x4x0.1", i, mLDD);
            } else if (Arrays.asList(s_3x6x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "3x6x0.1", i, mLDD);
            } else if (Arrays.asList(s_3x6x11).contains(g)) {
                LOSloop(api, shdr, geoname, g, "3x6x11", i, mLDD);
            } else if (Arrays.asList(s_3x8x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "3x8x0.1", i, mLDD);
            } else if (Arrays.asList(s_3x12x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "3x12x0.1", i, mLDD);
            } else if (Arrays.asList(s_4x1x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x1x0.1", i, mLDD);
            } else if (Arrays.asList(s_4x1x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x1x1", i, mLDD);
            } else if (Arrays.asList(s_4x1x2).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x1x2", i, mLDD);
            } else if (Arrays.asList(s_4x1x3).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x1x3", i, mLDD);
            } else if (Arrays.asList(s_4x1x7).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x1x7", i, mLDD);
            } else if (Arrays.asList(s_4x2x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x2x1", i, mLDD);
            } else if (Arrays.asList(s_4x2x2).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x2x2", i, mLDD);
            } else if (Arrays.asList(s_4x2x4).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x2x4", i, mLDD);
            } else if (Arrays.asList(s_4x3x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x3x0.1", i, mLDD);
            } else if (Arrays.asList(s_4x3x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x3x1", i, mLDD);
            } else if (Arrays.asList(s_4x4x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x4x0.1", i, mLDD);
            } else if (Arrays.asList(s_4x4x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x4x1", i, mLDD);
            } else if (Arrays.asList(s_4x4x3).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x4x3", i, mLDD);
            } else if (Arrays.asList(s_4x5x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x5x0.1", i, mLDD);
            } else if (Arrays.asList(s_4x6x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x6x0.1", i, mLDD);
            } else if (Arrays.asList(s_4x6x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x6x1", i, mLDD);
            } else if (Arrays.asList(s_4x6x9).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x6x9", i, mLDD);
            } else if (Arrays.asList(s_4x7x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x7x0.1", i, mLDD);
            } else if (Arrays.asList(s_4x7x3).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x7x3", i, mLDD);
            } else if (Arrays.asList(s_4x8x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x8x0.1", i, mLDD);
            } else if (Arrays.asList(s_4x8x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x8x1", i, mLDD);
            } else if (Arrays.asList(s_4x8x2).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x8x2", i, mLDD);
            } else if (Arrays.asList(s_4x9x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x9x0.1", i, mLDD);
            } else if (Arrays.asList(s_4x9x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x9x1", i, mLDD);
            } else if (Arrays.asList(s_4x10x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x10x0.1", i, mLDD);
            } else if (Arrays.asList(s_4x10x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x10x1", i, mLDD);
            } else if (Arrays.asList(s_4x12x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x12x0.1", i, mLDD);
            } else if (Arrays.asList(s_4x12x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x12x1", i, mLDD);
            } else if (Arrays.asList(s_4x18x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x18x1", i, mLDD);
            } else if (Arrays.asList(s_4x22x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "4x22x1", i, mLDD);
            } else if (Arrays.asList(s_5x5x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "5x5x1", i, mLDD);
            } else if (Arrays.asList(s_6x2x2).contains(g)) {
                LOSloop(api, shdr, geoname, g, "6x2x2", i, mLDD);
            } else if (Arrays.asList(s_6x4x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "6x4x1", i, mLDD);
            } else if (Arrays.asList(s_6x6x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "6x6x0.1", i, mLDD);
            } else if (Arrays.asList(s_6x6x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "6x6x1", i, mLDD);
            } else if (Arrays.asList(s_6x6x2).contains(g)) {
                LOSloop(api, shdr, geoname, g, "6x6x2", i, mLDD);
            } else if (Arrays.asList(s_6x7x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "6x7x0.1", i, mLDD);
            } else if (Arrays.asList(s_6x8x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "6x8x0.1", i, mLDD);
            } else if (Arrays.asList(s_6x9x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "6x9x0.1", i, mLDD);
            } else if (Arrays.asList(s_6x10x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "6x10x0.1", i, mLDD);
            } else if (Arrays.asList(s_6x12x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "6x12x0.1", i, mLDD);
            } else if (Arrays.asList(s_6x14x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "6x14x0.1", i, mLDD);
            } else if (Arrays.asList(s_6x16x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "6x16x0.1", i, mLDD);
            } else if (Arrays.asList(s_6x24x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "6x24x0.1", i, mLDD);
            } else if (Arrays.asList(s_7x4x6).contains(g)) {
                LOSloop(api, shdr, geoname, g, "7x4x6", i, mLDD);
            } else if (Arrays.asList(s_7x7x2).contains(g)) {
                LOSloop(api, shdr, geoname, g, "7x7x2", i, mLDD);
            } else if (Arrays.asList(s_7x12x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "7x12x0.1", i, mLDD);
            } else if (Arrays.asList(s_8x8x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "8x8x0.1", i, mLDD);
            } else if (Arrays.asList(s_8x8x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "8x8x1", i, mLDD);
            } else if (Arrays.asList(s_8x16x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "8x16x0.1", i, mLDD);
            } else if (Arrays.asList(s_8x16x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "8x16x1", i, mLDD);
            } else if (Arrays.asList(s_10x9x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "10x9x0.1", i, mLDD);
            } else if (Arrays.asList(s_10x10x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "10x10x0.1", i, mLDD);
            } else if (Arrays.asList(s_10x10x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "10x10x1", i, mLDD);
            } else if (Arrays.asList(s_12x8x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "12x8x0.1", i, mLDD);
            } else if (Arrays.asList(s_12x12x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "12x12x1", i, mLDD);
            } else if (Arrays.asList(s_12x14x5).contains(g)) {
                LOSloop(api, shdr, geoname, g, "12x14x5", i, mLDD);
            } else if (Arrays.asList(s_12x24x1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "12x24x1", i, mLDD);
            } else if (Arrays.asList(s_16x14x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "16x14x0.1", i, mLDD);
            } else if (Arrays.asList(s_16x16x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "16x16x0.1", i, mLDD);
            } else if (Arrays.asList(s_56x20x0_1).contains(g)) {
                LOSloop(api, shdr, geoname, g, "56x20x0.1", i, mLDD);
            } else if (Arrays.asList(s_bp_8x16).contains(g)) {
                LOSloop(api, shdr, geoname, g, "8x16x0.05", i, mLDD);
            } else if (Arrays.asList(s_bp_16x16).contains(g)) {
                LOSloop(api, shdr, geoname, g, "16x16x0.05", i, mLDD);
            } else if (Arrays.asList(s_bp_16x32).contains(g)) {
                LOSloop(api, shdr, geoname, g, "16x32x0.05", i, mLDD);
            } else if (Arrays.asList(s_bp_32x32).contains(g)) {
                if (geoname.equals("3947_crater")) {
                } else {
                    LOSloop(api, shdr, geoname, g, "32x32x0.05", i, mLDD);
                }
            } else if (Arrays.asList(s_bp_48x48).contains(g)) {
                LOSloop(api, shdr, geoname, g, "48x48x0.05", i, mLDD);
            }
        }
    }

    private void LOSloop(SunflowAPI api, String shdr, String geoname, String g, String v, float fv, Matrix4 mLDD) {

        m = mLDD;
        String[] vals = v.split("x");
        int ROWS = parseInt(vals[0]);
        int COLS = parseInt(vals[1]);
        float overallAdjustY = fv + 0.005f;
        float HEIGHT = parseFloat(vals[2]);
        float offsetY = 0.0125f;
        float studH = 0.145f;
        float plateH = 0.457f;
        float brickH = 1.104f;
        float oneThird = plateH - studH + offsetY;
        float sORIG = 0.84f;
        float tnORIG = 0.8f;
        float tx = 0.0f;
        float ty;
        if (HEIGHT < 1) {
            ty = (HEIGHT == 0.05f) ? plateH / 3.3f : plateH;
        } else {
            ty = (brickH * HEIGHT) - (studH * (HEIGHT - 1));
        }
        float tz = -0.03f;
        float ty0_2 = ty - plateH + studH - offsetY;

        class LOS {

            private void add(int i, int j) {

                float s = sORIG;
                float tn = tnORIG;

                if (g.equals("3947")) {
                    s = s / 4;
                    tn = tn / 4;
                }

                Matrix4 m4 = Matrix4.IDENTITY;
                Matrix4 t;

                // 1. scale
                t = Matrix4.scale((float) s);
                m4 = t.multiply(m4);

                // 2. rotate on Y axis
                if (g.equals("4346")) {
                    t = Matrix4.rotateY((float) Math.toRadians((float) 0));
                } else if (g.equals("4595")) {
                    t = Matrix4.rotateY((float) Math.toRadians((float) 45));
                } else if (g.equals("3676") || g.equals("3660") || g.equals("3665") || g.equals("4287")
                        || g.equals("3747") || g.equals("18759") || g.equals("2341") || g.equals("6248")
                        || g.equals("30183") || g.equals("3947")) {
                    t = Matrix4.rotateY((float) Math.toRadians((float) 90));
                } else if (g.equals("3956") || g.equals("30022") || (g.equals("15626") && (j < 3 || j > 10))) {
                    t = Matrix4.rotateY((float) Math.toRadians((float) -90));
                } else {
                    t = Matrix4.rotateY((float) Math.toRadians((float) 135));
                }
                m4 = t.multiply(m4);

                // 4. rotate on X axis
                if (g.equals("3956") || g.equals("4346") || g.equals("30022") || (g.equals("15626") && (j < 3 || j > 10))) {
                    t = Matrix4.rotateX((float) Math.toRadians((float) 90));
                } else if (g.equals("6248")) {
                    t = Matrix4.rotateX((float) Math.toRadians((float) -90));
                }
                m4 = t.multiply(m4);

                // 5. translate
                switch (g) {
                    case "15397":
                    case "54384":
                    case "11833":
                    case "98282":
                    case "50745":
                    case "2420":
                    case "3586":
                        t = Matrix4.translation(tx + (tn * j), ty + overallAdjustY, tz - (tn * (i - 1)));
                        break;
                    case "30505":
                    case "30181":
                    case "95188":
                    case "2639":
                    case "2450":
                    case "30357":
                    case "11213":
                    case "30062":
                    case "2419":
                    case "3936":
                    case "3933":
                    case "47397":
                    case "50305":
                    case "2539":
                    case "3474":
                        t = Matrix4.translation(tx + (tn * j), ty + overallAdjustY, tz - (tn * (i - 2)));
                        break;
                    case "2577":
                    case "58846":
                    case "30565":
                    case "30503":
                    case "32059":
                    case "6063":
                    case "89523":
                        t = Matrix4.translation(tx + (tn * j), ty + overallAdjustY, tz - (tn * (i - 3)));
                        break;
                    case "6003":
                    case "6106":
                    case "30355":
                        t = Matrix4.translation(tx + (tn * j), ty + overallAdjustY, tz - (tn * (i - 5)));
                        break;
                    case "30504":
                        t = Matrix4.translation(tx + (tn * j), ty + overallAdjustY, tz - (tn * (i - 7)));
                        break;
                    case "2401":
                    case "92584":
                        t = Matrix4.translation(tx + (tn * j), ty + overallAdjustY, tz - (tn * (i - 9)));
                        break;
                    case "6162":
                        t = Matrix4.translation(tx + (tn * j), ty + overallAdjustY, tz - (tn * (i - 11)));
                        break;
                    case "4213":
                        t = Matrix4.translation(tx + (tn * j), ty + overallAdjustY, tz - (tn * (i + 0.5f)));
                        break;
                    case "47407":
                    case "98287":
                    case "32086":
                    case "64867":
                    case "47757":
                    case "93604":
                    case "47758":
                    case "4237":
                    case "93587":
                        t = Matrix4.translation(tx + (tn * j), ty + overallAdjustY, tz - (tn * (i + 1)));
                        break;
                    case "45301": {
                        float y = (j < 4) ? ty + (plateH * 2) - studH - 0.125f : ty;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * (i + 1)));
                        break;
                    }
                    case "30485":
                    case "12818":
                    case "93597":
                    case "30180":
                        t = Matrix4.translation(tx + (tn * j), ty + overallAdjustY, tz - (tn * (i + 2)));
                        break;
                    case "6002":
                    case "2572":
                        t = Matrix4.translation(tx + (tn * j), ty + overallAdjustY, tz - (tn * (i + 4)));
                        break;
                    case "2408":
                    case "2409":
                        t = Matrix4.translation(tx + (tn * j), ty + overallAdjustY, tz - (tn * (i + 7)));
                        break;
                    case "4861":
                        t = Matrix4.translation(tx + (-tn * j), ty + overallAdjustY, tz - (tn * i));
                        break;
                    case "2357":
                    case "3046":
                    case "87620":
                        t = Matrix4.translation(tx + (tn * j), ty + overallAdjustY, tz + (tn * i));
                        break;
                    case "87081":
                    case "60474":
                        t = Matrix4.translation(tx + (tn * j), ty + overallAdjustY, tz + (tn * (i - 2)));
                        break;
                    case "15967":
                    case "6060":
                    case "76033":
                    case "41747":
                    case "41748":
                    case "30099":
                        t = Matrix4.translation(tx + (tn * (j + 4)), ty + overallAdjustY, tz - (tn * i));
                        break;
                    case "4858":
                        t = Matrix4.translation(tx + (tn * (j - 3)), ty + overallAdjustY, tz - (tn * i));
                        break;
                    case "6005":
                    case "92903":
                        t = Matrix4.translation(tx + (tn * (j + 2)), (ty - (plateH - studH)) + overallAdjustY, tz - (tn * i));
                        break;
                    case "6183":
                    case "2418":
                    case "98285":
                        t = Matrix4.translation(tx + (tn * (j + 2)), ty + overallAdjustY, tz - (tn * i));
                        break;
                    case "88292": {
                        float y = (j == 0) ? brickH : ty;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "13965": {
                        float y = (j == 0) ? ty - (brickH - studH) : ty;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "3943":
                    case "30150":
                        t = Matrix4.translation(tx + (tn * (j + 0.5f)), ty + overallAdjustY, tz - (tn * (i + 0.5f)));
                        break;
                    case "75347":
                        t = Matrix4.translation(tx + (tn * j), (ty + 0.005f) + overallAdjustY, tz - (tn * i));
                        break;
                    case "2399": {
                        float y = (j > 0) ? ty - (studH * 2) - 0.06f : ty;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "50373": {
                        float y = (j > 0) ? ty - (studH * 2) - 0.033f : ty;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "6037":
                    case "61072":
                        t = Matrix4.translation(tx + (tn * j), (ty + (plateH - studH) + 0.008f) + overallAdjustY, tz - (tn * i));
                        break;
                    case "6087":
                    case "76766":
                    case "11215": {
                        float y = (j < 2) ? plateH : ty + (plateH - studH);
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "4732": {
                        float y = (j > 1 && j < 5) ? plateH : ty + (plateH - studH);
                        t = Matrix4.translation(tx + (tn * (j - 1)), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "4597": {
                        float y = (i == 0 || i == 5 || j == 0 || j == 5) ? ty + (plateH - studH) : plateH;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * (i - 1)));
                        break;
                    }
                    case "47507": {
                        float y = (i == 0 || i == 5 || j == 0 || j == 5) ? ty : plateH;
                        t = Matrix4.translation(tx + (tn * (j - 1)), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "30250": {
                        float y;
                        if (j > 1) {
                            y = plateH;
                        } else if ((i == 1 && j < 2) || (i == 2 && j < 2)) {
                            y = brickH;
                        } else {
                            y = ty;
                        }
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "2336": {
                        float y = (j < 4) ? brickH - (offsetY / 2) : (plateH * 2) - studH + offsetY;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "6072": {
                        float y;
                        if ((i > 0 && j < 3) || (i == 2 && j < 4) || (i == 3 && j < 5) || (i > 3 && j < 6)) {
                            y = plateH;
                        } else if ((i == 0 && j == 1) || (i == 1 && j == 3) || (i == 3 && j == 5) || (i == 5 && j == 6)) {
                            y = brickH + (plateH - studH);
                        } else {
                            y = ty + (plateH - studH);
                        }
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "6066": {
                        float y;
                        if ((i == 1 && j > 1 && j < 6) || (i > 1 && j > 0 && j < 7)) {
                            y = plateH;
                        } else if ((i == 0 && j == 2) || (i == 0 && j == 5) || (i == 2 && j == 0) || (i == 2 && j == 7)) {
                            y = brickH + (plateH - studH);
                        } else {
                            y = ty + (plateH - studH);
                        }
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * (i - 2)));
                        break;
                    }
                    case "90194":
                    case "48183":
                    case "2512":
                        t = Matrix4.translation(tx + (tn * (j + 1)), ty + overallAdjustY, tz - (tn * (i + 1)));
                        break;
                    case "51739":
                        t = Matrix4.translation(tx + (tn * (j + 1)), ty + overallAdjustY, tz - (tn * (i - 1)));
                        break;
                    case "43719":
                    case "6177":
                    case "30042":
                        t = Matrix4.translation(tx + (tn * (j + 2)), ty + overallAdjustY, tz - (tn * (i + 1)));
                        break;
                    case "30118": {
                        float y = ((i == 1 && j == 7) || (i == 2 && j == 7)) ? (brickH * 3) + (studH / 6f) : plateH;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "15706": {
                        float x;
                        float z;
                        if (i == 1 && j == 0) {
                            x = (tn / 2) * -1;
                            z = ((tn / 4) - 0.03f) * -1;
                        } else if (i == 2 && j == 0) {
                            x = 0.15f;
                            z = 0.07f;
                        } else if (i == 3 && j == 1) {
                            x = -0.075f;
                            z = 0.3f;
                        } else if (i == 3 && j == 2) {
                            x = -0.3f;
                            z = -0.27f;
                        } else {
                            x = 0f;
                            z = 0f;
                        }
                        t = Matrix4.translation(tx + (tn * j) + x, ty + overallAdjustY, tz - (tn * i) + z);
                        break;
                    }
                    case "44571":
                        t = Matrix4.translation(tx + (tn * (j + 1)), ty + (plateH - (studH / 2) + (offsetY / 2)) + overallAdjustY, tz - (tn * (i - 0.5f)));
                        break;
                    case "2397": {
                        float y = (j == 6) ? brickH - (offsetY / 2) : ty;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "3788":
                    case "60212": {
                        float y = (j == 0 || j == 3) ? ty + oneThird : ty;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "62694":
                        t = Matrix4.translation(tx + (tn * (j + 1f)), (plateH - studH - 0.1f) + overallAdjustY, tz - (tn * (i - 0.5f)));
                        break;
                    case "92474":
                        t = Matrix4.translation(tx + (tn * j), (ty + brickH - studH) + overallAdjustY, tz - (tn * i));
                        break;
                    case "15536":
                        t = Matrix4.translation(tx + (tn * j), (ty + brickH + studH + 0.03f) + overallAdjustY, tz - (tn * (i + 1)));
                        break;
                    case "55768":
                        t = Matrix4.translation(tx + (tn * j), (ty + (plateH + studH + 0.03f)) + overallAdjustY, tz - (tn * i));
                        break;
                    case "99206": {
                        float y = (j == 0) ? ty + plateH - studH + 0.01f : ty;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "87609": {
                        float y = (i == 0 && j > 0 && j < 5) ? ty + plateH - studH + 0.01f : ty;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "92099":
                        t = Matrix4.translation(tx + (tn * (j - 1)), (ty + 0.01f) + overallAdjustY, tz - (tn * i));
                        break;
                    case "3741":
                        t = Matrix4.translation(tx + (tn * j), (ty - plateH - 0.0275f) + overallAdjustY, tz - (tn * i));
                        break;
                    case "15469":
                    case "4488":
                    case "10313":
                    case "6252":
                    case "6255":
                    case "6040":
                    case "3186":
                    case "4094":
                        t = Matrix4.translation(tx + (tn * j), ty0_2 + overallAdjustY, tz - (tn * i));
                        break;
                    case "40996":
                        t = Matrix4.translation(tx + (tn * (j + 1)), ty0_2 + overallAdjustY, tz - (tn * i));
                        break;
                    case "50949":
                    case "47457":
                    case "41855":
                    case "50946":
                        t = Matrix4.translation(tx + (tn * j), ty0_2 + overallAdjustY, tz - (tn * (i + 1)));
                        break;
                    case "98281":
                        t = Matrix4.translation(tx + (tn * (j + 2)), ty0_2 + overallAdjustY, tz - (tn * (i + 1)));
                        break;
                    case "47456":
                        t = Matrix4.translation(tx + (tn * j), ty0_2 + overallAdjustY, tz - (tn * (i + 2)));
                        break;
                    case "30286":
                        t = Matrix4.translation(tx + (tn * j), (ty + ty0_2 - studH) + overallAdjustY, tz - (tn * i));
                        break;
                    case "30293":
                        t = Matrix4.translation(tx + (tn * j), (ty + plateH - studH) + overallAdjustY, tz - (tn * i));
                        break;
                    case "11291":
                    case "61484":
                    case "4744":
                        t = Matrix4.translation(tx + (tn * (j + 1)), ty + overallAdjustY, tz - (tn * i));
                        break;
                    case "6195":
                        t = Matrix4.translation(tx + (tn * j), ((brickH * 3) + brickH - studH + 0.03f) + overallAdjustY, tz - (tn * (i + 3)));
                        break;
                    case "4739":
                        t = Matrix4.translation(tx + (tn * j), (ty + brickH - studH) + overallAdjustY, tz - (tn * (i + 0.5f)));
                        break;
                    case "4238":
                        t = Matrix4.translation(tx + (tn * j), ty0_2 + overallAdjustY, tz - (tn * (i + 1f)));
                        break;
                    case "30018": {
                        float y = (i > 1 && i < 4 && j > 4 && j < 7) ? -(brickH + (plateH - studH + (offsetY * 3))) : ty;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "30149":
                        t = Matrix4.translation(tx + (tn * j), (ty - (brickH - plateH)) + overallAdjustY, tz - (tn * i));
                        break;
                    case "57906":
                        t = Matrix4.translation(tx + (tn * (j + 1)), (ty - (studH + 0.1f)) + overallAdjustY, tz - (tn * i));
                        break;
                    case "15455":
                        t = Matrix4.translation(tx + (tn * (j + 7)), ty + overallAdjustY, tz - (tn * i));
                        break;
                    case "92547":
                        t = Matrix4.translation(tx + (tn * (j - 2)), (ty + (plateH - studH)) + overallAdjustY, tz - (tn * (i - 2)));
                        break;
                    case "51858":
                        t = Matrix4.translation(tx + (tn * (j - 0.5f)), -(brickH - (offsetY * 3)) + overallAdjustY, tz - (tn * (i + 1.5f)));
                        break;
                    case "2441": {
                        float y = ((i > 0 && i < 3 && j < 2) || (i > 0 && i < 3 && j > 4)) ? brickH - oneThird : ty;
                        t = Matrix4.translation(tx + (tn * (j - 1)), y + overallAdjustY, tz - (tn * (i - 1)));
                        break;
                    }
                    case "4211": {
                        float y = ((i == 0 && j > 1 && j < 4) || (i == 3 && j > 1 && j < 4)) ? brickH - oneThird : ty;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "30303": {
                        float y = (i > 1 && i < 4 && j > 0 && j < 5) ? brickH - oneThird : ty;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * (i - 2)));
                        break;
                    }
                    case "30029": {
                        float y = (i > 0 && i < 3 && j > 2 && j < 7) ? -(studH + (offsetY * 3)) : ty;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * (i - 1)));
                        break;
                    }
                    case "4212": {
                        float y = (i > 0 && i < 3 && j > 3 && j < 6) ? -(studH + (offsetY * 3)) : ty;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "52036": {
                        float y = (i > 0 && i < 3 && j > 3 && j < 8) ? -(studH + (offsetY * 3)) : ty;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * (i - 1)));
                        break;
                    }
                    case "30300":
                        t = Matrix4.translation(tx + (tn * (j + 3)), ty + overallAdjustY, tz - (tn * (i + 1)));
                        break;
                    case "87615": {
                        float y = (i > 0 && i < 3 && j > 6) ? -(studH - (plateH + studH + offsetY)) : ty;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * (i + 1.5f)));
                        break;
                    }
                    case "87613":
                        t = Matrix4.translation(tx + (tn * (j + 7)), ty + overallAdjustY, tz - (tn * (i - 2)));
                        break;
                    case "11293":
                        t = Matrix4.translation(tx + (tn * (j + 6)), ty + overallAdjustY, tz - (tn * (i - 2)));
                        break;
                    case "54923":
                        t = Matrix4.translation(tx + (tn * j), ty + overallAdjustY, tz - (tn * (i + 3)));
                        break;
                    case "47755": {
                        float y = (j == 3) ? brickH : ty;
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "54093": {
                        float y = (i > 23 && i < 32) ? brickH - oneThird : ty;
                        t = Matrix4.translation(tx + (tn * (j - 4)), y + overallAdjustY, tz - (tn * (i - 24)));
                        break;
                    }
                    case "52031":
                        t = Matrix4.translation(tx + (tn * (j + 1)), ty - oneThird + overallAdjustY, tz - (tn * (i + 3)));
                        break;
                    case "45677":
                        t = Matrix4.translation(tx + (tn * j), ty + oneThird + overallAdjustY, tz - (tn * (i + 1)));
                        break;
                    case "2578":
                        t = Matrix4.translation(tx + (tn * (j - 1.5f)), ty + overallAdjustY, tz - (tn * (i + 2)));
                        break;
                    case "93591":
                        t = Matrix4.translation(tx + (tn * (j + 1)), ty + (plateH - studH) + overallAdjustY, tz - (tn * (i + 1)));
                        break;
                    case "98835":
                        t = Matrix4.translation(tx + (tn * j), ty + oneThird - offsetY + overallAdjustY, tz - (tn * (i + 2)));
                        break;
                    case "62361": {
                        float y;
                        if (j == 1 || j == 4) {
                            y = ty + oneThird;
                        } else if (j == 2 || j == 3) {
                            y = brickH;
                        } else {
                            y = ty;
                        }
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "30134": {
                        float y;
                        if (i == 6) {
                            y = ty - oneThird;
                        } else if (i == 4) {
                            y = ty - (oneThird * 3) + offsetY;
                        } else if (i == 3) {
                            y = ty - (oneThird * 6) + (offsetY * 2);
                        } else if (i == 2) {
                            y = ty - (oneThird * 9) + (offsetY * 3);
                        } else if (i == 1) {
                            y = ty - (oneThird * 12) + (offsetY * 4);
                        } else if (i == 0) {
                            y = ty - (oneThird * 15) + (offsetY * 5);
                        } else {
                            y = ty;
                        }
                        t = Matrix4.translation(tx + (tn * (j - 1)), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "52037": {
                        float y;
                        if (i > 0 && i < 5 && j > 4 && j < 9) {
                            y = ty - oneThird;
                        } else {
                            y = ty;
                        }
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * (i - 1)));
                        break;
                    }
                    case "30296":
                        t = Matrix4.translation(tx + (tn * (j + 1)), ty + oneThird + overallAdjustY, tz - (tn * i));
                        break;
                    case "30248": {
                        float y;
                        if (j == 4 || j == 7) {
                            y = brickH + oneThird - offsetY;
                        } else {
                            y = ty;
                        }
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "30644":
                        t = Matrix4.translation(tx + (tn * (j - 10)), ty + overallAdjustY, tz - (tn * (i - 1)));
                        break;
                    case "91996":
                        t = Matrix4.translation(tx + (tn * j), ty + oneThird + overallAdjustY, tz - (tn * i));
                        break;
                    case "11267":
                        t = Matrix4.translation(tx + (tn * (j - 8)), ty + oneThird + overallAdjustY, tz - (tn * (i - 1)));
                        break;
                    case "6007":
                        t = Matrix4.translation(tx + (tn * j), ty + oneThird - offsetY + overallAdjustY, tz - (tn * i));
                        break;
                    case "3956": {
                        float y;
                        float z;
                        if (i == 0) {
                            y = ty + (tn / 3) + (offsetY * 1.5f);
                            z = tz - (tn * i) + tn + (studH / 2) + (offsetY * 1.25f);
                        } else {
                            y = ty + brickH - offsetY;
                            z = tz - (tn * i) + brickH - offsetY + 0.595f;
                        }
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, z);
                        break;
                    }
                    case "3679":
                        t = Matrix4.translation(tx + (tn * j), ty - oneThird + overallAdjustY, tz - (tn * i));
                        break;
                    case "3404":
                    case "30658":
                        t = Matrix4.translation(tx + (tn * j), ty + oneThird + overallAdjustY, tz - (tn * (i - 1)));
                        break;
                    case "90109": {
                        float y;
                        if (j == 8) {
                            y = ty + (brickH * 4) - (plateH / 1.75f) + (offsetY / 2);
                        } else {
                            y = ty;
                        }
                        t = Matrix4.translation(tx + (tn * (j + 1)), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "2635": {
                        float y;
                        if (i > 1) {
                            y = ty + (brickH * 6) + (studH / 1.5f) + (offsetY / 2);
                        } else {
                            y = ty;
                        }
                        t = Matrix4.translation(tx + (tn * (j + 5)), y + overallAdjustY, tz - (tn * i));
                        break;
                    }
                    case "4474":
                        t = Matrix4.translation(tx + (tn * j), ty - (plateH / 2.44f) + overallAdjustY, tz - (tn * i));
                        break;
                    case "4595":
                        t = Matrix4.translation(tx + (tn * (j + 0.5f)), ty + studH - (offsetY / 3) + overallAdjustY, tz - (tn * i));
                        break;
                    case "4346":
                        t = Matrix4.translation(tx + (tn * (j + 0.5f)), ty + (brickH / 2) + overallAdjustY, tz - (tn * (i - 0.823f)) + offsetY);
                        break;
                    case "15626": {
                        float y;
                        float z;
                        if (j > 2 && j < 10) {
                            y = ty + oneThird;
                            z = tz - (tn * (i - 1));
                        } else {
                            if (i == 0) {
                                y = (j < 2 || j > 11) ? (ty + oneThird + (tn * 1.55f)) + (brickH * 6.5f) : ty + oneThird + (tn * 1.55f);
                                z = tz - (tn * (i - 1)) + (tn * 0.71f);
                            } else {
                                y = ty + oneThird + (tn * 2.55f);
                                z = tz - (tn * (i - 2)) + (tn * 0.71f);
                            }
                        }
                        t = Matrix4.translation(tx + (tn * (j + 1)), y + overallAdjustY, z);
                        break;
                    }
                    case "54654": {
                        float y;
                        if (i == 5 || i == 6) {
                            y = (j == 1) ? ty + (brickH * 2) - (plateH - (studH * 1.175f)) : ty + (brickH * 2) - plateH - studH;
                        } else {
                            y = ty - oneThird;
                        }
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * (i - 4)));
                        break;
                    }
                    case "2618": {
                        float y;
                        if (j == 1 || j == 6 || i == 1 || i == 6) {
                            y = ty - oneThird;
                        } else if (i > 2 && i < 5 && j > 2 && j < 5) {
                            y = ty - (oneThird * 4) + offsetY;
                        } else {
                            y = ty;
                        }
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * (i - 3)));
                        break;
                    }
                    case "30022":
                        t = Matrix4.translation(tx + (tn * (j - 1)), ty + (brickH * 1.82f) + overallAdjustY, tz - (tn * (i - 0.71f)));
                        break;
                    case "6248": {
                        float y;
                        float z;
                        if (i == 0) {
                            y = (ty + (tn / 3) + (offsetY * 1.5f)) - (brickH * 1.6f);
                            z = (tz - (tn * i) + tn + (studH / 2) + (offsetY * 1.25f)) - (brickH * 1.6f) - offsetY;
                        } else {
                            y = (ty + brickH - offsetY) - (brickH * 1.6f);
                            z = (tz - (tn * i) + brickH - offsetY + 0.595f) - (brickH * 1.6f) - offsetY;
                        }
                        t = Matrix4.translation(tx + (tn * (j - 0.5f)), y + overallAdjustY, z);
                        break;
                    }
                    case "3585":
                        t = Matrix4.translation(tx + (tn * j), ty + overallAdjustY, tz - (tn * (i - 6)));
                        break;
                    case "3960":
                        t = Matrix4.translation(tx + (tn * j), ty + oneThird + overallAdjustY, tz - (tn * i));
                        break;
                    case "30183": {
                        float y;
                        if (i > 1 && i < 4 && j > 0 && j < 3) {
                            y = (ty - brickH) + (plateH);
                        } else {
                            y = ty;
                        }
                        t = Matrix4.translation(tx + (tn * j), y + overallAdjustY, tz - (tn * (i - 1)));
                        break;
                    }
                    case "3947":
                        t = Matrix4.translation(tx + (tn * (j - 15.475f)), (ty / 1.715f) + overallAdjustY, tz - (tn * (i - 16)));
                        break;
                    default:
                        t = Matrix4.translation(tx + (tn * j), ty + overallAdjustY, tz - (tn * i));
                        break;
                }
                m4 = t.multiply(m4);

                // 5. lddbrick
                m4 = m.multiply(m4);
                api.parameter("transform", m4);

                // 6. shader
                String[] shaders;
                shaders = new String[]{shdr};
                api.parameter("shaders", shaders);

                // update
                api.instance("instance_" + geoname + "_los" + logoonstuds, "logoonstuds");
                logoonstuds++;
            }
        }

        // ROWS
        for (int i = 0; i < ROWS; i++) {

            LOS loz = new LOS();

            // COLUMNS
            for (int j = 0; j < COLS; j++) {
                switch (g) {
                    case "2357":
                    case "3046":
                        if (i == 1 && j == 0) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "3063":
                    case "85080":
                    case "87620":
                        if ((i == 0 && j == 1) || (i == 1 && j == 0)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "99301":
                        if (i != 2 && j != 0) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "87081":
                    case "60474":
                    case "3404":
                    case "30658":
                        if ((i == 0 && j == 0) || (i == 0 && j == 3) || (i == 3 && j == 0) || (i == 3 && j == 3)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "30505":
                    case "2450":
                    case "2409":
                        if ((i == 0 && j > 0) || (i == 1 && j > 1)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "2577":
                    case "30565":
                        if ((i == 0 && j > 0) || (i == 1 && j == 3) || (i == 2 && j == 3)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "6162":
                        if ((i == 0 && j > 3) || (i == 1 && j > 6) || (i == 2 && j > 7) || (i == 3 && j > 8) || (i == 4 && j > 9) || (i == 5 && j > 10) || (i == 6 && j > 10) || (i == 7 && j > 10)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "47974":
                        if ((i == 0 && j > 1 && j < 6) || (i == 1 && j < 1) || (i == 1 && j == 7) || (i == 2 && j < 1) || (i == 2 && j == 7) || (i == 3 && j < 3) || (i == 3 && j > 4)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "30181":
                        if ((i == 0 && j < 3) || (i == 0 && j > 6) || (i == 1 && j < 2) || (i == 1 && j > 7)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "58846":
                        if ((i < 2) || (i == 2 && j > 0) || (i == 3 && j > 3) || (i == 4 && j < 3) || (i == 4 && j > 4)
                                || (i == 5 && j < 3) || (i == 5 && j > 5) || (i == 6 && j < 3) || (i == 6 && j > 6)
                                || (i == 7 && j < 6) || (i == 7 && j > 6) || (i == 8 && j < 6) || (i == 8 && j > 6)
                                || (i == 9 && j < 6) || (i == 9 && j > 7)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "95188":
                        if ((i < 2) || (i == 2 && j > 0) || (i == 3 && j < 1) || (i == 3 && j > 2)
                                || (i == 4 && j < 2) || (i == 4 && j > 2) || (i == 5 && j < 3) || (i == 5 && j > 3)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "48092":
                        if ((i == 0 && j > 0) || (i == 1 && j < 2) || (i == 1 && j > 2) || i == 2 || (i == 3 && j < 3)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "2462":
                        if ((i == 0 && j > 0) || (i == 1 && j < 1) || (i == 1 && j > 1) || (i == 2 && j < 2)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "14413":
                        if ((i == 0 && j > 0) || (i == 1 && j < 1) || (i == 1 && j > 1) || (i == 2 && j < 2) || (i == 2 && j > 2) || (i == 3 && j < 3)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "6107":
                        if ((i == 0 && j > 0) || (i == 1 && j < 1) || (i == 1 && j > 1) || (i == 2 && j < 2) || (i == 2 && j > 2) || (i == 3 && j < 3) || (i == 3 && j > 3) || (i == 4 && j < 4)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "87559":
                        if (i == 1 || i > 3 || (i == 0 && j < 2) || (i == 0 && j > 2) || (i == 2 && j < 3) || (i == 2 && j > 3) || (i == 3 && j < 5)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "50373":
                        if ((i == 0 && j > 0) || (i == 1 && j < 1) || (i == 2 && j < 1) || (i == 3 && j > 0)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "2399":
                        if (i == 0 || i == 3 || (i == 1 && j < 1) || (i == 2 && j < 1)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "52040":
                        if ((i == 0 && j > 3 && j < 8) || (i == 11 && j > 3 && j < 8) || (i < 2 && j < 2) || (i < 2 && j > 9)
                                || (i > 9 && j < 2) || (i > 9 && j > 9) || (i > 3 && i < 8 && j == 0) || (i > 3 && i < 8 && j == 11)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "47507":
                        if ((i == 0 && j > 0 && j < 5) || (i == 5 && j > 0 && j < 5)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "30250":
                        if ((i == 0 && j == 6) || (i == 3 && j == 6) || (i == 1 && j > 1 && j < 5) || (i == 2 && j > 1 && j < 5)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "2336":
                        if (j < 3) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "6072":
                        if ((i == 0 && j > 2) || (i == 1 && j > 3) || (i == 2 && j > 4) || (i == 3 && j > 5) || (i > 3 && j < 3)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "6066":
                        if ((i == 0 && j < 2) || (i == 0 && j > 5) || (i == 1 && j < 1) || (i == 1 && j > 6) || (i > 1 && j > 1 && j < 6)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "6178":
                        if (i < 5 && j > 0 && j < 11) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "6180":
                        if (i < 3 && j > 0 && j < 5) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "6205":
                        if (i < 5 && j > 0 && j < 15) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "6179":
                        if (i < 3) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "88646":
                        if (i != 1) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "6576":
                        if (i < 1 || i > 2 || j == 0 || j == 7) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "64799":
                    case "6067":
                    case "4844":
                    case "4211":
                        if (i > 0 && i < 3 && j > 0 && j < 3) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "2639":
                        if (i < 2 && j < 2) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "15397":
                        if ((i == 0 && j != 1) || (i == 2 && j != 1)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "30357":
                        if (i == 0 && j == 2) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "30503":
                        if ((i == 0 && j > 0) || (i == 1 && j > 1) || (i == 2 && j > 2)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "11213":
                        if ((i == 0 && j < 2) || (i == 0 && j > 3) || (i == 1 && j < 1) || (i == 1 && j > 4)
                                || (i == 4 && j < 1) || (i == 4 && j > 4) || (i == 5 && j < 2) || (i == 5 && j > 3)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "30062":
                        if ((i == 0 && j < 2) || (i == 0 && j > 3) || (i == 1 && j < 1) || (i == 1 && j > 4)
                                || (i == 4 && j < 1) || (i == 4 && j > 4) || (i == 5 && j < 2) || (i == 5 && j > 3)
                                || (i == 1 && j > 1 && j < 4) || (i == 4 && j > 1 && j < 4) || (i > 1 && i < 4 && j > 0 && j < 5)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "6003":
                        if ((i == 0 && j > 2) || (i > 0 && i < 3 && j > 4)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "6106":
                        if ((i == 0 && j > 1) || (i == 1 && j > 2) || (i == 2 && j > 3) || (i == 2 && j > 3) || (i == 3 && j > 4)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "2413":
                    case "14181":
                        if ((i == 0 && j > 3) || (i == 3 && j > 3)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "30504":
                        if ((i == 0 && j > 0) || (i == 1 && j > 1) || (i == 2 && j > 2) || (i == 3 && j > 3)
                                || (i == 4 && j > 4) || (i == 5 && j > 5) || (i == 6 && j > 6)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "32059":
                        if ((i < 2 && j == 0) || (i < 2 && j == 5)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "2419":
                        if ((i < 2 && j == 0) || (i < 2 && j == 5) || (i == 0 && j == 1) || (i == 0 && j == 4)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "47397":
                        if ((i < 2 && j < 5) || (i == 0 && j != 11)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "47398":
                        if ((i > 0 && j < 5) || (i == 2 && j != 11)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "3935":
                        if ((i == 2 && j < 2) || (i == 1 && j < 1)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "3936":
                        if ((i == 0 && j < 2) || (i == 1 && j < 1)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "54383":
                        if (i == 1 && j < 3) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "54384":
                        if (i == 0 && j < 3) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "3933":
                        if ((i == 0 && j < 4) || (i == 1 && j < 2)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "3934":
                        if ((i == 2 && j < 4) || (i == 1 && j < 2)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "11833":
                        if ((i == 0 && j == 0) || (i == 0 && j == 3) || (i == 3 && j == 0) || (i == 3 && j == 3)
                                || (i > 0 && i < 3 && j > 0 && j < 3)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "50304":
                        if ((i == 1 && j < 3) || (i == 2 && j < 6)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "50305":
                        if ((i == 1 && j < 3) || (i == 0 && j < 6)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "2625":
                    case "50303":
                        if ((i == 0 && j > 1) || (i == 1 && j > 4) || (i == 5 && j > 1) || (i == 4 && j > 4)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "30355":
                        if ((i == 0 && j < 9) || (i == 1 && j < 6) || (i == 2 && j < 3)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "30356":
                        if ((i == 5 && j < 9) || (i == 4 && j < 6) || (i == 3 && j < 3)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "89523":
                        if ((i == 0 && j < 3) || (i == 0 && j > 6) || (i == 1 && j < 2) || (i == 1 && j > 7)
                                || (i == 2 && j < 1) || (i == 2 && j > 8) || (i == 9 && j < 3) || (i == 9 && j > 6)
                                || (i == 8 && j < 2) || (i == 8 && j > 7) || (i == 7 && j < 1) || (i == 7 && j > 8)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "6063":
                        if ((i == 0 && j < 3) || (i == 0 && j > 6) || (i == 1 && j < 2) || (i == 1 && j > 7)
                                || (i == 2 && j < 1) || (i == 2 && j > 8) || (i == 9 && j < 3) || (i == 9 && j > 6)
                                || (i == 8 && j < 2) || (i == 8 && j > 7) || (i == 7 && j < 1) || (i == 7 && j > 8)
                                || (i == 2 && j > 2 && j < 7) || (i == 7 && j > 2 && j < 7) || (i > 2 && i < 7 && j > 1 && j < 8)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "2621":
                        if ((i == 0 && j > 1) || (i == 1 && j > 4) || (i == 2 && j > 5) || (i == 3 && j > 7)
                                || (i == 9 && j > 1) || (i == 8 && j > 4) || (i == 7 && j > 5) || (i == 6 && j > 7)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "47405":
                        if ((i == 0 && j > 0) || (i == 1 && j > 2) || (i == 2 && j > 4) || (i == 3 && j > 5) || (i == 4 && j > 6)
                                || (i == 11 && j > 0) || (i == 10 && j > 2) || (i == 9 && j > 4) || (i == 8 && j > 5) || (i == 7 && j > 6)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "2401":
                        if ((i < 4 && j < 4) || (i == 4 && j == 9) || (i == 5 && j > 7) || (i == 6 && j > 6)
                                || (i == 7 && j > 5) || (i == 8 && j > 4) || (i == 9 && j > 3)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "47407":
                        if ((i == 0 && j > 1) || (i == 3 && j > 1) || (i > 0 && i < 3 && j < 2)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "6104":
                        if ((i == 0 && j > 3) || (i == 1 && j > 5) || (i == 5 && j > 3) || (i == 4 && j > 5) || (i > 0 && i < 5 && j < 2) || (i > 1 && i < 4 && j == 2)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "3474":
                        if ((i == 0 && j < 2) || (i == 0 && j > 5) || (i == 2 && j > 0 && j < 7)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "2539":
                        if ((i == 0 && j < 2) || (i == 0 && j > 3) || (i == 1 && j < 1) || (i == 1 && j > 4)
                                || (i == 5 && j < 2) || (i == 5 && j > 3) || (i == 4 && j < 1) || (i == 4 && j > 4)
                                || (i > 1 && i < 4 && j > 1 && j < 4)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "92584":
                        if ((i == 0 && j > 1) || (i == 1 && j > 2) || (i == 2 && j > 3) || (i == 3 && j > 4) || (i == 4 && j > 5)
                                || (i == 5 && j > 6) || (i == 6 && j > 7) || (i == 7 && j > 8)
                                || (i == 3 && j > 1 && j < 4) || (i == 4 && j > 1 && j < 5) || (i == 5 && j > 1 && j < 6)
                                || (i == 6 && j > 1 && j < 7) || (i == 7 && j > 1 && j < 7)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "30118":
                        if ((j > 1 && j < 7) || (i == 0 && j == 7) || (i == 3 && j == 7)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "6219":
                        if ((i == 0 && j > 1) || (i == 1 && j > 2) || (i == 2 && j > 3) || (i == 3 && j > 4) || (i == 4 && j > 5) || (i == 5 && j > 9)
                                || (i == 15 && j > 1) || (i == 14 && j > 2) || (i == 13 && j > 3) || (i == 12 && j > 4) || (i == 11 && j > 5) || (i == 10 && j > 9)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "91405":
                        loz.add(i, j);
                        break;
                    case "15706":
                        if ((i == 1 && j > 0) || (i == 2 && j > 0) || (i == 3 && j == 0) || (i == 3 && j == 3)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "4151":
                        if ((i > 0 && i < 3 && j > 0 && j < 7) || (i > 4 && i < 7 && j > 0 && j < 7)
                                || (i > 2 && i < 5 && j > 0 && j < 3) || (i > 2 && i < 5 && j > 4 && j < 7)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "2397":
                        if (j > 1 && j < 6) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "92107":
                    case "30041":
                        if (i > 0 && i < 5 && j > 0 && j < 7) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "44571":
                        if (j == 2) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "3939":
                    case "58181":
                    case "30077":
                    case "93140":
                        if (j > 0 && j < 5) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "47843":
                    case "93589":
                        if (i == 1 || i == 2) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "17454":
                        if ((i == 0 && j == 0) || (i == 0 && j == 5) || (i == 1 && j > 0 && j < 5)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "4447":
                    case "60806":
                        if (i != 3) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "4130":
                        if ((i == 0 && j == 0) || (i == 0 && j == 3)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "4132":
                    case "61072":
                        if (j == 0 || j == 3) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "30018":
                        if ((i == 1 && j > 0 && j < 11) || (i == 4 && j > 0 && j < 11) || (i > 1 && i < 4 && j > 0 && j < 5)
                                || (i > 1 && i < 4 && j > 6 && j < 11)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "2549":
                        if ((i == 0 && j > 0 && j < 15) || (i == 3 && j > 0 && j < 15) || (i > 0 && i < 3)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "92547":
                        if ((i < 2 && j < 2) || (i < 2 && j > 3) || (i > 3 && j < 2) || (i > 3 && j > 3)
                                || (i > 1 && i < 4 && j > 1 && j < 4)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "2441":
                        if ((i == 0 && j < 2) || (i == 0 && j > 4) || (i == 3 && j < 2) || (i == 3 && j > 4)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "30303":
                        if (i == 1 || i == 4 || (i < 2 && j < 2) || (i < 2 && j > 3) || (i > 3 && j < 2) || (i > 3 && j > 3)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "30029":
                        if ((i == 0 && j < 2) || (i == 0 && j > 7) || (i == 3 && j < 2) || (i == 3 && j > 7)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "4212":
                        if ((i == 0 && j > 0 && j < 3) || (i == 0 && j > 6 && j < 9) || (i == 3 && j > 0 && j < 3) || (i == 3 && j > 6 && j < 9)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "52036":
                        if ((i == 0 && j < 4) || (i == 0 && j > 7) || (i == 3 && j < 4) || (i == 3 && j > 7)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "87615":
                        if ((i == 0 && j > 2) || (i == 3 && j > 2)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "87613":
                    case "11293":
                    case "92099":
                        if ((i == 0 && j == 0) || (i == 3 && j == 0)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "87616":
                        if ((i == 0 && j == 2) || (i == 3 && j == 2)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "54923":
                        if (j == 0) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "47755":
                        if (j > 0 && j < 3) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "54093":
                        if (j < 2 || i == 23 || i == 32 || (i > 1 && i < 8) || (i > 9 && i < 16) || (i > 17 && i < 21)
                                || (i > 34 && i < 38) || (i > 39 && i < 46) || (i > 47 && i < 54)
                                || (i > 23 && i < 32 && j < 4) || (i > 24 && i < 31 && j > 4 && j < 19)
                                || (i < 2 && j > 5)
                                || (i > 7 && i < 10 && j < 4) || (i > 7 && i < 10 && j > 9)
                                || (i > 15 && i < 18 && j < 8) || (i > 15 && i < 18 && j > 13)
                                || (i > 20 && i < 23 && j < 6) || (i > 20 && i < 23 && j > 9)
                                || (i > 32 && i < 35 && j < 6) || (i > 32 && i < 35 && j > 9)
                                || (i > 37 && i < 40 && j < 8) || (i > 37 && i < 40 && j > 13)
                                || (i > 45 && i < 48 && j < 4) || (i > 45 && i < 48 && j > 9)
                                || (i > 53 && j > 5)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "30263":
                        if (j == 9 || (j > 2 && j < 6) || (i < 2 && j == 1) || (i > 3 && j == 1) || (i < 2 && j == 7) || (i > 3 && j == 7)
                                || (i > 1 && i < 4 && j == 0) || (i > 1 && i < 4 && j == 6)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "30134":
                        if ((i == 6 && j == 0) || (i == 6 && j == 3)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "52037":
                        if ((i == 0 && j < 4) || (i == 0 && j > 9) || (i == 5 && j < 4) || (i == 5 && j > 9)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "30248":
                        if ((i == 0 && j > 2 && j < 5) || (i == 0 && j == 7) || (i == 5 && j > 2 && j < 5) || (i == 5 && j == 7)
                                || (i > 0 && i < 5 && j < 4) || (i > 0 && i < 5 && j > 4 && j < 7) || (i > 0 && i < 5 && j > 7)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "30644":
                        if ((i == 0 && j < 10) || (i == 0 && j > 10)
                                || (i == 1 && j < 7) || (i == 1 && j > 7 && j < 14) || (i == 1 && j > 14 && j < 20)
                                || (i == 2 && j > 1 && j < 7) || (i == 2 && j > 7 && j < 14) || (i == 2 && j > 14)
                                || (i == 3 && j < 11) || (i == 3 && j > 11)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "90109":
                        if ((j > 5 && j < 8) || (i == 0 && j < 8) || (i == 5 && j < 8)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "2635":
                        if (i == 1 || (i > 1 && j == 0) || (i > 1 && j == 5)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "15626":
                        if (j == 3 || j == 10 || (i == 1 && j < 2) || (i == 1 && j > 11)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "90201":
                        if ((i == 1 && j < 2) || (i == 1 && j > 3)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "54654":
                        if (j == 0 || (i > 1 && i < 5) || (i > 6 && i < 10) || (i < 2 && j < 4) || (i < 2 && j > 9)
                                || (i > 9 && j < 4) || (i > 9 && j > 9)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "2618":
                        if (i == 2 || i == 5 || j == 2 || j == 5 || (i < 3 && j < 3) || (i < 3 && j > 4)
                                || (i > 4 && j < 3) || (i > 4 && j > 4)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "2420":
                        if (i == 0 && j == 0) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "51595":
                        if (j > 6 && j < 15) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "30225":
                        if ((j > 6 && j < 15) || (j > 16 && j < 25)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "44336":
                        if (i > 5 && i < 26) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "44341":
                        if ((i > 5 && i < 26) || (i > 25 && j > 5 && j < 26)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "44343":
                        if ((i > 5 && i < 26) || (i > 25 && j > 5 && j < 26) || (i < 6 && j > 5 && j < 26)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "44342":
                        if ((i < 7 && j > 5 && j < 26) || (i > 5 && i < 26 && j > 24) || (i > 5 && i < 25 && j > 21)
                                || (i > 5 && i < 24 && j > 19) || (i > 5 && i < 23 && j > 17) || (i > 5 && i < 22 && j > 16)
                                || (i > 5 && i < 21 && j > 14) || (i > 5 && i < 20 && j > 13) || (i > 5 && i < 19 && j > 12)
                                || (i > 5 && i < 18 && j > 11) || (i > 5 && i < 17 && j > 10) || (i > 5 && i < 15 && j > 9)
                                || (i > 5 && i < 14 && j > 8) || (i > 5 && i < 12 && j > 7) || (i > 5 && i < 10 && j > 6)
                                || (i == 5 && j > 24 && j < 31) || (i == 4 && j > 24 && j < 29) || (i == 3 && j > 24 && j < 28)
                                || (i > 0 && i < 3 && j == 26)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "3585":
                        if ((i == 0 && j < 10) || (i == 1 && j < 8) || (i == 2 && j < 6) || (i == 3 && j < 4) || (i == 4 && j < 2) || (i == 6 && j > 1)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "3586":
                        if ((i == 6 && j < 10) || (i == 5 && j < 8) || (i == 4 && j < 6) || (i == 3 && j < 4) || (i == 2 && j < 2) || (i == 0 && j > 1)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "30183":
                        if (i == 0 || i == 5) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "45301":
                        if (j > 3 && j < 15) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "3947":
                        if ((i > 1 && i < 30 && j > 26 && j < 30) || (i > 2 && i < 30 && j == 26) || (i > 5 && i < 30 && j == 25)
                                || (i > 7 && i < 30 && j == 24) || (i > 12 && i < 30 && j == 23) || (i > 13 && i < 30 && j == 22)
                                || (i > 17 && i < 30 && j == 21) || (i > 18 && i < 30 && j == 20) || (i > 20 && i < 30 && j == 19)
                                || (i > 21 && i < 30 && j > 15 && j < 19) || (i > 22 && i < 30 && j > 11 && j < 16)
                                || (i > 23 && i < 30 && j > 8 && j < 12) || (i > 24 && i < 30 && j > 4 && j < 9)
                                || (i > 25 && i < 30 && j > 2 && j < 5) || (i > 26 && i < 30 && j == 2)) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    case "92593":
                    case "4858":
                        if (j == 1 || j == 2) {
                        } else {
                            loz.add(i, j);
                        }
                        break;
                    default:
                        loz.add(i, j);
                        break;
                }
            }
        }
    }

    /**
     * Adds grain to selected (mostly) slope bricks.
     *
     * @param api
     * @param geoname brick's name
     * @return
     */
    public String GrainySlopes(SunflowAPI api, String geoname) {
        String[] mdfrs = null;
        if (geoname.contains("_")) {
            String[] g = geoname.split("_");
            String brick = g[0];
            if (g[0].matches("[0-9]+") && brick.length() >= 4) {
                if (Arrays.asList(grainySlopes).contains(brick) || Arrays.asList(grainyBP16x16).contains(brick) || Arrays.asList(grainyBP32x32).contains(brick)) {
                    String a = brick;
                    float b = 0.5f;
                    String c = "Slopes" + brick;
                    if (SCParser.exactdecorbp.equals("on")) {
                        if (Arrays.asList(grainyBP32x32).contains(brick)) {
                            a = "BP32x32";
                            b = 0.002f;
                            c = "BP32x32";
                        } else if (Arrays.asList(grainyBP16x16).contains(brick)) {
                            a = "BP16x16";
                            b = 0.002f;
                            c = "BP16x16";
                        }
                    }
                    String mdfr = "modGrainy" + c;
                    //System.out.println("mdfr = " + mdfr);
                    Modifier s = api.lookupModifier(mdfr);
                    mdfrs = new String[]{mdfr};
                    return mdfr;
                }
            }
        }
        return null;
    }

    /**
     * Returns array of all slope bricks with grainy surface.
     *
     * @return String array
     */
    public String[] checkGrainySlopes() {
        return grainySlopes;
    }

    /**
     * Returns array of all baseplates with grainy surface.
     *
     * @return String array
     */
    public String[] checkGrainyBP16x16() {
        return grainyBP16x16;
    }

    /**
     * Returns array of all baseplates with grainy surface.
     *
     * @return String array
     */
    public String[] checkGrainyBP32x32() {
        return grainyBP32x32;
    }

    /**
     * Returns array of all bricks with rubber material.
     *
     * @return String array
     */
    public String[] checkRubberParts() {
        return rubberParts;
    }
}
