%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TOSI
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Two-Directional Simultaneous Inference for High-Dimensional Models

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-hdi 
BuildRequires:    R-CRAN-scalreg 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-hdi 
Requires:         R-CRAN-scalreg 
Requires:         R-CRAN-glmnet 

%description
A general framework of two directional simultaneous inference is provided
for high-dimensional as well as the fixed dimensional models with manifest
variable or latent variable structure, such as high-dimensional mean
models, high- dimensional sparse regression models, and high-dimensional
latent factors models. It is making the simultaneous inference on a set of
parameters from two directions, one is testing whether the estimated zero
parameters indeed are zero and the other is testing whether there exists
zero in the parameter set of non-zero. More details can be referred to Wei
Liu, et al. (2022) <doi:10.48550/arXiv.2012.11100>.

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
