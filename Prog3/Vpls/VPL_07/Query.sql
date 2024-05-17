/* ################### */

/* Digite aqui seu SQL */

DELETE FROM aluno
WHERE nome = 'Eloisa Oliveira';

INSERT INTO aluno (aluno_key, nome, cidade_key, ingresso, sexo_key)
VALUES (10, 'João da Silva', 3, 2018, 1);

SELECT a.aluno_key, a.nome, a.ingresso, c.nome, s.nome, disciplina.sigla
FROM aluno a
JOIN matricula m ON a.aluno_key = m.aluno_key
JOIN cidade c ON a.cidade_key = c.cidade_key
JOIN sexo s ON a.sexo_key = s.sexo_key
JOIN disciplina ON m.disciplina_key = disciplina.disciplina_key
WHERE a.sexo_key = 1 AND disciplina.sigla = 'MAT-I';

SELECT a.aluno_key, a.nome, a.ingresso, c.nome, s.nome, disciplina.sigla
FROM aluno a
JOIN matricula m ON a.aluno_key = m.aluno_key
JOIN cidade c ON a.cidade_key = c.cidade_key
JOIN sexo s ON a.sexo_key = s.sexo_key
JOIN disciplina ON m.disciplina_key = disciplina.disciplina_key
WHERE s.nome = 'Masculino' AND a.cidade_key = 2 AND disciplina.sigla = 'DAD-I';


/* ################### */
