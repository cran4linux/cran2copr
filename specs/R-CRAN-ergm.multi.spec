%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ergm.multi
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fit, Simulate and Diagnose Exponential-Family Models for Multiple or Multilayer Networks

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-ergm >= 4.9.0
BuildRequires:    R-CRAN-statnet.common >= 4.12.0
BuildRequires:    R-CRAN-tibble >= 3.3.0
BuildRequires:    R-CRAN-Rdpack >= 2.6.4
BuildRequires:    R-CRAN-glue >= 1.8.0
BuildRequires:    R-CRAN-network >= 1.19.0
BuildRequires:    R-CRAN-rlang >= 1.1.6
BuildRequires:    R-CRAN-networkLite >= 1.1.0
BuildRequires:    R-CRAN-purrr >= 1.0.4
BuildRequires:    R-CRAN-rle >= 0.10.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-CRAN-ergm >= 4.9.0
Requires:         R-CRAN-statnet.common >= 4.12.0
Requires:         R-CRAN-tibble >= 3.3.0
Requires:         R-CRAN-Rdpack >= 2.6.4
Requires:         R-CRAN-glue >= 1.8.0
Requires:         R-CRAN-network >= 1.19.0
Requires:         R-CRAN-rlang >= 1.1.6
Requires:         R-CRAN-networkLite >= 1.1.0
Requires:         R-CRAN-purrr >= 1.0.4
Requires:         R-CRAN-rle >= 0.10.0
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-parallel 

%description
A set of extensions for the 'ergm' package to fit
multilayer/multiplex/multirelational networks and samples of multiple
networks. 'ergm.multi' is a part of the Statnet suite of packages for
network analysis. See Krivitsky, Koehly, and Marcum (2020)
<doi:10.1007/s11336-020-09720-7> and Krivitsky, Coletti, and Hens (2023)
<doi:10.1080/01621459.2023.2242627>.

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
