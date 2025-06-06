%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  formatters
%global packver   0.5.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.11
Release:          1%{?dist}%{?buildtag}
Summary:          ASCII Formatting for Values and Tables

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-stringi >= 1.7.12
BuildRequires:    R-CRAN-htmltools >= 0.5.3
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-methods 
BuildRequires:    R-grid 
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-stringi >= 1.7.12
Requires:         R-CRAN-htmltools >= 0.5.3
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-methods 
Requires:         R-grid 

%description
We provide a framework for rendering complex tables to ASCII, and a set of
formatters for transforming values or sets of values into ASCII-ready
display strings.

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
