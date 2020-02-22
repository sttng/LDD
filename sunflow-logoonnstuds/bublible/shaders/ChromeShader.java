package bublible.shaders;

import bublible.Colors;
import bublible.Utils;
import org.sunflow.SunflowAPI;
import org.sunflow.core.ParameterList;
import org.sunflow.core.Shader;
import org.sunflow.core.ShadingState;
import org.sunflow.core.shader.AnisotropicWardShader;
import org.sunflow.core.shader.UberShader;
import org.sunflow.image.Color;

// mat309
public final class ChromeShader implements Shader {

    boolean b1, b2, ok = false;
    Color c;
    
    private final String n1 = "n" + Utils.rndRng(0,100) + Utils.rndRng(0,100) + Utils.rndRng(0,100);
    final AnisotropicWardShader $n1 = new AnisotropicWardShader();
    private final String n2 = "n" + Utils.rndRng(0,100) + Utils.rndRng(0,100) + Utils.rndRng(0,100);
    final UberShader $n2 = new UberShader();

    public boolean update(ParameterList pl, SunflowAPI api)
    {
        if (!ok)
        {
            // one shot
            ok = true;

            c = pl.getColor("color", c);
            pl.clear(true);
            
            // ANISOTROPIC
            api.parameter( "diffuse",  c );
            api.parameter( "specular", Colors.bleech(0.3f, c).clamp(0f, 1f) );
            api.parameter( "roughnessX",  0.05f );
            api.parameter( "roughnessY",  0.01f );
            api.parameter( "samples", 1 );
            b1 = $n1.update(pl, api);
            pl.clear(true);
            
            // UBER
            api.parameter( "diffuse",  c );
            api.parameter( "specular",  Colors.bleech(0.3f, c).clamp(0f, 1f) );
            api.parameter( "glossyness",  0f );
            api.parameter( "samples", 100 );
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
        return Color.blend($n1.getRadiance(state), $n2.getRadiance(state), 0.5f).clamp(0f, 1f);
    }

    @Override
    public void scatterPhoton(ShadingState state, Color power) {
    }

    @Override
    public float getReflectionValue() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}