%global packname  hdpGLM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical Dirichlet Process Generalized Linear Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.3
Requires:         R-core >= 3.3.3
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-isotone 
BuildRequires:    R-CRAN-questionr 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggjoy 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-isotone 
Requires:         R-CRAN-questionr 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rprojroot 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggjoy 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-formula.tools 

%description
Implementation of MCMC algorithms to estimate the Hierarchical Dirichlet
Process Generalized Linear Model (hdpGLM) presented in the paper Ferrari
(2020) Modeling Context-Dependent Latent Heterogeneity, Political Analysis
<DOI:10.1017/pan.2019.13>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
