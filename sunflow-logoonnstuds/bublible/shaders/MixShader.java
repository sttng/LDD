package bublible.shaders;

import org.sunflow.core.shader.ConstantShader;
import bublible.Utils;
import java.util.Arrays;
import org.sunflow.SunflowAPI;
import org.sunflow.core.ParameterList;
import org.sunflow.core.Shader;
import org.sunflow.core.ShadingState;
import org.sunflow.core.shader.AmbientOcclusionShader;
import org.sunflow.core.shader.AnisotropicWardShader;
import org.sunflow.core.shader.DiffuseShader;
import org.sunflow.core.shader.GlassShader;
import org.sunflow.core.shader.MirrorShader;
import org.sunflow.core.shader.PhongShader;
import org.sunflow.core.shader.ShinyDiffuseShader;
import org.sunflow.image.Color;

//
public final class MixShader implements Shader {

    // GLASS NEEDS TO BE ALWAYS DEFFINED FIRST ELSE IT WON'T WORK AT ALL!!!!!
    boolean b1, b2, ok = false;
    Color c1, c2;
    String s1, s2;
    float ratio;

    private final String n1 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
    private final String n2 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
    Shader $n1, $n2;

    public boolean update(ParameterList pl, SunflowAPI api) {
        if (!ok) {

            // one shot
            ok = true;

            s1 = pl.getString("shader1", s1);
            c1 = pl.getColor("color1", c1);
            s2 = pl.getString("shader2", s2);
            c2 = pl.getColor("color2", c2);
            ratio = pl.getFloat("ratio", ratio);
            pl.clear(true);

            switch (s1) {
                case "diffuse":
                    // DIFFUSE
                    String nD = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    DiffuseShader $nD = new DiffuseShader();
                    api.parameter("diffuse", c1);
                    b1 = $nD.update(pl, api);
                    $n1 = $nD;
                    break;
                case "shiny":
                    // SHINY
                    String nS = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    ShinyDiffuseShader $nS = new ShinyDiffuseShader();
                    api.parameter("diffuse", c1);
                    api.parameter("reflection", 0.05f);
                    b1 = $nS.update(pl, api);
                    $n1 = $nS;
                    break;
                case "plastic":
                    // PLASTIC
                    String nP = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    PlasticShader $nP = new PlasticShader();
                    api.parameter("color", c1);
                    b1 = $nP.update(pl, api);
                    $n1 = $nP;
                    break;
                case "trans":
                    // TRANSPARENT
                    String nT = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    GlassShader $nT = new GlassShader();
                    api.parameter("color", c1);
                    api.parameter("eta", 1.6f);
                    b1 = $nT.update(pl, api);
                    $n1 = $nT;
                    break;
                case "glass":
                    // GLASS
                    String nG = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    GlassShader $nG = new GlassShader();
                    api.parameter("color", c1);
                    api.parameter("eta", 1.6f);
                    api.parameter("absorbtion.distance", 100f);
                    api.parameter("absorbtion.color", c1);
                    b1 = $nG.update(pl, api);
                    $n1 = $nG;
                    break;
                case "pearl":
                    // PEARL
                    String nPRL = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    PearlShader $nPRL = new PearlShader();
                    api.parameter("color", c1);
                    b1 = $nPRL.update(pl, api);
                    $n1 = $nPRL;
                    break;
                case "phong":
                    // PHONG
                    String nQ = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    PhongShader $nQ = new PhongShader();
                    api.parameter("diffuse", c1);
                    api.parameter("specular", c1);
                    api.parameter("power", 300f);
                    api.parameter("samples", 10);
                    b1 = $nQ.update(pl, api);
                    $n1 = $nQ;
                    break;
                case "metallic":
                    // ANISOTROPIC
                    String nA = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    AnisotropicWardShader $nA = new AnisotropicWardShader();
                    api.parameter("diffuse", c1);
                    api.parameter("specular", Color.WHITE);
                    api.parameter("roughnessX", 0.05f);
                    api.parameter("roughnessY", 0.05f);
                    api.parameter("samples", 1);
                    b1 = $nA.update(pl, api);
                    $n1 = $nA;
                    break;
                case "mirror":
                    // MIRROR
                    String nM = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    MirrorShader $nM = new MirrorShader();
                    api.parameter("color", c1);
                    b1 = $nM.update(pl, api);
                    $n1 = $nM;
                    break;
                case "stainedmirror":
                    // STAINED MIRROR
                    String nBM = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    StainedMirrorShader $nBM = new StainedMirrorShader();
                    api.parameter("color", c1);
                    b1 = $nBM.update(pl, api);
                    $n1 = $nBM;
                    break;
                case "ambient":
                    // AMBIENT OCCLUSION MIRROR
                    String nAO = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    AmbientOcclusionShader $nAO = new AmbientOcclusionShader();
                    api.parameter("bright", c1);
                    api.parameter("dark", new Color(0f, 0f, 0f));
                    api.parameter("samples", 4);
                    api.parameter("maxdist", 1000.0f);
                    b1 = $nAO.update(pl, api);
                    $n1 = $nAO;
                    break;
                case "constant":
                default:
                    // CONSTANT
                    String nC = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    ConstantShader $nC = new ConstantShader();
                    api.parameter("color", c1);
                    b1 = $nC.update(pl, api);
                    $n1 = $nC;
                    break;
            }
            pl.clear(true);

            switch (s2) {
                case "diffuse":
                    // DIFFUSE
                    String nD = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    DiffuseShader $nD = new DiffuseShader();
                    api.parameter("diffuse", c2);
                    b2 = $nD.update(pl, api);
                    $n2 = $nD;
                    break;
                case "shiny":
                    // SHINY
                    String nS = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    ShinyDiffuseShader $nS = new ShinyDiffuseShader();
                    api.parameter("diffuse", c2);
                    api.parameter("reflection", 0.05f);
                    b2 = $nS.update(pl, api);
                    $n2 = $nS;
                    break;
                case "plastic":
                    // PLASTIC
                    String nP = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    PlasticShader $nP = new PlasticShader();
                    api.parameter("color", c2);
                    b2 = $nP.update(pl, api);
                    $n2 = $nP;
                    break;
                case "trans":
                    // TRANSPARENT
                    String nT = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    GlassShader $nT = new GlassShader();
                    api.parameter("color", c2);
                    api.parameter("eta", 1.6f);
                    b2 = $nT.update(pl, api);
                    $n2 = $nT;
                    break;
                case "glass":
                    // GLASS
                    String nG = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    GlassShader $nG = new GlassShader();
                    api.parameter("color", c2);
                    api.parameter("eta", 1.6f);
                    api.parameter("absorbtion.distance", 100f);
                    api.parameter("absorbtion.color", c2);
                    b2 = $nG.update(pl, api);
                    $n2 = $nG;
                    break;
                case "pearl":
                    // PEARL
                    String nPRL = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    PearlShader $nPRL = new PearlShader();
                    api.parameter("color", c1);
                    b2 = $nPRL.update(pl, api);
                    $n2 = $nPRL;
                    break;
                case "phong":
                    // PHONG
                    String nQ = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    PhongShader $nQ = new PhongShader();
                    api.parameter("diffuse", c1);
                    api.parameter("specular", c1);
                    api.parameter("power", 300f);
                    api.parameter("samples", 10);
                    b2 = $nQ.update(pl, api);
                    $n2 = $nQ;
                    break;
                case "metallic":
                    // ANISOTROPIC
                    String nA = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    AnisotropicWardShader $nA = new AnisotropicWardShader();
                    api.parameter("diffuse", c2);
                    api.parameter("specular", Color.WHITE);
                    api.parameter("roughnessX", 0.05f);
                    api.parameter("roughnessY", 0.05f);
                    api.parameter("samples", 1);
                    b2 = $nA.update(pl, api);
                    $n2 = $nA;
                    break;
                case "mirror":
                    // MIRROR
                    String nM = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    MirrorShader $nM = new MirrorShader();
                    api.parameter("color", c2);
                    b2 = $nM.update(pl, api);
                    $n2 = $nM;
                    break;
                case "stainedmirror":
                    // STAINED MIRROR
                    String nBM = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    StainedMirrorShader $nBM = new StainedMirrorShader();
                    api.parameter("color", c2);
                    b2 = $nBM.update(pl, api);
                    $n2 = $nBM;
                    break;
                case "ambient":
                    // AMBIENT OCCLUSION MIRROR
                    String nAO = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    AmbientOcclusionShader $nAO = new AmbientOcclusionShader();
                    api.parameter("bright", c2);
                    api.parameter("dark", new Color(0f, 0f, 0f));
                    api.parameter("samples", 4);
                    api.parameter("maxdist", 1000.0f);
                    b2 = $nAO.update(pl, api);
                    $n2 = $nAO;
                    break;
                case "constant":
                default:
                    // CONSTANT
                    String nC = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    ConstantShader $nC = new ConstantShader();
                    api.parameter("color", c2);
                    b2 = $nC.update(pl, api);
                    $n2 = $nC;
                    break;
            }
            pl.clear(true);

            return (b1 && b2);
        }
        return true;
    }

    public Color getMaterialColor() {
        return Color.blend(c1, c2, ratio);
    }

    public Color getRadiance(ShadingState state) {

        Color sA = $n1.getRadiance(state);
        Color sB = $n2.getRadiance(state);
        
        //return Color.blend(sA, sB, ratio);

        if (ratio == 0f) {
            //System.out.println("---------------------> SHADER1 ONLY = " + Arrays.toString(sB.getRGB()));
            return sA;
        } else if (ratio >= 1f) {
            //System.out.println("---------------------> SHADER2 ONLY = " + Arrays.toString(sB.getRGB()));
            return sB;
        } else if (Arrays.equals(c1.getRGB(), c2.getRGB()) && $n1.getClass().equals($n2.getClass())) {
            //System.out.println("---------------------> SAME SHADER AND COLOR");
            return sA;
        } else {
            //System.out.println("---------------------> MIX");
            return Color.blend(sA, sB, ratio);
        }
    }

    @Override
    public void scatterPhoton(ShadingState state, Color power) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public float getReflectionValue() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
