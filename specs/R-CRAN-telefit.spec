%global packname  telefit
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Estimation and Prediction for Remote Effects Spatial ProcessModels

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-itertools 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-scoringRules 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-itertools 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-scoringRules 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sp 

%description
Implementation of the remote effects spatial process (RESP) model for
teleconnection.  The RESP model is a geostatistical model that allows a
spatially-referenced variable (like average precipitation) to be
influenced by covariates defined on a remote domain (like sea surface
temperatures).  The RESP model is introduced in Hewitt et al. (2018)
<doi:10.1002/env.2523>.  Sample code for working with the RESP model is
available at <https://jmhewitt.github.io/research/resp_example>. This
material is based upon work supported by the National Science Foundation
under grant number AGS 1419558. Any opinions, findings, and conclusions or
recommendations expressed in this material are those of the authors and do
not necessarily reflect the views of the National Science Foundation.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
