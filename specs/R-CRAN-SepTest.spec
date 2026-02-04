%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SepTest
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tests for First-Order Separability in Spatio-Temporal Point Processes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-dHSIC 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-GET 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.model 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-stats 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-dHSIC 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-GET 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.model 
Requires:         R-CRAN-splancs 
Requires:         R-stats 

%description
Provides statistical tools for testing first-order separability in
spatio-temporal point processes, that is, assessing whether the
spatio-temporal intensity function can be expressed as the product of
spatial and temporal components. The package implements several hypothesis
tests, including exact and asymptotic methods for Poisson and non-Poisson
processes. Methods include global envelope tests, chi-squared type
statistics, and a novel Hilbert-Schmidt independence criterion (HSIC)
test, all with both block and pure permutation procedures. Simulation
studies and real world examples, including the 2001 UK foot and mouth
disease outbreak data, illustrate the utility of the proposed methods. The
package contains all simulation studies and applications presented in
Ghorbani et al. (2021) <doi:10.1016/j.csda.2021.107245> and Ghorbani et
al. (2025) <doi:10.1007/s11749-025-00972-y>.

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
