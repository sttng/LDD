##RenderMan RIB
# Generated with LegoToR 0.4.8.3 on 2020-02-25 01:08:41.521044
version 3.04
Option "searchpath" "string archive" ["/Users/hannes/Downloads/LegoToR/"] "string texture" [".:@:/Applications/Pixar/RenderManProServer-23.1/lib/RenderManAssetLibrary/EnvironmentMaps/Outdoor/GriffithObservatory.rma:/Users/hannes/Downloads/LegoToR/"]
Option "Ri" "int Frame" [1]
	"float PixelVariance" [0.1]
	"string PixelFilterName" ["gaussian"]
	"float[2] PixelFilterWidth" [2 2]
	#"int[2] FormatResolution" [960 540] # Low res
	#"int[2] FormatResolution" [1280 720] # 720p
	#"int[2] FormatResolution" [1920 1080] # 1080p 
	#"int[2] FormatResolution" [4096 2160] # 4k
	"int[2] FormatResolution" [1280 720]
	"float FormatPixelAspectRatio" [1]
	"float[2] Clipping" [0.1 10000]
	"float[4] ScreenWindow" [-1 1 -0.5625 0.5625]
	"float[2] Shutter" [0 0]
Option "bucket" "string order" ["circle"]
Option "statistics" "int level" [1] "string xmlfilename" ["./test01.xml"]

Integrator "PxrVCM" "PxrVCM1"
Hider "raytrace" "int minsamples" [32] "int maxsamples" [64] "float darkfalloff" [0.025] "int incremental" [1] "string pixelfiltermode" ["importance"]
ShadingRate 10.0

# Beauty
DisplayChannel "color Ci"
DisplayChannel "float a"
DisplayChannel "color mse" "string source" "color Ci" "string statistics" "mse"

# Shading
DisplayChannel "color albedo" "string source" "color lpe:nothruput;noinfinitecheck;noclamp;unoccluded;overwrite;C(U2L)|O"
DisplayChannel "color albedo_var" "string source" "color lpe:nothruput;noinfinitecheck;noclamp;unoccluded;overwrite;C(U2L)|O" "string statistics" "variance"
DisplayChannel "color diffuse" "string source" "color lpe:C(D[DS]*[LO])|O"
DisplayChannel "color diffuse_mse" "string source" "color lpe:C(D[DS]*[LO])|O" "string statistics" "mse"
DisplayChannel "color specular" "string source" "color lpe:CS[DS]*[LO]"
DisplayChannel "color specular_mse" "string source" "color lpe:CS[DS]*[LO]" "string statistics" "mse"

# Geometry
DisplayChannel "float zfiltered" "string source" "float z" "string filter" "gaussian"
DisplayChannel "float zfiltered_var" "string source" "float z" "string filter" "gaussian" "string statistics" "variance"
DisplayChannel "normal normal" "string source" "normal Nn"
DisplayChannel "normal normal_var" "string source" "normal Nn" "string statistics" "variance"
DisplayChannel "vector forward" "string source" "vector motionFore"
DisplayChannel "vector backward" "string source" "vector motionBack"

Projection "PxrCamera" "float fov" [30.0] "float fStop" [144] "float focalLength" [0.8] "float focalDistance" [5] "point focus1" [0.0 0.0 -1] "point focus2" [1 0.0 -1] "point focus3" [1 1 -1]
# Camera Minus One
TransformBegin
	Translate 0 -2 80
	Rotate -25 1 0 0
	Rotate 45 0 1 0
	Camera "Cam--1"
		"float shutterOpenTime" [0] 
		"float shutterCloseTime" [1] 
		"int apertureNSides" [0] 
		"float apertureAngle" [0] 
		"float apertureRoundness" [0] 
		"float apertureDensity" [0] 
		"float dofaspect" [1] 
		"float nearClip" [0.100000001] 
		"float farClip" [10000]
TransformEnd

# Camera 0
TransformBegin
	ConcatTransform [0.638512790203 0.0 0.769611299038 0 -0.294636070728 0.923815608025 0.244446650147 0 -0.710978984833 -0.382837593555 0.589868187904 0 32.0428848267 20.4122123718 -28.3208332062 1]
	Camera "Cam-0"
		"float shutterOpenTime" [0] 
		"float shutterCloseTime" [1] 
		"int apertureNSides" [0] 
		"float apertureAngle" [0] 
		"float apertureRoundness" [0] 
		"float apertureDensity" [0] 
		"float dofaspect" [1] 
		"float nearClip" [0.100000001] 
		"float farClip" [10000]
TransformEnd

# Inverse Camera 0
TransformBegin
	ConcatTransform [0.638512738772 -0.294636106694 -0.710978855352 0.0 1.39641670584e-08 0.92381574541 -0.382837521495 0.0 0.769611166477 0.244446674334 0.589868019445 0.0 1.33623904555 -2.49319886354 47.3019281612 1.0]
	Camera "Inv-Cam-0"
		"float shutterOpenTime" [0] 
		"float shutterCloseTime" [1] 
		"int apertureNSides" [0] 
		"float apertureAngle" [0] 
		"float apertureRoundness" [0] 
		"float apertureDensity" [0] 
		"float dofaspect" [1] 
		"float nearClip" [0.100000001] 
		"float farClip" [10000]
TransformEnd

Display "./test01.beauty.001.exr" "openexr" "Ci,a,mse,albedo,albedo_var,diffuse,diffuse_mse,specular,specular_mse,zfiltered,zfiltered_var,normal,normal_var,forward,backward" "int asrgba" 1
	"string storage" ["scanline"]
	"string exrpixeltype" ["half"]
	"string compression" ["zips"]
	"float compressionlevel" [45]
	"string camera" ["Cam--1"]

