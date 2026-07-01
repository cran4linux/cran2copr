%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GMLTM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Multicomponent Latent Trait Model for Diagnosis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstan >= 2.21.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan >= 2.21.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rstantools

%description
Provides Bayesian estimation of Item Response Theory models that decompose
item difficulty into cognitive operations or rules. Implements the Linear
Logistic Test Model (LLTM; Fischer (1973)
<doi:10.1016/0001-6918(73)90003-6>), the Multicomponent Latent Trait Model
for Diagnosis (MLTM-D; Embretson and Yang (2013)
<doi:10.1007/s11336-012-9296-y>), and the Generalized Multicomponent
Latent Trait Model for Diagnosis (GMLTM-D; Ramirez et al. (2024)
<doi:10.3390/jintelligence12070067>). All models are estimated via
Hamiltonian Monte Carlo using 'Stan' through the 'rstan' interface.
Includes tools for model validation, reliability estimation, and
visualization of item characteristic curves. Supports user-defined prior
distributions for all model parameters.

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
