%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  blapsr
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Inference with Laplace Approximations and P-Splines

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.51
BuildRequires:    R-graphics >= 3.6.0
BuildRequires:    R-utils >= 3.6.0
BuildRequires:    R-CRAN-survival >= 2.44.1
BuildRequires:    R-CRAN-sn >= 1.5.4
BuildRequires:    R-CRAN-Matrix >= 1.2.17
BuildRequires:    R-CRAN-coda >= 0.19.3
BuildRequires:    R-CRAN-RSpectra >= 0.16.0
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS >= 7.3.51
Requires:         R-graphics >= 3.6.0
Requires:         R-utils >= 3.6.0
Requires:         R-CRAN-survival >= 2.44.1
Requires:         R-CRAN-sn >= 1.5.4
Requires:         R-CRAN-Matrix >= 1.2.17
Requires:         R-CRAN-coda >= 0.19.3
Requires:         R-CRAN-RSpectra >= 0.16.0
Requires:         R-stats 

%description
Laplace approximations and penalized B-splines are combined for fast
Bayesian inference in latent Gaussian models. The routines can be used to
fit survival models, especially proportional hazards and promotion time
cure models (Gressani, O. and Lambert, P. (2018)
<doi:10.1016/j.csda.2018.02.007>). The Laplace-P-spline methodology can
also be implemented for inference in (generalized) additive models
(Gressani, O. and Lambert, P. (2021) <doi:10.1016/j.csda.2020.107088>).
See the associated website for more information and examples.

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
