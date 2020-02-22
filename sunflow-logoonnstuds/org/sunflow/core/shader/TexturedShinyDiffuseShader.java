package org.sunflow.core.shader;

import org.sunflow.SunflowAPI;
import org.sunflow.core.ParameterList;
import org.sunflow.core.Texture;
import org.sunflow.core.TextureCache;

public class TexturedShinyDiffuseShader extends ShinyDiffuseShader {
    
    private Texture tex;

    public TexturedShinyDiffuseShader() {
        tex = null;
    }

    public boolean update(ParameterList pl, SunflowAPI api) {
        String filename = pl.getString("texture", null);
        if (filename != null)
            tex = TextureCache.getTexture(api.resolveTextureFilename(filename), false);
        return tex != null && super.update(pl, api);
    }
}