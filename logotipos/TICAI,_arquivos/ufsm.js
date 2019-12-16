;var ufsm = {
    utils       : {},
    cpd         : {},
    concursos   : {},
    cursos      : {},
    ementario   : {},
    orcamento   : {},
    servidor    : {},
    webservice  : {
        host: "https://" + (['www.ufsm.br','w5.ufsm.br','clone.ufsm.br','dev.ufsm'].includes(window.location.host) ? "portal" : "edge.cpd") + ".ufsm.br"  
    },
    widgets     : {}
};