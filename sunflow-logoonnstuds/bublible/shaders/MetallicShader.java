package bublible.shaders;

import bublible.Utils;
import org.sunflow.SunflowAPI;
import org.sunflow.core.ParameterList;
import org.sunflow.core.Shader;
import org.sunflow.core.ShadingState;
import org.sunflow.core.shader.AnisotropicWardShader;
import org.sunflow.image.Color;

public final class MetallicShader implements Shader {

    boolean b1, ok = false;
    Color c;
    
    private final String n1 = "n" + Utils.rndRng(0,100) + Utils.rndRng(0,100) + Utils.rndRng(0,100);
    final AnisotropicWardShader $n1 = new AnisotropicWardShader();

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
            api.parameter( "specular", Color.WHITE );
            api.parameter( "roughnessX",  0.5f );
            api.parameter( "roughnessY",  0.01f );
            api.parameter( "samples", 4 );
            b1 = $n1.update(pl, api);
            pl.clear(true);

            return (b1);
        }
        return true;
    }

    public Color getMaterialColor() {
        return c;
    }

    public Color getRadiance(ShadingState state) {
        return $n1.getRadiance(state).mul(1.5f).clamp(0f, 1f);
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
