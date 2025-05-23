%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dynamite
%global packver   1.5.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.6
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Modeling and Causal Inference for Multivariate Longitudinal Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.0.0
BuildRequires:    R-CRAN-data.table >= 1.15.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-tibble >= 2.0.0
Requires:         R-CRAN-data.table >= 1.15.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rstan 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rstantools

%description
Easy-to-use and efficient interface for Bayesian inference of complex
panel (time series) data using dynamic multivariate panel models by Helske
and Tikka (2024) <doi:10.1016/j.alcr.2024.100617>. The package supports
joint modeling of multiple measurements per individual, time-varying and
time-invariant effects, and a wide range of discrete and continuous
distributions. Estimation of these dynamic multivariate panel models is
carried out via 'Stan'. For an in-depth tutorial of the package, see
(Tikka and Helske, 2024) <doi:10.48550/arXiv.2302.01607>.

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
