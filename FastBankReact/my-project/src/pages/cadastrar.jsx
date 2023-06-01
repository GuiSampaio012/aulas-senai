import React, { Component, useState} from 'react';
import axios from 'axios'
import Botaocad from '../componentes/botaoCadastro';
import InputV from '../componentes/inputText';
import { useNavigate } from 'react-router-dom';

const Cadastrar = () => {
    const navigate = useNavigate();

    const [nome, setNome] = useState('');
    const [cpf, setCpf] = useState('');
    const foto = "teste"
    const [data_nascimento, setData_nascimento] = useState('');
    const [celular, setCelular] = useState('');
    const [email, setEmail] = useState('');
    const tipo_cliente = "F"
    const [password, setPassword] = useState('');
    const dataReal = data_nascimento

    // var data = new Date();
    // var dia = String(data.getDate()).padStart(2, '0');
    // var mes = String(data.getMonth() + 1).padStart(2, '0');
    // var ano = data.getFullYear();
    // const data_abertura = ano + '/' + mes + '/' + dia ;
    // const agencia = '171'
    const ativa = "A"
    const saldo = 1000

    const[token, setToken] = useState('')
    const[teste, setTeste] = useState([])

    
    useEffect(() => {
        pegartoken()
    }, [])

    const pegartoken = () => {
        const acesso = localStorage.getItem("dados")
        let chave =""
        if (acesso) {
            chave = JSON.parse(acesso).access
            setToken(chave)
        }
    }



    const cadastrar = () => {
        // essa funcão CADASTRA
        axios.post('http://127.0.0.1:8000/auth/users/', {
          nome: nome,
          cpf: cpf,
          foto_logo:foto,
          data_nascimento:data_nascimento,
          celular:celular,
          tipo_cliente:tipo_cliente,
          email:email,
          password: password
        // }).then((res) =>{ 
        //     if(res.status==200||res.status==201) {
        //         console.log(res.data.id)
        //     localStorage.setItem('dadosCad',JSON.stringify(res.data))
        //         axios.post('http://127.0.0.1:8000/crud/contas/', {
        //             cliente_conta:res.data.id,
        //             // data_abertura:data_abertura,
        //             // agencia:agencia,
        //             // numero:numero,
        //             ativa:ativa,
        //             saldo:saldo

        //         },/*{headers:{Authotization:` JWT ${a}`}}*/)
        //         .then((res) =>{
        //             console.log(res.data);
        //         })
        //     }
        // })
        }).then((res) =>{ 
            if(res.status==200||res.status==201) {
                console.log(res.data.id)
                localStorage.setItem('dadosCad',JSON.stringify(res.data))
                axios.post('http://127.0.0.1:8000/auth/jwt/create', {
                    email: email,
                    password: password
                }).then((res) =>{ 
                    localStorage.setItem('dados',JSON.stringify(res.data))
                    axios.get('http://127.0.0.1:8000/auth/users/me/',  {headers:{Authorization: 'JWT ' + res.data.access}})
                    .then((response) => {
                        console.log(response.data)
                        axios.post('http://127.0.0.1:8000/crud/contas/',{
                            cliente_conta:response.data.id,
                            ativa:ativa,
                            saldo:saldo
                            },{headers:{Authorization: 'JWT ' + res.data.access}},)
                            .then((res) =>{
                                console.log(res.data);
                                navigate('/home')
                            })
                    })    
                })
                
            }
        })
        console.log('function cadastrar:');
    }
        return (
            <div className='w-screen h-screen flex justify-center bg-[#3D8C64]'>
                <div className=' flex justify-center items-center flex-col w-4/6 bg-[#0C633D] p-12'>
                    <InputV onChange={(e) => setNome(e.target.value)} placeholder="nome:" ></InputV>
                    <InputV onChange={(e) => setCpf(e.target.value)} placeholder="cpf:" ></InputV>
                    <InputV type={'date'} onChange={(e) => setData_nascimento(e.target.value)} placeholder="data de nascimento:" ></InputV>
                    <InputV onChange={(e) => setCelular(e.target.value)} placeholder="celular:" ></InputV>
                    <InputV onChange={(e) => setEmail(e.target.value)} placeholder="email:" ></InputV>
                    <input onChange={(e) => setPassword(e.target.value)} type="password" placeholder="senha:" 
                    className=" m-3  w-4/4  border-b border-white text-slate-800 bg-[#0C633D] outline-none"
                    ></input>
                    {/* <Botaocad  placeholder= "CADASTRO"></Botaocad> */}
                    <Botaocad onClick={cadastrar} >CADASTRO</Botaocad>
                
                </div>
            </div>
            
        );

}

export default Cadastrar;