import 'dart:convert';

class Dependente {
  late String _nome;

  Dependente(String nome) {
    this._nome = nome;
  }

  Map <String, dynamic> toJson(){
    return {
      'nome': _nome,
    };
  }
  
}

class Funcionario {
  late String _nome;
  late List<Dependente> _dependentes;

  Funcionario(String nome, List<Dependente> dependentes) {
    this._nome = nome;
    this._dependentes = dependentes;
  }

  Map <String, dynamic> toJson(){
    return {
      'nome': _nome,
      'dependente': _dependentes.map((depen) => depen.toJson()).toList(),
    };
  }
}

class EquipeProjeto {
  late String _nomeProjeto;
  late List<Funcionario> _funcionarios;

  EquipeProjeto(String nomeprojeto, List<Funcionario> funcionarios) {
    _nomeProjeto = nomeprojeto;
    _funcionarios = funcionarios;
  }

  Map <String, dynamic> toJson(){
    return {
      'nome do projeto': _nomeProjeto,
      'funcionários': _funcionarios.map((func) => func.toJson()).toList(),
    };
  }
}

void main() {
  // 1. Criar varios objetos Dependentes
  Dependente dp1 = Dependente("Allan");
  Dependente dp2 = Dependente("Abner");
  Dependente dp3 = Dependente("Camila");
  Dependente dp4 = Dependente("Denise");
  Dependente dp5 = Dependente("Wladison");
  
  // 2. Criar varios objetos Funcionario

  Funcionario func1 = Funcionario("Beatriz", [dp1]);
  Funcionario func2 = Funcionario("Duda", [dp2]);
  Funcionario func3 = Funcionario("Mirela", [dp3]);
  Funcionario func4 = Funcionario("Matheus", [dp4]);
  Funcionario func5 = Funcionario("Victor", [dp5]);
  // 3. Associar os Dependentes criados aos respectivos funcionarios
  
  // Isso foi realizado na etapa anterior.
  
  // 4. Criar uma lista de Funcionarios
  List <Funcionario> listFunc = [func1, func2, func3, func4, func5];
  
  // 5. criar um objeto Equipe Projeto chamando o metodo contrutor que da nome ao projeto e insere uma coleção de funcionario
  EquipeProjeto eqp = EquipeProjeto("Projeto Tecno", listFunc);
  
  // 6. Printar no formato JSON o objeto Equipe Projeto.
  print(jsonEncode(eqp.toJson()));
}
