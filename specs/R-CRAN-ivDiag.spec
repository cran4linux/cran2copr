%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ivDiag
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Diagnostic Tools for Instrumental Variables Designs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-lfe 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggfortify 
BuildRequires:    R-CRAN-wCorr 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-lfe 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggfortify 
Requires:         R-CRAN-wCorr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-patchwork 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
Estimation and diagnostic tools for instrumental variables designs with
one endogenous treatment, implementing the guidelines in Lal, Lockhart,
Xu, and Zu (2024) <doi:10.1017/pan.2024.2>. The package reports ordinary
least squares and two-stage least squares estimates with analytic and
bootstrapped confidence intervals, several first-stage F statistics
including the effective F statistic, the Anderson-Rubin test and its
confidence set, the tF procedure of Lee, McCrary, Moreira, and Porter
(2022) <doi:10.1257/aer.20211063>, and local-to-zero sensitivity tests. It
also supports fuzzy regression discontinuity designs.

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
