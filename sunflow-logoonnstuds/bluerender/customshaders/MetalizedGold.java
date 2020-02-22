package bluerender.customshaders;

import bublible.Utils;
import org.sunflow.SunflowAPI;
import org.sunflow.core.ParameterList;
import org.sunflow.core.Shader;
import org.sunflow.core.ShadingState;
import org.sunflow.core.shader.GlassShader;
import org.sunflow.core.shader.PhongShader;
import org.sunflow.image.Color;

// mat310
public final class MetalizedGold implements Shader {

    // GLASS NEEDS TO BE ALWAYS DEFFINED FIRST ELSE IT WON'T WORK AT ALL!!!!!
    boolean b1, b2, ok = false;
    Color c = new Color(0.8745098f, 0.75686276f, 0.4627451f);
    
    private final String n1 = "n" + Utils.rndRng(0,100) + Utils.rndRng(0,100) + Utils.rndRng(0,100);
    final GlassShader $n1 = new GlassShader();
    private final String n2 = "n" + Utils.rndRng(0,100) + Utils.rndRng(0,100) + Utils.rndRng(0,100);
    final PhongShader $n2 = new PhongShader();

    public boolean update(ParameterList pl, SunflowAPI api)
    {
        if (!ok)
        {
            // one shot
            ok = true;

            // GLASS
            api.parameter( "color", c );
            api.parameter( "eta", 100.1f );
            api.parameter( "absorbtion.distance", 0.001f );
            api.parameter( "absorbtion.color", new Color(1f, 1f, 1f) );
            b1 = $n1.update(pl, api);
            pl.clear(true);

            // PHONG
            api.parameter( "diffuse",  c );
            api.parameter( "specular",  new Color(0.8f, 0.7f, 0.4f) );
            api.parameter( "power",  50f );
            api.parameter( "samples", 32 );
            b2 = $n2.update(pl, api);
            pl.clear(true);

            return (b1 && b2);
        }
        return true;
    }

    public Color getMaterialColor() {
        return c;
    }

    public Color getRadiance(ShadingState state) {
        Color g = $n1.getRadiance(state);
        Color p = $n2.getRadiance(state);
        Color rColor = Color.blend(g, p, 0.7f);
        return rColor;
    }

    @Override
    public void scatterPhoton(ShadingState state, Color power) {
    }

    @Override
    public float getReflectionValue() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}