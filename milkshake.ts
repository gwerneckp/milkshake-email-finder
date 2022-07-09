/*
 * Reimplemented on July 9, 2022
 * Author: Gabriel Paiva
 */

class MailGenerator {
  SEP: Array<string> = ["", ".", "_"];

  nameList: Array<string> = [];
  domainList: Array<string> = [];

  combinedNames: Array<string> = [];
  result: Array<string> = [];

  splitName = (name: string) => {
    name = name.toLowerCase().trim();
    name = name.replace("/ (de|da|do|dos|das ) /", " ");
    let names = name.split(" ");
    return names;
  };

  addName = (name) => {
    this.nameList = this.splitName(name);
  };

  addDomain = (domains) => {
    domains.split(" ").map((domain) => {
      this.domainList.push(domain);
    });
  };

  run = () => {
    this.combineNames();
    this.combineDomains();
  };

  combineDomains = () => {
    for (let i in this.domainList) {
      for (let j in this.combinedNames) {
        // let filteredName = this.combinedNames[j].replace("_", "");
        // filteredName = filteredName.replace(".", "");
        let filteredName = this.combinedNames[j]
        if (filteredName.length <= 3) {
          continue;
        }
        this.result.push(`${filteredName}@${this.domainList[i]}`);
      }
    }
  };

  combineNames = () => {
    let names = this.nameList
    let separators = this.SEP
    let n = names.length
    let combinedNames = []
   
    // Caminhar nos nomes
    for (let i=0;i<n;i++){
        // Tamanho da janela definida pela quantidade de nomes
        for (let t=0;t<=n-i;t++){
            // Percorrer o final dos nomes
            for (let j=i;j<n;j++){ 
                if ((t)>n-j){
                    continue;  
                } 
                // Não repetir o nome sozinho (t=0)
                if (j==i && t>0){
                    continue;
                } 
                  for(let sepI in separators){
                    let separator = separators[sepI]
                      for (let w=0;w<=((t+1)*2)-1;w++){
                        let name
                          // Acumular os nomes	
                          if (w-(t+1)+1<=1 && 1<=w){	   		
                              name=names[i][0];
                          } else {
                              name=names[i];
                          }
                       let name2=name; // Reverte os nomes <sobrenome> <nome>	
                          for(let k=1;k<=t;k++){
                              if (w-(t+1)+1<=k+1 && k+1<=w){
                                  name+=separator+names[j+k-1][0];
                                  name2=names[j+k-1][0]+separator+name2;
                              } else {
                                  name+=separator+names[j+k-1];
                                  name2=names[j+k-1]+separator+name2;
                              }
                          }
                       combinedNames.push(name);
                       if ( name2 != name ){
                           combinedNames.push(name2);
                       }
                      }
                      if (t==0) break;		   		
                  }
                  if (t==0) break;
            }	
        }
    }
    this.combinedNames = combinedNames
    }
  }

const mb = new MailGenerator();
const names = "Sheldon Cooper";
const domains = "caltech.edu";
mb.addName(names);
mb.addDomain(domains);
mb.run()
console.log(mb.result)
