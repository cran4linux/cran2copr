%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesPower
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Sample Size and Power Calculation for Bayesian Testing with Bayes Factor

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ExtDist 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-hypergeo 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ExtDist 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-hypergeo 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-grDevices 
Requires:         R-CRAN-tidyr 

%description
The goal of 'BayesPower' is to provide tools for Bayesian sample size
determination and power analysis across a range of common hypothesis
testing scenarios using Bayes factors. The main function,
BayesPower_BayesFactor(), launches an interactive 'shiny' application for
performing these analyses. The application also provides command-line code
for reproducibility. Details of the methods are described in the tutorial
by Wong, Pawel, and Tendeiro (2025) <doi:10.31234/osf.io/pgdac_v2>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
