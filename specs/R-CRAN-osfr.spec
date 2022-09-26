%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  osfr
%global packver   0.2.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.9
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the 'Open Science Framework' ('OSF')

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-fs >= 1.3.0
BuildRequires:    R-CRAN-crul >= 0.7
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-fs >= 1.3.0
Requires:         R-CRAN-crul >= 0.7
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-httr 

%description
An interface for interacting with 'OSF' (<https://osf.io>). 'osfr' enables
you to access open research materials and data, or create and manage your
own private or public projects.

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
