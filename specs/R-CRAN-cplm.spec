%global packname  cplm
%global packver   0.7-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.8
Release:          2%{?dist}
Summary:          Compound Poisson Linear Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-Matrix 
BuildRequires:    R-splines 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-biglm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-tweedie 
Requires:         R-CRAN-coda 
Requires:         R-Matrix 
Requires:         R-splines 
Requires:         R-methods 
Requires:         R-CRAN-biglm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-minqa 
Requires:         R-nlme 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-statmod 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-CRAN-tweedie 

%description
Likelihood-based and Bayesian methods for various compound Poisson linear
models based on Zhang, Yanwei (2013)
<https://link.springer.com/article/10.1007/s11222-012-9343-7>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
