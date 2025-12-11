%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ivd
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Individual Variance Detection

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nimble >= 1.1.0
BuildRequires:    R-CRAN-coda >= 0.19.4
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-nimble >= 1.1.0
Requires:         R-CRAN-coda >= 0.19.4
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-utils 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-rstantools

%description
Fit mixed-effects location scale models with spike-and-slab priors on the
location random effects to identify units with unusual residual variances.
The method is described in detail in Carmo, Williams and Rast (2025)
<https://osf.io/sh6ne>.

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
