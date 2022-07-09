<?php
/*
 * Created on Sep 8, 2005
 * Author: Ricardo Paiva
 */
  
 class MailGenerator {
 	
 	private $listaNomes=array();
 	private $listaDomains=array();
 	private $SEP=array("", ".", "_");
 	
 	private $combNomes=array();
 	public $result=array();
 	 	
 	public function addNome($nome){
		$this->listaNomes[]=self::splitNome($nome); 		
 	}
 	
 	public function addDomain($domain){
		$this->listaDomains[]=$domain;  		
 	}
 	
 	public function run(){
		$this->combinaNomes();
		$this->combinaDomains();
 	}
 	
 	public function combinaDomains(){
 		foreach($this->listaDomains as $domain){
	 		foreach($this->combNomes as $nome){	 				
				$filteredName = str_replace("_", "", $nome);
				$filteredName = str_replace(".", "", $filteredName);
				if (strlen($filteredName) <= 3) continue;
	 			$this->result[]="$nome@$domain";
	 		}
 		}
 	}
 	
	public function combinaNomes(){
	 	foreach($this->listaNomes as $nomes){
	 	 $n=count($nomes);
		
		 // Caminhar nos nomes
		 for ($i=0;$i<$n;$i++){
		 	// Tamanho da janela definida pela quantidade de nomes
		 	for ($t=0;$t<=$n-$i;$t++){
		 		// Percorrer o final dos nomes
		 		for ($j=$i;$j<$n;$j++){ 
		 			if (($t)>$n-$j) continue;
		 			// Não repetir o nome sozinho (t=0)
		 			if ($j==$i && $t>0) continue;
			   		foreach($this->SEP as $sep){
			   			for ($w=0;$w<=(($t+1)*2)-1;$w++){
					   		// Acumular os nomes	
					   		if ($w-($t+1)+1<=1 && 1<=$w){	   		
					   			$nome=$nomes[$i][0];
					   		} else {
					   			$nome=$nomes[$i];
					   		}
							$nome2=$nome; // Reverte os nomes <sobrenome> <nome>	
					   		for($k=1;$k<=$t;$k++){
					   			if ($w-($t+1)+1<=$k+1 && $k+1<=$w){	   		  
				   					$nome.=$sep.$nomes[$j+$k-1][0];
				   					$nome2=$nomes[$j+$k-1][0].$sep.$nome2;
					   			} else {
					   				$nome.=$sep.$nomes[$j+$k-1];
				   					$nome2=$nomes[$j+$k-1].$sep.$nome2;
					   			}
					   		}
							$this->combNomes[]=$nome;
							if ( $nome2 != $nome ){
								$this->combNomes[]=$nome2;
							}
			   			}
				   		if ($t==0) break;		   		
			   		}
			   		if ($t==0) break;
		 		}	
		 	}
		 }
	 	}
	}
 
	private static function splitNome($nome){
		$nome=trim(strtolower($nome));
	 	$nome=preg_replace("/ (de|da|do|dos|das) /", " ", $nome);
	 	$nomes=preg_split("/\s+/", $nome);
	 	return $nomes;
	}
	
 }

$mb=new MailGenerator();
$nomes=array("ricardo luis silva paiva");
$domains=array("fb.com");
foreach($nomes as $nome){
  $mb->addNome($nome);	
} 
foreach($domains as $domain){
  $mb->addDomain($domain);
}
$mb->run();

print_r($mb->result);
?>