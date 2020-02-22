package bluerender.customshaders;

import bublible.Utils;
import org.sunflow.SunflowAPI;
import org.sunflow.core.ParameterList;
import org.sunflow.core.Shader;
import org.sunflow.core.ShadingState;
import org.sunflow.core.shader.AmbientOcclusionShader;
import org.sunflow.core.shader.GlassShader;
import org.sunflow.core.shader.ShinyDiffuseShader;
import org.sunflow.image.Color;

// mat329
public final class WhiteGlowORIGINAL implements Shader {

    // GLASS NEEDS TO BE ALWAYS DEFFINED FIRST ELSE IT WON'T WORK AT ALL!!!!!
    boolean b1, b2, b3, ok = false;
    Color c = new Color(0.99f, 0.99f, 0.99f);
    
    private final String n1 = "n" + Utils.rndRng(0,100) + Utils.rndRng(0,100) + Utils.rndRng(0,100);
    final GlassShader $n1 = new GlassShader();
    private final String n2 = "n" + Utils.rndRng(0,100) + Utils.rndRng(0,100) + Utils.rndRng(0,100);
    final ShinyDiffuseShader $n2 = new ShinyDiffuseShader();
    private final String n3 = "n" + Utils.rndRng(0,100) + Utils.rndRng(0,100) + Utils.rndRng(0,100);
    final AmbientOcclusionShader $n3 = new AmbientOcclusionShader();

    public boolean update(ParameterList pl, SunflowAPI api) {
        if (!ok) {

            // one shot
            ok = true;

            // GLASS
            api.parameter("color", new Color(0.99f, 0.99f, 0.99f));
            api.parameter("eta", 1.6f);
            api.parameter("absorbtion.distance", 0.05f);
            api.parameter("absorbtion.color", new Color(0.99f, 0.99f, 0.99f));
            b1 = $n1.update(pl, api);
            pl.clear(true);

            // SHINY
            api.parameter("diffuse", new Color(0.99f, 0.99f, 0.99f));
            api.parameter("reflection", 0.0f);
            b2 = $n2.update(pl, api);
            pl.clear(true);

            // AMBIENT OCCLUSION
            api.parameter("bright", new Color(0.99f, 0.99f, 0.99f));
            api.parameter("dark", new Color(0f, 0.5f, 0f));
            api.parameter("samples", 128);
            api.parameter("maxdist", 0.2f);
            b3 = $n3.update(pl, api);
            pl.clear(true);

            return (b1 && b2 && b3);
        }
        return true;
    }

    public Color getMaterialColor() {
        return c;
    }

    public Color getRadiance(ShadingState state) {
        Color g = $n1.getRadiance(state);
        Color s = $n2.getRadiance(state);
        Color a = $n3.getRadiance(state);
        Color rColor = Color.blend(a, s, 0.7f);
        Color.blend(rColor, g, 0.4f, rColor);
        return rColor;
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
