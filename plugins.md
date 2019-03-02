**Renderman Plugins**
A list of the default plugins from Renderman in python and rib format

# Bxdf
## Plugin PxrBlack 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Bxdf "PxrBlack" "id" 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Bxdf('PxrBlack','id',
{
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrDiffuse 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Bxdf "PxrDiffuse" "id" 
	"color diffuseColor"  [0.5 0.5 0.5] 
	"int transmissionBehavior"  [2] 
	"color transmissionColor"  [0. 0. 0.] 
	"float presence"  [1.] 
	"normal bumpNormal"  [0. 0. 0.] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Bxdf('PxrDiffuse','id',
{
	'color diffuseColor' : [0.5,0.5,0.5], 
	'int transmissionBehavior' : [2], 
	'color transmissionColor' : [0.,0.,0.], 
	'float presence' : [1.], 
	'normal bumpNormal' : [0.,0.,0.], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrConstant 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Bxdf "PxrConstant" "id" 
	"color emitColor"  [1. 1. 1.] 
	"float presence"  [1] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Bxdf('PxrConstant','id',
{
	'color emitColor' : [1.,1.,1.], 
	'float presence' : [1], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrLayerSurface 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Bxdf "PxrLayerSurface" "id" 
	"float inputMaterial"  ['No Value'] 
	"int utilityPattern"  [0] 
	"float diffuseGain"  [1.0] 
	"color diffuseColor"  [0.18 0.18 0.18] 
	"float diffuseRoughness"  [0.0] 
	"float diffuseExponent"  [1.0] 
	"normal diffuseBumpNormal"  [0 0 0] 
	"int diffuseDoubleSided"  [0] 
	"int diffuseBackUseDiffuseColor"  [1] 
	"color diffuseBackColor"  [0.18 0.18 0.18] 
	"float diffuseTransmitGain"  [0.0] 
	"color diffuseTransmitColor"  [0.18 0.18 0.18] 
	"int specularFresnelMode"  [0] 
	"color specularFaceColor"  [0 0 0] 
	"color specularEdgeColor"  [0 0 0] 
	"float specularFresnelShape"  [5.0] 
	"color specularIor"  [1.5 1.5 1.5] 
	"color specularExtinctionCoeff"  [0.0 0.0 0.0] 
	"float specularRoughness"  [0.2] 
	"int specularModelType"  [0] 
	"float specularAnisotropy"  [0.0] 
	"vector specularAnisotropyDirection"  [0 0 0] 
	"normal specularBumpNormal"  [0 0 0] 
	"int specularDoubleSided"  [0] 
	"int roughSpecularFresnelMode"  [0] 
	"color roughSpecularFaceColor"  [0 0 0] 
	"color roughSpecularEdgeColor"  [0 0 0] 
	"float roughSpecularFresnelShape"  [5.0] 
	"color roughSpecularIor"  [1.5 1.5 1.5] 
	"color roughSpecularExtinctionCoeff"  [0.0 0.0 0.0] 
	"float roughSpecularRoughness"  [0.6] 
	"int roughSpecularModelType"  [0] 
	"float roughSpecularAnisotropy"  [0.0] 
	"vector roughSpecularAnisotropyDirection"  [0 0 0] 
	"normal roughSpecularBumpNormal"  [0 0 0] 
	"int roughSpecularDoubleSided"  [0] 
	"int clearcoatFresnelMode"  [0] 
	"color clearcoatFaceColor"  [0 0 0] 
	"color clearcoatEdgeColor"  [0 0 0] 
	"float clearcoatFresnelShape"  [5.0] 
	"color clearcoatIor"  [1.5 1.5 1.5] 
	"color clearcoatExtinctionCoeff"  [0.0 0.0 0.0] 
	"float clearcoatRoughness"  [0.0] 
	"int clearcoatModelType"  [0] 
	"float clearcoatAnisotropy"  [0.0] 
	"vector clearcoatAnisotropyDirection"  [0 0 0] 
	"normal clearcoatBumpNormal"  [0 0 0] 
	"float clearcoatThickness"  [0] 
	"color clearcoatAbsorptionTint"  [0 0 0] 
	"int clearcoatDoubleSided"  [0] 
	"float specularEnergyCompensation"  [0.0] 
	"float clearcoatEnergyCompensation"  [0.0] 
	"float iridescenceFaceGain"  [0] 
	"float iridescenceEdgeGain"  [0] 
	"float iridescenceFresnelShape"  [5.0] 
	"int iridescenceMode"  [0] 
	"color iridescencePrimaryColor"  [1 0 0] 
	"color iridescenceSecondaryColor"  [0 0 1] 
	"float iridescenceRoughness"  [0.2] 
	"float iridescenceCurve"  [1] 
	"float iridescenceScale"  [1] 
	"int iridescenceFlip"  [0] 
	"float iridescenceThickness"  [800] 
	"int iridescenceDoubleSided"  [0] 
	"float fuzzGain"  [0.0] 
	"color fuzzColor"  [1 1 1] 
	"float fuzzConeAngle"  [8] 
	"normal fuzzBumpNormal"  [0 0 0] 
	"int fuzzDoubleSided"  [0] 
	"int subsurfaceType"  [0] 
	"float subsurfaceGain"  [0.0] 
	"color subsurfaceColor"  [0.830 0.791 0.753] 
	"float subsurfaceDmfp"  [10] 
	"color subsurfaceDmfpColor"  [0.851 0.557 0.395] 
	"float shortSubsurfaceGain"  [0.0] 
	"color shortSubsurfaceColor"  [0.9 0.9 0.9] 
	"float shortSubsurfaceDmfp"  [5] 
	"float longSubsurfaceGain"  [0.0] 
	"color longSubsurfaceColor"  [0.8 0.0 0.0] 
	"float longSubsurfaceDmfp"  [20] 
	"float subsurfaceDirectionality"  [0.0] 
	"float subsurfaceBleed"  [0.0] 
	"float subsurfaceDiffuseBlend"  [0.0] 
	"int subsurfaceResolveSelfIntersections"  [0] 
	"float subsurfaceIor"  [1.4] 
	"color subsurfacePostTint"  [1.0 1.0 1.0] 
	"float subsurfaceDiffuseSwitch"  [1.0] 
	"int subsurfaceDoubleSided"  [0] 
	"float subsurfaceTransmitGain"  [0.0] 
	"float singlescatterGain"  [0.0] 
	"color singlescatterColor"  [0.830 0.791 0.753] 
	"float singlescatterMfp"  [10] 
	"color singlescatterMfpColor"  [0.851 0.557 0.395] 
	"float singlescatterDirectionality"  [0] 
	"float singlescatterIor"  [1.3] 
	"float singlescatterBlur"  [0.0] 
	"float singlescatterDirectGain"  [0.0] 
	"color singlescatterDirectGainTint"  [1.0 1.0 1.0] 
	"int singlescatterDoubleSided"  [0] 
	"color irradianceTint"  [1.0 1.0 1.0] 
	"float irradianceRoughness"  [0.0] 
	"float unitLength"  [0.1] 
	"float refractionGain"  [0.0] 
	"float reflectionGain"  [0.0] 
	"color refractionColor"  [1 1 1] 
	"float glassRoughness"  [0.1] 
	"float glassIor"  [1.5] 
	"int mwWalkable"  [0] 
	"float mwIor"  [-1.0] 
	"int thinGlass"  [0] 
	"int ignoreFresnel"  [0] 
	"int ignoreAccumOpacity"  [0] 
	"float glowGain"  [0.0] 
	"color glowColor"  [1 1 1] 
	"normal bumpNormal"  [0 0 0] 
	"color shadowColor"  [0.0 0.0 0.0] 
	"int shadowMode"  [0] 
	"float presence"  [1] 
	"int presenceCached"  [1] 
	"int mwStartable"  [0] 
	"float roughnessMollificationClamp"  [32] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Bxdf('PxrLayerSurface','id',
{
	'float inputMaterial' : ['No Value'], 
	'int utilityPattern' : [0], 
	'float diffuseGain' : [1.0], 
	'color diffuseColor' : [0.18,0.18,0.18], 
	'float diffuseRoughness' : [0.0], 
	'float diffuseExponent' : [1.0], 
	'normal diffuseBumpNormal' : [0,0,0], 
	'int diffuseDoubleSided' : [0], 
	'int diffuseBackUseDiffuseColor' : [1], 
	'color diffuseBackColor' : [0.18,0.18,0.18], 
	'float diffuseTransmitGain' : [0.0], 
	'color diffuseTransmitColor' : [0.18,0.18,0.18], 
	'int specularFresnelMode' : [0], 
	'color specularFaceColor' : [0,0,0], 
	'color specularEdgeColor' : [0,0,0], 
	'float specularFresnelShape' : [5.0], 
	'color specularIor' : [1.5,1.5,1.5], 
	'color specularExtinctionCoeff' : [0.0,0.0,0.0], 
	'float specularRoughness' : [0.2], 
	'int specularModelType' : [0], 
	'float specularAnisotropy' : [0.0], 
	'vector specularAnisotropyDirection' : [0,0,0], 
	'normal specularBumpNormal' : [0,0,0], 
	'int specularDoubleSided' : [0], 
	'int roughSpecularFresnelMode' : [0], 
	'color roughSpecularFaceColor' : [0,0,0], 
	'color roughSpecularEdgeColor' : [0,0,0], 
	'float roughSpecularFresnelShape' : [5.0], 
	'color roughSpecularIor' : [1.5,1.5,1.5], 
	'color roughSpecularExtinctionCoeff' : [0.0,0.0,0.0], 
	'float roughSpecularRoughness' : [0.6], 
	'int roughSpecularModelType' : [0], 
	'float roughSpecularAnisotropy' : [0.0], 
	'vector roughSpecularAnisotropyDirection' : [0,0,0], 
	'normal roughSpecularBumpNormal' : [0,0,0], 
	'int roughSpecularDoubleSided' : [0], 
	'int clearcoatFresnelMode' : [0], 
	'color clearcoatFaceColor' : [0,0,0], 
	'color clearcoatEdgeColor' : [0,0,0], 
	'float clearcoatFresnelShape' : [5.0], 
	'color clearcoatIor' : [1.5,1.5,1.5], 
	'color clearcoatExtinctionCoeff' : [0.0,0.0,0.0], 
	'float clearcoatRoughness' : [0.0], 
	'int clearcoatModelType' : [0], 
	'float clearcoatAnisotropy' : [0.0], 
	'vector clearcoatAnisotropyDirection' : [0,0,0], 
	'normal clearcoatBumpNormal' : [0,0,0], 
	'float clearcoatThickness' : [0], 
	'color clearcoatAbsorptionTint' : [0,0,0], 
	'int clearcoatDoubleSided' : [0], 
	'float specularEnergyCompensation' : [0.0], 
	'float clearcoatEnergyCompensation' : [0.0], 
	'float iridescenceFaceGain' : [0], 
	'float iridescenceEdgeGain' : [0], 
	'float iridescenceFresnelShape' : [5.0], 
	'int iridescenceMode' : [0], 
	'color iridescencePrimaryColor' : [1,0,0], 
	'color iridescenceSecondaryColor' : [0,0,1], 
	'float iridescenceRoughness' : [0.2], 
	'float iridescenceCurve' : [1], 
	'float iridescenceScale' : [1], 
	'int iridescenceFlip' : [0], 
	'float iridescenceThickness' : [800], 
	'int iridescenceDoubleSided' : [0], 
	'float fuzzGain' : [0.0], 
	'color fuzzColor' : [1,1,1], 
	'float fuzzConeAngle' : [8], 
	'normal fuzzBumpNormal' : [0,0,0], 
	'int fuzzDoubleSided' : [0], 
	'int subsurfaceType' : [0], 
	'float subsurfaceGain' : [0.0], 
	'color subsurfaceColor' : [0.830,0.791,0.753], 
	'float subsurfaceDmfp' : [10], 
	'color subsurfaceDmfpColor' : [0.851,0.557,0.395], 
	'float shortSubsurfaceGain' : [0.0], 
	'color shortSubsurfaceColor' : [0.9,0.9,0.9], 
	'float shortSubsurfaceDmfp' : [5], 
	'float longSubsurfaceGain' : [0.0], 
	'color longSubsurfaceColor' : [0.8,0.0,0.0], 
	'float longSubsurfaceDmfp' : [20], 
	'float subsurfaceDirectionality' : [0.0], 
	'float subsurfaceBleed' : [0.0], 
	'float subsurfaceDiffuseBlend' : [0.0], 
	'int subsurfaceResolveSelfIntersections' : [0], 
	'float subsurfaceIor' : [1.4], 
	'color subsurfacePostTint' : [1.0,1.0,1.0], 
	'float subsurfaceDiffuseSwitch' : [1.0], 
	'int subsurfaceDoubleSided' : [0], 
	'float subsurfaceTransmitGain' : [0.0], 
	'float singlescatterGain' : [0.0], 
	'color singlescatterColor' : [0.830,0.791,0.753], 
	'float singlescatterMfp' : [10], 
	'color singlescatterMfpColor' : [0.851,0.557,0.395], 
	'float singlescatterDirectionality' : [0], 
	'float singlescatterIor' : [1.3], 
	'float singlescatterBlur' : [0.0], 
	'float singlescatterDirectGain' : [0.0], 
	'color singlescatterDirectGainTint' : [1.0,1.0,1.0], 
	'int singlescatterDoubleSided' : [0], 
	'color irradianceTint' : [1.0,1.0,1.0], 
	'float irradianceRoughness' : [0.0], 
	'float unitLength' : [0.1], 
	'float refractionGain' : [0.0], 
	'float reflectionGain' : [0.0], 
	'color refractionColor' : [1,1,1], 
	'float glassRoughness' : [0.1], 
	'float glassIor' : [1.5], 
	'int mwWalkable' : [0], 
	'float mwIor' : [-1.0], 
	'int thinGlass' : [0], 
	'int ignoreFresnel' : [0], 
	'int ignoreAccumOpacity' : [0], 
	'float glowGain' : [0.0], 
	'color glowColor' : [1,1,1], 
	'normal bumpNormal' : [0,0,0], 
	'color shadowColor' : [0.0,0.0,0.0], 
	'int shadowMode' : [0], 
	'float presence' : [1], 
	'int presenceCached' : [1], 
	'int mwStartable' : [0], 
	'float roughnessMollificationClamp' : [32], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrVolume 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Bxdf "PxrVolume" "id" 
	"color diffuseColor"  [1. 1. 1.] 
	"color emitColor"  [0. 0. 0.] 
	"int multiScatter"  [0] 
	"vector velocity"  [0 0 0] 
	"float velocityMultiplier"  [1.] 
	"string densityFloatPrimVar"  [''] 
	"float densityFloat"  [1.] 
	"string densityColorPrimVar"  [''] 
	"color densityColor"  [1. 1. 1.] 
	"float maxDensity"  [-1.] 
	"float anisotropy"  [0.] 
	"float anisotropy2"  [0.] 
	"float blendFactor"  [0.] 
	"float equiangularWeight"  [0.5] 
	"int minSamples"  [4] 
	"int maxSamples"  [4] 
	"float stepSize"  [0.1] 
	"int multiScatterOpt"  [0] 
	"float extinctionMultiplier"  [1.] 
	"float contributionMultiplier"  [1.] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Bxdf('PxrVolume','id',
{
	'color diffuseColor' : [1.,1.,1.], 
	'color emitColor' : [0.,0.,0.], 
	'int multiScatter' : [0], 
	'vector velocity' : [0,0,0], 
	'float velocityMultiplier' : [1.], 
	'string densityFloatPrimVar' : [''], 
	'float densityFloat' : [1.], 
	'string densityColorPrimVar' : [''], 
	'color densityColor' : [1.,1.,1.], 
	'float maxDensity' : [-1.], 
	'float anisotropy' : [0.], 
	'float anisotropy2' : [0.], 
	'float blendFactor' : [0.], 
	'float equiangularWeight' : [0.5], 
	'int minSamples' : [4], 
	'int maxSamples' : [4], 
	'float stepSize' : [0.1], 
	'int multiScatterOpt' : [0], 
	'float extinctionMultiplier' : [1.], 
	'float contributionMultiplier' : [1.], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrMarschnerHair 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Bxdf "PxrMarschnerHair" "id" 
	"int diffuseModelType"  [0] 
	"float diffuseGain"  [0.0] 
	"color diffuseColor"  [0.18 0.18 0.18] 
	"float specularGainR"  [1.0] 
	"float specularGainTRT"  [1.0] 
	"float specularGainTT"  [1.0] 
	"float specularGainGLINTS"  [1.0] 
	"color specularColorR"  [1.0 1.0 1.0] 
	"color specularColorTRT"  [0.4 0.4 0.4] 
	"color specularColorTT"  [0.4 0.4 0.4] 
	"float specularConeAngleR"  [8.0] 
	"float specularConeAngleTRT"  [8.0] 
	"float specularConeAngleTT"  [8.0] 
	"float specularOffset"  [-3] 
	"float specularIor"  [1.55] 
	"float specularMixFresnel"  [1.0] 
	"float specularGlintWidth"  [10.0] 
	"float specularEccentricity"  [1.0] 
	"float glowGain"  [0.0] 
	"color glowColor"  [1 1 1] 
	"float specularEnergyCompensation"  [0.0] 
	"normal eccentricityDirection"  [0 0 0] 
	"color shadowColor"  [0.0 0.0 0.0] 
	"float presence"  [1.0] 
	"int inputAOV"  [0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Bxdf('PxrMarschnerHair','id',
{
	'int diffuseModelType' : [0], 
	'float diffuseGain' : [0.0], 
	'color diffuseColor' : [0.18,0.18,0.18], 
	'float specularGainR' : [1.0], 
	'float specularGainTRT' : [1.0], 
	'float specularGainTT' : [1.0], 
	'float specularGainGLINTS' : [1.0], 
	'color specularColorR' : [1.0,1.0,1.0], 
	'color specularColorTRT' : [0.4,0.4,0.4], 
	'color specularColorTT' : [0.4,0.4,0.4], 
	'float specularConeAngleR' : [8.0], 
	'float specularConeAngleTRT' : [8.0], 
	'float specularConeAngleTT' : [8.0], 
	'float specularOffset' : [-3], 
	'float specularIor' : [1.55], 
	'float specularMixFresnel' : [1.0], 
	'float specularGlintWidth' : [10.0], 
	'float specularEccentricity' : [1.0], 
	'float glowGain' : [0.0], 
	'color glowColor' : [1,1,1], 
	'float specularEnergyCompensation' : [0.0], 
	'normal eccentricityDirection' : [0,0,0], 
	'color shadowColor' : [0.0,0.0,0.0], 
	'float presence' : [1.0], 
	'int inputAOV' : [0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrSurface 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Bxdf "PxrSurface" "id" 
	"float inputMaterial"  ['No Value'] 
	"int utilityPattern"  [0] 
	"float diffuseGain"  [1.0] 
	"color diffuseColor"  [0.18 0.18 0.18] 
	"float diffuseRoughness"  [0.0] 
	"int specularFresnelMode"  [0] 
	"color specularFaceColor"  [0 0 0] 
	"color specularEdgeColor"  [0 0 0] 
	"float specularFresnelShape"  [5.0] 
	"color specularIor"  [1.5 1.5 1.5] 
	"color specularExtinctionCoeff"  [0.0 0.0 0.0] 
	"float specularRoughness"  [0.2] 
	"int roughSpecularFresnelMode"  [0] 
	"color roughSpecularFaceColor"  [0 0 0] 
	"color roughSpecularEdgeColor"  [0 0 0] 
	"float roughSpecularFresnelShape"  [5.0] 
	"color roughSpecularIor"  [1.5 1.5 1.5] 
	"color roughSpecularExtinctionCoeff"  [0.0 0.0 0.0] 
	"float roughSpecularRoughness"  [0.6] 
	"int clearcoatFresnelMode"  [0] 
	"color clearcoatFaceColor"  [0 0 0] 
	"color clearcoatEdgeColor"  [0 0 0] 
	"float clearcoatFresnelShape"  [5.0] 
	"color clearcoatIor"  [1.5 1.5 1.5] 
	"color clearcoatExtinctionCoeff"  [0.0 0.0 0.0] 
	"float clearcoatThickness"  [0.0] 
	"color clearcoatAbsorptionTint"  [0.0 0.0 0.0] 
	"float clearcoatRoughness"  [0.0] 
	"float specularEnergyCompensation"  [0.0] 
	"float clearcoatEnergyCompensation"  [0.0] 
	"float iridescenceFaceGain"  [0] 
	"float iridescenceEdgeGain"  [0] 
	"float iridescenceFresnelShape"  [5.0] 
	"int iridescenceMode"  [0] 
	"color iridescencePrimaryColor"  [1 0 0] 
	"color iridescenceSecondaryColor"  [0 0 1] 
	"float iridescenceRoughness"  [0.2] 
	"float fuzzGain"  [0.0] 
	"color fuzzColor"  [1 1 1] 
	"float fuzzConeAngle"  [8] 
	"int subsurfaceType"  [0] 
	"float subsurfaceGain"  [0.0] 
	"color subsurfaceColor"  [0.830 0.791 0.753] 
	"float subsurfaceDmfp"  [10] 
	"color subsurfaceDmfpColor"  [0.851 0.557 0.395] 
	"float shortSubsurfaceGain"  [0.0] 
	"color shortSubsurfaceColor"  [0.9 0.9 0.9] 
	"float shortSubsurfaceDmfp"  [5] 
	"float longSubsurfaceGain"  [0.0] 
	"color longSubsurfaceColor"  [0.8 0.0 0.0] 
	"float longSubsurfaceDmfp"  [20] 
	"float subsurfaceDirectionality"  [0.0] 
	"float subsurfaceBleed"  [0.0] 
	"float subsurfaceDiffuseBlend"  [0.0] 
	"int subsurfaceResolveSelfIntersections"  [0] 
	"float subsurfaceIor"  [1.4] 
	"float singlescatterGain"  [0.0] 
	"color singlescatterColor"  [0.830 0.791 0.753] 
	"float singlescatterMfp"  [10] 
	"color singlescatterMfpColor"  [0.851 0.557 0.395] 
	"color irradianceTint"  [1.0 1.0 1.0] 
	"float irradianceRoughness"  [0.0] 
	"float unitLength"  [0.1] 
	"float refractionGain"  [0.0] 
	"float reflectionGain"  [0.0] 
	"color refractionColor"  [1 1 1] 
	"float glassRoughness"  [0.1] 
	"float glowGain"  [0.0] 
	"color glowColor"  [1 1 1] 
	"normal bumpNormal"  [0 0 0] 
	"color shadowColor"  [0.0 0.0 0.0] 
	"int shadowMode"  [0] 
	"float presence"  [1] 
	"int presenceCached"  [1] 
	"int mwStartable"  [0] 
	"float roughnessMollificationClamp"  [32] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Bxdf('PxrSurface','id',
{
	'float inputMaterial' : ['No Value'], 
	'int utilityPattern' : [0], 
	'float diffuseGain' : [1.0], 
	'color diffuseColor' : [0.18,0.18,0.18], 
	'float diffuseRoughness' : [0.0], 
	'int specularFresnelMode' : [0], 
	'color specularFaceColor' : [0,0,0], 
	'color specularEdgeColor' : [0,0,0], 
	'float specularFresnelShape' : [5.0], 
	'color specularIor' : [1.5,1.5,1.5], 
	'color specularExtinctionCoeff' : [0.0,0.0,0.0], 
	'float specularRoughness' : [0.2], 
	'int roughSpecularFresnelMode' : [0], 
	'color roughSpecularFaceColor' : [0,0,0], 
	'color roughSpecularEdgeColor' : [0,0,0], 
	'float roughSpecularFresnelShape' : [5.0], 
	'color roughSpecularIor' : [1.5,1.5,1.5], 
	'color roughSpecularExtinctionCoeff' : [0.0,0.0,0.0], 
	'float roughSpecularRoughness' : [0.6], 
	'int clearcoatFresnelMode' : [0], 
	'color clearcoatFaceColor' : [0,0,0], 
	'color clearcoatEdgeColor' : [0,0,0], 
	'float clearcoatFresnelShape' : [5.0], 
	'color clearcoatIor' : [1.5,1.5,1.5], 
	'color clearcoatExtinctionCoeff' : [0.0,0.0,0.0], 
	'float clearcoatThickness' : [0.0], 
	'color clearcoatAbsorptionTint' : [0.0,0.0,0.0], 
	'float clearcoatRoughness' : [0.0], 
	'float specularEnergyCompensation' : [0.0], 
	'float clearcoatEnergyCompensation' : [0.0], 
	'float iridescenceFaceGain' : [0], 
	'float iridescenceEdgeGain' : [0], 
	'float iridescenceFresnelShape' : [5.0], 
	'int iridescenceMode' : [0], 
	'color iridescencePrimaryColor' : [1,0,0], 
	'color iridescenceSecondaryColor' : [0,0,1], 
	'float iridescenceRoughness' : [0.2], 
	'float fuzzGain' : [0.0], 
	'color fuzzColor' : [1,1,1], 
	'float fuzzConeAngle' : [8], 
	'int subsurfaceType' : [0], 
	'float subsurfaceGain' : [0.0], 
	'color subsurfaceColor' : [0.830,0.791,0.753], 
	'float subsurfaceDmfp' : [10], 
	'color subsurfaceDmfpColor' : [0.851,0.557,0.395], 
	'float shortSubsurfaceGain' : [0.0], 
	'color shortSubsurfaceColor' : [0.9,0.9,0.9], 
	'float shortSubsurfaceDmfp' : [5], 
	'float longSubsurfaceGain' : [0.0], 
	'color longSubsurfaceColor' : [0.8,0.0,0.0], 
	'float longSubsurfaceDmfp' : [20], 
	'float subsurfaceDirectionality' : [0.0], 
	'float subsurfaceBleed' : [0.0], 
	'float subsurfaceDiffuseBlend' : [0.0], 
	'int subsurfaceResolveSelfIntersections' : [0], 
	'float subsurfaceIor' : [1.4], 
	'float singlescatterGain' : [0.0], 
	'color singlescatterColor' : [0.830,0.791,0.753], 
	'float singlescatterMfp' : [10], 
	'color singlescatterMfpColor' : [0.851,0.557,0.395], 
	'color irradianceTint' : [1.0,1.0,1.0], 
	'float irradianceRoughness' : [0.0], 
	'float unitLength' : [0.1], 
	'float refractionGain' : [0.0], 
	'float reflectionGain' : [0.0], 
	'color refractionColor' : [1,1,1], 
	'float glassRoughness' : [0.1], 
	'float glowGain' : [0.0], 
	'color glowColor' : [1,1,1], 
	'normal bumpNormal' : [0,0,0], 
	'color shadowColor' : [0.0,0.0,0.0], 
	'int shadowMode' : [0], 
	'float presence' : [1], 
	'int presenceCached' : [1], 
	'int mwStartable' : [0], 
	'float roughnessMollificationClamp' : [32], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrDisney 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Bxdf "PxrDisney" "id" 
	"color baseColor"  [.2 .5 .8] 
	"color emitColor"  [0 0 0] 
	"float subsurface"  [0] 
	"color subsurfaceColor"  [0 0 0] 
	"float metallic"  [0] 
	"float specular"  [.5] 
	"float specularTint"  [0] 
	"float roughness"  [.25] 
	"float anisotropic"  [0] 
	"float sheen"  [0] 
	"float sheenTint"  [.5] 
	"float clearcoat"  [0] 
	"float clearcoatGloss"  [1] 
	"normal bumpNormal"  [0 0 0] 
	"float presence"  [1] 
	"int inputAOV"  [0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Bxdf('PxrDisney','id',
{
	'color baseColor' : [.2,.5,.8], 
	'color emitColor' : [0,0,0], 
	'float subsurface' : [0], 
	'color subsurfaceColor' : [0,0,0], 
	'float metallic' : [0], 
	'float specular' : [.5], 
	'float specularTint' : [0], 
	'float roughness' : [.25], 
	'float anisotropic' : [0], 
	'float sheen' : [0], 
	'float sheenTint' : [.5], 
	'float clearcoat' : [0], 
	'float clearcoatGloss' : [1], 
	'normal bumpNormal' : [0,0,0], 
	'float presence' : [1], 
	'int inputAOV' : [0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Pattern
## Plugin PxrVary 
This node creates controlled random variations.
        The variation source can be attribute or primvar based.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrVary" "id" 
	"color inputRGB"  [0.5 0.5 0.5] 
	"int varySource"  [0] 
	"string varName"  [''] 
	"int varType"  [0] 
	"float hue"  [0] 
	"float saturation"  [0] 
	"float luminance"  [0] 
	"float gamma"  [0] 
	"float probability"  [1] 
	"int hueMode"  [0] 
	"int saturationMode"  [0] 
	"int luminanceMode"  [0] 
	"int gammaMode"  [0] 
	"int verbosity"  [0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrVary','id',
{
	'color inputRGB' : [0.5,0.5,0.5], 
	'int varySource' : [0], 
	'string varName' : [''], 
	'int varType' : [0], 
	'float hue' : [0], 
	'float saturation' : [0], 
	'float luminance' : [0], 
	'float gamma' : [0], 
	'float probability' : [1], 
	'int hueMode' : [0], 
	'int saturationMode' : [0], 
	'int luminanceMode' : [0], 
	'int gammaMode' : [0], 
	'int verbosity' : [0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrBumpManifold2D 
PxrBumpManifold2D defines 2D mapping coordinates for the PxrBump node.
        PxrBump is able to efficiently compute bumped normals when using a simple
        texture. If you want to scale or rotate the texture, you have to use this
        node instead of PxrManifold2D. PxrBumpManifold2D provides additional data
        (surface derivatives) necessary to compute bumped normals.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
struct pxrbumpmanifold2d  result
float  resultS
float  resultT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrBumpManifold2D" "id" 
	"float angle"  [0] 
	"float scaleS"  [1] 
	"float scaleT"  [1] 
	"float offsetS"  [0] 
	"float offsetT"  [0] 
	"int invertT"  [1] 
	"string primvarS"  [''] 
	"string primvarT"  [''] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrBumpManifold2D','id',
{
	'float angle' : [0], 
	'float scaleS' : [1], 
	'float scaleT' : [1], 
	'float offsetS' : [0], 
	'float offsetT' : [0], 
	'int invertT' : [1], 
	'string primvarS' : [''], 
	'string primvarT' : [''], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrRandomTextureManifold 
Encapsulates 2D parameterization for
        pattern generators. Allows transformations and selection
        of arbitrary variables bound to primitives. Uses a simple
        struct to represent bundled dataflow of outputs.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
struct manifold  result
float  resultS
float  resultT
struct pxrmanifoldmulti  resultMulti
color vector normal point  resultMask
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrRandomTextureManifold" "id" 
	"int numTextures"  [1] 
	"int textureOrder"  [1] 
	"int randomSource"  [0] 
	"float randomExtraSeed"  [0] 
	"int randomOrientation"  [0] 
	"int randomFlipS"  [0] 
	"int randomFlipT"  [0] 
	"int randomOffsetS"  [0] 
	"int randomOffsetT"  [0] 
	"float angle"  [0] 
	"float globalScale"  [1] 
	"float scaleS"  [1] 
	"float scaleT"  [1] 
	"float offsetS"  [0] 
	"float offsetT"  [0] 
	"int invertT"  [1] 
	"string primvarS"  [''] 
	"string primvarT"  [''] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrRandomTextureManifold','id',
{
	'int numTextures' : [1], 
	'int textureOrder' : [1], 
	'int randomSource' : [0], 
	'float randomExtraSeed' : [0], 
	'int randomOrientation' : [0], 
	'int randomFlipS' : [0], 
	'int randomFlipT' : [0], 
	'int randomOffsetS' : [0], 
	'int randomOffsetT' : [0], 
	'float angle' : [0], 
	'float globalScale' : [1], 
	'float scaleS' : [1], 
	'float scaleT' : [1], 
	'float offsetS' : [0], 
	'float offsetT' : [0], 
	'int invertT' : [1], 
	'string primvarS' : [''], 
	'string primvarT' : [''], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrThreshold 
Thresholds an input color pattern to create a black and white mask.
        The falloff will define a gradual transition from black to
        white. The output is always between 0 and 1.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrThreshold" "id" 
	"color inputRGB"  [0. 0. 0.] 
	"int channel"  [3] 
	"float threshold"  [0.5] 
	"float transitionWidth"  [0.05] 
	"int transitionProfile"  [1] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrThreshold','id',
{
	'color inputRGB' : [0.,0.,0.], 
	'int channel' : [3], 
	'float threshold' : [0.5], 
	'float transitionWidth' : [0.05], 
	'int transitionProfile' : [1], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrHairColor 
This node creates beautiful natural human hair color, by modeling
        melanin concentration in hair fibers.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultDiff
color vector normal point  resultTT
color vector normal point  resultTRT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrHairColor" "id" 
	"int mode"  [0] 
	"int colorSpace"  [0] 
	"float melanin"  [0.2] 
	"color color"  [0.0 0.3 0.1] 
	"float randomMelanin"  [0.05] 
	"color randomColor"  [0.05 0.05 0.05] 
	"float darkenRoots"  [0.0] 
	"float darkenSlope"  [1.0] 
	"float darkenEndPosition"  [0.5] 
	"float strayDensity"  [0.1] 
	"float strayMelanin"  [0.05] 
	"color strayColor"  [0.05 0.05 0.05] 
	"float strayRandomMelanin"  [0.0] 
	"color strayRandomColor"  [0.0 0.0 0.0] 
	"color dye"  [1.0 1.0 1.0] 
	"float randomDyeHue"  [0.0] 
	"float randomDyeSaturation"  [0.0] 
	"string hairIndexPrimvar"  [''] 
	"float randPivot"  [0.5] 
	"float randSeed"  [0.0] 
	"int viewIndexRandom"  [0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrHairColor','id',
{
	'int mode' : [0], 
	'int colorSpace' : [0], 
	'float melanin' : [0.2], 
	'color color' : [0.0,0.3,0.1], 
	'float randomMelanin' : [0.05], 
	'color randomColor' : [0.05,0.05,0.05], 
	'float darkenRoots' : [0.0], 
	'float darkenSlope' : [1.0], 
	'float darkenEndPosition' : [0.5], 
	'float strayDensity' : [0.1], 
	'float strayMelanin' : [0.05], 
	'color strayColor' : [0.05,0.05,0.05], 
	'float strayRandomMelanin' : [0.0], 
	'color strayRandomColor' : [0.0,0.0,0.0], 
	'color dye' : [1.0,1.0,1.0], 
	'float randomDyeHue' : [0.0], 
	'float randomDyeSaturation' : [0.0], 
	'string hairIndexPrimvar' : [''], 
	'float randPivot' : [0.5], 
	'float randSeed' : [0.0], 
	'int viewIndexRandom' : [0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrDispTransform 
Transforms the displacement values.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
vector  resultXYZ
float  resultF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrDispTransform" "id" 
	"int dispType"  [1] 
	"float dispScalar"  [0.0] 
	"vector dispVector"  [0.0 0.0 0.0] 
	"int vectorSpace"  [3] 
	"float dispHeight"  [1.0] 
	"float dispDepth"  [1.0] 
	"int dispRemapMode"  [1] 
	"float dispCenter"  [0.5] 
	"string dispScaleSpace"  ['object'] 
	"int useDispDirection"  [0] 
	"vector dispDirection"  [0.0 0.0 0.0] 
	"string dispDirectionSpace"  ['object'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrDispTransform','id',
{
	'int dispType' : [1], 
	'float dispScalar' : [0.0], 
	'vector dispVector' : [0.0,0.0,0.0], 
	'int vectorSpace' : [3], 
	'float dispHeight' : [1.0], 
	'float dispDepth' : [1.0], 
	'int dispRemapMode' : [1], 
	'float dispCenter' : [0.5], 
	'string dispScaleSpace' : ['object'], 
	'int useDispDirection' : [0], 
	'vector dispDirection' : [0.0,0.0,0.0], 
	'string dispDirectionSpace' : ['object'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrBlend 
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
float  resultA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrBlend" "id" 
	"int operation"  [19] 
	"color topRGB"  [0. 0. 0.] 
	"float topA"  [1] 
	"color bottomRGB"  [0. 0. 0.] 
	"float bottomA"  [1] 
	"int clampOutput"  [1] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrBlend','id',
{
	'int operation' : [19], 
	'color topRGB' : [0.,0.,0.], 
	'float topA' : [1], 
	'color bottomRGB' : [0.,0.,0.], 
	'float bottomA' : [1], 
	'int clampOutput' : [1], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrMix 
This node mixes two colors according to the
        given mix percentage. A mix value of 0 results in Color 1.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrMix" "id" 
	"color color1"  [0. 0. 0.] 
	"color color2"  [1. 1. 1.] 
	"float mix"  [0.] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrMix','id',
{
	'color color1' : [0.,0.,0.], 
	'color color2' : [1.,1.,1.], 
	'float mix' : [0.], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrRemap 
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
float  resultA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrRemap" "id" 
	"color inputRGB"  [0. 0. 0.] 
	"float inputMin"  [0.0] 
	"float inputMax"  [1.0] 
	"int clampInput"  [1] 
	"color bias"  [.5 .5 .5] 
	"color gain"  [.5 .5 .5] 
	"float outputMin"  [0.0] 
	"float outputMax"  [1.0] 
	"int clampOutput"  [1] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrRemap','id',
{
	'color inputRGB' : [0.,0.,0.], 
	'float inputMin' : [0.0], 
	'float inputMax' : [1.0], 
	'int clampInput' : [1], 
	'color bias' : [.5,.5,.5], 
	'color gain' : [.5,.5,.5], 
	'float outputMin' : [0.0], 
	'float outputMax' : [1.0], 
	'int clampOutput' : [1], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrVoronoise 
A noise function based on Inigo Quilez function. The u and v
        parameters control the amount of jitter and the amount of noise.
        jitter=0,smoothness=0 produces a minimum distance non jittered grid of values.
        jitter=0,smoothness=1 gives a noise function.
        jitter=1,smoothness=0 produces a jittered, minimum distance Voronoi pattern.
        jitter=1,smoothness=1 produces a a combination of jittered Voronoi and noise
        also called "voronoise". Note, this version adds
        fractal octaves and turbulence.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
float  resultF
color  resultRGB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrVoronoise" "id" 
	"int surfacePosition"  [0] 
	"float frequency"  [1.0] 
	"int octaves"  [3] 
	"float gain"  [0.5] 
	"float lacunarity"  [2.0] 
	"float jitter"  [.0] 
	"float smoothness"  [1.0] 
	"int turbulent"  [0] 
	"struct manifold"  ['No Value'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrVoronoise','id',
{
	'int surfacePosition' : [0], 
	'float frequency' : [1.0], 
	'int octaves' : [3], 
	'float gain' : [0.5], 
	'float lacunarity' : [2.0], 
	'float jitter' : [.0], 
	'float smoothness' : [1.0], 
	'int turbulent' : [0], 
	'struct manifold' : ['No Value'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrMultiTexture 
Read a texture file.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
float  resultA
color vector normal point  resultMask
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrMultiTexture" "id" 
	"struct manifoldMulti"  [] 
	"string filename0"  [''] 
	"string filename1"  [''] 
	"string filename2"  [''] 
	"string filename3"  [''] 
	"string filename4"  [''] 
	"string filename5"  [''] 
	"string filename6"  [''] 
	"string filename7"  [''] 
	"string filename8"  [''] 
	"string filename9"  [''] 
	"int firstChannel"  [0] 
	"int invertT"  [1] 
	"int filter"  [1] 
	"float blur"  [0.] 
	"int lerp"  [1] 
	"color missingColor"  [1. 0. 1.] 
	"float missingAlpha"  [1.] 
	"int linearize"  [0] 
	"int randomSource"  [0] 
	"float randomSeed"  [0] 
	"float randomHue"  [0] 
	"float randomSaturation"  [0] 
	"float randomLuminance"  [0] 
	"float randomGamma"  [0] 
	"int hueMode"  [0] 
	"int saturationMode"  [0] 
	"int luminanceMode"  [0] 
	"int gammaMode"  [0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrMultiTexture','id',
{
	'struct manifoldMulti' : [], 
	'string filename0' : [''], 
	'string filename1' : [''], 
	'string filename2' : [''], 
	'string filename3' : [''], 
	'string filename4' : [''], 
	'string filename5' : [''], 
	'string filename6' : [''], 
	'string filename7' : [''], 
	'string filename8' : [''], 
	'string filename9' : [''], 
	'int firstChannel' : [0], 
	'int invertT' : [1], 
	'int filter' : [1], 
	'float blur' : [0.], 
	'int lerp' : [1], 
	'color missingColor' : [1.,0.,1.], 
	'float missingAlpha' : [1.], 
	'int linearize' : [0], 
	'int randomSource' : [0], 
	'float randomSeed' : [0], 
	'float randomHue' : [0], 
	'float randomSaturation' : [0], 
	'float randomLuminance' : [0], 
	'float randomGamma' : [0], 
	'int hueMode' : [0], 
	'int saturationMode' : [0], 
	'int luminanceMode' : [0], 
	'int gammaMode' : [0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrClamp 
Clamps the separate channels of a color between the specified min and
    max values. If an RGB channel value is less then min, it will be set to the
    min value, and if an RGB channel is greater than max, it will be set to the
    max value.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrClamp" "id" 
	"color inputRGB"  [0. 0. 0.] 
	"color min"  [0. 0. 0.] 
	"color max"  [1. 1. 1.] 
	"int modulus"  [0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrClamp','id',
{
	'color inputRGB' : [0.,0.,0.], 
	'color min' : [0.,0.,0.], 
	'color max' : [1.,1.,1.], 
	'int modulus' : [0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrExposure 
Adjust the exposure of the input color by the given stops.  Each positive
    stop will double the input's intensity.  Each negative stop will halve the
    input's intensity.  Often it is preferable to use Exposure instead of a
    straight multiplication (also called gain), as it is perceptually linear.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrExposure" "id" 
	"color inputRGB"  [0. 0. 0.] 
	"float stops"  [0.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrExposure','id',
{
	'color inputRGB' : [0.,0.,0.], 
	'float stops' : [0.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrRamp 
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrRamp" "id" 
	"int rampType"  [0] 
	"int tile"  [0] 
	"int useNewRamp"  [1] 
	"int reverse"  [0] 
	"float splineMap"  [0] 
	"int randomSource"  [0] 
	"float randomSeed"  [0] 
	"struct manifold"  ['No Value'] 
	"int colorRamp"  [4] 
	"float colorRamp_Knots"  [0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1] 
	"color colorRamp_Colors"  [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1] 
	"string colorRamp_Interpolation"  ['catmull-rom'] 
	"float positions"  [0] 
	"color colors"  [-1.0 -1.0 -1.0] 
	"int basis"  [4] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrRamp','id',
{
	'int rampType' : [0], 
	'int tile' : [0], 
	'int useNewRamp' : [1], 
	'int reverse' : [0], 
	'float splineMap' : [0], 
	'int randomSource' : [0], 
	'float randomSeed' : [0], 
	'struct manifold' : ['No Value'], 
	'int colorRamp' : [4], 
	'float colorRamp_Knots' : [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
	'color colorRamp_Colors' : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
	'string colorRamp_Interpolation' : ['catmull-rom'], 
	'float positions' : [0], 
	'color colors' : [-1.0,-1.0,-1.0], 
	'int basis' : [4], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrToFloat3 
Produces a triple output from a single float input.
        The single float **input** is copied to each channel.
        If float **inputR**, **inputG**, **inputB** are connected,
        then those will be convert to a color instead
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrToFloat3" "id" 
	"float input"  [0.] 
	"float inputR"  [0.] 
	"float inputG"  [0.] 
	"float inputB"  [0.] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrToFloat3','id',
{
	'float input' : [0.], 
	'float inputR' : [0.], 
	'float inputG' : [0.], 
	'float inputB' : [0.], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrBlackBody 
Produces a color that represents the radiation emitted by
        an ideal black body heated at the given temperature in the visible
        spectrum. This allows you to easily create plausible light colors based
        on standard temperature measurement. See the Color temperature article
        for more infomration.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrBlackBody" "id" 
	"float temperature"  [6500.0] 
	"float physicalIntensity"  [0.0] 
	"float exposure"  [0.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrBlackBody','id',
{
	'float temperature' : [6500.0], 
	'float physicalIntensity' : [0.0], 
	'float exposure' : [0.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrLayeredTexture 
Read a texture file and composite it with another PxrLayeredTexture.
        This is the most efficient way to layer textures.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
float  resultA
struct pxrtexoverlay  resultOverlay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrLayeredTexture" "id" 
	"int mute"  [0] 
	"struct textureOverlay"  ['No Value'] 
	"int doNotOptimize"  [0] 
	"float maskValue"  [1] 
	"string maskTexture"  [''] 
	"int maskChannel"  [0] 
	"int maskAtlasStyle"  [0] 
	"float missingMask"  [0.0] 
	"string filename"  [''] 
	"int firstChannel"  [0] 
	"int atlasStyle"  [0] 
	"int invertT"  [1] 
	"struct manifold"  [] 
	"int linearize"  [0] 
	"color colorTint"  [1. 1. 1.] 
	"color colorOffset"  [0. 0. 0.] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrLayeredTexture','id',
{
	'int mute' : [0], 
	'struct textureOverlay' : ['No Value'], 
	'int doNotOptimize' : [0], 
	'float maskValue' : [1], 
	'string maskTexture' : [''], 
	'int maskChannel' : [0], 
	'int maskAtlasStyle' : [0], 
	'float missingMask' : [0.0], 
	'string filename' : [''], 
	'int firstChannel' : [0], 
	'int atlasStyle' : [0], 
	'int invertT' : [1], 
	'struct manifold' : [], 
	'int linearize' : [0], 
	'color colorTint' : [1.,1.,1.], 
	'color colorOffset' : [0.,0.,0.], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrSwitch 
This node selects one of the connected inputs based on the index value.  Index values are
        expected to be integers, but the node accepts float values for ease of use.

        The first input is selected for index values between -0.5 and 0.5, the second input for
        index values between 0.5 and 1.5, and so on...

        If the index value is larger than the actual number of connected inputs, the node will cycle
        through the connected inputs.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrSwitch" "id" 
	"float index"  [0.] 
	"color inputsRGB"  [0.0 0.0 0.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrSwitch','id',
{
	'float index' : [0.], 
	'color inputsRGB' : [0.0,0.0,0.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrProjector 
Encapsulates 2D parameterization for
        pattern generators. Allows transformations and selection
        of arbitrary variables bound to primitives. Uses a simple
        struct to represent bundled dataflow of outputs.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
struct manifold  result
float  resultS
float  resultT
float  resultMask
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrProjector" "id" 
	"int projection"  [0] 
	"string coordsys"  [''] 
	"int use"  [0] 
	"int frontOnly"  [1] 
	"float frontFalloff"  [0] 
	"int traceOcclusion"  [0] 
	"float traceMaxDistance"  [10000] 
	"string traceSet"  [''] 
	"int resolutionX"  [2048] 
	"int resolutionY"  [1556] 
	"float focalLength"  [50] 
	"float apertureX"  [0.980] 
	"float apertureY"  [0.735] 
	"float nearClipPlane"  [0.01] 
	"float farClipPlane"  [10000] 
	"int filmFit"  [0] 
	"int clampTo"  [1] 
	"float angle"  [0] 
	"float scaleS"  [1] 
	"float scaleT"  [1] 
	"float offsetS"  [0] 
	"float offsetT"  [0] 
	"int invertT"  [1] 
	"int verbose"  [0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrProjector','id',
{
	'int projection' : [0], 
	'string coordsys' : [''], 
	'int use' : [0], 
	'int frontOnly' : [1], 
	'float frontFalloff' : [0], 
	'int traceOcclusion' : [0], 
	'float traceMaxDistance' : [10000], 
	'string traceSet' : [''], 
	'int resolutionX' : [2048], 
	'int resolutionY' : [1556], 
	'float focalLength' : [50], 
	'float apertureX' : [0.980], 
	'float apertureY' : [0.735], 
	'float nearClipPlane' : [0.01], 
	'float farClipPlane' : [10000], 
	'int filmFit' : [0], 
	'int clampTo' : [1], 
	'float angle' : [0], 
	'float scaleS' : [1], 
	'float scaleT' : [1], 
	'float offsetS' : [0], 
	'float offsetT' : [0], 
	'int invertT' : [1], 
	'int verbose' : [0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrChecker 
A checker pattern
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrChecker" "id" 
	"color colorA"  [1.0 1.0 1.0] 
	"color colorB"  [0.0 0.0 0.0] 
	"int dimensions"  [2] 
	"struct manifold"  [] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrChecker','id',
{
	'color colorA' : [1.0,1.0,1.0], 
	'color colorB' : [0.0,0.0,0.0], 
	'int dimensions' : [2], 
	'struct manifold' : [], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrTexture 
Read a texture file.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
float  resultA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrTexture" "id" 
	"string filename"  [''] 
	"int firstChannel"  [0] 
	"int atlasStyle"  [0] 
	"int invertT"  [1] 
	"int filter"  [1] 
	"float blur"  [0.] 
	"int lerp"  [1] 
	"color missingColor"  [1. 0. 1.] 
	"float missingAlpha"  [1.] 
	"int linearize"  [0] 
	"struct manifold"  [] 
	"int mipBias"  [0] 
	"float maxResolution"  [0] 
	"int optimizeIndirect"  [1] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrTexture','id',
{
	'string filename' : [''], 
	'int firstChannel' : [0], 
	'int atlasStyle' : [0], 
	'int invertT' : [1], 
	'int filter' : [1], 
	'float blur' : [0.], 
	'int lerp' : [1], 
	'color missingColor' : [1.,0.,1.], 
	'float missingAlpha' : [1.], 
	'int linearize' : [0], 
	'struct manifold' : [], 
	'int mipBias' : [0], 
	'float maxResolution' : [0], 
	'int optimizeIndirect' : [1], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrInvert 
Inverts one or more components of the incoming color. The input color
        can be in the in the RGB, HSL, or HSV color models. Note: The output is
        a RGB color clamped to the [0 0 0] to [1 1 1] range.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrInvert" "id" 
	"color inputRGB"  [0. 0. 0.] 
	"int colorModel"  [0] 
	"int invertChannel0"  [1] 
	"int invertChannel1"  [1] 
	"int invertChannel2"  [1] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrInvert','id',
{
	'color inputRGB' : [0.,0.,0.], 
	'int colorModel' : [0], 
	'int invertChannel0' : [1], 
	'int invertChannel1' : [1], 
	'int invertChannel2' : [1], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrToFloat 
Produces a single float output from a triple float input. The index specifies which of the 3 floats to pull from the triple.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
float  resultF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrToFloat" "id" 
	"color input"  [0. 0. 0.] 
	"int mode"  [0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrToFloat','id',
{
	'color input' : [0.,0.,0.], 
	'int mode' : [0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrRoundCube 
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultMask
struct pxrmanifoldmulti  resultMulti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrRoundCube" "id" 
	"int numberOfTextures"  [1] 
	"float frequency"  [1] 
	"float transitionWidth"  [0.5] 
	"int use"  [0] 
	"string pref"  [''] 
	"string nref"  [''] 
	"string coordsys"  ['object'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrRoundCube','id',
{
	'int numberOfTextures' : [1], 
	'float frequency' : [1], 
	'float transitionWidth' : [0.5], 
	'int use' : [0], 
	'string pref' : [''], 
	'string nref' : [''], 
	'string coordsys' : ['object'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrThinFilm 
Computes a thin-film interference effect on six spectral bands.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrThinFilm" "id" 
	"color inputRGB"  [1. 1. 1.] 
	"float eta"  [1.5] 
	"float spread"  [0.01] 
	"float thickness"  [1896.0] 
	"float thicknessScale"  [1.0] 
	"int frontOnly"  [0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrThinFilm','id',
{
	'color inputRGB' : [1.,1.,1.], 
	'float eta' : [1.5], 
	'float spread' : [0.01], 
	'float thickness' : [1896.0], 
	'float thicknessScale' : [1.0], 
	'int frontOnly' : [0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrBakePointCloud 
Bake 3d Point Clouds
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrBakePointCloud" "id" 
	"color inputRGB"  [0. 0. 0.] 
	"float inputF"  [0.] 
	"string filename"  [''] 
	"int bakeMode"  [1] 
	"string display"  ['pointcloud'] 
	"float density"  [10.0] 
	"string coordsys"  ['object'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrBakePointCloud','id',
{
	'color inputRGB' : [0.,0.,0.], 
	'float inputF' : [0.], 
	'string filename' : [''], 
	'int bakeMode' : [1], 
	'string display' : ['pointcloud'], 
	'float density' : [10.0], 
	'string coordsys' : ['object'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrMatteID 
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
int  resultAOV
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrMatteID" "id" 
	"int inputAOV"  ['No Value'] 
	"int enable"  [1] 
	"color matteTexture0"  [0 0 0] 
	"color matteTexture1"  [0 0 0] 
	"color matteTexture2"  [0 0 0] 
	"color matteTexture3"  [0 0 0] 
	"color matteTexture4"  [0 0 0] 
	"color matteTexture5"  [0 0 0] 
	"color matteTexture6"  [0 0 0] 
	"color matteTexture7"  [0 0 0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrMatteID','id',
{
	'int inputAOV' : ['No Value'], 
	'int enable' : [1], 
	'color matteTexture0' : [0,0,0], 
	'color matteTexture1' : [0,0,0], 
	'color matteTexture2' : [0,0,0], 
	'color matteTexture3' : [0,0,0], 
	'color matteTexture4' : [0,0,0], 
	'color matteTexture5' : [0,0,0], 
	'color matteTexture6' : [0,0,0], 
	'color matteTexture7' : [0,0,0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrDispVectorLayer 
Layer vector displacement textures/values.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
vector  resultXYZ
float  resultX
float  resultY
float  resultZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrDispVectorLayer" "id" 
	"float overallAmount"  [1.0] 
	"int baseLayerEnabled"  [1] 
	"float baseLayerAmount"  [1.0] 
	"vector baseLayerDispVector"  [0.0 0.0 0.0] 
	"int layer1Enabled"  [1] 
	"float layer1Amount"  [1.0] 
	"vector layer1DispVector"  [0.0 0.0 0.0] 
	"float layer1Mask"  [1.0] 
	"int layer1Comp"  [1] 
	"int layer2Enabled"  [0] 
	"float layer2Amount"  [1.0] 
	"vector layer2DispVector"  [0.0 0.0 0.0] 
	"float layer2Mask"  [1.0] 
	"int layer2Comp"  [1] 
	"int layer3Enabled"  [0] 
	"float layer3Amount"  [1.0] 
	"vector layer3DispVector"  [0.0 0.0 0.0] 
	"float layer3Mask"  [1.0] 
	"int layer3Comp"  [1] 
	"int layer4Enabled"  [0] 
	"float layer4Amount"  [1.0] 
	"vector layer4DispVector"  [0.0 0.0 0.0] 
	"float layer4Mask"  [1.0] 
	"int layer4Comp"  [1] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrDispVectorLayer','id',
{
	'float overallAmount' : [1.0], 
	'int baseLayerEnabled' : [1], 
	'float baseLayerAmount' : [1.0], 
	'vector baseLayerDispVector' : [0.0,0.0,0.0], 
	'int layer1Enabled' : [1], 
	'float layer1Amount' : [1.0], 
	'vector layer1DispVector' : [0.0,0.0,0.0], 
	'float layer1Mask' : [1.0], 
	'int layer1Comp' : [1], 
	'int layer2Enabled' : [0], 
	'float layer2Amount' : [1.0], 
	'vector layer2DispVector' : [0.0,0.0,0.0], 
	'float layer2Mask' : [1.0], 
	'int layer2Comp' : [1], 
	'int layer3Enabled' : [0], 
	'float layer3Amount' : [1.0], 
	'vector layer3DispVector' : [0.0,0.0,0.0], 
	'float layer3Mask' : [1.0], 
	'int layer3Comp' : [1], 
	'int layer4Enabled' : [0], 
	'float layer4Amount' : [1.0], 
	'vector layer4DispVector' : [0.0,0.0,0.0], 
	'float layer4Mask' : [1.0], 
	'int layer4Comp' : [1], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrBakeTexture 
Bake 2d Textures
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrBakeTexture" "id" 
	"color inputRGB"  [0. 0. 0.] 
	"float inputF"  [0.] 
	"string filename"  [''] 
	"int atlasStyle"  [0] 
	"int bakeMode"  [1] 
	"int renderMode"  [0] 
	"string display"  ['texture'] 
	"string displayFormat"  ['openexr'] 
	"string displayType"  ['half'] 
	"string displayCompression"  ['zip'] 
	"int resolutionX"  [512] 
	"int resolutionY"  [512] 
	"string primVar"  ['st'] 
	"string primVar2"  [''] 
	"string activeUdim"  [''] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrBakeTexture','id',
{
	'color inputRGB' : [0.,0.,0.], 
	'float inputF' : [0.], 
	'string filename' : [''], 
	'int atlasStyle' : [0], 
	'int bakeMode' : [1], 
	'int renderMode' : [0], 
	'string display' : ['texture'], 
	'string displayFormat' : ['openexr'], 
	'string displayType' : ['half'], 
	'string displayCompression' : ['zip'], 
	'int resolutionX' : [512], 
	'int resolutionY' : [512], 
	'string primVar' : ['st'], 
	'string primVar2' : [''], 
	'string activeUdim' : [''], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrLayeredBlend 
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
float  resultA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrLayeredBlend" "id" 
	"color backgroundRGB"  [0. 0. 0.] 
	"float backgroundA"  [1] 
	"int clampOutput"  [1] 
	"int enable_0"  [0] 
	"int operation_0"  [19] 
	"color RGB_0"  [0. 0. 0.] 
	"float A_0"  [1] 
	"int enable_1"  [0] 
	"int operation_1"  [19] 
	"color RGB_1"  [0. 0. 0.] 
	"float A_1"  [1] 
	"int enable_2"  [0] 
	"int operation_2"  [19] 
	"color RGB_2"  [0. 0. 0.] 
	"float A_2"  [1] 
	"int enable_3"  [0] 
	"int operation_3"  [19] 
	"color RGB_3"  [0. 0. 0.] 
	"float A_3"  [1] 
	"int enable_4"  [0] 
	"int operation_4"  [19] 
	"color RGB_4"  [0. 0. 0.] 
	"float A_4"  [1] 
	"int enable_5"  [0] 
	"int operation_5"  [19] 
	"color RGB_5"  [0. 0. 0.] 
	"float A_5"  [1] 
	"int enable_6"  [0] 
	"int operation_6"  [19] 
	"color RGB_6"  [0. 0. 0.] 
	"float A_6"  [1] 
	"int enable_7"  [0] 
	"int operation_7"  [19] 
	"color RGB_7"  [0. 0. 0.] 
	"float A_7"  [1] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrLayeredBlend','id',
{
	'color backgroundRGB' : [0.,0.,0.], 
	'float backgroundA' : [1], 
	'int clampOutput' : [1], 
	'int enable_0' : [0], 
	'int operation_0' : [19], 
	'color RGB_0' : [0.,0.,0.], 
	'float A_0' : [1], 
	'int enable_1' : [0], 
	'int operation_1' : [19], 
	'color RGB_1' : [0.,0.,0.], 
	'float A_1' : [1], 
	'int enable_2' : [0], 
	'int operation_2' : [19], 
	'color RGB_2' : [0.,0.,0.], 
	'float A_2' : [1], 
	'int enable_3' : [0], 
	'int operation_3' : [19], 
	'color RGB_3' : [0.,0.,0.], 
	'float A_3' : [1], 
	'int enable_4' : [0], 
	'int operation_4' : [19], 
	'color RGB_4' : [0.,0.,0.], 
	'float A_4' : [1], 
	'int enable_5' : [0], 
	'int operation_5' : [19], 
	'color RGB_5' : [0.,0.,0.], 
	'float A_5' : [1], 
	'int enable_6' : [0], 
	'int operation_6' : [19], 
	'color RGB_6' : [0.,0.,0.], 
	'float A_6' : [1], 
	'int enable_7' : [0], 
	'int operation_7' : [19], 
	'color RGB_7' : [0.,0.,0.], 
	'float A_7' : [1], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrFractal 
A fractal noise function.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
float  resultF
color  resultRGB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrFractal" "id" 
	"int surfacePosition"  [0] 
	"int layers"  [6] 
	"float frequency"  [1.0] 
	"float lacunarity"  [2.0] 
	"float dimension"  [1.0] 
	"float erosion"  [0.0] 
	"float variation"  [0.0] 
	"int turbulent"  [0] 
	"struct manifold"  ['No Value'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrFractal','id',
{
	'int surfacePosition' : [0], 
	'int layers' : [6], 
	'float frequency' : [1.0], 
	'float lacunarity' : [2.0], 
	'float dimension' : [1.0], 
	'float erosion' : [0.0], 
	'float variation' : [0.0], 
	'int turbulent' : [0], 
	'struct manifold' : ['No Value'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrPtexture 
Read a ptex file.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
float  resultA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrPtexture" "id" 
	"string filename"  [''] 
	"int firstChannel"  [0] 
	"int faceIndexOffset"  [0] 
	"int invertWindingOrder"  [0] 
	"int filter"  [1] 
	"float blur"  [0.] 
	"int lerp"  [1] 
	"color missingColor"  [1. 0. 1.] 
	"float missingAlpha"  [1.] 
	"int linearize"  [0] 
	"struct manifold"  [] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrPtexture','id',
{
	'string filename' : [''], 
	'int firstChannel' : [0], 
	'int faceIndexOffset' : [0], 
	'int invertWindingOrder' : [0], 
	'int filter' : [1], 
	'float blur' : [0.], 
	'int lerp' : [1], 
	'color missingColor' : [1.,0.,1.], 
	'float missingAlpha' : [1.], 
	'int linearize' : [0], 
	'struct manifold' : [], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrFlakes 
Pattern plugin to generate a flake-like normal perturbation.
        Returns a normal.
        Connecting this to the Bump Normal parameter of PxrLMMetal can
        create metallic fleck paint.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
normal  resultN
float  resultA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrFlakes" "id" 
	"normal inputNormal"  [0 0 0] 
	"float flakeAmount"  [.5] 
	"float flakeFreq"  [57.30] 
	"float density"  [1.0] 
	"float size"  [1.0] 
	"int octaves"  [1] 
	"float jitter"  [0.75] 
	"int validateNormals"  [0] 
	"struct manifold"  ['No Value'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrFlakes','id',
{
	'normal inputNormal' : [0,0,0], 
	'float flakeAmount' : [.5], 
	'float flakeFreq' : [57.30], 
	'float density' : [1.0], 
	'float size' : [1.0], 
	'int octaves' : [1], 
	'float jitter' : [0.75], 
	'int validateNormals' : [0], 
	'struct manifold' : ['No Value'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrAdjustNormal 
Utility to adjust the normals.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
normal  resultN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrAdjustNormal" "id" 
	"normal inputNormal"  [0 0 0] 
	"float adjustAmount"  [1.0] 
	"float surfaceNormalMix"  [0.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrAdjustNormal','id',
{
	'normal inputNormal' : [0,0,0], 
	'float adjustAmount' : [1.0], 
	'float surfaceNormalMix' : [0.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrGamma 
Adjust the exposure of the input color by the given gamma.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrGamma" "id" 
	"color inputRGB"  [0. 0. 0.] 
	"float gamma"  [1.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrGamma','id',
{
	'color inputRGB' : [0.,0.,0.], 
	'float gamma' : [1.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrColorCorrect 
PxrColorCorrect combines a number of classic remapping and color correction
    methods.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrColorCorrect" "id" 
	"color inputRGB"  [0. 0. 0.] 
	"float inputMask"  [1.0] 
	"int invertMask"  [0] 
	"float mixMask"  [1.0] 
	"vector inputMin"  [0. 0. 0.] 
	"vector inputMax"  [1. 1. 1.] 
	"vector gamma"  [1. 1. 1.] 
	"vector contrast"  [0.0 0.0 0.0] 
	"vector contrastPivot"  [0.5 0.5 0.5] 
	"color rgbGain"  [1. 1. 1.] 
	"vector hsv"  [0.0 1.0 1.0] 
	"float exposure"  [0] 
	"vector outputMin"  [0. 0. 0.] 
	"vector outputMax"  [1. 1. 1.] 
	"int clampOutput"  [0] 
	"vector clampMin"  [0. 0. 0.] 
	"vector clampMax"  [1. 1. 1.] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrColorCorrect','id',
{
	'color inputRGB' : [0.,0.,0.], 
	'float inputMask' : [1.0], 
	'int invertMask' : [0], 
	'float mixMask' : [1.0], 
	'vector inputMin' : [0.,0.,0.], 
	'vector inputMax' : [1.,1.,1.], 
	'vector gamma' : [1.,1.,1.], 
	'vector contrast' : [0.0,0.0,0.0], 
	'vector contrastPivot' : [0.5,0.5,0.5], 
	'color rgbGain' : [1.,1.,1.], 
	'vector hsv' : [0.0,1.0,1.0], 
	'float exposure' : [0], 
	'vector outputMin' : [0.,0.,0.], 
	'vector outputMax' : [1.,1.,1.], 
	'int clampOutput' : [0], 
	'vector clampMin' : [0.,0.,0.], 
	'vector clampMax' : [1.,1.,1.], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrVariable 
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
float  resultRadius
string  resultString
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrVariable" "id" 
	"string variable"  [''] 
	"string name"  [''] 
	"string type"  ['float'] 
	"string coordsys"  ['object'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrVariable','id',
{
	'string variable' : [''], 
	'string name' : [''], 
	'string type' : ['float'], 
	'string coordsys' : ['object'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrManifold3D 
Encapsulates 3D parameterization for
        pattern generators. Allows selection of Pref and
        specification of a coordinate system to transform to.
        Uses a simple struct to represent bundled dataflow of
        outputs.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
struct manifold  result
float  resultX
float  resultY
float  resultZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrManifold3D" "id" 
	"float scale"  [1] 
	"int use"  [0] 
	"string pref"  [''] 
	"string coordsys"  ['object'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrManifold3D','id',
{
	'float scale' : [1], 
	'int use' : [0], 
	'string pref' : [''], 
	'string coordsys' : ['object'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrTileManifold 
Encapsulates 2D parameterization for
        pattern generators. Allows transformations and selection
        of arbitrary variables bound to primitives. Uses a simple
        struct to represent bundled dataflow of outputs.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
struct manifold  result
float  resultS
float  resultT
struct pxrmanifoldmulti  resultMulti
color vector normal point  resultMask
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrTileManifold" "id" 
	"int numTextures"  [1] 
	"int textureOrder"  [1] 
	"float gridOffset"  [0.5] 
	"float groutWidth"  [0.0] 
	"float tileBevelWidth"  [0.0] 
	"int swapTileST"  [0] 
	"float angle"  [0] 
	"float globalScale"  [1] 
	"float scaleS"  [1] 
	"float scaleT"  [1] 
	"float offsetS"  [0] 
	"float offsetT"  [0] 
	"int invertT"  [1] 
	"string primvarS"  [''] 
	"string primvarT"  [''] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrTileManifold','id',
{
	'int numTextures' : [1], 
	'int textureOrder' : [1], 
	'float gridOffset' : [0.5], 
	'float groutWidth' : [0.0], 
	'float tileBevelWidth' : [0.0], 
	'int swapTileST' : [0], 
	'float angle' : [0], 
	'float globalScale' : [1], 
	'float scaleS' : [1], 
	'float scaleT' : [1], 
	'float offsetS' : [0], 
	'float offsetT' : [0], 
	'int invertT' : [1], 
	'string primvarS' : [''], 
	'string primvarT' : [''], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrWorley 
An implementation of a noise function by Steven Worley.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
float  resultF
color  resultRGB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrWorley" "id" 
	"int surfacePosition"  [0] 
	"float frequency"  [4.0] 
	"int distancemetric"  [0] 
	"float jitter"  [0.75] 
	"float c1"  [0.8] 
	"float c2"  [-0.2] 
	"float minkowskiExponent"  [4.0] 
	"int shape"  [0] 
	"int clamp"  [1] 
	"int invert"  [0] 
	"float randomScale"  [0.] 
	"float randomScaleCenter"  [0.] 
	"struct manifold"  ['No Value'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrWorley','id',
{
	'int surfacePosition' : [0], 
	'float frequency' : [4.0], 
	'int distancemetric' : [0], 
	'float jitter' : [0.75], 
	'float c1' : [0.8], 
	'float c2' : [-0.2], 
	'float minkowskiExponent' : [4.0], 
	'int shape' : [0], 
	'int clamp' : [1], 
	'int invert' : [0], 
	'float randomScale' : [0.], 
	'float randomScaleCenter' : [0.], 
	'struct manifold' : ['No Value'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrProjectionLayer 
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
float  resultA
int  outNumChannels
color  outChannelsRGB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrProjectionLayer" "id" 
	"string filename"  [''] 
	"int firstChannel"  [0] 
	"int filter"  [1] 
	"float blur"  [0.] 
	"int lerp"  [1] 
	"color missingColor"  [1. 0. 1.] 
	"float missingAlpha"  [1.] 
	"int linearize"  [0] 
	"int premultiply"  [0] 
	"float mask"  [1.0] 
	"string channelsFilenames"  [''] 
	"int channelsLinearize"  [0] 
	"color channelsMissingColor"  [0. 0. 0.] 
	"color channelsInBlack"  [0. 0. 0.] 
	"color channelsInGamma"  [1. 1. 1.] 
	"color channelsInWhite"  [1. 1. 1.] 
	"color channelsOutBlack"  [0. 0. 0.] 
	"color channelsOutWhite"  [1. 1. 1.] 
	"struct manifold"  [] 
	"int mipBias"  [0] 
	"float maxResolution"  [0] 
	"int optimizeIndirect"  [1] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrProjectionLayer','id',
{
	'string filename' : [''], 
	'int firstChannel' : [0], 
	'int filter' : [1], 
	'float blur' : [0.], 
	'int lerp' : [1], 
	'color missingColor' : [1.,0.,1.], 
	'float missingAlpha' : [1.], 
	'int linearize' : [0], 
	'int premultiply' : [0], 
	'float mask' : [1.0], 
	'string channelsFilenames' : [''], 
	'int channelsLinearize' : [0], 
	'color channelsMissingColor' : [0.,0.,0.], 
	'color channelsInBlack' : [0.,0.,0.], 
	'color channelsInGamma' : [1.,1.,1.], 
	'color channelsInWhite' : [1.,1.,1.], 
	'color channelsOutBlack' : [0.,0.,0.], 
	'color channelsOutWhite' : [1.,1.,1.], 
	'struct manifold' : [], 
	'int mipBias' : [0], 
	'float maxResolution' : [0], 
	'int optimizeIndirect' : [1], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrBump 
Calculate a bumped normal based on a floating point scalar displacement map.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
normal  resultN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrBump" "id" 
	"float scale"  [1.] 
	"int disable"  [0] 
	"float inputBump"  [0.] 
	"string filename"  [''] 
	"int firstChannel"  [0] 
	"int atlasStyle"  [0] 
	"int invertT"  [1] 
	"float blur"  [0.] 
	"int lerp"  [1] 
	"struct manifold"  [] 
	"normal inputN"  [1. 0. 0.] 
	"int reverse"  [0] 
	"float adjustAmount"  [1.0] 
	"float surfaceNormalMix"  [0.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrBump','id',
{
	'float scale' : [1.], 
	'int disable' : [0], 
	'float inputBump' : [0.], 
	'string filename' : [''], 
	'int firstChannel' : [0], 
	'int atlasStyle' : [0], 
	'int invertT' : [1], 
	'float blur' : [0.], 
	'int lerp' : [1], 
	'struct manifold' : [], 
	'normal inputN' : [1.,0.,0.], 
	'int reverse' : [0], 
	'float adjustAmount' : [1.0], 
	'float surfaceNormalMix' : [0.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrAttribute 
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrAttribute" "id" 
	"string varname"  [''] 
	"string type"  ['float'] 
	"int defaultInt"  [0] 
	"float defaultFloat"  [0.0] 
	"vector defaultFloat3"  [0.0 0.0 0.0] 
	"color defaultColor"  [0.0 0.0 0.0] 
	"int verbosity"  [0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrAttribute','id',
{
	'string varname' : [''], 
	'string type' : ['float'], 
	'int defaultInt' : [0], 
	'float defaultFloat' : [0.0], 
	'vector defaultFloat3' : [0.0,0.0,0.0], 
	'color defaultColor' : [0.0,0.0,0.0], 
	'int verbosity' : [0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrFacingRatio 
Computes the facing ratio of the geometry : a simple dot product between
        the camera vector and the surface normal.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
float  resultF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrFacingRatio" "id" 
	"int use"  [0] 
	"vector direction"  [0.0 1.0 0.0] 
	"string coordSys"  [''] 
	"int faceForward"  [1] 
	"int clamp"  [0] 
	"int invert"  [0] 
	"int mode"  [0] 
	"float gamma"  [1.0] 
	"float ior"  [1.5] 
	"normal bumpNormal"  [0 0 0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrFacingRatio','id',
{
	'int use' : [0], 
	'vector direction' : [0.0,1.0,0.0], 
	'string coordSys' : [''], 
	'int faceForward' : [1], 
	'int clamp' : [0], 
	'int invert' : [0], 
	'int mode' : [0], 
	'float gamma' : [1.0], 
	'float ior' : [1.5], 
	'normal bumpNormal' : [0,0,0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrProjectionStack 
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
float  resultA
color vector normal point  channelOut0
color vector normal point  channelOut1
color vector normal point  channelOut2
color vector normal point  channelOut3
color vector normal point  channelOut4
color vector normal point  channelOut5
color vector normal point  channelOut6
color vector normal point  channelOut7
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrProjectionStack" "id" 
	"int layersMode"  [1] 
	"color layersRGB"  [0.5 0.5 0.5] 
	"float layersA"  [1] 
	"int layersNumChannels"  [0] 
	"color layersChannelsRGB"  [0 0 0] 
	"string channelsAovNames"  [''] 
	"int outputChanIdx"  [-1] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrProjectionStack','id',
{
	'int layersMode' : [1], 
	'color layersRGB' : [0.5,0.5,0.5], 
	'float layersA' : [1], 
	'int layersNumChannels' : [0], 
	'color layersChannelsRGB' : [0,0,0], 
	'string channelsAovNames' : [''], 
	'int outputChanIdx' : [-1], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrHSL 
Adjust the hue, saturation and value of a given input color. Note the output is in RGB color space.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrHSL" "id" 
	"color inputRGB"  [0. 0. 0.] 
	"float hue"  [0.0] 
	"float saturation"  [1.0] 
	"float luminance"  [1.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrHSL','id',
{
	'color inputRGB' : [0.,0.,0.], 
	'float hue' : [0.0], 
	'float saturation' : [1.0], 
	'float luminance' : [1.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrTee 
This utility pattern takes either an input parameter and passes it
    through unchanged to its result.  As a side effect, it will send the
    values out into an AOV when shading a camera-visible primary ray.  Note
    that either inputF and resultF should be connected, or inputRGB and
    resultRGB, but not both, and the type of the AOV should also match.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrTee" "id" 
	"color inputRGB"  [0.0 0.0 0.0] 
	"float inputF"  [0.0] 
	"string aov"  [''] 
	"int verbosity"  [0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrTee','id',
{
	'color inputRGB' : [0.0,0.0,0.0], 
	'float inputF' : [0.0], 
	'string aov' : [''], 
	'int verbosity' : [0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin aaOceanPrmanShader 
A Tessendorf Ocean generator. Amaan Akram. www.amaanakram.com
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  outDisplacementRGB
float  outEigenvalueFloat
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "aaOceanPrmanShader" "id" 
	"int resolution"  [3] 
	"float oceanScale"  [100.0] 
	"int seed"  [1] 
	"float currentTime"  [0.0] 
	"float repeatTime"  [1000.0] 
	"float fade"  [0.0] 
	"float chopAmount"  [1.0] 
	"float velocity"  [10.0] 
	"float waveSpeed"  [1.0] 
	"float cutoff"  [0.0] 
	"float waveHeight"  [1.0] 
	"float windDir"  [45.0] 
	"float damp"  [0.985] 
	"int windAlign"  [1] 
	"int raw"  [0] 
	"int invertFoam"  [0] 
	"float gamma"  [1.0] 
	"float brightness"  [1.0] 
	"int normalize"  [0] 
	"float fMin"  [-5.0] 
	"float fMax"  [5.0] 
	"int writeFile"  [0] 
	"string outputFolder"  [''] 
	"string postfix"  [''] 
	"int currentFrame"  [1] 
	"int invertT"  [1] 
	"struct manifold"  [] 
	"float oceanDepth"  [1000.0] 
	"float surfaceTension"  [0.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('aaOceanPrmanShader','id',
{
	'int resolution' : [3], 
	'float oceanScale' : [100.0], 
	'int seed' : [1], 
	'float currentTime' : [0.0], 
	'float repeatTime' : [1000.0], 
	'float fade' : [0.0], 
	'float chopAmount' : [1.0], 
	'float velocity' : [10.0], 
	'float waveSpeed' : [1.0], 
	'float cutoff' : [0.0], 
	'float waveHeight' : [1.0], 
	'float windDir' : [45.0], 
	'float damp' : [0.985], 
	'int windAlign' : [1], 
	'int raw' : [0], 
	'int invertFoam' : [0], 
	'float gamma' : [1.0], 
	'float brightness' : [1.0], 
	'int normalize' : [0], 
	'float fMin' : [-5.0], 
	'float fMax' : [5.0], 
	'int writeFile' : [0], 
	'string outputFolder' : [''], 
	'string postfix' : [''], 
	'int currentFrame' : [1], 
	'int invertT' : [1], 
	'struct manifold' : [], 
	'float oceanDepth' : [1000.0], 
	'float surfaceTension' : [0.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrNormalMap 
Calculate a bumped normal based on a normal map file or color input.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
normal  resultN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrNormalMap" "id" 
	"float bumpScale"  [1.0] 
	"color inputRGB"  [0 0 0] 
	"string filename"  [''] 
	"normal bumpOverlay"  [0 0 0] 
	"int invertBump"  [0] 
	"int orientation"  [2] 
	"int flipX"  [0] 
	"int flipY"  [0] 
	"int firstChannel"  [0] 
	"int atlasStyle"  [0] 
	"int invertT"  [1] 
	"float blur"  [0.] 
	"int lerp"  [1] 
	"int filter"  [1] 
	"struct manifold"  [] 
	"int reverse"  [0] 
	"float adjustAmount"  [0.0] 
	"float surfaceNormalMix"  [0.0] 
	"int disable"  [0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrNormalMap','id',
{
	'float bumpScale' : [1.0], 
	'color inputRGB' : [0,0,0], 
	'string filename' : [''], 
	'normal bumpOverlay' : [0,0,0], 
	'int invertBump' : [0], 
	'int orientation' : [2], 
	'int flipX' : [0], 
	'int flipY' : [0], 
	'int firstChannel' : [0], 
	'int atlasStyle' : [0], 
	'int invertT' : [1], 
	'float blur' : [0.], 
	'int lerp' : [1], 
	'int filter' : [1], 
	'struct manifold' : [], 
	'int reverse' : [0], 
	'float adjustAmount' : [0.0], 
	'float surfaceNormalMix' : [0.0], 
	'int disable' : [0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrDispScalarLayer 
Layer scalar (float) displacement textures/values.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
float  resultF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrDispScalarLayer" "id" 
	"float overallAmount"  [1.0] 
	"int baseLayerEnabled"  [1] 
	"float baseLayerAmount"  [1.0] 
	"float baseLayerDispScalar"  [0.0] 
	"int layer1Enabled"  [1] 
	"float layer1Amount"  [1.0] 
	"float layer1DispScalar"  [0.0] 
	"float layer1Mask"  [1.0] 
	"int layer1Comp"  [1] 
	"int layer2Enabled"  [0] 
	"float layer2Amount"  [1.0] 
	"float layer2DispScalar"  [0.0] 
	"float layer2Mask"  [1.0] 
	"int layer2Comp"  [1] 
	"int layer3Enabled"  [0] 
	"float layer3Amount"  [1.0] 
	"float layer3DispScalar"  [0.0] 
	"float layer3Mask"  [1.0] 
	"int layer3Comp"  [1] 
	"int layer4Enabled"  [0] 
	"float layer4Amount"  [1.0] 
	"float layer4DispScalar"  [0.0] 
	"float layer4Mask"  [1.0] 
	"int layer4Comp"  [1] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrDispScalarLayer','id',
{
	'float overallAmount' : [1.0], 
	'int baseLayerEnabled' : [1], 
	'float baseLayerAmount' : [1.0], 
	'float baseLayerDispScalar' : [0.0], 
	'int layer1Enabled' : [1], 
	'float layer1Amount' : [1.0], 
	'float layer1DispScalar' : [0.0], 
	'float layer1Mask' : [1.0], 
	'int layer1Comp' : [1], 
	'int layer2Enabled' : [0], 
	'float layer2Amount' : [1.0], 
	'float layer2DispScalar' : [0.0], 
	'float layer2Mask' : [1.0], 
	'int layer2Comp' : [1], 
	'int layer3Enabled' : [0], 
	'float layer3Amount' : [1.0], 
	'float layer3DispScalar' : [0.0], 
	'float layer3Mask' : [1.0], 
	'int layer3Comp' : [1], 
	'int layer4Enabled' : [0], 
	'float layer4Amount' : [1.0], 
	'float layer4DispScalar' : [0.0], 
	'float layer4Mask' : [1.0], 
	'int layer4Comp' : [1], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrPrimvar 
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color  resultRGB
float  resultF
vector normal point  resultP
float  width
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrPrimvar" "id" 
	"string varname"  [''] 
	"string type"  ['float'] 
	"string coordsys"  ['object'] 
	"float defaultFloat"  [0.0] 
	"vector defaultFloat3"  [0.0 0.0 0.0] 
	"int transformDefaultValues"  [1] 
	"color defaultColor"  [0.0 0.0 0.0] 
	"int verbosity"  [0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrPrimvar','id',
{
	'string varname' : [''], 
	'string type' : ['float'], 
	'string coordsys' : ['object'], 
	'float defaultFloat' : [0.0], 
	'vector defaultFloat3' : [0.0,0.0,0.0], 
	'int transformDefaultValues' : [1], 
	'color defaultColor' : [0.0,0.0,0.0], 
	'int verbosity' : [0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrDirt 
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrDirt" "id" 
	"color occluded"  [1.0 1.0 1.0] 
	"color unoccluded"  [0.0 0.0 0.0] 
	"int numSamples"  [4] 
	"int distribution"  [1] 
	"float cosineSpread"  [1.0] 
	"float falloff"  [0.0] 
	"float maxDistance"  [0.0] 
	"int direction"  [0] 
	"vector biasDirection"  [0.0 0.0 0.0] 
	"string biasDirectionCoordsys"  ['object'] 
	"string traceSet"  [''] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrDirt','id',
{
	'color occluded' : [1.0,1.0,1.0], 
	'color unoccluded' : [0.0,0.0,0.0], 
	'int numSamples' : [4], 
	'int distribution' : [1], 
	'float cosineSpread' : [1.0], 
	'float falloff' : [0.0], 
	'float maxDistance' : [0.0], 
	'int direction' : [0], 
	'vector biasDirection' : [0.0,0.0,0.0], 
	'string biasDirectionCoordsys' : ['object'], 
	'string traceSet' : [''], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrTangentField 
Defines a tangent field typically used to control anisotropic direction.
        InputRotation takes a single grayscale channel where black = 0 degrees
        and white = 360 degrees.
        InputVector takes a 2 channels map where the red channels is x and green
        is y. The blue channel is ignored.
        The vector method often gives better results by minimizing texture
        filtering artifacts. If such artifacts are too visible, use the "nearest"
        texture filter. The "nearest" filter disables entirely mip-mapping, so you
        should only us it with a low resolutiion map to avoid slowing down the
        renderer and consuming too much texture memory.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
vector normal point  resultXYZ
float  resultX
float  resultY
float  resultZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrTangentField" "id" 
	"float inputRotation"  [0.0] 
	"color inputVector"  [0.0 0.0 0.0] 
	"float rotationOffset"  [0.0] 
	"float rotationRange"  [1.0] 
	"int centeredVectors"  [1] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrTangentField','id',
{
	'float inputRotation' : [0.0], 
	'color inputVector' : [0.0,0.0,0.0], 
	'float rotationOffset' : [0.0], 
	'float rotationRange' : [1.0], 
	'int centeredVectors' : [1], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrCross 
Computes the cross product of two vectors and optionally
        normalizes the resulting vector.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
vector normal point  resultXYZ
float  resultX
float  resultY
float  resultZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrCross" "id" 
	"vector vector1"  [0. 0. 0.] 
	"vector vector2"  [0. 0. 0.] 
	"int normalizeResult"  [1] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrCross','id',
{
	'vector vector1' : [0.,0.,0.], 
	'vector vector2' : [0.,0.,0.], 
	'int normalizeResult' : [1], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrDot 
Computes the dot product of two vectors.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
float  result
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrDot" "id" 
	"vector vector1"  [0. 0. 0.] 
	"vector vector2"  [0. 0. 0.] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrDot','id',
{
	'vector vector1' : [0.,0.,0.], 
	'vector vector2' : [0.,0.,0.], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrSeExpr 
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
color vector normal point  resultRGB
float  resultR
float  resultG
float  resultB
float  resultF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrSeExpr" "id" 
	"color colorInput1"  [0.0 0.0 0.0] 
	"color colorInput2"  [0.0 0.0 0.0] 
	"color colorInput3"  [0.0 0.0 0.0] 
	"color colorInput4"  [0.0 0.0 0.0] 
	"float floatInput1"  [0.0] 
	"float floatInput2"  [0.0] 
	"float floatInput3"  [0.0] 
	"float floatInput4"  [0.0] 
	"string expression"  [''] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrSeExpr','id',
{
	'color colorInput1' : [0.0,0.0,0.0], 
	'color colorInput2' : [0.0,0.0,0.0], 
	'color colorInput3' : [0.0,0.0,0.0], 
	'color colorInput4' : [0.0,0.0,0.0], 
	'float floatInput1' : [0.0], 
	'float floatInput2' : [0.0], 
	'float floatInput3' : [0.0], 
	'float floatInput4' : [0.0], 
	'string expression' : [''], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrManifold2D 
Encapsulates 2D parameterization for
        pattern generators. Allows transformations and selection
        of arbitrary variables bound to primitives. Uses a simple
        struct to represent bundled dataflow of outputs.
#### Outputs  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
struct manifold  result
float  resultS
float  resultT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Pattern "PxrManifold2D" "id" 
	"float angle"  [0] 
	"float scaleS"  [1] 
	"float scaleT"  [1] 
	"float offsetS"  [0] 
	"float offsetT"  [0] 
	"int invertS"  [0] 
	"int invertT"  [1] 
	"string primvarS"  [''] 
	"string primvarT"  [''] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Pattern('PxrManifold2D','id',
{
	'float angle' : [0], 
	'float scaleS' : [1], 
	'float scaleT' : [1], 
	'float offsetS' : [0], 
	'float offsetT' : [0], 
	'int invertS' : [0], 
	'int invertT' : [1], 
	'string primvarS' : [''], 
	'string primvarT' : [''], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Light
## Plugin PxrPortalLight 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Light "PxrPortalLight" "id" 
	"string notes"  ['No Value'] 
	"float intensityMult"  [1.0] 
	"color tint"  [1 1 1] 
	"string domeColorMap"  ['No Value'] 
	"color lightColor"  ['No Value'] 
	"float intensity"  ['No Value'] 
	"float exposure"  ['No Value'] 
	"vector colorMapGamma"  [1.0 1.0 1.0] 
	"float colorMapSaturation"  [1.0] 
	"int enableTemperature"  [0] 
	"float temperature"  [6500] 
	"float specular"  [1.0] 
	"float diffuse"  [1.0] 
	"int enableShadows"  [1] 
	"color shadowColor"  [0 0 0] 
	"float shadowDistance"  [-1.0] 
	"float shadowFalloff"  [-1.0] 
	"float shadowFalloffGamma"  [1.0] 
	"string shadowSubset"  [''] 
	"string shadowExcludeSubset"  [''] 
	"int traceLightPaths"  [0] 
	"int thinShadow"  [1] 
	"int visibleInRefractionPath"  [0] 
	"int cheapCaustics"  [0] 
	"string cheapCausticsExcludeGroup"  [''] 
	"int fixedSampleCount"  [0] 
	"string lightGroup"  [''] 
	"float importanceMultiplier"  [1.0] 
	"matrix portalToDome"  ['No Value'] 
	"string portalName"  ['No Value'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Light('PxrPortalLight','id',
{
	'string notes' : ['No Value'], 
	'float intensityMult' : [1.0], 
	'color tint' : [1,1,1], 
	'string domeColorMap' : ['No Value'], 
	'color lightColor' : ['No Value'], 
	'float intensity' : ['No Value'], 
	'float exposure' : ['No Value'], 
	'vector colorMapGamma' : [1.0,1.0,1.0], 
	'float colorMapSaturation' : [1.0], 
	'int enableTemperature' : [0], 
	'float temperature' : [6500], 
	'float specular' : [1.0], 
	'float diffuse' : [1.0], 
	'int enableShadows' : [1], 
	'color shadowColor' : [0,0,0], 
	'float shadowDistance' : [-1.0], 
	'float shadowFalloff' : [-1.0], 
	'float shadowFalloffGamma' : [1.0], 
	'string shadowSubset' : [''], 
	'string shadowExcludeSubset' : [''], 
	'int traceLightPaths' : [0], 
	'int thinShadow' : [1], 
	'int visibleInRefractionPath' : [0], 
	'int cheapCaustics' : [0], 
	'string cheapCausticsExcludeGroup' : [''], 
	'int fixedSampleCount' : [0], 
	'string lightGroup' : [''], 
	'float importanceMultiplier' : [1.0], 
	'matrix portalToDome' : ['No Value'], 
	'string portalName' : ['No Value'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrDomeLight 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Light "PxrDomeLight" "id" 
	"string notes"  ['No Value'] 
	"float intensity"  [1.0] 
	"float exposure"  [0] 
	"color lightColor"  [1 1 1] 
	"string lightColorMap"  ['No Value'] 
	"vector colorMapGamma"  [1.0 1.0 1.0] 
	"float colorMapSaturation"  [1.0] 
	"int enableTemperature"  [0] 
	"float temperature"  [6500] 
	"float specular"  [1.0] 
	"float diffuse"  [1.0] 
	"int enableShadows"  [1] 
	"color shadowColor"  [0 0 0] 
	"float shadowDistance"  [-1.0] 
	"float shadowFalloff"  [-1.0] 
	"float shadowFalloffGamma"  [1.0] 
	"string shadowSubset"  [''] 
	"string shadowExcludeSubset"  [''] 
	"int traceLightPaths"  [0] 
	"int thinShadow"  [1] 
	"int visibleInRefractionPath"  [0] 
	"int cheapCaustics"  [0] 
	"string cheapCausticsExcludeGroup"  [''] 
	"int fixedSampleCount"  [0] 
	"string lightGroup"  [''] 
	"float importanceMultiplier"  [1.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Light('PxrDomeLight','id',
{
	'string notes' : ['No Value'], 
	'float intensity' : [1.0], 
	'float exposure' : [0], 
	'color lightColor' : [1,1,1], 
	'string lightColorMap' : ['No Value'], 
	'vector colorMapGamma' : [1.0,1.0,1.0], 
	'float colorMapSaturation' : [1.0], 
	'int enableTemperature' : [0], 
	'float temperature' : [6500], 
	'float specular' : [1.0], 
	'float diffuse' : [1.0], 
	'int enableShadows' : [1], 
	'color shadowColor' : [0,0,0], 
	'float shadowDistance' : [-1.0], 
	'float shadowFalloff' : [-1.0], 
	'float shadowFalloffGamma' : [1.0], 
	'string shadowSubset' : [''], 
	'string shadowExcludeSubset' : [''], 
	'int traceLightPaths' : [0], 
	'int thinShadow' : [1], 
	'int visibleInRefractionPath' : [0], 
	'int cheapCaustics' : [0], 
	'string cheapCausticsExcludeGroup' : [''], 
	'int fixedSampleCount' : [0], 
	'string lightGroup' : [''], 
	'float importanceMultiplier' : [1.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrSphereLight 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Light "PxrSphereLight" "id" 
	"string notes"  ['No Value'] 
	"float intensity"  [1.0] 
	"float exposure"  [0] 
	"color lightColor"  [1 1 1] 
	"int enableTemperature"  [0] 
	"float temperature"  [6500] 
	"float emissionFocus"  [0.0] 
	"color emissionFocusTint"  [0 0 0] 
	"float specular"  [1.0] 
	"float diffuse"  [1.0] 
	"float intensityNearDist"  [0.0] 
	"float coneAngle"  [90.0] 
	"float coneSoftness"  [0.0] 
	"string iesProfile"  [''] 
	"float iesProfileScale"  [0] 
	"int iesProfileNormalize"  [0] 
	"int enableShadows"  [1] 
	"color shadowColor"  [0 0 0] 
	"float shadowDistance"  [-1.0] 
	"float shadowFalloff"  [-1.0] 
	"float shadowFalloffGamma"  [1.0] 
	"string shadowSubset"  [''] 
	"string shadowExcludeSubset"  [''] 
	"int areaNormalize"  [0] 
	"int traceLightPaths"  [0] 
	"int thinShadow"  [1] 
	"int visibleInRefractionPath"  [0] 
	"int cheapCaustics"  [0] 
	"string cheapCausticsExcludeGroup"  [''] 
	"int fixedSampleCount"  [0] 
	"string lightGroup"  [''] 
	"float importanceMultiplier"  [1.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Light('PxrSphereLight','id',
{
	'string notes' : ['No Value'], 
	'float intensity' : [1.0], 
	'float exposure' : [0], 
	'color lightColor' : [1,1,1], 
	'int enableTemperature' : [0], 
	'float temperature' : [6500], 
	'float emissionFocus' : [0.0], 
	'color emissionFocusTint' : [0,0,0], 
	'float specular' : [1.0], 
	'float diffuse' : [1.0], 
	'float intensityNearDist' : [0.0], 
	'float coneAngle' : [90.0], 
	'float coneSoftness' : [0.0], 
	'string iesProfile' : [''], 
	'float iesProfileScale' : [0], 
	'int iesProfileNormalize' : [0], 
	'int enableShadows' : [1], 
	'color shadowColor' : [0,0,0], 
	'float shadowDistance' : [-1.0], 
	'float shadowFalloff' : [-1.0], 
	'float shadowFalloffGamma' : [1.0], 
	'string shadowSubset' : [''], 
	'string shadowExcludeSubset' : [''], 
	'int areaNormalize' : [0], 
	'int traceLightPaths' : [0], 
	'int thinShadow' : [1], 
	'int visibleInRefractionPath' : [0], 
	'int cheapCaustics' : [0], 
	'string cheapCausticsExcludeGroup' : [''], 
	'int fixedSampleCount' : [0], 
	'string lightGroup' : [''], 
	'float importanceMultiplier' : [1.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrRectLight 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Light "PxrRectLight" "id" 
	"string notes"  ['No Value'] 
	"float intensity"  [1.0] 
	"float exposure"  [0] 
	"color lightColor"  [1 1 1] 
	"string lightColorMap"  ['No Value'] 
	"vector colorMapGamma"  [1.0 1.0 1.0] 
	"float colorMapSaturation"  [1.0] 
	"int enableTemperature"  [0] 
	"float temperature"  [6500] 
	"float emissionFocus"  [0.0] 
	"color emissionFocusTint"  [0 0 0] 
	"float specular"  [1.0] 
	"float diffuse"  [1.0] 
	"float intensityNearDist"  [0.0] 
	"float coneAngle"  [90.0] 
	"float coneSoftness"  [0.0] 
	"string iesProfile"  [''] 
	"float iesProfileScale"  [0] 
	"int iesProfileNormalize"  [0] 
	"int enableShadows"  [1] 
	"color shadowColor"  [0 0 0] 
	"float shadowDistance"  [-1] 
	"float shadowFalloff"  [-1.0] 
	"float shadowFalloffGamma"  [1.0] 
	"string shadowSubset"  [''] 
	"string shadowExcludeSubset"  [''] 
	"int areaNormalize"  [0] 
	"int traceLightPaths"  [0] 
	"int thinShadow"  [1] 
	"int visibleInRefractionPath"  [0] 
	"int cheapCaustics"  [0] 
	"string cheapCausticsExcludeGroup"  [''] 
	"int fixedSampleCount"  [0] 
	"string lightGroup"  [''] 
	"float importanceMultiplier"  [1.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Light('PxrRectLight','id',
{
	'string notes' : ['No Value'], 
	'float intensity' : [1.0], 
	'float exposure' : [0], 
	'color lightColor' : [1,1,1], 
	'string lightColorMap' : ['No Value'], 
	'vector colorMapGamma' : [1.0,1.0,1.0], 
	'float colorMapSaturation' : [1.0], 
	'int enableTemperature' : [0], 
	'float temperature' : [6500], 
	'float emissionFocus' : [0.0], 
	'color emissionFocusTint' : [0,0,0], 
	'float specular' : [1.0], 
	'float diffuse' : [1.0], 
	'float intensityNearDist' : [0.0], 
	'float coneAngle' : [90.0], 
	'float coneSoftness' : [0.0], 
	'string iesProfile' : [''], 
	'float iesProfileScale' : [0], 
	'int iesProfileNormalize' : [0], 
	'int enableShadows' : [1], 
	'color shadowColor' : [0,0,0], 
	'float shadowDistance' : [-1], 
	'float shadowFalloff' : [-1.0], 
	'float shadowFalloffGamma' : [1.0], 
	'string shadowSubset' : [''], 
	'string shadowExcludeSubset' : [''], 
	'int areaNormalize' : [0], 
	'int traceLightPaths' : [0], 
	'int thinShadow' : [1], 
	'int visibleInRefractionPath' : [0], 
	'int cheapCaustics' : [0], 
	'string cheapCausticsExcludeGroup' : [''], 
	'int fixedSampleCount' : [0], 
	'string lightGroup' : [''], 
	'float importanceMultiplier' : [1.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrEnvDayLight 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Light "PxrEnvDayLight" "id" 
	"string notes"  ['No Value'] 
	"float intensity"  [1.0] 
	"float exposure"  [0.0] 
	"vector sunDirection"  [0.0 1.0 0.0] 
	"float haziness"  [2.0] 
	"color skyTint"  [1.0 1.0 1.0] 
	"color sunTint"  [1.0 1.0 1.0] 
	"float sunSize"  [1.0] 
	"int groundMode"  [0] 
	"color groundColor"  [0.18 0.18 0.18] 
	"int month"  [11] 
	"int day"  [20] 
	"int year"  [2014] 
	"float hour"  [14.633333] 
	"float zone"  [-8] 
	"float latitude"  [47.6019] 
	"float longitude"  [-122.3318] 
	"float specular"  [1.0] 
	"float diffuse"  [1.0] 
	"int enableShadows"  [1] 
	"color shadowColor"  [0 0 0] 
	"float shadowDistance"  [-1.0] 
	"float shadowFalloff"  [-1.0] 
	"float shadowFalloffGamma"  [1.0] 
	"string shadowSubset"  [''] 
	"string shadowExcludeSubset"  [''] 
	"int traceLightPaths"  [0] 
	"int thinShadow"  [1] 
	"int visibleInRefractionPath"  [0] 
	"int cheapCaustics"  [0] 
	"string cheapCausticsExcludeGroup"  [''] 
	"int fixedSampleCount"  [0] 
	"string lightGroup"  [''] 
	"float importanceMultiplier"  [1.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Light('PxrEnvDayLight','id',
{
	'string notes' : ['No Value'], 
	'float intensity' : [1.0], 
	'float exposure' : [0.0], 
	'vector sunDirection' : [0.0,1.0,0.0], 
	'float haziness' : [2.0], 
	'color skyTint' : [1.0,1.0,1.0], 
	'color sunTint' : [1.0,1.0,1.0], 
	'float sunSize' : [1.0], 
	'int groundMode' : [0], 
	'color groundColor' : [0.18,0.18,0.18], 
	'int month' : [11], 
	'int day' : [20], 
	'int year' : [2014], 
	'float hour' : [14.633333], 
	'float zone' : [-8], 
	'float latitude' : [47.6019], 
	'float longitude' : [-122.3318], 
	'float specular' : [1.0], 
	'float diffuse' : [1.0], 
	'int enableShadows' : [1], 
	'color shadowColor' : [0,0,0], 
	'float shadowDistance' : [-1.0], 
	'float shadowFalloff' : [-1.0], 
	'float shadowFalloffGamma' : [1.0], 
	'string shadowSubset' : [''], 
	'string shadowExcludeSubset' : [''], 
	'int traceLightPaths' : [0], 
	'int thinShadow' : [1], 
	'int visibleInRefractionPath' : [0], 
	'int cheapCaustics' : [0], 
	'string cheapCausticsExcludeGroup' : [''], 
	'int fixedSampleCount' : [0], 
	'string lightGroup' : [''], 
	'float importanceMultiplier' : [1.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrDiskLight 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Light "PxrDiskLight" "id" 
	"string notes"  ['No Value'] 
	"float intensity"  [1.0] 
	"float exposure"  [0] 
	"color lightColor"  [1 1 1] 
	"int enableTemperature"  [0] 
	"float temperature"  [6500] 
	"float emissionFocus"  [0.0] 
	"color emissionFocusTint"  [0 0 0] 
	"float specular"  [1.0] 
	"float diffuse"  [1.0] 
	"float intensityNearDist"  [0.0] 
	"float coneAngle"  [90.0] 
	"float coneSoftness"  [0.0] 
	"string iesProfile"  [''] 
	"float iesProfileScale"  [0] 
	"int iesProfileNormalize"  [0] 
	"int enableShadows"  [1] 
	"color shadowColor"  [0 0 0] 
	"float shadowDistance"  [-1.0] 
	"float shadowFalloff"  [-1.0] 
	"float shadowFalloffGamma"  [1.0] 
	"string shadowSubset"  [''] 
	"string shadowExcludeSubset"  [''] 
	"int areaNormalize"  [0] 
	"int traceLightPaths"  [0] 
	"int thinShadow"  [1] 
	"int visibleInRefractionPath"  [0] 
	"int cheapCaustics"  [0] 
	"string cheapCausticsExcludeGroup"  [''] 
	"int fixedSampleCount"  [0] 
	"string lightGroup"  [''] 
	"float importanceMultiplier"  [1.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Light('PxrDiskLight','id',
{
	'string notes' : ['No Value'], 
	'float intensity' : [1.0], 
	'float exposure' : [0], 
	'color lightColor' : [1,1,1], 
	'int enableTemperature' : [0], 
	'float temperature' : [6500], 
	'float emissionFocus' : [0.0], 
	'color emissionFocusTint' : [0,0,0], 
	'float specular' : [1.0], 
	'float diffuse' : [1.0], 
	'float intensityNearDist' : [0.0], 
	'float coneAngle' : [90.0], 
	'float coneSoftness' : [0.0], 
	'string iesProfile' : [''], 
	'float iesProfileScale' : [0], 
	'int iesProfileNormalize' : [0], 
	'int enableShadows' : [1], 
	'color shadowColor' : [0,0,0], 
	'float shadowDistance' : [-1.0], 
	'float shadowFalloff' : [-1.0], 
	'float shadowFalloffGamma' : [1.0], 
	'string shadowSubset' : [''], 
	'string shadowExcludeSubset' : [''], 
	'int areaNormalize' : [0], 
	'int traceLightPaths' : [0], 
	'int thinShadow' : [1], 
	'int visibleInRefractionPath' : [0], 
	'int cheapCaustics' : [0], 
	'string cheapCausticsExcludeGroup' : [''], 
	'int fixedSampleCount' : [0], 
	'string lightGroup' : [''], 
	'float importanceMultiplier' : [1.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrDistantLight 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Light "PxrDistantLight" "id" 
	"string notes"  ['No Value'] 
	"float intensity"  [50000] 
	"float exposure"  [0] 
	"float angleExtent"  [0.53] 
	"color lightColor"  [1 1 1] 
	"int enableTemperature"  [0] 
	"float temperature"  [6500] 
	"float emissionFocus"  [0.0] 
	"color emissionFocusTint"  [0 0 0] 
	"float specular"  [1.0] 
	"float diffuse"  [1.0] 
	"int enableShadows"  [1] 
	"color shadowColor"  [0 0 0] 
	"float shadowDistance"  [-1.0] 
	"float shadowFalloff"  [-1.0] 
	"float shadowFalloffGamma"  [1.0] 
	"string shadowSubset"  [''] 
	"string shadowExcludeSubset"  [''] 
	"int areaNormalize"  [0] 
	"int traceLightPaths"  [0] 
	"int thinShadow"  [1] 
	"int visibleInRefractionPath"  [0] 
	"int cheapCaustics"  [0] 
	"string cheapCausticsExcludeGroup"  [''] 
	"int fixedSampleCount"  [0] 
	"string lightGroup"  [''] 
	"float importanceMultiplier"  [1.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Light('PxrDistantLight','id',
{
	'string notes' : ['No Value'], 
	'float intensity' : [50000], 
	'float exposure' : [0], 
	'float angleExtent' : [0.53], 
	'color lightColor' : [1,1,1], 
	'int enableTemperature' : [0], 
	'float temperature' : [6500], 
	'float emissionFocus' : [0.0], 
	'color emissionFocusTint' : [0,0,0], 
	'float specular' : [1.0], 
	'float diffuse' : [1.0], 
	'int enableShadows' : [1], 
	'color shadowColor' : [0,0,0], 
	'float shadowDistance' : [-1.0], 
	'float shadowFalloff' : [-1.0], 
	'float shadowFalloffGamma' : [1.0], 
	'string shadowSubset' : [''], 
	'string shadowExcludeSubset' : [''], 
	'int areaNormalize' : [0], 
	'int traceLightPaths' : [0], 
	'int thinShadow' : [1], 
	'int visibleInRefractionPath' : [0], 
	'int cheapCaustics' : [0], 
	'string cheapCausticsExcludeGroup' : [''], 
	'int fixedSampleCount' : [0], 
	'string lightGroup' : [''], 
	'float importanceMultiplier' : [1.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrMeshLight 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Light "PxrMeshLight" "id" 
	"float intensity"  [1.0] 
	"float exposure"  [0] 
	"color lightColor"  [1 1 1] 
	"color textureColor"  [1 1 1] 
	"int enableTemperature"  [0] 
	"float temperature"  [6500] 
	"float specular"  [1.0] 
	"float diffuse"  [1.0] 
	"float intensityNearDist"  [0.0] 
	"int enableShadows"  [1] 
	"color shadowColor"  [0 0 0] 
	"float shadowDistance"  [-1] 
	"float shadowFalloff"  [-1.0] 
	"float shadowFalloffGamma"  [1.0] 
	"string shadowSubset"  [''] 
	"string shadowExcludeSubset"  [''] 
	"int areaNormalize"  [0] 
	"int traceLightPaths"  [0] 
	"int thinShadow"  [1] 
	"float importanceMultiplier"  [1.0] 
	"string lightGroup"  [''] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Light('PxrMeshLight','id',
{
	'float intensity' : [1.0], 
	'float exposure' : [0], 
	'color lightColor' : [1,1,1], 
	'color textureColor' : [1,1,1], 
	'int enableTemperature' : [0], 
	'float temperature' : [6500], 
	'float specular' : [1.0], 
	'float diffuse' : [1.0], 
	'float intensityNearDist' : [0.0], 
	'int enableShadows' : [1], 
	'color shadowColor' : [0,0,0], 
	'float shadowDistance' : [-1], 
	'float shadowFalloff' : [-1.0], 
	'float shadowFalloffGamma' : [1.0], 
	'string shadowSubset' : [''], 
	'string shadowExcludeSubset' : [''], 
	'int areaNormalize' : [0], 
	'int traceLightPaths' : [0], 
	'int thinShadow' : [1], 
	'float importanceMultiplier' : [1.0], 
	'string lightGroup' : [''], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrAovLight 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Light "PxrAovLight" "id" 
	"string aovName"  [''] 
	"string notes"  ['No Value'] 
	"int useColor"  [0] 
	"int invert"  [0] 
	"int inPrimaryHit"  [1] 
	"int inRefraction"  [0] 
	"int inReflection"  [0] 
	"int onVolumeBoundaries"  [1] 
	"int useThroughput"  [1] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Light('PxrAovLight','id',
{
	'string aovName' : [''], 
	'string notes' : ['No Value'], 
	'int useColor' : [0], 
	'int invert' : [0], 
	'int inPrimaryHit' : [1], 
	'int inRefraction' : [0], 
	'int inReflection' : [0], 
	'int onVolumeBoundaries' : [1], 
	'int useThroughput' : [1], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Displacement
## Plugin PxrDisplace 
A C++ displacement plugin.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Displacement "PxrDisplace" "id" 
	"int enabled"  [1] 
	"float dispAmount"  [1.0] 
	"float dispScalar"  [0.0] 
	"vector dispVector"  [0.0 0.0 0.0] 
	"vector modelDispVector"  [0.0 0.0 0.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Displacement('PxrDisplace','id',
{
	'int enabled' : [1], 
	'float dispAmount' : [1.0], 
	'float dispScalar' : [0.0], 
	'vector dispVector' : [0.0,0.0,0.0], 
	'vector modelDispVector' : [0.0,0.0,0.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Integrator
## Plugin PxrPathTracer 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Integrator "PxrPathTracer" "id" 
	"int maxPathLength"  [10] 
	"int maxContinuationLength"  [-1] 
	"int maxNonStochasticOpacityEvents"  [0] 
	"string sampleMode"  ['bxdf'] 
	"int numLightSamples"  [1] 
	"int numBxdfSamples"  [1] 
	"int numIndirectSamples"  [1] 
	"int numDiffuseSamples"  [1] 
	"int numSpecularSamples"  [1] 
	"int numSubsurfaceSamples"  [1] 
	"int numRefractionSamples"  [1] 
	"int allowCaustics"  [0] 
	"int accumOpacity"  [0] 
	"int rouletteDepth"  [4] 
	"float rouletteThreshold"  [0.2] 
	"int clampDepth"  [2] 
	"float clampLuminance"  [10.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Integrator('PxrPathTracer','id',
{
	'int maxPathLength' : [10], 
	'int maxContinuationLength' : [-1], 
	'int maxNonStochasticOpacityEvents' : [0], 
	'string sampleMode' : ['bxdf'], 
	'int numLightSamples' : [1], 
	'int numBxdfSamples' : [1], 
	'int numIndirectSamples' : [1], 
	'int numDiffuseSamples' : [1], 
	'int numSpecularSamples' : [1], 
	'int numSubsurfaceSamples' : [1], 
	'int numRefractionSamples' : [1], 
	'int allowCaustics' : [0], 
	'int accumOpacity' : [0], 
	'int rouletteDepth' : [4], 
	'float rouletteThreshold' : [0.2], 
	'int clampDepth' : [2], 
	'float clampLuminance' : [10.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrUnified 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Integrator "PxrUnified" "id" 
	"int traceLightPaths"  [0] 
	"int maxPathLength"  [8] 
	"float maxRayDistance"  [10000] 
	"float catchAllLights"  [0] 
	"float emissionMultiplier"  [1] 
	"int accumOpacity"  [1] 
	"float specularCurvatureFilter"  [1.0] 
	"int numLightSamples"  [1] 
	"int numBxdfSamples"  [1] 
	"int numIndirectSamples"  [1] 
	"int sssOversampling"  [8] 
	"int allowMultilobeIndirect"  [0] 
	"int manifoldWalk"  [0] 
	"int maxIterations"  [10] 
	"int maxInterfaces"  [2] 
	"float walkThreshold"  [0.005] 
	"int enableVolumeCaustics"  [0] 
	"float photonEstimationRadius"  [0.0] 
	"int photonEstimationNumber"  [64] 
	"int photonVisibilityRod"  [0] 
	"float photonVisibilityRodDirectProb"  [0.0] 
	"point photonVisibilityRodMin"  [0.0 0.0 0.0] 
	"point photonVisibilityRodMax"  [0.0 0.0 0.0] 
	"int photonAdaptive"  [0] 
	"int indirectTrainingSamples"  [0] 
	"float indirectSpatialBlurRadius"  [0.25] 
	"float indirectDirectionalBlurRadius"  [0.0] 
	"int indirectOversampling"  [2] 
	"int suppressNaNs"  [0] 
	"int enableShadingTimers"  [0] 
	"int enableSampleTimers"  [0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Integrator('PxrUnified','id',
{
	'int traceLightPaths' : [0], 
	'int maxPathLength' : [8], 
	'float maxRayDistance' : [10000], 
	'float catchAllLights' : [0], 
	'float emissionMultiplier' : [1], 
	'int accumOpacity' : [1], 
	'float specularCurvatureFilter' : [1.0], 
	'int numLightSamples' : [1], 
	'int numBxdfSamples' : [1], 
	'int numIndirectSamples' : [1], 
	'int sssOversampling' : [8], 
	'int allowMultilobeIndirect' : [0], 
	'int manifoldWalk' : [0], 
	'int maxIterations' : [10], 
	'int maxInterfaces' : [2], 
	'float walkThreshold' : [0.005], 
	'int enableVolumeCaustics' : [0], 
	'float photonEstimationRadius' : [0.0], 
	'int photonEstimationNumber' : [64], 
	'int photonVisibilityRod' : [0], 
	'float photonVisibilityRodDirectProb' : [0.0], 
	'point photonVisibilityRodMin' : [0.0,0.0,0.0], 
	'point photonVisibilityRodMax' : [0.0,0.0,0.0], 
	'int photonAdaptive' : [0], 
	'int indirectTrainingSamples' : [0], 
	'float indirectSpatialBlurRadius' : [0.25], 
	'float indirectDirectionalBlurRadius' : [0.0], 
	'int indirectOversampling' : [2], 
	'int suppressNaNs' : [0], 
	'int enableShadingTimers' : [0], 
	'int enableSampleTimers' : [0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrOcclusion 
Render occlusion.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Integrator "PxrOcclusion" "id" 
	"int numSamples"  [4] 
	"int distribution"  [1] 
	"float cosineSpread"  [1.0] 
	"float falloff"  [0.0] 
	"float maxDistance"  [0.0] 
	"int useAlbedo"  [0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Integrator('PxrOcclusion','id',
{
	'int numSamples' : [4], 
	'int distribution' : [1], 
	'float cosineSpread' : [1.0], 
	'float falloff' : [0.0], 
	'float maxDistance' : [0.0], 
	'int useAlbedo' : [0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrDefault 
Even simpler than PxrDirectLighting, the default integrator
        places a virtual light at the camera (the "headlamp
        integrator"). No shadows or indirect lighting are evaluated. A
        good option when all is black - this integrator can help
        narrow down where a problem is occurring (for example, when
        the fault is in the lighting, particularly). Like
        PxrDirectLighting, it is not designed to produce
        "final-quality" images.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Integrator "PxrDefault" "id" 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Integrator('PxrDefault','id',
{
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrDebugShadingContext 
This integrator is used to visualize data in the shading
        context, such as normals and texture coordinates. It is not
        designed to produce "final-quality" images.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Integrator "PxrDebugShadingContext" "id" 
	"string viewchannel"  ['Nn'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Integrator('PxrDebugShadingContext','id',
{
	'string viewchannel' : ['Nn'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrVCM 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Integrator "PxrVCM" "id" 
	"int connectPaths"  [1] 
	"int mergePaths"  [1] 
	"int numLightSamples"  [1] 
	"int numBxdfSamples"  [1] 
	"int maxPathLength"  [10] 
	"float specularCurvatureFilter"  [1.0] 
	"int rouletteDepth"  [4] 
	"float rouletteThreshold"  [0.2] 
	"int clampDepth"  [2] 
	"float clampLuminance"  [10.0] 
	"float mergeRadius"  [5.0] 
	"float timeRadius"  [1.0] 
	"float photonGuiding"  [0.0] 
	"point photonGuidingBBoxMin"  [1e30 1e30 1e30] 
	"point photonGuidingBBoxMax"  [-1e30 -1e30 -1e30] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Integrator('PxrVCM','id',
{
	'int connectPaths' : [1], 
	'int mergePaths' : [1], 
	'int numLightSamples' : [1], 
	'int numBxdfSamples' : [1], 
	'int maxPathLength' : [10], 
	'float specularCurvatureFilter' : [1.0], 
	'int rouletteDepth' : [4], 
	'float rouletteThreshold' : [0.2], 
	'int clampDepth' : [2], 
	'float clampLuminance' : [10.0], 
	'float mergeRadius' : [5.0], 
	'float timeRadius' : [1.0], 
	'float photonGuiding' : [0.0], 
	'point photonGuidingBBoxMin' : [1e30,1e30,1e30], 
	'point photonGuidingBBoxMax' : [-1e30,-1e30,-1e30], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrDirectLighting 
This is a debugging or "draft-quality" integrator that
        implements only the direct lighting portion of the light
        transport. It is not designed to produce "final-quality"
        images. Since it doesn't implement indirect lighting paths it
        cannot produce reflections, refractions, or other global
        illumination effects, nor can it handle any effects that
        require a volume integrator.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Integrator "PxrDirectLighting" "id" 
	"int numLightSamples"  [4] 
	"int numBxdfSamples"  [4] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Integrator('PxrDirectLighting','id',
{
	'int numLightSamples' : [4], 
	'int numBxdfSamples' : [4], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrValidateBxdf 
This integrator serves mainly as a debugging tool to authors of
       Bxdf plugins. The 3 channels of the output are the luminance
       results for total hemispherical reflectance, computed in three
       different ways: the red channel gives the results of using the
       Bxdf's GenerateSample method to sample the bxdf; the green
       channel gives the results of running the Bxdf's EvaluateSample
       (or EvaluateSamplesAtIndex) method using the same generated
       samples, and only accumulating them if they agree with the
       values returned by GenerateSample; and the blue channel gives
       the results of integrating a set of hemispherical samples
       generated with a cosine weighting using the EvaluateSample
       method on the bxdf. Ideally, this will converge to the other
       two results.

       If the Bxdf is given "white" values and is correct, the
       resulting image should converge to all white pixels. Energy
       lost (either due to explicit absorption or due to the bxdf
       model losing energy) or gained shows up as non-white
       pixels. Bxdf authors should take care to observe what happens
       at grazing angles, as that can be a good place to lose energy.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Integrator "PxrValidateBxdf" "id" 
	"int numSamples"  [4] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Integrator('PxrValidateBxdf','id',
{
	'int numSamples' : [4], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrVisualizer 
A utility integrator to navigate and inspect large scenes interactively.
        Can also be used for modeling or animation turntables and in general to 
        detect geometric problems in your scenes.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Integrator "PxrVisualizer" "id" 
	"string style"  ['shaded'] 
	"int wireframe"  [1] 
	"int normalCheck"  [0] 
	"string matCap"  [''] 
	"color wireframeColor"  [0.0 0.0 0.0] 
	"float wireframeOpacity"  [0.5] 
	"float wireframeWidth"  [1.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Integrator('PxrVisualizer','id',
{
	'string style' : ['shaded'], 
	'int wireframe' : [1], 
	'int normalCheck' : [0], 
	'string matCap' : [''], 
	'color wireframeColor' : [0.0,0.0,0.0], 
	'float wireframeOpacity' : [0.5], 
	'float wireframeWidth' : [1.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# DisplayFilter
## Plugin PxrFilmicTonemapperDisplayFilter 
Display filter plugin based on Naughty Dog's Filmic Tonemapper from GDC Uncharted 2 HDR Lighting presentation.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
DisplayFilter "PxrFilmicTonemapperDisplayFilter" "id" 
	"float A"  [0.22] 
	"float B"  [0.30] 
	"float C"  [0.10] 
	"float D"  [0.20] 
	"float E"  [0.01] 
	"float F"  [0.3] 
	"float linearWhitePoint"  [11.2] 
	"float exposureAdjust"  [1.0] 
	"string aov"  ['Ci'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.DisplayFilter('PxrFilmicTonemapperDisplayFilter','id',
{
	'float A' : [0.22], 
	'float B' : [0.30], 
	'float C' : [0.10], 
	'float D' : [0.20], 
	'float E' : [0.01], 
	'float F' : [0.3], 
	'float linearWhitePoint' : [11.2], 
	'float exposureAdjust' : [1.0], 
	'string aov' : ['Ci'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrHalfBufferErrorFilter 
Estimate the error of an image by comparing two half buffers.  If two
    statistically-independent images are each produced from half the camera
    samples, then we can estimate the mean-squared-error between the ground
    truth and their average and as one-quarter of the squared difference of
    the two.  The AOVs may be either all scalar or all color.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
DisplayFilter "PxrHalfBufferErrorFilter" "id" 
	"string aov1"  ['even'] 
	"string aov2"  ['odd'] 
	"string result"  ['mse'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.DisplayFilter('PxrHalfBufferErrorFilter','id',
{
	'string aov1' : ['even'], 
	'string aov2' : ['odd'], 
	'string result' : ['mse'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrLightSaturation 
A small example display filter that changes the color saturation in the
    beauty pass (or any other AOV) according to whether a region is lit or
    shadowed by particular light group.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
DisplayFilter "PxrLightSaturation" "id" 
	"string aov"  ['Ci'] 
	"string light"  [''] 
	"float threshold"  [1.0] 
	"int invert"  [0] 
	"float shift"  [1.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.DisplayFilter('PxrLightSaturation','id',
{
	'string aov' : ['Ci'], 
	'string light' : [''], 
	'float threshold' : [1.0], 
	'int invert' : [0], 
	'float shift' : [1.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrCopyAOVDisplayFilter 
Display filter plugin to look up a named AOV and copy it
    to Ci.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
DisplayFilter "PxrCopyAOVDisplayFilter" "id" 
	"string readAov"  [''] 
	"string writeAov"  ['Ci'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.DisplayFilter('PxrCopyAOVDisplayFilter','id',
{
	'string readAov' : [''], 
	'string writeAov' : ['Ci'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrDisplayFilterCombiner 
Display filter combiner.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
DisplayFilter "PxrDisplayFilterCombiner" "id" 
	"displayfilter filter"  ['No Value'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.DisplayFilter('PxrDisplayFilterCombiner','id',
{
	'displayfilter filter' : ['No Value'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrBackgroundDisplayFilter 
Display filter plugin to color the background.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
DisplayFilter "PxrBackgroundDisplayFilter" "id" 
	"color backgroundColor"  [0 0 0] 
	"string aov"  ['Ci'] 
	"string aovAlpha"  ['a'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.DisplayFilter('PxrBackgroundDisplayFilter','id',
{
	'color backgroundColor' : [0,0,0], 
	'string aov' : ['Ci'], 
	'string aovAlpha' : ['a'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrImageDisplayFilter 
Display filter plugin to render image planes including holdouts.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
DisplayFilter "PxrImageDisplayFilter" "id" 
	"string filename"  [''] 
	"color colorGain"  [1.0 1.0 1.0] 
	"color colorOffset"  [0.0 0.0 0.0] 
	"int linearize"  [0] 
	"int fit"  [0] 
	"float filmMinX"  [0.0] 
	"float filmMaxX"  [0.0] 
	"float filmMinY"  [0.0] 
	"float filmMaxY"  [0.0] 
	"float offsetX"  [0.0] 
	"float offsetY"  [0.0] 
	"float scaleX"  [1.0] 
	"float scaleY"  [1.0] 
	"float rotate"  [0.0] 
	"string holdoutShadowAov"  [''] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.DisplayFilter('PxrImageDisplayFilter','id',
{
	'string filename' : [''], 
	'color colorGain' : [1.0,1.0,1.0], 
	'color colorOffset' : [0.0,0.0,0.0], 
	'int linearize' : [0], 
	'int fit' : [0], 
	'float filmMinX' : [0.0], 
	'float filmMaxX' : [0.0], 
	'float filmMinY' : [0.0], 
	'float filmMaxY' : [0.0], 
	'float offsetX' : [0.0], 
	'float offsetY' : [0.0], 
	'float scaleX' : [1.0], 
	'float scaleY' : [1.0], 
	'float rotate' : [0.0], 
	'string holdoutShadowAov' : [''], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrEdgeDetect 
A small example display filter that demonstrates image processing.
    This filter replaces the image in the beauty pass (or any other AOV)
    with its gradient magnitude computed from a Sobel edge-detection
    filter.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
DisplayFilter "PxrEdgeDetect" "id" 
	"string aov"  ['Ci'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.DisplayFilter('PxrEdgeDetect','id',
{
	'string aov' : ['Ci'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrWhitePointDisplayFilter 
This display filter allows you to adjust the output colors so that the given color temperature is considered white.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
DisplayFilter "PxrWhitePointDisplayFilter" "id" 
	"float temperature"  [6500] 
	"int useManualWhitePoint"  [0] 
	"color manualWhitePoint"  [1 1 1] 
	"string aov"  ['Ci'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.DisplayFilter('PxrWhitePointDisplayFilter','id',
{
	'float temperature' : [6500], 
	'int useManualWhitePoint' : [0], 
	'color manualWhitePoint' : [1,1,1], 
	'string aov' : ['Ci'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrGradeDisplayFilter 
Nuke-like grade display filter. Allows simple grading of the beauty pass.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
DisplayFilter "PxrGradeDisplayFilter" "id" 
	"color blackPoint"  [0 0 0] 
	"color whitePoint"  [1 1 1] 
	"color lift"  [0 0 0] 
	"color gain"  [1 1 1] 
	"color multiply"  [1 1 1] 
	"color gamma"  [1 1 1] 
	"color offset"  [1 1 1] 
	"int clampWhite"  [0] 
	"int clampBlack"  [1] 
	"color mask"  [1 1 1] 
	"string aov"  ['Ci'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.DisplayFilter('PxrGradeDisplayFilter','id',
{
	'color blackPoint' : [0,0,0], 
	'color whitePoint' : [1,1,1], 
	'color lift' : [0,0,0], 
	'color gain' : [1,1,1], 
	'color multiply' : [1,1,1], 
	'color gamma' : [1,1,1], 
	'color offset' : [1,1,1], 
	'int clampWhite' : [0], 
	'int clampBlack' : [1], 
	'color mask' : [1,1,1], 
	'string aov' : ['Ci'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrShadowDisplayFilter 
Display filter plugin to calculate shadow AOV output from occluded and unoccluded AOV inputs.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
DisplayFilter "PxrShadowDisplayFilter" "id" 
	"string occludedAov"  [''] 
	"string unoccludedAov"  [''] 
	"string shadowAov"  [''] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.DisplayFilter('PxrShadowDisplayFilter','id',
{
	'string occludedAov' : [''], 
	'string unoccludedAov' : [''], 
	'string shadowAov' : [''], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# SampleFilter
## Plugin PxrWatermarkFilter 
Sample filter plugin to add watermarks to renders.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
SampleFilter "PxrWatermarkFilter" "id" 
	"string filename"  [''] 
	"float transparency"  [0.0] 
	"int linearize"  [0] 
	"int mode"  [3] 
	"int fit"  [1] 
	"float offsetX"  [0.0] 
	"float offsetY"  [0.0] 
	"float scaleX"  [1.0] 
	"float scaleY"  [1.0] 
	"float rotate"  [0.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.SampleFilter('PxrWatermarkFilter','id',
{
	'string filename' : [''], 
	'float transparency' : [0.0], 
	'int linearize' : [0], 
	'int mode' : [3], 
	'int fit' : [1], 
	'float offsetX' : [0.0], 
	'float offsetY' : [0.0], 
	'float scaleX' : [1.0], 
	'float scaleY' : [1.0], 
	'float rotate' : [0.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrBackgroundSampleFilter 
Sample filter plugin to color the background.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
SampleFilter "PxrBackgroundSampleFilter" "id" 
	"color backgroundColor"  [0 0 0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.SampleFilter('PxrBackgroundSampleFilter','id',
{
	'color backgroundColor' : [0,0,0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrWhitePointSampleFilter 
This sample filter allows you to adjust the output colors so that the given color temperature is considered white.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
SampleFilter "PxrWhitePointSampleFilter" "id" 
	"float temperature"  [6500] 
	"int useManualWhitePoint"  [0] 
	"color manualWhitePoint"  [1 1 1] 
	"string aov"  ['Ci'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.SampleFilter('PxrWhitePointSampleFilter','id',
{
	'float temperature' : [6500], 
	'int useManualWhitePoint' : [0], 
	'color manualWhitePoint' : [1,1,1], 
	'string aov' : ['Ci'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrSampleFilterCombiner 
Sample filter combiner.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
SampleFilter "PxrSampleFilterCombiner" "id" 
	"samplefilter filter"  ['No Value'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.SampleFilter('PxrSampleFilterCombiner','id',
{
	'samplefilter filter' : ['No Value'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrShadowFilter 
Sample filter plugin to calculate shadow AOV output from occluded and unoccluded AOV inputs.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
SampleFilter "PxrShadowFilter" "id" 
	"string occludedAov"  [''] 
	"string unoccludedAov"  [''] 
	"string shadowAov"  [''] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.SampleFilter('PxrShadowFilter','id',
{
	'string occludedAov' : [''], 
	'string unoccludedAov' : [''], 
	'string shadowAov' : [''], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrGradeSampleFilter 
Nuke-like grade sample filter. Allows simple grading of the beauty pass.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
SampleFilter "PxrGradeSampleFilter" "id" 
	"color blackPoint"  [0 0 0] 
	"color whitePoint"  [1 1 1] 
	"color lift"  [0 0 0] 
	"color gain"  [1 1 1] 
	"color multiply"  [1 1 1] 
	"color gamma"  [1 1 1] 
	"color offset"  [1 1 1] 
	"int clampWhite"  [0] 
	"int clampBlack"  [1] 
	"color mask"  [1 1 1] 
	"string aov"  ['Ci'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.SampleFilter('PxrGradeSampleFilter','id',
{
	'color blackPoint' : [0,0,0], 
	'color whitePoint' : [1,1,1], 
	'color lift' : [0,0,0], 
	'color gain' : [1,1,1], 
	'color multiply' : [1,1,1], 
	'color gamma' : [1,1,1], 
	'color offset' : [1,1,1], 
	'int clampWhite' : [0], 
	'int clampBlack' : [1], 
	'color mask' : [1,1,1], 
	'string aov' : ['Ci'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrCopyAOVSampleFilter 
Sample filter plugin to look up a named AOV and copy it
    to Ci.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
SampleFilter "PxrCopyAOVSampleFilter" "id" 
	"string readAov"  [''] 
	"string writeAov"  ['Ci'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.SampleFilter('PxrCopyAOVSampleFilter','id',
{
	'string readAov' : [''], 
	'string writeAov' : ['Ci'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrFilmicTonemapperSampleFilter 
Sample filter plugin based on Naughty Dog's Filmic Tonemapper from GDC Uncharted 2 HDR Lighting presentation.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
SampleFilter "PxrFilmicTonemapperSampleFilter" "id" 
	"float A"  [0.22] 
	"float B"  [0.30] 
	"float C"  [0.10] 
	"float D"  [0.20] 
	"float E"  [0.01] 
	"float F"  [0.3] 
	"float linearWhitePoint"  [11.2] 
	"float exposureAdjust"  [1.0] 
	"string aov"  ['Ci'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.SampleFilter('PxrFilmicTonemapperSampleFilter','id',
{
	'float A' : [0.22], 
	'float B' : [0.30], 
	'float C' : [0.10], 
	'float D' : [0.20], 
	'float E' : [0.01], 
	'float F' : [0.3], 
	'float linearWhitePoint' : [11.2], 
	'float exposureAdjust' : [1.0], 
	'string aov' : ['Ci'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrCryptomatte 
Sample filter to generate Cryptomatte files for easy creation of
    keyable ID mattes.  See https://github.com/Psyop/Cryptomatte for tools
    and details.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
SampleFilter "PxrCryptomatte" "id" 
	"string filename"  ['cryptomatte.exr'] 
	"string manifest"  ['header'] 
	"string layer"  ['identifier:name'] 
	"string attribute"  [''] 
	"int levels"  [6] 
	"int accuracy"  [4] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.SampleFilter('PxrCryptomatte','id',
{
	'string filename' : ['cryptomatte.exr'], 
	'string manifest' : ['header'], 
	'string layer' : ['identifier:name'], 
	'string attribute' : [''], 
	'int levels' : [6], 
	'int accuracy' : [4], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrImagePlaneFilter 
Sample filter plugin to render image planes including holdouts.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
SampleFilter "PxrImagePlaneFilter" "id" 
	"string filename"  [''] 
	"color colorGain"  [1.0 1.0 1.0] 
	"color colorOffset"  [0.0 0.0 0.0] 
	"int linearize"  [0] 
	"int useAlpha"  [0] 
	"int fit"  [0] 
	"float filmMinX"  [0.0] 
	"float filmMaxX"  [0.0] 
	"float filmMinY"  [0.0] 
	"float filmMaxY"  [0.0] 
	"float offsetX"  [0.0] 
	"float offsetY"  [0.0] 
	"float scaleX"  [1.0] 
	"float scaleY"  [1.0] 
	"float rotate"  [0.0] 
	"string holdoutShadowAov"  [''] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.SampleFilter('PxrImagePlaneFilter','id',
{
	'string filename' : [''], 
	'color colorGain' : [1.0,1.0,1.0], 
	'color colorOffset' : [0.0,0.0,0.0], 
	'int linearize' : [0], 
	'int useAlpha' : [0], 
	'int fit' : [0], 
	'float filmMinX' : [0.0], 
	'float filmMaxX' : [0.0], 
	'float filmMinY' : [0.0], 
	'float filmMaxY' : [0.0], 
	'float offsetX' : [0.0], 
	'float offsetY' : [0.0], 
	'float scaleX' : [1.0], 
	'float scaleY' : [1.0], 
	'float rotate' : [0.0], 
	'string holdoutShadowAov' : [''], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# LightFilter
## Plugin PxrCombinerLightFilter 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
LightFilter "PxrCombinerLightFilter" "id" 
	"lightfilter mult"  ['No Value'] 
	"lightfilter max"  ['No Value'] 
	"lightfilter min"  ['No Value'] 
	"lightfilter screen"  ['No Value'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.LightFilter('PxrCombinerLightFilter','id',
{
	'lightfilter mult' : ['No Value'], 
	'lightfilter max' : ['No Value'], 
	'lightfilter min' : ['No Value'], 
	'lightfilter screen' : ['No Value'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrGoboLightFilter 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
LightFilter "PxrGoboLightFilter" "id" 
	"string combineMode"  ['mult'] 
	"string coordsys"  [''] 
	"string __lightFilterParentShader"  [''] 
	"float __lightFilterParentParam_width"  [10.0] 
	"float __lightFilterParentParam_height"  [10.0] 
	"float __lightFilterParentParam_radius"  [10.0] 
	"string notes"  [''] 
	"string map"  ['ratGrid.tex'] 
	"int premultipliedAlpha"  [1] 
	"int refreshMap"  [0] 
	"color fillColor"  [1.0 1.0 1.0] 
	"float width"  [1.0] 
	"float height"  [1.0] 
	"float density"  [1] 
	"int invert"  [0] 
	"float intensity"  [1.0] 
	"float diffuse"  [1.0] 
	"float specular"  [1.0] 
	"int tileMode"  [0] 
	"float scaleU"  [1.0] 
	"float scaleV"  [1.0] 
	"float offsetU"  [0.0] 
	"float offsetV"  [0.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.LightFilter('PxrGoboLightFilter','id',
{
	'string combineMode' : ['mult'], 
	'string coordsys' : [''], 
	'string __lightFilterParentShader' : [''], 
	'float __lightFilterParentParam_width' : [10.0], 
	'float __lightFilterParentParam_height' : [10.0], 
	'float __lightFilterParentParam_radius' : [10.0], 
	'string notes' : [''], 
	'string map' : ['ratGrid.tex'], 
	'int premultipliedAlpha' : [1], 
	'int refreshMap' : [0], 
	'color fillColor' : [1.0,1.0,1.0], 
	'float width' : [1.0], 
	'float height' : [1.0], 
	'float density' : [1], 
	'int invert' : [0], 
	'float intensity' : [1.0], 
	'float diffuse' : [1.0], 
	'float specular' : [1.0], 
	'int tileMode' : [0], 
	'float scaleU' : [1.0], 
	'float scaleV' : [1.0], 
	'float offsetU' : [0.0], 
	'float offsetV' : [0.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrBlockerLightFilter 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
LightFilter "PxrBlockerLightFilter" "id" 
	"string combineMode"  ['mult'] 
	"string coordsys"  [''] 
	"string notes"  [''] 
	"float width"  [0.0] 
	"float height"  [0.0] 
	"float depth"  [0.0] 
	"float radius"  [1.0] 
	"float edge"  [0.25] 
	"float density"  [1.0] 
	"int invert"  [0] 
	"float intensity"  [0.0] 
	"float diffuse"  [1.0] 
	"float specular"  [1.0] 
	"float saturation"  [1.0] 
	"int falloff"  [6] 
	"float falloff_Knots"  [0 0 0.3 0.7 1 1 1 1 1 1 1 1 1 1 1 1] 
	"float falloff_Floats"  [0 0 0.2 0.8 1 1 1 1 1 1 1 1 1 1 1 1] 
	"string falloff_Interpolation"  ['bspline'] 
	"int colorRamp"  [4] 
	"float colorRamp_Knots"  [0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1] 
	"color colorRamp_Colors"  [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1] 
	"string colorRamp_Interpolation"  ['linear'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.LightFilter('PxrBlockerLightFilter','id',
{
	'string combineMode' : ['mult'], 
	'string coordsys' : [''], 
	'string notes' : [''], 
	'float width' : [0.0], 
	'float height' : [0.0], 
	'float depth' : [0.0], 
	'float radius' : [1.0], 
	'float edge' : [0.25], 
	'float density' : [1.0], 
	'int invert' : [0], 
	'float intensity' : [0.0], 
	'float diffuse' : [1.0], 
	'float specular' : [1.0], 
	'float saturation' : [1.0], 
	'int falloff' : [6], 
	'float falloff_Knots' : [0,0,0.3,0.7,1,1,1,1,1,1,1,1,1,1,1,1], 
	'float falloff_Floats' : [0,0,0.2,0.8,1,1,1,1,1,1,1,1,1,1,1,1], 
	'string falloff_Interpolation' : ['bspline'], 
	'int colorRamp' : [4], 
	'float colorRamp_Knots' : [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
	'color colorRamp_Colors' : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
	'string colorRamp_Interpolation' : ['linear'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrCookieLightFilter 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
LightFilter "PxrCookieLightFilter" "id" 
	"int cookieMode"  [0] 
	"string combineMode"  ['mult'] 
	"string coordsys"  [''] 
	"string __lightFilterParentShader"  [''] 
	"string linkingGroups"  [''] 
	"string notes"  [''] 
	"string map"  ['ratGrid.tex'] 
	"int refreshMap"  [0] 
	"color fillColor"  [1.0 1.0 1.0] 
	"int useAlpha"  [1] 
	"int premultipliedAlpha"  [1] 
	"float width"  [1.0] 
	"float height"  [1.0] 
	"float density"  [1] 
	"int invert"  [0] 
	"float intensity"  [1.0] 
	"float diffuse"  [1.0] 
	"float specular"  [1.0] 
	"int directional"  [0] 
	"float shearX"  [0] 
	"float shearY"  [0] 
	"float apex"  [25] 
	"int useLightDirection"  [0] 
	"int tileMode"  [0] 
	"int invertU"  [0] 
	"int invertV"  [0] 
	"float scaleU"  [1.0] 
	"float scaleV"  [1.0] 
	"float offsetU"  [0.0] 
	"float offsetV"  [0.0] 
	"float blur"  [0.0] 
	"float sBlurMult"  [1.0] 
	"float tBlurMult"  [1.0] 
	"float blurNearDist"  [0.0] 
	"float blurMidpoint"  [0.5] 
	"float blurFarDist"  [10.0] 
	"float blurNearVal"  [1.0] 
	"float blurMidVal"  [1.0] 
	"float blurFarVal"  [1.0] 
	"float blurPow"  [1.0] 
	"float densityNearDist"  [0.0] 
	"float densityMidpoint"  [0.5] 
	"float densityFarDist"  [10.0] 
	"float densityNearVal"  [1.0] 
	"float densityMidVal"  [1.0] 
	"float densityFarVal"  [1.0] 
	"float densityPow"  [1.0] 
	"float saturation"  [1.0] 
	"float midpoint"  [0.18] 
	"float contrast"  [1.0] 
	"float whitepoint"  [1.0] 
	"color tint"  [1.0 1.0 1.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.LightFilter('PxrCookieLightFilter','id',
{
	'int cookieMode' : [0], 
	'string combineMode' : ['mult'], 
	'string coordsys' : [''], 
	'string __lightFilterParentShader' : [''], 
	'string linkingGroups' : [''], 
	'string notes' : [''], 
	'string map' : ['ratGrid.tex'], 
	'int refreshMap' : [0], 
	'color fillColor' : [1.0,1.0,1.0], 
	'int useAlpha' : [1], 
	'int premultipliedAlpha' : [1], 
	'float width' : [1.0], 
	'float height' : [1.0], 
	'float density' : [1], 
	'int invert' : [0], 
	'float intensity' : [1.0], 
	'float diffuse' : [1.0], 
	'float specular' : [1.0], 
	'int directional' : [0], 
	'float shearX' : [0], 
	'float shearY' : [0], 
	'float apex' : [25], 
	'int useLightDirection' : [0], 
	'int tileMode' : [0], 
	'int invertU' : [0], 
	'int invertV' : [0], 
	'float scaleU' : [1.0], 
	'float scaleV' : [1.0], 
	'float offsetU' : [0.0], 
	'float offsetV' : [0.0], 
	'float blur' : [0.0], 
	'float sBlurMult' : [1.0], 
	'float tBlurMult' : [1.0], 
	'float blurNearDist' : [0.0], 
	'float blurMidpoint' : [0.5], 
	'float blurFarDist' : [10.0], 
	'float blurNearVal' : [1.0], 
	'float blurMidVal' : [1.0], 
	'float blurFarVal' : [1.0], 
	'float blurPow' : [1.0], 
	'float densityNearDist' : [0.0], 
	'float densityMidpoint' : [0.5], 
	'float densityFarDist' : [10.0], 
	'float densityNearVal' : [1.0], 
	'float densityMidVal' : [1.0], 
	'float densityFarVal' : [1.0], 
	'float densityPow' : [1.0], 
	'float saturation' : [1.0], 
	'float midpoint' : [0.18], 
	'float contrast' : [1.0], 
	'float whitepoint' : [1.0], 
	'color tint' : [1.0,1.0,1.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrRodLightFilter 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
LightFilter "PxrRodLightFilter" "id" 
	"string combineMode"  ['mult'] 
	"string coordsys"  [''] 
	"string linkingGroups"  [''] 
	"string notes"  [''] 
	"float width"  [0.0] 
	"float height"  [0.0] 
	"float depth"  [0.0] 
	"float radius"  [1.0] 
	"float edge"  [0.25] 
	"float density"  [1.0] 
	"int invert"  [0] 
	"float intensity"  [0.0] 
	"float diffuse"  [1.0] 
	"float specular"  [1.0] 
	"float saturation"  [1.0] 
	"int falloff"  [6] 
	"float falloff_Knots"  [0 0 0.3 0.7 1 1 1 1 1 1 1 1 1 1 1 1] 
	"float falloff_Floats"  [0 0 0.2 0.8 1 1 1 1 1 1 1 1 1 1 1 1] 
	"string falloff_Interpolation"  ['bspline'] 
	"int colorRamp"  [4] 
	"float colorRamp_Knots"  [0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1] 
	"color colorRamp_Colors"  [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1] 
	"string colorRamp_Interpolation"  ['linear'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.LightFilter('PxrRodLightFilter','id',
{
	'string combineMode' : ['mult'], 
	'string coordsys' : [''], 
	'string linkingGroups' : [''], 
	'string notes' : [''], 
	'float width' : [0.0], 
	'float height' : [0.0], 
	'float depth' : [0.0], 
	'float radius' : [1.0], 
	'float edge' : [0.25], 
	'float density' : [1.0], 
	'int invert' : [0], 
	'float intensity' : [0.0], 
	'float diffuse' : [1.0], 
	'float specular' : [1.0], 
	'float saturation' : [1.0], 
	'int falloff' : [6], 
	'float falloff_Knots' : [0,0,0.3,0.7,1,1,1,1,1,1,1,1,1,1,1,1], 
	'float falloff_Floats' : [0,0,0.2,0.8,1,1,1,1,1,1,1,1,1,1,1,1], 
	'string falloff_Interpolation' : ['bspline'], 
	'int colorRamp' : [4], 
	'float colorRamp_Knots' : [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
	'color colorRamp_Colors' : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
	'string colorRamp_Interpolation' : ['linear'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrBarnLightFilter 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
LightFilter "PxrBarnLightFilter" "id" 
	"int barnMode"  [0] 
	"string combineMode"  ['mult'] 
	"string coordsys"  [''] 
	"string __lightFilterParentShader"  [''] 
	"string linkingGroups"  [''] 
	"string notes"  [''] 
	"int directional"  [0] 
	"float shearX"  [0] 
	"float shearY"  [0] 
	"float apex"  [25] 
	"int useLightDirection"  [0] 
	"float width"  [1.0] 
	"float height"  [1.0] 
	"float radius"  [0.5] 
	"float edge"  [0.0] 
	"int preBarn"  [2] 
	"float density"  [1.0] 
	"int invert"  [0] 
	"float intensity"  [0.0] 
	"float diffuse"  [1.0] 
	"float specular"  [1.0] 
	"float densityNear"  [0.0] 
	"float densityFar"  [10.0] 
	"float densityNearVal"  [1.0] 
	"float densityFarVal"  [1.0] 
	"float densityPow"  [1.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.LightFilter('PxrBarnLightFilter','id',
{
	'int barnMode' : [0], 
	'string combineMode' : ['mult'], 
	'string coordsys' : [''], 
	'string __lightFilterParentShader' : [''], 
	'string linkingGroups' : [''], 
	'string notes' : [''], 
	'int directional' : [0], 
	'float shearX' : [0], 
	'float shearY' : [0], 
	'float apex' : [25], 
	'int useLightDirection' : [0], 
	'float width' : [1.0], 
	'float height' : [1.0], 
	'float radius' : [0.5], 
	'float edge' : [0.0], 
	'int preBarn' : [2], 
	'float density' : [1.0], 
	'int invert' : [0], 
	'float intensity' : [0.0], 
	'float diffuse' : [1.0], 
	'float specular' : [1.0], 
	'float densityNear' : [0.0], 
	'float densityFar' : [10.0], 
	'float densityNearVal' : [1.0], 
	'float densityFarVal' : [1.0], 
	'float densityPow' : [1.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrRampLightFilter 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
LightFilter "PxrRampLightFilter" "id" 
	"string coordsys"  [''] 
	"string combineMode"  ['mult'] 
	"string linkingGroups"  [''] 
	"string notes"  [''] 
	"int rampType"  [0] 
	"float beginDist"  [0.0] 
	"float endDist"  [10.0] 
	"int ramp"  [4] 
	"float ramp_Knots"  [0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1] 
	"float ramp_Floats"  [0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1] 
	"string ramp_Interpolation"  ['linear'] 
	"float density"  [1.0] 
	"int invert"  [0] 
	"float intensity"  [1.0] 
	"float diffuse"  [1.0] 
	"float specular"  [1.0] 
	"int colorRamp"  [4] 
	"float colorRamp_Knots"  [0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1] 
	"color colorRamp_Colors"  [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1] 
	"string colorRamp_Interpolation"  ['linear'] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.LightFilter('PxrRampLightFilter','id',
{
	'string coordsys' : [''], 
	'string combineMode' : ['mult'], 
	'string linkingGroups' : [''], 
	'string notes' : [''], 
	'int rampType' : [0], 
	'float beginDist' : [0.0], 
	'float endDist' : [10.0], 
	'int ramp' : [4], 
	'float ramp_Knots' : [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
	'float ramp_Floats' : [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
	'string ramp_Interpolation' : ['linear'], 
	'float density' : [1.0], 
	'int invert' : [0], 
	'float intensity' : [1.0], 
	'float diffuse' : [1.0], 
	'float specular' : [1.0], 
	'int colorRamp' : [4], 
	'float colorRamp_Knots' : [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
	'color colorRamp_Colors' : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
	'string colorRamp_Interpolation' : ['linear'], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrIntMultLightFilter 

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
LightFilter "PxrIntMultLightFilter" "id" 
	"string combineMode"  ['mult'] 
	"string linkingGroups"  [''] 
	"string notes"  [''] 
	"float intensity"  [1.0] 
	"float exposure"  [0.0] 
	"int invert"  [0] 
	"float diffuse"  [1.0] 
	"float specular"  [1.0] 
	"float saturation"  [1.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.LightFilter('PxrIntMultLightFilter','id',
{
	'string combineMode' : ['mult'], 
	'string linkingGroups' : [''], 
	'string notes' : [''], 
	'float intensity' : [1.0], 
	'float exposure' : [0.0], 
	'int invert' : [0], 
	'float diffuse' : [1.0], 
	'float specular' : [1.0], 
	'float saturation' : [1.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Projection
## Plugin PxrCylinderCamera 
A simple camera model that projects through a section of a cylinder
    from the point at the cylinder's center.  For very wide aspect images,
    this may be useful for rendering a circular panorama.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Projection "PxrCylinderCamera" "id" 
	"float hsweep"  [360.0] 
	"float vsweep"  [90.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Projection('PxrCylinderCamera','id',
{
	'float hsweep' : [360.0], 
	'float vsweep' : [90.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrCamera 
A camera model that approximates a number of real world physical
    effects.  This supports all of the traditional prman perspective camera
    settings including shaped motion blur and bokeh.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Projection "PxrCamera" "id" 
	"float fov"  [90.0] 
	"float fovEnd"  [0.0] 
	"float fStop"  [16] 
	"float focalLength"  [0.0] 
	"float focalDistance"  [1.0] 
	"float tilt"  [0.0] 
	"float roll"  [0.0] 
	"point focus1"  [0.0 0.0 0.0] 
	"point focus2"  [0.0 0.0 0.0] 
	"point focus3"  [0.0 0.0 0.0] 
	"float shiftX"  [0.0] 
	"float shiftY"  [0.0] 
	"float radial1"  [0.0] 
	"float radial2"  [0.0] 
	"float assymX"  [0.0] 
	"float assymY"  [0.0] 
	"float squeeze"  [1.0] 
	"color transverse"  [1.0 1.0 1.0] 
	"color axial"  [0.0 0.0 0.0] 
	"float natural"  [0.0] 
	"float optical"  [0.0] 
	"string sweep"  ['down'] 
	"float duration"  [1.0] 
	"float detail"  [0.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Projection('PxrCamera','id',
{
	'float fov' : [90.0], 
	'float fovEnd' : [0.0], 
	'float fStop' : [16], 
	'float focalLength' : [0.0], 
	'float focalDistance' : [1.0], 
	'float tilt' : [0.0], 
	'float roll' : [0.0], 
	'point focus1' : [0.0,0.0,0.0], 
	'point focus2' : [0.0,0.0,0.0], 
	'point focus3' : [0.0,0.0,0.0], 
	'float shiftX' : [0.0], 
	'float shiftY' : [0.0], 
	'float radial1' : [0.0], 
	'float radial2' : [0.0], 
	'float assymX' : [0.0], 
	'float assymY' : [0.0], 
	'float squeeze' : [1.0], 
	'color transverse' : [1.0,1.0,1.0], 
	'color axial' : [0.0,0.0,0.0], 
	'float natural' : [0.0], 
	'float optical' : [0.0], 
	'string sweep' : ['down'], 
	'float duration' : [1.0], 
	'float detail' : [0.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrLightProbe 
A simple camera model that renders an image as though photographing a
    perfectly specular mirrored ball.  Note that the view direction is
    flipped and the image mirrored compared to a real ball so that the
    orientation appears similar to other projections.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Projection "PxrLightProbe" "id" 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Projection('PxrLightProbe','id',
{
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrPerspective 
A simple pinhole camera.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Projection "PxrPerspective" "id" 
	"float fov"  [90.0] 
	"float fStop"  [16] 
	"float focalLength"  [0.0] 
	"float focalDistance"  [1.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Projection('PxrPerspective','id',
{
	'float fov' : [90.0], 
	'float fStop' : [16], 
	'float focalLength' : [0.0], 
	'float focalDistance' : [1.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrOrthographic 
A simple parallel projection camera.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Projection "PxrOrthographic" "id" 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Projection('PxrOrthographic','id',
{
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin OmnidirectionalStereo 
This camera projection renders the scene as a stereo pair of 360 degree
        projections. It is intended to be rendered in a square format with 
        the top half as the left eye and the bottom half as the right eye.

        Author: Mach Kobayashi

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Projection "OmnidirectionalStereo" "id" 
	"float interpupilaryDistance"  [0.0635] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Projection('OmnidirectionalStereo','id',
{
	'float interpupilaryDistance' : [0.0635], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrPanini 
The Panini projection is designed for producing ultra-wide angle images
    with large fields of view.  It can be particularly effective for
    architectural scenes.  Like the traditional rectilinear perspective
    projection, vertical lines remain vertical when the view direction is
    horizontal, and radial lines that converge towards the vanishing point
    also remain straight.  However, it can do this while accommodating wide
    angles up to 180 degrees and beyond.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Projection "PxrPanini" "id" 
	"float fov"  [90.0] 
	"float compression"  [1.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Projection('PxrPanini','id',
{
	'float fov' : [90.0], 
	'float compression' : [1.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Plugin PxrSphereCamera 
A simple camera model that projects through a section of a sphere from
    the point at the sphere's center.  With its default settings, this may
    be useful for rendering a latlong environment map.

### Rib Format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C
Projection "PxrSphereCamera" "id" 
	"float hsweep"  [360.0] 
	"float vsweep"  [180.0] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Python Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python

ri.Projection('PxrSphereCamera','id',
{
	'float hsweep' : [360.0], 
	'float vsweep' : [180.0], 
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
