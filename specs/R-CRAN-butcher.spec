%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  butcher
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Model Butcher

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.3.0
BuildRequires:    R-CRAN-tibble >= 3.1.7
BuildRequires:    R-CRAN-lobstr >= 1.1.2
BuildRequires:    R-CRAN-rlang >= 1.0.2
BuildRequires:    R-CRAN-vctrs >= 0.4.1
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.3.0
Requires:         R-CRAN-tibble >= 3.1.7
Requires:         R-CRAN-lobstr >= 1.1.2
Requires:         R-CRAN-rlang >= 1.0.2
Requires:         R-CRAN-vctrs >= 0.4.1
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-methods 
Requires:         R-utils 

%description
Provides a set of S3 generics to axe components of fitted model objects
and help reduce the size of model objects saved to disk.

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
