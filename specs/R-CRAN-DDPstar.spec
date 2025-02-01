%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DDPstar
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Density Regression via Dirichlet Process Mixtures of Normal Structured Additive Regression Models

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-splines 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-Matrix 
Requires:         R-parallel 
Requires:         R-CRAN-MASS 

%description
Implements a flexible, versatile, and computationally tractable model for
density regression based on a single-weights dependent Dirichlet process
mixture of normal distributions model for univariate continuous responses.
The model assumes an additive structure for the mean of each mixture
component and the effects of continuous covariates are captured through
smooth nonlinear functions. The key components of our modelling approach
are penalised B-splines and their bivariate tensor product extension. The
proposed method can also easily deal with parametric effects of
categorical covariates, linear effects of continuous covariates,
interactions between categorical and/or continuous covariates, varying
coefficient terms, and random effects. Please see Rodriguez-Alvarez,
Inacio et al. (2025) for more details.

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
