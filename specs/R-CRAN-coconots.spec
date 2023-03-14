%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  coconots
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Convolution-Closed Models for Count Time Series

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-StanHeaders >= 2.21.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-HMMpa 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-JuliaConnectoR 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-HMMpa 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-utils 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-JuliaConnectoR 

%description
Useful tools for fitting, validating, and forecasting of practical
convolution-closed time series models for low counts are provided.
Marginal distributions of the data can be modeled via Poisson and
Generalized Poisson innovations. Regression effects can be modelled via
time varying innovation rates. The models are described in Jung and
Tremayne (2011) <doi:10.1111/j.1467-9892.2010.00697.x> and the model
assessment tools are presented in Czado et al. (2009)
<doi:10.1111/j.1541-0420.2009.01191.x>, Gneiting and Raftery (2007)
<doi:10.1198/016214506000001437> and, Tsay (1992) <doi:10.2307/2347612>.

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
