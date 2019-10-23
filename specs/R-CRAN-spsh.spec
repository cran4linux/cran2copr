%global packname  spsh
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Estimation and Prediction of Parameters of Various SoilHydraulic Property Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DEoptim >= 2.2.4
BuildRequires:    R-CRAN-pracma >= 2.1.4
BuildRequires:    R-CRAN-FME >= 1.3.5
BuildRequires:    R-CRAN-lhs >= 0.16.0
Requires:         R-CRAN-DEoptim >= 2.2.4
Requires:         R-CRAN-pracma >= 2.1.4
Requires:         R-CRAN-FME >= 1.3.5
Requires:         R-CRAN-lhs >= 0.16.0

%description
Estimates model parameters of soil hydraulic property functions by
inverting measured data. A wide range of hydraulic models, weighting
schemes, global optimization algorithms, Markov chain Monte Carlo
samplers, and extended statistical analyses of results are provided.
Prediction of soil hydraulic property model parameters and common soil
properties using pedotransfer functions is facilitated. Models include the
unimodal van Genuchten-Mualem Model (van Genuchten, M.T. (1980)
<doi:10.2136/sssaj1980.03615995004400050002x>, Mualem, Y. (1976)
<doi:10.1029/WR012i003p00513>), the multimodel van Genuchten-Mualem model
(Durner, W. (1994) <doi:10.1029/93WR02676> and Priesack, E. and Durner, W.
(2006) <doi:10.2136/vzj2005.0066>, as used in Weber, T.K.D., Iden, S.C.,
and Durner, W. (2017a) <doi:10.1002/2016WR019707>, Weber, T.K.D., Iden,
S.C., and Durner, W. (2017b <doi:10.5194/hess-21-6185-2017>), the Kosugi 2
parametric-Mualem model (Kosugi, K. (1996) <doi:10.1029/96WR01776>) and
the Fredlund-Xing model (Fredlund D.G., and Xing, A. (1994)
<doi:10.1139/t94-061>). All models can be extended to account for
non-capillary water storage and transport. The isothermal vapour
conductivity (Saito, H., Simunek, J. and Mohanty, B.P. (2006)
<doi:10.2136/vzj2006.0007>)is calculated based on volumetric air space and
a selection of different tortuosity models (Grable, A.R., Siemer, E.G.
(1968) <doi:10.2136/sssaj1968.03615995003200020011x>, Lai, S.H., Tiedje
J.M., Erickson, E. (1976) <doi:10.2136/sssaj1976.03615995004000010006x>,
Moldrup, P., Olesen, T., Rolston, D.E., and Yamaguchi, T. (1997)
<doi:10.1097/00010694-199709000-00004>, Moldrup, P., Olesen, T.,
Yoshikawa, S., Komatsu, T., and Rolston, D.E. (2004)
<doi:10.2136/sssaj2004.7500>, Moldrup, P., Olesen, T., Yoshikawa, S.,
Komatsu, T., and Rolston, D.E. (2005)
<doi:10.1097/01.ss.0000196768.44165.1f>, Millington, R.J., Quirk, J.P.
(1961) <doi:10.1039/TF9615701200>, Penman, H.L. (1940)
<doi:10.1017/S0021859600048164>, and Xu, X, Nieber, J.L. Gupta, S.C.
(1992) <doi:10.2136/sssaj1992.03615995005600060014x>). Parameter
estimation is based on identically and independentally distributed
(weighted) model residuals (Seber and Wild (2003, ISBN:9780471617600)),
and simple model selection criteria (Hoege, M., Woehling, T., and Nowak,
W. (2018) <doi:10.1002/2017WR021902>) can be calculated.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
