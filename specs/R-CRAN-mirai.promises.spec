%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mirai.promises
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Make 'Mirai' 'Promises'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12
Requires:         R-core >= 2.12
BuildArch:        noarch
BuildRequires:    R-CRAN-promises >= 1.1.0
BuildRequires:    R-CRAN-later >= 1.0.0
BuildRequires:    R-CRAN-mirai 
Requires:         R-CRAN-promises >= 1.1.0
Requires:         R-CRAN-later >= 1.0.0
Requires:         R-CRAN-mirai 

%description
Allows 'mirai' objects encapsulating asynchronous computations, from the
'mirai' package by Gao (2023) <doi:10.5281/zenodo.7912722>, to be used
interchangeably with 'promise' objects from the 'promises' package by
Cheng (2021) <https://CRAN.R-project.org/package=promises>. This
facilitates their use with packages 'plumber' by Schloerke and Allen
(2022) <https://CRAN.R-project.org/package=plumber> and 'shiny' by Cheng,
Allaire, Sievert, Schloerke, Xie, Allen, McPherson, Dipert and Borges
(2022) <https://CRAN.R-project.org/package=shiny>.

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
