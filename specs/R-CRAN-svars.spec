%global packname  svars
%global packver   1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          3%{?dist}
Summary:          Data-Driven Identification of SVAR Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-vars >= 1.5.3
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-steadyICA 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-vars >= 1.5.3
Requires:         R-CRAN-expm 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-steadyICA 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-strucchange 
Requires:         R-CRAN-Rcpp 

%description
Implements data-driven identification methods for structural vector
autoregressive (SVAR) models. Based on an existing VAR model object
(provided by e.g. VAR() from the 'vars' package), the structural impact
matrix is obtained via data-driven identification techniques (i.e. changes
in volatility (Rigobon, R. (2003) <doi:10.1162/003465303772815727>),
patterns of GARCH (Normadin, M., Phaneuf, L. (2004)
<doi:10.1016/j.jmoneco.2003.11.002>), independent component analysis
(Matteson, D. S, Tsay, R. S., (2013) <doi:10.1080/01621459.2016.1150851>),
least dependent innovations (Herwartz, H., Ploedt, M., (2016)
<doi:10.1016/j.jimonfin.2015.11.001>), smooth transition in variances
(Luetkepohl, H., Netsunajev, A. (2017) <doi:10.1016/j.jedc.2017.09.001>)
or non-Gaussian maximum likelihood (Lanne, M., Meitz, M., Saikkonen, P.
(2017) <doi:10.1016/j.jeconom.2016.06.002>)).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