WorldBegin
	Scale 1 1 1
	AttributeBegin
		Attribute "visibility" "int indirect" [0] "int transmission" [0]
		Attribute "visibility" "int camera" [1]
		Rotate 50 0 1 0
		Rotate -90 1 0 0
		Light "PxrDomeLight" "domeLight" "string lightColorMap" ["islandsun_small.tex"]
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.29153445363 0.0 -0.956560373306 0 0.0 1.0 -0.0 0 0.956560373306 -0.0 0.29153445363 0 2.79999923706 2.85899996758 -3.59997987747 1]
		Scale 0.995680455167 0.995680455167 0.995680455167
		Attribute "identifier" "name" ["26047_208"]
		ReadArchive "test01_Bricks_Archive.zip!26047_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-0.668772876263 -0.714980900288 -0.20382642746 0 0.291537344456 0.0 -0.956559538841 0 0.683921098709 -0.699144601822 0.208443641663 0 4.0642414093 2.548817873 -3.04740571976 1]
		Scale 0.994184166244 0.994184166244 0.994184166244
		Attribute "identifier" "name" ["4085_208"]
		ReadArchive "test01_Bricks_Archive.zip!4085_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.668772995472 0.714980781078 0.203826442361 0 0.291537314653 0.0 -0.956559419632 0 -0.683920860291 0.699144899845 -0.20844386518 0 3.97094893456 2.54881739616 -2.74130630493 1]
		Scale 0.998751639848 0.998751639848 0.998751639848
		Attribute "identifier" "name" ["2420_208"]
		ReadArchive "test01_Bricks_Archive.zip!2420_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.668773174286 0.714980661869 0.203826367855 0 0.291537314653 0.0 -0.956559419632 0 -0.683920919895 0.69914484024 -0.208443894982 0 4.15753364563 2.54881668091 -3.35350251198 1]
		Scale 0.992828408087 0.992828408087 0.992828408087
		Attribute "identifier" "name" ["11153_208"]
		ReadArchive "test01_Bricks_Archive.zip!11153_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.668772995472 0.714980781078 0.203826501966 0 0.29153740406 0.0 -0.956559419632 0 -0.683921039104 0.699144721031 -0.208443641663 0 4.70467090607 1.98950111866 -3.18675041199 1]
		Scale 0.994551803899 0.994551803899 0.994551803899
		Attribute "identifier" "name" ["11153_23"]
		ReadArchive "test01_Bricks_Archive.zip!11153_23.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 0.799999952316 3.1799993515 -5.1999874115 1]
		Scale 0.995480323282 0.995480323282 0.995480323282
		Attribute "identifier" "name" ["11477_111"]
		ReadArchive "test01_Bricks_Archive.zip!11477_111.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 0.799999952316 2.85999941826 -5.1999874115 1]
		Scale 0.995503456732 0.995503456732 0.995503456732
		Attribute "identifier" "name" ["3024_26"]
		ReadArchive "test01_Bricks_Archive.zip!3024_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 0.799999952316 2.53999948502 -6.79998493195 1]
		Scale 0.99551667188 0.99551667188 0.99551667188
		Attribute "identifier" "name" ["3623_26"]
		ReadArchive "test01_Bricks_Archive.zip!3623_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 1.99999976158 2.5389995575 -5.99998044968 1]
		Scale 0.994597782768 0.994597782768 0.994597782768
		Attribute "identifier" "name" ["3794_23"]
		ReadArchive "test01_Bricks_Archive.zip!3794_23.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 1.99999976158 2.21899986267 -5.99998044968 1]
		Scale 0.993697812858 0.993697812858 0.993697812858
		Attribute "identifier" "name" ["3024_194"]
		ReadArchive "test01_Bricks_Archive.zip!3024_194.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -0.399994134903 1.89999961853 -5.99998807907 1]
		Scale 0.996445167826 0.996445167826 0.996445167826
		Attribute "identifier" "name" ["3710_194"]
		ReadArchive "test01_Bricks_Archive.zip!3710_194.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 0.400005936623 2.21999931335 -5.99998807907 1]
		Scale 0.996365715899 0.996365715899 0.996365715899
		Attribute "identifier" "name" ["3794_194"]
		ReadArchive "test01_Bricks_Archive.zip!3794_194.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 0.400004982948 1.57999956608 -5.99998807907 1]
		Scale 0.99833306576 0.99833306576 0.99833306576
		Attribute "identifier" "name" ["3022_194"]
		ReadArchive "test01_Bricks_Archive.zip!3022_194.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 0.400004982948 2.21999931335 -5.19998502731 1]
		Scale 0.996609483232 0.996609483232 0.996609483232
		Attribute "identifier" "name" ["3794_194"]
		ReadArchive "test01_Bricks_Archive.zip!3794_194.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 0.400004982948 1.89999961853 -5.19998502731 1]
		Scale 0.993239815306 0.993239815306 0.993239815306
		Attribute "identifier" "name" ["3023_194"]
		ReadArchive "test01_Bricks_Archive.zip!3023_194.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -0.399994134903 1.25999963284 -5.99998807907 1]
		Scale 0.999823211773 0.999823211773 0.999823211773
		Attribute "identifier" "name" ["3710_194"]
		ReadArchive "test01_Bricks_Archive.zip!3710_194.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 0.400004982948 1.26000225544 -5.19997358322 1]
		Scale 0.998494621129 0.998494621129 0.998494621129
		Attribute "identifier" "name" ["3022_194"]
		ReadArchive "test01_Bricks_Archive.zip!3022_194.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 1.19999849796 1.5799998045 -4.39997911453 1]
		Scale 0.992736293023 0.992736293023 0.992736293023
		Attribute "identifier" "name" ["11211_26"]
		ReadArchive "test01_Bricks_Archive.zip!11211_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 1.0 -0.0 0 0.0 0.0 1.0 0 1.0 -0.0 0.0 0 0.399998545647 2.13999986649 -3.99997854233 1]
		Scale 0.999767536571 0.999767536571 0.999767536571
		Attribute "identifier" "name" ["85984_26_26_616009"]
		ReadArchive "test01_Bricks_Archive.zip!85984_26_26_616009.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -0.399994134903 0.939999580383 -6.79999113083 1]
		Scale 0.997127254644 0.997127254644 0.997127254644
		Attribute "identifier" "name" ["3020_194"]
		ReadArchive "test01_Bricks_Archive.zip!3020_194.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 1.20000422001 1.25999963284 -6.79999113083 1]
		Scale 0.998214679907 0.998214679907 0.998214679907
		Attribute "identifier" "name" ["50943_23"]
		ReadArchive "test01_Bricks_Archive.zip!50943_23.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -1.19999337196 0.619998693466 -6.79999113083 1]
		Scale 0.997952734682 0.997952734682 0.997952734682
		Attribute "identifier" "name" ["18980_26"]
		ReadArchive "test01_Bricks_Archive.zip!18980_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 -1.0 -0.0 0 -0.0 -0.0 1.0 0 1.20000803471 1.06000232697 -7.59999036789 1]
		Scale 0.99870681386 0.99870681386 0.99870681386
		Attribute "identifier" "name" ["42446_208"]
		ReadArchive "test01_Bricks_Archive.zip!42446_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 0.0 -1.0 0 -0.0 1.0 0.0 0 0.399787545204 1.46000230312 -8.11999130249 1]
		Scale 0.998860115918 0.998860115918 0.998860115918
		Attribute "identifier" "name" ["3069_1_1_88252"]
		ReadArchive "test01_Bricks_Archive.zip!3069_1_1_88252.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 1.20000422001 0.619998693466 -5.99998998642 1]
		Scale 0.996175436284 0.996175436284 0.996175436284
		Attribute "identifier" "name" ["3021_26"]
		ReadArchive "test01_Bricks_Archive.zip!3021_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -0.399994134903 0.299999713898 -4.39998006821 1]
		Scale 0.999010381948 0.999010381948 0.999010381948
		Attribute "identifier" "name" ["18975_199"]
		ReadArchive "test01_Bricks_Archive.zip!18975_199.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 1.99999976158 1.57899975777 -5.99998044968 1]
		Scale 0.994896124206 0.994896124206 0.994896124206
		Attribute "identifier" "name" ["18974_208"]
		ReadArchive "test01_Bricks_Archive.zip!18974_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 2.7999997139 3.17999958992 -4.400203228 1]
		Scale 0.997182543557 0.997182543557 0.997182543557
		Attribute "identifier" "name" ["3069_208_208_0"]
		ReadArchive "test01_Bricks_Archive.zip!3069_208_208_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 2.79999947548 2.85999965668 -4.39998006821 1]
		Scale 0.996782082768 0.996782082768 0.996782082768
		Attribute "identifier" "name" ["3024_208"]
		ReadArchive "test01_Bricks_Archive.zip!3024_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 1.99999976158 2.85999965668 -5.19998121262 1]
		Scale 0.993027407507 0.993027407507 0.993027407507
		Attribute "identifier" "name" ["3794_23"]
		ReadArchive "test01_Bricks_Archive.zip!3794_23.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 1.99999976158 1.89999961853 -3.59998083115 1]
		Scale 0.992925200808 0.992925200808 0.992925200808
		Attribute "identifier" "name" ["50746_26"]
		ReadArchive "test01_Bricks_Archive.zip!50746_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 1.99999976158 1.25999975204 -3.5999751091 1]
		Scale 0.998971037306 0.998971037306 0.998971037306
		Attribute "identifier" "name" ["6141_199"]
		ReadArchive "test01_Bricks_Archive.zip!6141_199.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 0.40000641346 0.299998760223 -6.79999113083 1]
		Scale 0.992740039772 0.992740039772 0.992740039772
		Attribute "identifier" "name" ["3022_199"]
		ReadArchive "test01_Bricks_Archive.zip!3022_199.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 -1.0 -0.0 0 -0.0 -0.0 1.0 0 0.400008797646 1.06000232697 -7.59999036789 1]
		Scale 0.996994794373 0.996994794373 0.996994794373
		Attribute "identifier" "name" ["42446_208"]
		ReadArchive "test01_Bricks_Archive.zip!42446_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 0.400004982948 0.940002202988 2.00002717972 1]
		Scale 0.996147554715 0.996147554715 0.996147554715
		Attribute "identifier" "name" ["30029_23"]
		ReadArchive "test01_Bricks_Archive.zip!30029_23.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 2.00000357628 0.619998693466 -1.99997663498 1]
		Scale 0.993125036655 0.993125036655 0.993125036655
		Attribute "identifier" "name" ["24299_208"]
		ReadArchive "test01_Bricks_Archive.zip!24299_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 2.00000357628 0.299998760223 -1.99997663498 1]
		Scale 0.993330357813 0.993330357813 0.993330357813
		Attribute "identifier" "name" ["41770_26"]
		ReadArchive "test01_Bricks_Archive.zip!41770_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 2.00000739098 0.619998693466 -0.39997625351 1]
		Scale 0.996914890858 0.996914890858 0.996914890858
		Attribute "identifier" "name" ["3710_208"]
		ReadArchive "test01_Bricks_Archive.zip!3710_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 2.00000739098 0.940002202988 1.20002412796 1]
		Scale 0.995663168225 0.995663168225 0.995663168225
		Attribute "identifier" "name" ["3023_208"]
		ReadArchive "test01_Bricks_Archive.zip!3023_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 2.00000500679 0.620002150536 -3.59997320175 1]
		Scale 0.999699742745 0.999699742745 0.999699742745
		Attribute "identifier" "name" ["3023_26"]
		ReadArchive "test01_Bricks_Archive.zip!3023_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 1.20000422001 1.58199977875 -2.79997587204 1]
		Scale 0.996616963619 0.996616963619 0.996616963619
		Attribute "identifier" "name" ["3829_194"]
		ReadArchive "test01_Bricks_Archive.zip!3829_194.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.819151937962 -0.573576569557 0 0.0 0.573576569557 0.819151937962 0 1.0 -0.0 0.0 0 0.800000071526 2.7980363369 -3.02984189987 1]
		Scale 0.992752663185 0.992752663185 0.992752663185
		Attribute "identifier" "name" ["3828_26"]
		ReadArchive "test01_Bricks_Archive.zip!3828_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 1.20000422001 0.621999740601 -2.79997587204 1]
		Scale 0.996848407366 0.996848407366 0.996848407366
		Attribute "identifier" "name" ["2877_194"]
		ReadArchive "test01_Bricks_Archive.zip!2877_194.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 2.00000357628 1.25999975204 0.400028705597 1]
		Scale 0.997336304234 0.997336304234 0.997336304234
		Attribute "identifier" "name" ["85080_23"]
		ReadArchive "test01_Bricks_Archive.zip!85080_23.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 0.400006175041 0.622002243996 -0.399971961975 1]
		Scale 0.999604506676 0.999604506676 0.999604506676
		Attribute "identifier" "name" ["85984_1_1_0"]
		ReadArchive "test01_Bricks_Archive.zip!85984_1_1_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -0.399994134903 1.25999963284 -6.79999113083 1]
		Scale 0.996262157562 0.996262157562 0.996262157562
		Attribute "identifier" "name" ["50943_23"]
		ReadArchive "test01_Bricks_Archive.zip!50943_23.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -0.3999979496 2.21899986267 -5.99998998642 1]
		Scale 0.994236277356 0.994236277356 0.994236277356
		Attribute "identifier" "name" ["3024_194"]
		ReadArchive "test01_Bricks_Archive.zip!3024_194.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 0.400001168251 0.619998693466 2.80002641678 1]
		Scale 0.993103335371 0.993103335371 0.993103335371
		Attribute "identifier" "name" ["3021_194"]
		ReadArchive "test01_Bricks_Archive.zip!3021_194.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -1.19999289513 0.299998760223 1.20002365112 1]
		Scale 0.995776747639 0.995776747639 0.995776747639
		Attribute "identifier" "name" ["3666_26"]
		ReadArchive "test01_Bricks_Archive.zip!3666_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -0.399986505508 0.299999713898 3.60002374649 1]
		Scale 0.993057988682 0.993057988682 0.993057988682
		Attribute "identifier" "name" ["18975_199"]
		ReadArchive "test01_Bricks_Archive.zip!18975_199.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 2.00000739098 1.57899975777 2.00002527237 1]
		Scale 0.998597861739 0.998597861739 0.998597861739
		Attribute "identifier" "name" ["18974_208"]
		ReadArchive "test01_Bricks_Archive.zip!18974_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 2.80000305176 2.86000013351 2.79979753494 1]
		Scale 0.998686382217 0.998686382217 0.998686382217
		Attribute "identifier" "name" ["3069_26_26_0"]
		ReadArchive "test01_Bricks_Archive.zip!3069_26_26_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 2.80000686646 2.85899972916 2.00002527237 1]
		Scale 0.993432963094 0.993432963094 0.993432963094
		Attribute "identifier" "name" ["3070_26_26_0"]
		ReadArchive "test01_Bricks_Archive.zip!3070_26_26_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 2.80000686646 2.53900003433 2.00002527237 1]
		Scale 0.995333512464 0.995333512464 0.995333512464
		Attribute "identifier" "name" ["3024_208"]
		ReadArchive "test01_Bricks_Archive.zip!3024_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 2.80000686646 2.53900003433 4.4000248909 1]
		Scale 0.996857412366 0.996857412366 0.996857412366
		Attribute "identifier" "name" ["6141_41"]
		ReadArchive "test01_Bricks_Archive.zip!6141_41.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 2.80000686646 2.85899972916 4.40002298355 1]
		Scale 0.997751055012 0.997751055012 0.997751055012
		Attribute "identifier" "name" ["25269_26_26_0"]
		ReadArchive "test01_Bricks_Archive.zip!25269_26_26_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 2.00000739098 2.21999979019 4.4000248909 1]
		Scale 0.995499973816 0.995499973816 0.995499973816
		Attribute "identifier" "name" ["3024_26"]
		ReadArchive "test01_Bricks_Archive.zip!3024_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 2.00000739098 1.89999985695 4.4000248909 1]
		Scale 0.99923563943 0.99923563943 0.99923563943
		Attribute "identifier" "name" ["3024_26"]
		ReadArchive "test01_Bricks_Archive.zip!3024_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 1.99999976158 2.53999996185 4.40002679825 1]
		Scale 0.993440436197 0.993440436197 0.993440436197
		Attribute "identifier" "name" ["24299_26"]
		ReadArchive "test01_Bricks_Archive.zip!24299_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 2.00000119209 1.25899958611 4.4000287056 1]
		Scale 0.997906708835 0.997906708835 0.997906708835
		Attribute "identifier" "name" ["3024_26"]
		ReadArchive "test01_Bricks_Archive.zip!3024_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 2.00000119209 0.938999652863 4.4000287056 1]
		Scale 0.997877888088 0.997877888088 0.997877888088
		Attribute "identifier" "name" ["3024_26"]
		ReadArchive "test01_Bricks_Archive.zip!3024_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 1.20000112057 0.61899971962 3.60002946854 1]
		Scale 0.996245648551 0.996245648551 0.996245648551
		Attribute "identifier" "name" ["2420_26"]
		ReadArchive "test01_Bricks_Archive.zip!2420_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 2.00000357628 2.21999979019 2.00002336502 1]
		Scale 0.993171068917 0.993171068917 0.993171068917
		Attribute "identifier" "name" ["6141_199"]
		ReadArchive "test01_Bricks_Archive.zip!6141_199.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 2.00000357628 1.89999961853 2.00002527237 1]
		Scale 0.994674034671 0.994674034671 0.994674034671
		Attribute "identifier" "name" ["2420_26"]
		ReadArchive "test01_Bricks_Archive.zip!2420_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 0.40001642704 2.85999965668 2.00001764297 1]
		Scale 0.996607107888 0.996607107888 0.996607107888
		Attribute "identifier" "name" ["3794_26"]
		ReadArchive "test01_Bricks_Archive.zip!3794_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -0.399994134903 2.53999996185 2.00002527237 1]
		Scale 0.994044173468 0.994044173468 0.994044173468
		Attribute "identifier" "name" ["3710_26"]
		ReadArchive "test01_Bricks_Archive.zip!3710_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 1.20000422001 2.21999979019 2.00002527237 1]
		Scale 0.995481972453 0.995481972453 0.995481972453
		Attribute "identifier" "name" ["3021_26"]
		ReadArchive "test01_Bricks_Archive.zip!3021_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 0.40001642704 2.85999965668 2.80001688004 1]
		Scale 0.995067498525 0.995067498525 0.995067498525
		Attribute "identifier" "name" ["3794_26"]
		ReadArchive "test01_Bricks_Archive.zip!3794_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 0.400004982948 2.53999996185 2.80002450943 1]
		Scale 0.998728332808 0.998728332808 0.998728332808
		Attribute "identifier" "name" ["3022_26"]
		ReadArchive "test01_Bricks_Archive.zip!3022_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 1.20022547245 2.85999965668 3.60002565384 1]
		Scale 0.999293884791 0.999293884791 0.999293884791
		Attribute "identifier" "name" ["3069_26_26_0"]
		ReadArchive "test01_Bricks_Archive.zip!3069_26_26_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 0.400001168251 1.57999968529 2.00002527237 1]
		Scale 0.993844092737 0.993844092737 0.993844092737
		Attribute "identifier" "name" ["3022_26"]
		ReadArchive "test01_Bricks_Archive.zip!3022_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 1.99999976158 1.25999975204 2.00002717972 1]
		Scale 0.999948470614 0.999948470614 0.999948470614
		Attribute "identifier" "name" ["2420_26"]
		ReadArchive "test01_Bricks_Archive.zip!2420_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 0.400001168251 1.25899982452 3.60002756119 1]
		Scale 0.994424934826 0.994424934826 0.994424934826
		Attribute "identifier" "name" ["3065_26"]
		ReadArchive "test01_Bricks_Archive.zip!3065_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 1.20000422001 1.57899975777 4.4000287056 1]
		Scale 0.997866270713 0.997866270713 0.997866270713
		Attribute "identifier" "name" ["11211_208"]
		ReadArchive "test01_Bricks_Archive.zip!11211_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 0.400001168251 0.938999652863 4.4000287056 1]
		Scale 0.996382671142 0.996382671142 0.996382671142
		Attribute "identifier" "name" ["99206_208"]
		ReadArchive "test01_Bricks_Archive.zip!99206_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 0.0 1.0 0 -0.0 -1.0 0.0 0 0.399997353554 2.13899946213 5.1200299263 1]
		Scale 0.998784956002 0.998784956002 0.998784956002
		Attribute "identifier" "name" ["3794_26"]
		ReadArchive "test01_Bricks_Archive.zip!3794_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 0.0 1.0 0 -0.0 -1.0 0.0 0 -0.400001764297 2.13899946213 4.80003023148 1]
		Scale 0.995640511077 0.995640511077 0.995640511077
		Attribute "identifier" "name" ["3020_26"]
		ReadArchive "test01_Bricks_Archive.zip!3020_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -0.399992704391 0.299998760223 2.00002336502 1]
		Scale 0.99945648194 0.99945648194 0.99945648194
		Attribute "identifier" "name" ["3710_199"]
		ReadArchive "test01_Bricks_Archive.zip!3710_199.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -1.19999814034 2.5389995575 -5.99998998642 1]
		Scale 0.997297783984 0.997297783984 0.997297783984
		Attribute "identifier" "name" ["3794_23"]
		ReadArchive "test01_Bricks_Archive.zip!3794_23.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 0.400001168251 1.25999987125 1.20003175735 1]
		Scale 0.996552679901 0.996552679901 0.996552679901
		Attribute "identifier" "name" ["85080_23"]
		ReadArchive "test01_Bricks_Archive.zip!85080_23.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 0.0 1.0 0 -0.0 1.0 0.0 0 1.20021784306 1.33899927139 5.1200299263 1]
		Scale 0.99331824846 0.99331824846 0.99331824846
		Attribute "identifier" "name" ["3069_1_1_88252"]
		ReadArchive "test01_Bricks_Archive.zip!3069_1_1_88252.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 0.400012612343 1.89999961853 2.80002260208 1]
		Scale 0.994227370327 0.994227370327 0.994227370327
		Attribute "identifier" "name" ["2420_26"]
		ReadArchive "test01_Bricks_Archive.zip!2420_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 -0.3999979496 1.25999975204 -3.59998655319 1]
		Scale 0.995660226803 0.995660226803 0.995660226803
		Attribute "identifier" "name" ["6141_199"]
		ReadArchive "test01_Bricks_Archive.zip!6141_199.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 -0.399994134903 1.26000213623 -2.79997396469 1]
		Scale 0.995673620685 0.995673620685 0.995673620685
		Attribute "identifier" "name" ["50746_26"]
		ReadArchive "test01_Bricks_Archive.zip!50746_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 -0.399986505508 2.21999979019 2.00002145767 1]
		Scale 0.997823169714 0.997823169714 0.997823169714
		Attribute "identifier" "name" ["6141_199"]
		ReadArchive "test01_Bricks_Archive.zip!6141_199.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 0.400001168251 1.25999975204 2.80002832413 1]
		Scale 0.994710538957 0.994710538957 0.994710538957
		Attribute "identifier" "name" ["2420_26"]
		ReadArchive "test01_Bricks_Archive.zip!2420_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 -0.399995088577 0.620002269745 -3.59997320175 1]
		Scale 0.998948165119 0.998948165119 0.998948165119
		Attribute "identifier" "name" ["3023_26"]
		ReadArchive "test01_Bricks_Archive.zip!3023_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -0.3999979496 1.57899963856 -3.59999036789 1]
		Scale 0.997640805661 0.997640805661 0.997640805661
		Attribute "identifier" "name" ["18974_208"]
		ReadArchive "test01_Bricks_Archive.zip!18974_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -1.19999814034 2.85999965668 -5.19999074936 1]
		Scale 0.993190427233 0.993190427233 0.993190427233
		Attribute "identifier" "name" ["3794_23"]
		ReadArchive "test01_Bricks_Archive.zip!3794_23.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 -1.19999909401 3.1799993515 -4.40021371841 1]
		Scale 0.994523068346 0.994523068346 0.994523068346
		Attribute "identifier" "name" ["3069_208_208_0"]
		ReadArchive "test01_Bricks_Archive.zip!3069_208_208_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -1.19999814034 2.85999965668 -4.39999055862 1]
		Scale 0.993521262474 0.993521262474 0.993521262474
		Attribute "identifier" "name" ["3024_208"]
		ReadArchive "test01_Bricks_Archive.zip!3024_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 -0.3999979496 1.89999961853 -3.59999132156 1]
		Scale 0.999292195525 0.999292195525 0.999292195525
		Attribute "identifier" "name" ["50746_26"]
		ReadArchive "test01_Bricks_Archive.zip!50746_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 -0.399994134903 0.619998693466 -0.39997625351 1]
		Scale 0.994596880842 0.994596880842 0.994596880842
		Attribute "identifier" "name" ["3710_208"]
		ReadArchive "test01_Bricks_Archive.zip!3710_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 -0.399994134903 0.939999818802 1.20002603531 1]
		Scale 0.997611725452 0.997611725452 0.997611725452
		Attribute "identifier" "name" ["3023_208"]
		ReadArchive "test01_Bricks_Archive.zip!3023_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -0.399998903275 0.61899971962 4.4000287056 1]
		Scale 0.997294901715 0.997294901715 0.997294901715
		Attribute "identifier" "name" ["2420_26"]
		ReadArchive "test01_Bricks_Archive.zip!2420_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 -0.399994134903 0.619998693466 -1.99997282028 1]
		Scale 0.992792476152 0.992792476152 0.992792476152
		Attribute "identifier" "name" ["24307_208"]
		ReadArchive "test01_Bricks_Archive.zip!24307_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 -0.399994134903 0.299998760223 -1.99997615814 1]
		Scale 0.999976500196 0.999976500196 0.999976500196
		Attribute "identifier" "name" ["41769_26"]
		ReadArchive "test01_Bricks_Archive.zip!41769_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -0.399998903275 1.25899958611 4.4000287056 1]
		Scale 0.999963180586 0.999963180586 0.999963180586
		Attribute "identifier" "name" ["3024_26"]
		ReadArchive "test01_Bricks_Archive.zip!3024_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -0.399998903275 0.938999652863 4.4000287056 1]
		Scale 0.995330411396 0.995330411396 0.995330411396
		Attribute "identifier" "name" ["3024_26"]
		ReadArchive "test01_Bricks_Archive.zip!3024_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -0.399990320206 1.57899975777 4.4000248909 1]
		Scale 0.995787314218 0.995787314218 0.995787314218
		Attribute "identifier" "name" ["18974_208"]
		ReadArchive "test01_Bricks_Archive.zip!18974_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 -1.19998955727 2.86000013351 2.79980134964 1]
		Scale 0.997601193743 0.997601193743 0.997601193743
		Attribute "identifier" "name" ["3069_26_26_0"]
		ReadArchive "test01_Bricks_Archive.zip!3069_26_26_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -1.19998955727 2.85899972916 2.00002527237 1]
		Scale 0.998680424687 0.998680424687 0.998680424687
		Attribute "identifier" "name" ["3070_26_26_0"]
		ReadArchive "test01_Bricks_Archive.zip!3070_26_26_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -1.19998955727 2.53900003433 2.00002527237 1]
		Scale 0.997142037157 0.997142037157 0.997142037157
		Attribute "identifier" "name" ["3024_208"]
		ReadArchive "test01_Bricks_Archive.zip!3024_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -0.3999979496 2.53999996185 4.40002679825 1]
		Scale 0.997613945955 0.997613945955 0.997613945955
		Attribute "identifier" "name" ["24307_26"]
		ReadArchive "test01_Bricks_Archive.zip!24307_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -0.399990320206 2.21999979019 4.4000248909 1]
		Scale 0.998867756931 0.998867756931 0.998867756931
		Attribute "identifier" "name" ["3024_26"]
		ReadArchive "test01_Bricks_Archive.zip!3024_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -0.399990320206 1.89999985695 4.4000248909 1]
		Scale 0.993592860063 0.993592860063 0.993592860063
		Attribute "identifier" "name" ["3024_26"]
		ReadArchive "test01_Bricks_Archive.zip!3024_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -1.19998955727 2.53900003433 4.4000248909 1]
		Scale 0.997882228759 0.997882228759 0.997882228759
		Attribute "identifier" "name" ["6141_41"]
		ReadArchive "test01_Bricks_Archive.zip!6141_41.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -1.19998955727 2.85899972916 4.40002298355 1]
		Scale 0.996093316441 0.996093316441 0.996093316441
		Attribute "identifier" "name" ["25269_26_26_0"]
		ReadArchive "test01_Bricks_Archive.zip!25269_26_26_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 1.5999994278 3.1789996624 -5.1999797821 1]
		Scale 0.994441815329 0.994441815329 0.994441815329
		Attribute "identifier" "name" ["93606_208"]
		ReadArchive "test01_Bricks_Archive.zip!93606_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 0.400001049042 2.8599998951 0.400030612946 1]
		Scale 0.998725660274 0.998725660274 0.998725660274
		Attribute "identifier" "name" ["2412_26"]
		ReadArchive "test01_Bricks_Archive.zip!2412_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 2.00000333786 2.53999996185 0.400030612946 1]
		Scale 0.996336595641 0.996336595641 0.996336595641
		Attribute "identifier" "name" ["51739_26"]
		ReadArchive "test01_Bricks_Archive.zip!51739_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 0.400004863739 2.86000013351 1.20003175735 1]
		Scale 0.999020545772 0.999020545772 0.999020545772
		Attribute "identifier" "name" ["85984_26_26_0"]
		ReadArchive "test01_Bricks_Archive.zip!85984_26_26_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 2.00000333786 2.22000002861 0.400030612946 1]
		Scale 0.994944223165 0.994944223165 0.994944223165
		Attribute "identifier" "name" ["51739_26"]
		ReadArchive "test01_Bricks_Archive.zip!51739_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 2.00000333786 2.8599998951 0.400026798248 1]
		Scale 0.997012960991 0.997012960991 0.997012960991
		Attribute "identifier" "name" ["18973_111"]
		ReadArchive "test01_Bricks_Archive.zip!18973_111.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -1.20000123978 2.53900003433 -3.59997963905 1]
		Scale 0.999258798151 0.999258798151 0.999258798151
		Attribute "identifier" "name" ["3666_208"]
		ReadArchive "test01_Bricks_Archive.zip!3666_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -0.799998521805 3.1789996624 -5.19999027252 1]
		Scale 0.994586522365 0.994586522365 0.994586522365
		Attribute "identifier" "name" ["93606_208"]
		ReadArchive "test01_Bricks_Archive.zip!93606_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 2.40000104904 1.20000004768 -4.79997968674 1]
		Scale 0.995607575884 0.995607575884 0.995607575884
		Attribute "identifier" "name" ["18977_26"]
		ReadArchive "test01_Bricks_Archive.zip!18977_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 2.40000104904 1.20000004768 -4.79997968674 1]
		Scale 0.999668882982 0.999668882982 0.999668882982
		Attribute "identifier" "name" ["18976_315"]
		ReadArchive "test01_Bricks_Archive.zip!18976_315.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 3.2000002861 1.20000004768 -4.79997968674 1]
		Scale 0.996239875611 0.996239875611 0.996239875611
		Attribute "identifier" "name" ["43093_5"]
		ReadArchive "test01_Bricks_Archive.zip!43093_5.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 2.80000734329 2.53999876976 1.2000232935 1]
		Scale 0.995404706431 0.995404706431 0.995404706431
		Attribute "identifier" "name" ["50746_26"]
		ReadArchive "test01_Bricks_Archive.zip!50746_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 2.80000734329 0.619998693466 -0.399976611137 1]
		Scale 0.997432606289 0.997432606289 0.997432606289
		Attribute "identifier" "name" ["18653_208"]
		ReadArchive "test01_Bricks_Archive.zip!18653_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 0.0 1.0 0 -0.0 -1.0 0.0 0 1.99999570847 2.13899993896 5.12002849579 1]
		Scale 0.99917736602 0.99917736602 0.99917736602
		Attribute "identifier" "name" ["11477_26"]
		ReadArchive "test01_Bricks_Archive.zip!11477_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 2.00000476837 0.620002269745 -2.79997324944 1]
		Scale 0.993615772212 0.993615772212 0.993615772212
		Attribute "identifier" "name" ["24201_23"]
		ReadArchive "test01_Bricks_Archive.zip!24201_23.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.998265445232 0.0 0.0588751509786 0 0.0 1.0 -0.0 0 -0.0588751509786 -0.0 0.998265445232 0 -1.19999861717 2.85899972916 -3.59999370575 1]
		Scale 0.997697272252 0.997697272252 0.997697272252
		Attribute "identifier" "name" ["26047_208"]
		ReadArchive "test01_Bricks_Archive.zip!26047_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.000885172223207 0.999887049198 -0.0150098577142 0 -0.998265385628 0.0 -0.0588747933507 0 -0.0588681399822 0.0150359338149 0.998152554035 0 -0.81643986702 1.52099776268 -1.95061659813 1]
		Scale 0.99609640699 0.99609640699 0.99609640699
		Attribute "identifier" "name" ["2420_208"]
		ReadArchive "test01_Bricks_Archive.zip!2420_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-0.0588681548834 0.0150358751416 0.998152554035 0 -0.998265385628 0.0 -0.0588748492301 0 -0.000885170127731 -0.999887049198 0.0150097981095 0 -1.08808302879 2.30887842178 -2.77998614311 1]
		Scale 0.995316484349 0.995316484349 0.995316484349
		Attribute "identifier" "name" ["4085_208"]
		ReadArchive "test01_Bricks_Archive.zip!4085_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-0.0588681511581 0.0150358751416 0.998152554035 0 -0.998265326023 0.0 -0.0588748492301 0 -0.000885170011315 -0.999887049198 0.0150097981095 0 -1.40752792358 2.30887842178 -2.79882621765 1]
		Scale 0.993887041994 0.993887041994 0.993887041994
		Attribute "identifier" "name" ["11153_208"]
		ReadArchive "test01_Bricks_Archive.zip!11153_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-0.0588681995869 0.0150358565152 0.99815261364 0 -0.998265385628 0.0 -0.0588748492301 0 -0.000885166751686 -0.999887049198 0.0150097785518 0 -1.40823054314 1.50896835327 -2.78681612015 1]
		Scale 0.994606203469 0.994606203469 0.994606203469
		Attribute "identifier" "name" ["11153_23"]
		ReadArchive "test01_Bricks_Archive.zip!11153_23.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 1.10864639282e-05 3.17999982834 2.80001735687 1]
		Scale 0.998945353382 0.998945353382 0.998945353382
		Attribute "identifier" "name" ["63864_26"]
		ReadArchive "test01_Bricks_Archive.zip!63864_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -1.19999742508 2.53999996185 1.20002806187 1]
		Scale 0.999169479507 0.999169479507 0.999169479507
		Attribute "identifier" "name" ["50746_26"]
		ReadArchive "test01_Bricks_Archive.zip!50746_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 -1.19999742508 0.619998812675 -0.399972319603 1]
		Scale 0.992509434535 0.992509434535 0.992509434535
		Attribute "identifier" "name" ["18653_208"]
		ReadArchive "test01_Bricks_Archive.zip!18653_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 1.10864639282e-05 3.17999982834 2.00001764297 1]
		Scale 0.99908088121 0.99908088121 0.99908088121
		Attribute "identifier" "name" ["63864_26"]
		ReadArchive "test01_Bricks_Archive.zip!63864_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 2.40000486374 1.20000004768 3.20002269745 1]
		Scale 0.996237782791 0.996237782791 0.996237782791
		Attribute "identifier" "name" ["18977_26"]
		ReadArchive "test01_Bricks_Archive.zip!18977_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 2.40000486374 1.20000004768 3.20002269745 1]
		Scale 0.999728366055 0.999728366055 0.999728366055
		Attribute "identifier" "name" ["18976_315"]
		ReadArchive "test01_Bricks_Archive.zip!18976_315.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 3.2000079155 1.20000004768 3.20002269745 1]
		Scale 0.995636202547 0.995636202547 0.995636202547
		Attribute "identifier" "name" ["43093_5"]
		ReadArchive "test01_Bricks_Archive.zip!43093_5.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 0.0 1.0 0 -0.0 -1.0 0.0 0 0.800000011921 2.13899946213 5.44003009796 1]
		Scale 0.9949389457 0.9949389457 0.9949389457
		Attribute "identifier" "name" ["98138_23_23_0"]
		ReadArchive "test01_Bricks_Archive.zip!98138_23_23_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 0.0 1.0 0 -0.0 -1.0 0.0 0 1.99999570847 1.33899998665 5.12002849579 1]
		Scale 0.99864584071 0.99864584071 0.99864584071
		Attribute "identifier" "name" ["11477_208"]
		ReadArchive "test01_Bricks_Archive.zip!11477_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -1.59999895096 1.20000004768 -4.79997587204 1]
		Scale 0.993532234739 0.993532234739 0.993532234739
		Attribute "identifier" "name" ["43093_5"]
		ReadArchive "test01_Bricks_Archive.zip!43093_5.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -0.799999713898 1.20000004768 -4.79997587204 1]
		Scale 0.995971532994 0.995971532994 0.995971532994
		Attribute "identifier" "name" ["18976_194"]
		ReadArchive "test01_Bricks_Archive.zip!18976_194.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -0.799999713898 1.20000004768 -4.79997587204 1]
		Scale 0.993452991686 0.993452991686 0.993452991686
		Attribute "identifier" "name" ["18977_26"]
		ReadArchive "test01_Bricks_Archive.zip!18977_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 -1.0 -0.0 0 -0.0 -0.0 1.0 0 -0.400000035763 1.10000026226 -7.63999080658 1]
		Scale 0.996150052273 0.996150052273 0.996150052273
		Attribute "identifier" "name" ["42446_208"]
		ReadArchive "test01_Bricks_Archive.zip!42446_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 0.0 -1.0 0 -0.0 -1.0 0.0 0 -0.400000035763 1.50000023842 -8.15999126434 1]
		Scale 0.997483822726 0.997483822726 0.997483822726
		Attribute "identifier" "name" ["11477_208"]
		ReadArchive "test01_Bricks_Archive.zip!11477_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 -1.0 -0.0 0 0.0 0.0 -1.0 0 1.0 -0.0 0.0 0 -1.2000002861 1.50000011921 -7.51999187469 1]
		Scale 0.99410405001 0.99410405001 0.99410405001
		Attribute "identifier" "name" ["3024_208"]
		ReadArchive "test01_Bricks_Archive.zip!3024_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 -1.0 -0.0 0 0.0 0.0 -1.0 0 1.0 -0.0 0.0 0 -1.2000002861 1.50000011921 -7.19999217987 1]
		Scale 0.9940573802 0.9940573802 0.9940573802
		Attribute "identifier" "name" ["3024_208"]
		ReadArchive "test01_Bricks_Archive.zip!3024_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -1.20000123978 0.94000005722 -6.79999256134 1]
		Scale 0.995215529189 0.995215529189 0.995215529189
		Attribute "identifier" "name" ["87087_208"]
		ReadArchive "test01_Bricks_Archive.zip!87087_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -1.20000123978 2.22000002861 -6.79999446869 1]
		Scale 0.997242355831 0.997242355831 0.997242355831
		Attribute "identifier" "name" ["3070_23_23_0"]
		ReadArchive "test01_Bricks_Archive.zip!3070_23_23_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 -1.20000123978 1.90000009537 -7.59999370575 1]
		Scale 0.994741262682 0.994741262682 0.994741262682
		Attribute "identifier" "name" ["3023_26"]
		ReadArchive "test01_Bricks_Archive.zip!3023_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -1.20000123978 2.22000002861 -7.59999370575 1]
		Scale 0.997291561788 0.997291561788 0.997291561788
		Attribute "identifier" "name" ["25269_42_42_0"]
		ReadArchive "test01_Bricks_Archive.zip!25269_42_42_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 0.0 1.0 0 -0.0 1.0 0.0 0 -0.400005757809 1.33899962902 5.12002849579 1]
		Scale 0.996880613413 0.996880613413 0.996880613413
		Attribute "identifier" "name" ["11477_208"]
		ReadArchive "test01_Bricks_Archive.zip!11477_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -1.59999513626 1.20000004768 3.20002269745 1]
		Scale 0.994846913749 0.994846913749 0.994846913749
		Attribute "identifier" "name" ["43093_5"]
		ReadArchive "test01_Bricks_Archive.zip!43093_5.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -0.799992084503 1.20000004768 3.20002269745 1]
		Scale 0.99995339209 0.99995339209 0.99995339209
		Attribute "identifier" "name" ["18976_194"]
		ReadArchive "test01_Bricks_Archive.zip!18976_194.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -0.799992084503 1.20000004768 3.20002269745 1]
		Scale 0.995248783925 0.995248783925 0.995248783925
		Attribute "identifier" "name" ["18977_26"]
		ReadArchive "test01_Bricks_Archive.zip!18977_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 0.0 1.0 0 -0.0 1.0 0.0 0 -0.400001943111 2.13899970055 5.12002849579 1]
		Scale 0.995744717895 0.995744717895 0.995744717895
		Attribute "identifier" "name" ["11477_26"]
		ReadArchive "test01_Bricks_Archive.zip!11477_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 -0.399995267391 0.620002388954 -2.79997301102 1]
		Scale 0.995084165612 0.995084165612 0.995084165612
		Attribute "identifier" "name" ["24201_23"]
		ReadArchive "test01_Bricks_Archive.zip!24201_23.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 0.800000011921 2.85999941826 -6.79998731613 1]
		Scale 0.998465663367 0.998465663367 0.998465663367
		Attribute "identifier" "name" ["11477_208"]
		ReadArchive "test01_Bricks_Archive.zip!11477_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 -1.0 -0.0 0 0.0 0.0 -1.0 0 1.0 -0.0 0.0 0 2.80000257492 1.5 -7.51999568939 1]
		Scale 0.994416797322 0.994416797322 0.994416797322
		Attribute "identifier" "name" ["3024_208"]
		ReadArchive "test01_Bricks_Archive.zip!3024_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 -1.0 -0.0 0 0.0 0.0 -1.0 0 1.0 -0.0 0.0 0 2.80000257492 1.5 -7.19999599457 1]
		Scale 0.99454885444 0.99454885444 0.99454885444
		Attribute "identifier" "name" ["3024_208"]
		ReadArchive "test01_Bricks_Archive.zip!3024_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 2.80000257492 0.939999938011 -6.79999637604 1]
		Scale 0.996153430115 0.996153430115 0.996153430115
		Attribute "identifier" "name" ["87087_208"]
		ReadArchive "test01_Bricks_Archive.zip!87087_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 0.0 -1.0 0 -0.0 1.0 0.0 0 2.00000143051 1.5 -8.15999317169 1]
		Scale 0.995858260996 0.995858260996 0.995858260996
		Attribute "identifier" "name" ["11477_208"]
		ReadArchive "test01_Bricks_Archive.zip!11477_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 -1.0 -0.0 0 -0.0 -0.0 1.0 0 2.00000143051 1.09999990463 -7.63999271393 1]
		Scale 0.993473807674 0.993473807674 0.993473807674
		Attribute "identifier" "name" ["42446_208"]
		ReadArchive "test01_Bricks_Archive.zip!42446_208.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 2.80000257492 2.21999979019 -6.79999828339 1]
		Scale 0.99280525328 0.99280525328 0.99280525328
		Attribute "identifier" "name" ["3070_23_23_0"]
		ReadArchive "test01_Bricks_Archive.zip!3070_23_23_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 2.80000257492 1.90000009537 -7.59999752045 1]
		Scale 0.992828973148 0.992828973148 0.992828973148
		Attribute "identifier" "name" ["3023_26"]
		ReadArchive "test01_Bricks_Archive.zip!3023_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 2.80000257492 2.21999979019 -7.59999752045 1]
		Scale 0.992827185106 0.992827185106 0.992827185106
		Attribute "identifier" "name" ["25269_42_42_0"]
		ReadArchive "test01_Bricks_Archive.zip!25269_42_42_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 3.75999975204 1.2000002861 -4.79997968674 1]
		Scale 0.994057626079 0.994057626079 0.994057626079
		Attribute "identifier" "name" ["6589_26"]
		ReadArchive "test01_Bricks_Archive.zip!6589_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -0.400001466274 2.8599998951 -0.3999761343 1]
		Scale 0.996527906997 0.996527906997 0.996527906997
		Attribute "identifier" "name" ["18973_111"]
		ReadArchive "test01_Bricks_Archive.zip!18973_111.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -2.16000032425 1.20000016689 -4.79997682571 1]
		Scale 0.995744205346 0.995744205346 0.995744205346
		Attribute "identifier" "name" ["6589_26"]
		ReadArchive "test01_Bricks_Archive.zip!6589_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 0.0 1.0 -0.0 0 1.0 -0.0 0.0 0 -2.15999269485 1.20000016689 3.20002269745 1]
		Scale 0.993166838744 0.993166838744 0.993166838744
		Attribute "identifier" "name" ["6589_26"]
		ReadArchive "test01_Bricks_Archive.zip!6589_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 3.76000356674 1.2000002861 3.20002269745 1]
		Scale 0.998915973103 0.998915973103 0.998915973103
		Attribute "identifier" "name" ["6589_26"]
		ReadArchive "test01_Bricks_Archive.zip!6589_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.897292912006 0.00306926248595 0.441424936056 0 -0.00320614827797 0.999994754791 -0.000435858906712 0 -0.441423952579 -0.00102419871837 0.897298157215 0 6.40288925171 2.8828587532 1.11985254288 1]
		Scale 0.994175844589 0.994175844589 0.994175844589
		Attribute "identifier" "name" ["3626_283_283_283_283_99294_0_0"]
		ReadArchive "test01_Bricks_Archive.zip!3626_283_283_283_283_99294_0_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.951158761978 0.00318410992622 0.308685719967 0 -0.00320614827797 0.999994754791 -0.000435858994024 0 -0.308685332537 -0.000575140002184 0.951164126396 0 6.02652835846 1.60159218311 0.996934592724 1]
		Scale 0.993947146556 0.993947146556 0.993947146556
		Attribute "identifier" "name" ["3814_119_119_119_99660_0"]
		ReadArchive "test01_Bricks_Archive.zip!3814_119_119_119_99660_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.935815811157 -0.179103836417 0.30359607935 0 0.260356783867 0.93182682991 -0.252810537815 0 -0.237619638443 0.315627485514 0.91864913702 0 5.8143529892 2.51088643074 0.928627848625 1]
		Scale 0.99779718542 0.99779718542 0.99779718542
		Attribute "identifier" "name" ["3818_283_283_0"]
		ReadArchive "test01_Bricks_Archive.zip!3818_283_283_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.934647321701 0.185365229845 0.30343735218 0 -0.0924982875586 0.950736820698 -0.29587751627 0 -0.343334406614 0.248473674059 0.905749678612 0 6.9937877655 2.51483511925 1.31139683723 1]
		Scale 0.996324420581 0.996324420581 0.996324420581
		Attribute "identifier" "name" ["3819_283_283_0"]
		ReadArchive "test01_Bricks_Archive.zip!3819_283_283_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.920174241066 -0.229803204536 0.316969722509 0 0.311152219772 0.92063587904 -0.23582623899 0 -0.23761972785 0.315627574921 0.918649077415 0 5.70647907257 2.06949663162 0.30902826786 1]
		Scale 0.996169956633 0.996169956633 0.996169956633
		Attribute "identifier" "name" ["3820_283"]
		ReadArchive "test01_Bricks_Archive.zip!3820_283.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.921383798122 -0.0979071035981 0.376119941473 0 0.182135432959 0.963677823544 -0.19532482326 0 -0.343334496021 0.248473733664 0.905749559402 0 7.45065164566 2.11540460587 0.840218663216 1]
		Scale 0.9977939654 0.9977939654 0.9977939654
		Attribute "identifier" "name" ["3820_283"]
		ReadArchive "test01_Bricks_Archive.zip!3820_283.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.951158761978 0.00318410992622 0.308685719967 0 -0.00320614827797 0.999994754791 -0.000435858994024 0 -0.308685332537 -0.000575140002184 0.951164126396 0 6.02652835846 1.60159218311 0.996934592724 1]
		Scale 0.996781251234 0.996781251234 0.996781251234
		Attribute "identifier" "name" ["3815_119_119_119_0_0"]
		ReadArchive "test01_Bricks_Archive.zip!3815_119_119_119_0_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.951158881187 0.00318411248736 0.308685719967 0 -0.00320614827797 0.999994754791 -0.000435858906712 0 -0.308685392141 -0.000575139827561 0.951164066792 0 6.03165721893 0.00160135515034 0.997632980347 1]
		Scale 0.999226877444 0.999226877444 0.999226877444
		Attribute "identifier" "name" ["3816_119_119_119_119_93464_0_0"]
		ReadArchive "test01_Bricks_Archive.zip!3816_119_119_119_119_93464_0_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.951158881187 0.00318411248736 0.308685719967 0 -0.00320614827797 0.999994754791 -0.000435858906712 0 -0.308685392141 -0.000575139827561 0.951164066792 0 6.79257965088 0.00414862670004 1.24457979202 1]
		Scale 0.998096181627 0.998096181627 0.998096181627
		Attribute "identifier" "name" ["3817_119_119_119_119_93501_0_0"]
		ReadArchive "test01_Bricks_Archive.zip!3817_119_119_119_119_93501_0_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.897293031216 0.00306926225312 0.44142472744 0 -0.00320614827797 0.999994754791 -0.000435858994024 0 -0.441423892975 -0.00102419860195 0.897298157215 0 6.39981174469 3.84285378456 1.11943471432 1]
		Scale 0.994835159333 0.994835159333 0.994835159333
		Attribute "identifier" "name" ["85974_192_192_192_192_0_0_0"]
		ReadArchive "test01_Bricks_Archive.zip!85974_192_192_192_192_0_0_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.921383798122 -0.097907140851 0.376119911671 0 0.264790832996 0.866531550884 -0.423094540834 0 -0.284495592117 0.489425361156 0.824333131313 0 7.60386276245 2.06256961823 0.451144188643 1]
		Scale 0.993573485129 0.993573485129 0.993573485129
		Attribute "identifier" "name" ["15496_1"]
		ReadArchive "test01_Bricks_Archive.zip!15496_1.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 7.60000419617 1.59999608994 3.64998650551 1]
		Scale 0.994370086257 0.994370086257 0.994370086257
		Attribute "identifier" "name" ["3814_151_151_151_0_0"]
		ReadArchive "test01_Bricks_Archive.zip!3814_151_151_151_0_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.983255028725 -0.182235449553 -0.0 0 0.18223553896 0.983254909515 -0.0 0 -0.0 -0.0 1.0 0 7.38000679016 2.50999522209 3.64998745918 1]
		Scale 0.999865528274 0.999865528274 0.999865528274
		Attribute "identifier" "name" ["3818_151_151_0"]
		ReadArchive "test01_Bricks_Archive.zip!3818_151_151_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.983255028725 0.182235389948 -0.0 0 -0.175560086966 0.947237968445 0.268176972866 0 0.0488712675869 -0.263686090708 0.963369727135 0 8.62000846863 2.50999522209 3.64998698235 1]
		Scale 0.995033916452 0.995033916452 0.995033916452
		Attribute "identifier" "name" ["3819_151_151_0"]
		ReadArchive "test01_Bricks_Archive.zip!3819_151_151_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-0.983253538609 0.182243302464 -0.0 0 -0.182243406773 -0.983253538609 -0.0 0 -0.0 -0.0 1.0 0 7.1219959259 2.2702562809 2.96710753441 1]
		Scale 0.99680923185 0.99680923185 0.99680923185
		Attribute "identifier" "name" ["3820_283"]
		ReadArchive "test01_Bricks_Archive.zip!3820_283.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.964212536812 0.264098286629 0.0233728848398 0 -0.260587334633 0.927750945091 0.267156541348 0 0.0488712787628 -0.263686090708 0.963369727135 0 8.84272480011 2.46063971519 2.91633486748 1]
		Scale 0.99271451603 0.99271451603 0.99271451603
		Attribute "identifier" "name" ["3820_283"]
		ReadArchive "test01_Bricks_Archive.zip!3820_283.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 7.60000419617 1.59999608994 3.64998650551 1]
		Scale 0.994951851195 0.994951851195 0.994951851195
		Attribute "identifier" "name" ["3815_26_26_26_0_0"]
		ReadArchive "test01_Bricks_Archive.zip!3815_26_26_26_0_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 7.60000419617 0.0 3.64998650551 1]
		Scale 0.998936186357 0.998936186357 0.998936186357
		Attribute "identifier" "name" ["3816_26_26_26_26_0_0_0"]
		ReadArchive "test01_Bricks_Archive.zip!3816_26_26_26_26_0_0_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 8.40000343323 0.0 3.649985075 1]
		Scale 0.993022471676 0.993022471676 0.993022471676
		Attribute "identifier" "name" ["3817_26_26_26_26_0_0_0"]
		ReadArchive "test01_Bricks_Archive.zip!3817_26_26_26_26_0_0_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.979923069477 0.0 -0.199375957251 0 0.0 1.0 -0.0 0 0.199375957251 -0.0 0.979923069477 0 8.00000476837 2.87999534607 3.64998888969 1]
		Scale 0.997954234584 0.997954234584 0.997954234584
		Attribute "identifier" "name" ["3626_283_283_283_283_88940_0_0"]
		ReadArchive "test01_Bricks_Archive.zip!3626_283_283_283_283_88940_0_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.979923129082 0.0 -0.199375867844 0 0.0 1.0 -0.0 0 0.199375957251 -0.0 0.979923069477 0 8.00000476837 3.8399951458 3.64998936653 1]
		Scale 0.997026464788 0.997026464788 0.997026464788
		Attribute "identifier" "name" ["12893_283_194_283_0_0"]
		ReadArchive "test01_Bricks_Archive.zip!12893_283_194_283_0_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-0.7423132658 -0.197697103024 -0.640224099159 0 -0.264357000589 0.9643856287 0.00871545262635 0 0.615699768066 0.175717249513 -0.768138885498 0 8.40634059906 1.90603077412 2.0423412323 1]
		Scale 0.992642001253 0.992642001253 0.992642001253
		Attribute "identifier" "name" ["33054_40"]
		ReadArchive "test01_Bricks_Archive.zip!33054_40.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -5.20000076294 0.319999933243 -7.60000038147 1]
		Scale 0.997888161867 0.997888161867 0.997888161867
		Attribute "identifier" "name" ["87580_199"]
		ReadArchive "test01_Bricks_Archive.zip!87580_199.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 -4.40000009537 0.0 -7.60000038147 1]
		Scale 0.996024221885 0.996024221885 0.996024221885
		Attribute "identifier" "name" ["3020_26"]
		ReadArchive "test01_Bricks_Archive.zip!3020_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -5.20000076294 0.319999933243 -6.00000047684 1]
		Scale 0.995527489828 0.995527489828 0.995527489828
		Attribute "identifier" "name" ["87580_199"]
		ReadArchive "test01_Bricks_Archive.zip!87580_199.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -4.80000114441 0.95999956131 -6.4000005722 1]
		Scale 0.999474942047 0.999474942047 0.999474942047
		Attribute "identifier" "name" ["2921_28"]
		ReadArchive "test01_Bricks_Archive.zip!2921_28.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -4.80000114441 0.639999866486 -7.20000076294 1]
		Scale 0.993446264151 0.993446264151 0.993446264151
		Attribute "identifier" "name" ["85861_26"]
		ReadArchive "test01_Bricks_Archive.zip!85861_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 -4.80000019073 0.639999866486 -6.4000005722 1]
		Scale 0.992879070825 0.992879070825 0.992879070825
		Attribute "identifier" "name" ["3023_28"]
		ReadArchive "test01_Bricks_Archive.zip!3023_28.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -4.80000019073 0.959999799728 -5.60000038147 1]
		Scale 0.998171701415 0.998171701415 0.998171701415
		Attribute "identifier" "name" ["3005_28_28_0"]
		ReadArchive "test01_Bricks_Archive.zip!3005_28_28_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 -4.80000114441 1.91999959946 -6.4000005722 1]
		Scale 0.995141135837 0.995141135837 0.995141135837
		Attribute "identifier" "name" ["3023_28"]
		ReadArchive "test01_Bricks_Archive.zip!3023_28.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 -4.80000114441 2.23999977112 -6.4000005722 1]
		Scale 0.994538613937 0.994538613937 0.994538613937
		Attribute "identifier" "name" ["52107_28"]
		ReadArchive "test01_Bricks_Archive.zip!52107_28.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 -4.80000114441 3.19999933243 -6.4000005722 1]
		Scale 0.998610710685 0.998610710685 0.998610710685
		Attribute "identifier" "name" ["3023_28"]
		ReadArchive "test01_Bricks_Archive.zip!3023_28.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 -4.80000114441 3.51999902725 -6.4000005722 1]
		Scale 0.997535657978 0.997535657978 0.997535657978
		Attribute "identifier" "name" ["3023_28"]
		ReadArchive "test01_Bricks_Archive.zip!3023_28.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 -1.0 -0.0 0 1.0 0.0 -0.0 0 -0.0 -0.0 1.0 0 -4.40000104904 3.5999994278 -6.4000005722 1]
		Scale 0.997904622797 0.997904622797 0.997904622797
		Attribute "identifier" "name" ["87079_28_28_0"]
		ReadArchive "test01_Bricks_Archive.zip!87079_28_28_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 -1.0 -0.0 0 -1.0 0.0 -0.0 0 -0.0 -0.0 -1.0 0 -5.20000171661 3.59999990463 -5.60000038147 1]
		Scale 0.996021385233 0.996021385233 0.996021385233
		Attribute "identifier" "name" ["87079_28_28_0"]
		ReadArchive "test01_Bricks_Archive.zip!87079_28_28_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -4.80000114441 1.62999927998 -7.20000076294 1]
		Scale 0.995334874341 0.995334874341 0.995334874341
		Attribute "identifier" "name" ["85861_26"]
		ReadArchive "test01_Bricks_Archive.zip!85861_26.rib"
	AttributeEnd

	AttributeBegin
		Attribute "identifier" "name" ["64230_119_199_0_de212a4ec3814e1ca25b3c106ac65156"]
		ReadArchive "test01_Bricks_Archive.zip!64230_119_199_0_de212a4ec3814e1ca25b3c106ac65156.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 -4.80000114441 3.84000015259 -6.4000005722 1]
		Scale 0.997244765027 0.997244765027 0.997244765027
		Attribute "identifier" "name" ["26604_26"]
		ReadArchive "test01_Bricks_Archive.zip!26604_26.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 1.0 0.0 -0.0 0 -0.0 1.0 0.0 0 -4.40000104904 4.39999961853 -6.40022373199 1]
		Scale 0.999651466186 0.999651466186 0.999651466186
		Attribute "identifier" "name" ["3069_26_26_56756"]
		ReadArchive "test01_Bricks_Archive.zip!3069_26_26_56756.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [-1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 -1.0 0 -4.80000114441 3.83999896049 -5.60000038147 1]
		Scale 0.997823670569 0.997823670569 0.997823670569
		Attribute "identifier" "name" ["26604_26"]
		ReadArchive "test01_Bricks_Archive.zip!26604_26.rib"
	AttributeEnd

	AttributeBegin
		Attribute "identifier" "name" ["64230_311_26_0_194079425820443a85b67669853a2c9b"]
		ReadArchive "test01_Bricks_Archive.zip!64230_311_26_0_194079425820443a85b67669853a2c9b.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 -4.80000114441 4.79999923706 -6.4000005722 1]
		Scale 0.994652745601 0.994652745601 0.994652745601
		Attribute "identifier" "name" ["3794_28"]
		ReadArchive "test01_Bricks_Archive.zip!3794_28.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 -4.80000162125 5.11999940872 -6.00000095367 1]
		Scale 0.996138437466 0.996138437466 0.996138437466
		Attribute "identifier" "name" ["4589_1"]
		ReadArchive "test01_Bricks_Archive.zip!4589_1.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 1.0 0 0.0 1.0 -0.0 0 -1.0 -0.0 0.0 0 -4.80000162125 5.33004426956 -6.00000047684 1]
		Scale 0.993973971769 0.993973971769 0.993973971769
		Attribute "identifier" "name" ["3900_1"]
		ReadArchive "test01_Bricks_Archive.zip!3900_1.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.0 0.0 -1.0 0 1.0 0.0 -0.0 0 -0.0 -1.0 0.0 0 -4.72500181198 7.68004417419 -5.60000038147 1]
		Scale 0.994179380798 0.994179380798 0.994179380798
		Attribute "identifier" "name" ["14769_1_1_0"]
		ReadArchive "test01_Bricks_Archive.zip!14769_1_1_0.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [1.0 0.0 -0.0 0 0.0 1.0 -0.0 0 -0.0 -0.0 1.0 0 5.2000002861 0.0 -1.20000016689 1]
		Scale 0.999756348215 0.999756348215 0.999756348215
		Attribute "identifier" "name" ["3022_194"]
		ReadArchive "test01_Bricks_Archive.zip!3022_194.rib"
	AttributeEnd

	AttributeBegin
		ConcatTransform [0.416689574718 0.0 0.909048378468 0 0.0 1.0 -0.0 0 -0.909048378468 -0.0 0.416689574718 0 5.20000123978 0.319999992847 -0.400000572205 1]
		Scale 0.999625004369 0.999625004369 0.999625004369
		Attribute "identifier" "name" ["95342_1"]
		ReadArchive "test01_Bricks_Archive.zip!95342_1.rib"
	AttributeEnd

WorldEnd
