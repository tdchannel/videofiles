surface stripe(
                float fuzzy = 0.1;
              )
{
	color lc = color (1,0,0);
	color sc = color (0,1,0);
    float halfFuzz = fuzzy * 0.5;
	float lo = smoothstep(0.4 - halfFuzz,0.4 + halfFuzz,s) - 
               smoothstep(0.6 - halfFuzz,0.6 + halfFuzz,s);

    float loh = smoothstep(0.4 - halfFuzz,0.4 + halfFuzz,t) - 
                smoothstep(0.6 - halfFuzz,0.6 + halfFuzz,t);
	
    lo = clamp(lo + loh ,0,1);
    
    Oi = Os;
    Ci = Oi * mix(sc,lc,lo);
}
