%global __brp_check_rpaths %{nil}
%global packname  CITAN
%global packver   2021.11-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2021.11.1
Release:          1%{?dist}%{?buildtag}
Summary:          CITation ANalysis Toolpack

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-agop 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-agop 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-hash 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-DBI 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Supports quantitative research in scientometrics and bibliometrics.
Provides various tools for preprocessing bibliographic data retrieved,
e.g., from Elsevier's SciVerse Scopus, computing bibliometric impact of
individuals, or modelling phenomena encountered in the social sciences.
This package is deprecated, see 'agop' instead.

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
