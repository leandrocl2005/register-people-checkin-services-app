# Generated by Django 3.1.5 on 2021-05-16 11:29

from django.db import migrations, models
import people.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('mother_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome da mãe')),
                ('born_date', models.DateField(blank=True, help_text='Exemplo: 03/12/2015', null=True, verbose_name='Dt. nascimento')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True, verbose_name='E-mail')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1, null=True, verbose_name='Gênero')),
                ('cpf', models.CharField(blank=True, help_text='Exemplo: 00000000000', max_length=14, null=True, unique=True, validators=[people.validators.check_cpf], verbose_name='CPF')),
                ('rg', models.CharField(blank=True, max_length=14, null=True, verbose_name='RG')),
                ('rg_ssp', models.CharField(blank=True, choices=[('SP', 'São Paulo'), ('PR', 'Paraná'), ('SC', 'Santa Catarina'), ('RS', 'Rio Grande do Sul'), ('MS', 'Mato Grosso do Sul'), ('RO', 'Rondônia'), ('AC', 'Acre'), ('AM', 'Amazonas'), ('RR', 'Roraima'), ('PA', 'Pará'), ('AP', 'Amapá'), ('TO', 'Tocantins'), ('MA', 'Maranhão'), ('RN', 'Rio Grande do Norte'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('AL', 'Alagoas'), ('SE', 'Sergipe'), ('BA', 'Bahia'), ('MG', 'Minas Gerais'), ('RJ', 'Rio de Janeiro'), ('MT', 'Mato Grosso'), ('GO', 'Goiás'), ('DF', 'Distrito Federal'), ('PI', 'Piauí'), ('CE', 'Ceará'), ('ES', 'Espírito Santo')], max_length=2, null=True, verbose_name='SSP')),
                ('state', models.CharField(blank=True, choices=[('SP', 'São Paulo'), ('PR', 'Paraná'), ('SC', 'Santa Catarina'), ('RS', 'Rio Grande do Sul'), ('MS', 'Mato Grosso do Sul'), ('RO', 'Rondônia'), ('AC', 'Acre'), ('AM', 'Amazonas'), ('RR', 'Roraima'), ('PA', 'Pará'), ('AP', 'Amapá'), ('TO', 'Tocantins'), ('MA', 'Maranhão'), ('RN', 'Rio Grande do Norte'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('AL', 'Alagoas'), ('SE', 'Sergipe'), ('BA', 'Bahia'), ('MG', 'Minas Gerais'), ('RJ', 'Rio de Janeiro'), ('MT', 'Mato Grosso'), ('GO', 'Goiás'), ('DF', 'Distrito Federal'), ('PI', 'Piauí'), ('CE', 'Ceará'), ('ES', 'Espírito Santo')], max_length=2, null=True, verbose_name='Estado')),
                ('address_line_1', models.CharField(blank=True, help_text='Rua e número da residência', max_length=100, null=True, verbose_name='Rua e número da residência')),
                ('address_line_2', models.CharField(blank=True, help_text='apartamento, bloco,...', max_length=100, null=True, verbose_name='Complemento')),
                ('neighbourhood', models.CharField(blank=True, max_length=60, null=True, verbose_name='Bairro')),
                ('city', models.CharField(blank=True, max_length=60, null=True, validators=[people.validators.check_city], verbose_name='Cidade')),
                ('postal_code', models.CharField(blank=True, help_text='Exemplo: 00000000', max_length=15, null=True, validators=[people.validators.check_cep], verbose_name='CEP')),
                ('residence_type', models.CharField(blank=True, choices=[('urban', 'Urbano'), ('rural', 'Rural')], max_length=6, null=True, verbose_name='Distrito')),
                ('ddd_private_phone', models.CharField(blank=True, choices=[('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('21', '21'), ('22', '22'), ('24', '24'), ('27', '27'), ('28', '28'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('37', '37'), ('38', '38'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('51', '51'), ('53', '53'), ('54', '54'), ('55', '55'), ('61', '61'), ('62', '62'), ('63', '63'), ('64', '64'), ('65', '65'), ('66', '66'), ('67', '67'), ('68', '68'), ('69', '69'), ('71', '71'), ('73', '73'), ('74', '74'), ('75', '75'), ('77', '77'), ('79', '79'), ('81', '81'), ('82', '82'), ('83', '83'), ('84', '84'), ('85', '85'), ('86', '86'), ('87', '87'), ('88', '88'), ('89', '89'), ('91', '91'), ('92', '92'), ('93', '93'), ('94', '94'), ('95', '95'), ('96', '96'), ('97', '97'), ('98', '98'), ('99', '99')], max_length=2, null=True, verbose_name='DDD')),
                ('private_phone', models.CharField(blank=True, help_text='Exemplo: 999999999', max_length=10, null=True, validators=[people.validators.check_phone], verbose_name='Tel. p/ contato')),
                ('ddd_message_phone', models.CharField(blank=True, choices=[('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('21', '21'), ('22', '22'), ('24', '24'), ('27', '27'), ('28', '28'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('37', '37'), ('38', '38'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('51', '51'), ('53', '53'), ('54', '54'), ('55', '55'), ('61', '61'), ('62', '62'), ('63', '63'), ('64', '64'), ('65', '65'), ('66', '66'), ('67', '67'), ('68', '68'), ('69', '69'), ('71', '71'), ('73', '73'), ('74', '74'), ('75', '75'), ('77', '77'), ('79', '79'), ('81', '81'), ('82', '82'), ('83', '83'), ('84', '84'), ('85', '85'), ('86', '86'), ('87', '87'), ('88', '88'), ('89', '89'), ('91', '91'), ('92', '92'), ('93', '93'), ('94', '94'), ('95', '95'), ('96', '96'), ('97', '97'), ('98', '98'), ('99', '99')], max_length=2, null=True, verbose_name='DDD')),
                ('message_phone', models.CharField(blank=True, help_text='Exemplo: 999999999', max_length=10, null=True, validators=[people.validators.check_phone], verbose_name='Tel. p/ mensagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('observation', models.TextField(blank=True, max_length=600, null=True, verbose_name='Observação')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
                'ordering': ('name',),
            },
        ),
    ]
