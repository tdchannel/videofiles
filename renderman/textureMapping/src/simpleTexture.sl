/*
<meta id="slim"><![CDATA [
slim 2 appearance slim {
    instance surface simpleTexture simpleTexture {
        parameter float Kd {
            label "Diffuse"
            default 0.8
            range {0 10 0.01}
        }
        parameter color surfaceColor {
            label "Diffuse Color"
            default { 0.5 0.5 0.5 }
        }
        parameter string map {
            label "Texture Map"
            description "Choose a tx file"
            subtype texture
            default ""
        }
        parameter float useAlpha {
            subtype switch
            default 1
        }
        parameter float flipS {
            label "Flip S"
            subtype switch
            default 0
        }
        parameter float flipT {
            label "Flip T"
            subtype switch
            default 0
        }
    }
}
]]></meta>
*/
surface simpleTexture(
                        float Kd = 0.8;
                        color surfaceColor = color(0.5);
                        string map = "";
                        uniform float useAlpha = 1;
                        uniform float flipS = 0;
                        uniform float flipT = 0;
                     )
{
    // local variables
    normal Nn = normalize(N);
    color sc = surfaceColor;
    color lc = color(0);

    if (map != "") {
        float ss = flipS == 1 ? 1 - s : s;
        float tt = flipT == 1 ? 1 - t : t;

        lc = color texture(map,ss,tt);

        if (useAlpha == 1) {
            uniform float numChannels = 0;
            textureinfo(map,"channels",numChannels);

            if (numChannels == 4 ) {
                sc = mix (sc,lc,float texture(map[3],ss,tt));
            } else {
                sc = lc;
            }
        } else {
            sc = lc;
        }
    }
    
	Oi = Os;
	Ci = Oi * (sc * diffuse(Nn) * Kd);
}
