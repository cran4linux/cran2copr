%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  latents
%global packver   0.9.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.21
Release:          1%{?dist}%{?buildtag}
Summary:          Multilevel Latent Profile, Class and Transition Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Provides functions for fitting multilevel latent profile analysis, latent
class, and latent transition models for continuous, categorical, and
mixed-type variables. Models are estimated by expectation-maximization,
handle missing data, and provide standard and robust standard errors.
Model selection is supported by information criteria, entropy,
classification diagnostics, and a parametric bootstrap likelihood ratio
test. Covariates can be related to latent class membership using
three-step methods with correction for classification error. Latent
transition models estimate transitions between latent profiles across
ordered occasions and are compatible with the 'tna' package for network
and sequence analysis. The multilevel mixture formulation follows Vermunt
(2003) <doi:10.1111/j.0081-1750.2003.t01-1-00131.x>.

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
