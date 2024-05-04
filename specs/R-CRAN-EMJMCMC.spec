%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EMJMCMC
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Evolutionary Mode Jumping Markov Chain Monte Carlo Expert Toolbox

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.1
Requires:         R-core >= 3.4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-biglm 
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-CRAN-BAS 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-speedglm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-biglm 
Requires:         R-CRAN-hash 
Requires:         R-CRAN-BAS 
Requires:         R-CRAN-stringi 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-speedglm 
Requires:         R-stats 
Requires:         R-CRAN-withr 

%description
Implementation of the Mode Jumping Markov Chain Monte Carlo algorithm from
Hubin, A., Storvik, G. (2018) <doi:10.1016/j.csda.2018.05.020>,
Genetically Modified Mode Jumping Markov Chain Monte Carlo from Hubin, A.,
Storvik, G., & Frommlet, F. (2020) <doi:10.1214/18-BA1141>, Hubin, A.,
Storvik, G., & Frommlet, F. (2021) <doi:10.1613/jair.1.13047>, and Hubin,
A., Heinze, G., & De Bin, R. (2023) <doi:10.3390/fractalfract7090641>, and
Reversible Genetically Modified Mode Jumping Markov Chain Monte Carlo from
Hubin, A., Frommlet, F., & Storvik, G. (2021)
<doi:10.48550/arXiv.2110.05316>, which allow for estimating posterior
model probabilities and Bayesian model averaging across a wide set of
Bayesian models including linear, generalized linear, generalized linear
mixed, generalized nonlinear, generalized nonlinear mixed, and logic
regression models.

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
