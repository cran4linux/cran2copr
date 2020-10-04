%global packname  panelvar
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          3%{?dist}%{?buildtag}
Summary:          Panel Vector Autoregression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-Matrix >= 1.2.11
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-texreg 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-methods 
Requires:         R-Matrix >= 1.2.11
Requires:         R-CRAN-knitr 
Requires:         R-MASS 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-texreg 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-methods 

%description
We extend two general methods of moment estimators to panel vector
autoregression models (PVAR) with p lags of endogenous variables,
predetermined and strictly exogenous variables. This general PVAR model
contains the first difference GMM estimator by Holtz-Eakin et al. (1988)
<doi:10.2307/1913103>, Arellano and Bond (1991) <doi:10.2307/2297968> and
the system GMM estimator by Blundell and Bond (1998)
<doi:10.1016/S0304-4076(98)00009-8>. We also provide specification tests
(Hansen overidentification test, lag selection criterion and stability
test of the PVAR polynomial) and classical structural analysis for PVAR
models such as orthogonal and generalized impulse response functions,
bootstrapped confidence intervals for impulse response analysis and
forecast error variance decompositions.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
