%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lava
%global packver   1.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Latent Variable Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-SQUAREM 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-future.apply 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-progressr 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-SQUAREM 
Requires:         R-utils 

%description
A general implementation of Structural Equation Models with latent
variables (MLE, 2SLS, and composite likelihood estimators) with both
continuous, censored, and ordinal outcomes (Holst and Budtz-Joergensen
(2013) <doi:10.1007/s00180-012-0344-y>). Mixture latent variable models
and non-linear latent variable models (Holst and Budtz-Joergensen (2020)
<doi:10.1093/biostatistics/kxy082>). The package also provides methods for
graph exploration (d-separation, back-door criterion), simulation of
general non-linear latent variable models, and estimation of influence
functions for a broad range of statistical models.

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
