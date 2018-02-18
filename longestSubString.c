#include <stdio.h>
#include <string.h>
int lengthOfLongestSubstring(char* s) {
    int len = strlen(s);

    int flag = 1;
    int anslen=0;
    int curlen =0;
    //int matchIndex=0;
    int midlen=0;
    int j=0;
    int matchIndex = -1;
    for(int i=0;i<len;i++){
        if(len==1){
            return len;
        }
        else{
            for(j=matchIndex+1;j<i;j++){
            //printf("%d",j);
                if(s[j]==s[i]){
                    //printf("%d",curlen);
                    //printf("here");
                    //printf("%d",anslen);
                    flag = 0;
                    //midlen=i-j;
                    matchIndex = j;
                    if(anslen==0){
                        //printf("%d",anslen);
                        anslen=curlen;
                        //printf("%d",anslen);
                        curlen=i-j;
                    }
                    if(curlen>anslen){
                        //printf("%d",curlen);
                        anslen=curlen;
                        //printf("----------");
                        //printf("%d",anslen);
                        curlen=i-j;
                    }
                    if(curlen<=anslen){
                        curlen=i-j;
                    }
                    
                    break;
                    
                }
                else{
                    
                }
                
              
            }
            /*if(flag==1){
                anslen = anslen + 1;
                j=0;
            }*/
            
        }
        if(flag==1){
                curlen = curlen + 1;
                //j=0;
        }
        else{
            flag=1;
        }
    }
    if(curlen>anslen){
        anslen=curlen;
        //curlen=i-j;
    }
        return anslen;

}
