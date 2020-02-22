package bublible.shaders;

import org.sunflow.SunflowAPI;
import org.sunflow.core.ParameterList;
import org.sunflow.core.Texture;
import org.sunflow.core.TextureCache;
import org.sunflow.core.shader.DiffuseShader;

public class TexturedConstantShader extends DiffuseShader {
    private Texture tex;

    public TexturedConstantShader() {
        tex = null;
    }

    public boolean update(ParameterList pl, SunflowAPI api) {
        String filename = pl.getString("texture", null);
        if (filename != null)
            tex = TextureCache.getTexture(api.resolveTextureFilename(filename), false);
        return tex != null && super.update(pl, api);
    }
}