%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  madrat
%global packver   3.15.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.15.6
Release:          1%{?dist}%{?buildtag}
Summary:          May All Data be Reproducible and Transparent (MADRaT) *

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magclass >= 5.7.0
BuildRequires:    R-CRAN-igraph >= 2.1.1
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pkgload 
BuildRequires:    R-CRAN-renv 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-magclass >= 5.7.0
Requires:         R-CRAN-igraph >= 2.1.1
Requires:         R-CRAN-callr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-pkgload 
Requires:         R-CRAN-renv 
Requires:         R-CRAN-stringi 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-yaml 

%description
Provides a framework which should improve reproducibility and transparency
in data processing. It provides functionality such as automatic meta data
creation and management, rudimentary quality management, data caching,
work-flow management and data aggregation. * The title is a wish not a
promise. By no means we expect this package to deliver everything what is
needed to achieve full reproducibility and transparency, but we believe
that it supports efforts in this direction.

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
