%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  REMixed
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Regularized Estimation in Mixed Effects Model

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-Rsmlx 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-snow 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-Rmpfr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-Rsmlx 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fastGHQuad 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-snow 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-Rmpfr 

%description
Implementation of an algorithm in two steps to estimate parameters of a
model whose latent dynamics are inferred through latent processes, jointly
regularized. This package uses 'Monolix' software
(<https://monolixsuite.slp-software.com/>), which provide robust
statistical method for non-linear mixed effects modeling. 'Monolix' must
have been installed prior to use.

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
