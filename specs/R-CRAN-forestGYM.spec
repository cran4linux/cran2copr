%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  forestGYM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Forest Growth and Yield Model Based on Clutter Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.3.1
BuildRequires:    R-CRAN-gtools >= 3.8.5
Requires:         R-stats >= 4.3.1
Requires:         R-CRAN-gtools >= 3.8.5

%description
The Clutter model is a significant forest growth simulation tool. Grounded
on individual trees and comprehensively considering factors such as
competition among trees and the impact of environmental elements on
growth, it can accurately reflect the growth process of forest stands. It
can be applied in areas like forest resource management, harvesting
planning, and ecological research. With the help of the Clutter model,
people can better understand the dynamic changes of forests and provide a
scientific basis for rational forest management and protecting the
ecological environment. This R package can effectively realize the
construction of forest growth and harvest models based on the Clutter
model and achieve optimized forest management.References: Farias A, Soares
C, Leite H et al(2021)<doi:10.1007/s10342-021-01380-1>. Guera O, Silva J,
Ferreira R, et al(2019)<doi:10.1590/2179-8087.038117>.

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
