%global __brp_check_rpaths %{nil}
%global packname  qgam
%global packver   1.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Smooth Additive Quantile Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-mgcv >= 1.8.28
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-mgcv >= 1.8.28
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-grDevices 

%description
Smooth additive quantile regression models, fitted using the methods of
Fasiolo et al. (2020) <doi:10.1080/01621459.2020.1725521>. See Fasiolo at
al. (2021) <doi:10.18637/jss.v100.i09> for an introduction to the package.
Differently from 'quantreg', the smoothing parameters are estimated
automatically by marginal loss minimization, while the regression
coefficients are estimated using either PIRLS or Newton algorithm. The
learning rate is determined so that the Bayesian credible intervals of the
estimated effects have approximately the correct coverage. The main
function is qgam() which is similar to gam() in 'mgcv', but fits
non-parametric quantile regression models.

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
