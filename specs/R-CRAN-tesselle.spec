%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tesselle
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Install and Load 'tesselle' Packages

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tabula >= 3.2.1
BuildRequires:    R-CRAN-kairos >= 2.2.1
BuildRequires:    R-CRAN-folio >= 1.5.0
BuildRequires:    R-CRAN-isopleuros >= 1.4.0
BuildRequires:    R-CRAN-khroma >= 1.16.0
BuildRequires:    R-CRAN-nexus >= 0.5.0
BuildRequires:    R-CRAN-dimensio >= 0.13.0
Requires:         R-CRAN-tabula >= 3.2.1
Requires:         R-CRAN-kairos >= 2.2.1
Requires:         R-CRAN-folio >= 1.5.0
Requires:         R-CRAN-isopleuros >= 1.4.0
Requires:         R-CRAN-khroma >= 1.16.0
Requires:         R-CRAN-nexus >= 0.5.0
Requires:         R-CRAN-dimensio >= 0.13.0

%description
Easy install and load key packages from the 'tesselle' suite in a single
step. The 'tesselle' suite is a collection of packages for research and
teaching in archaeology. These packages focus on quantitative analysis
methods developed for archaeology. The 'tesselle' packages are designed to
work seamlessly together and to complement general-purpose and other
specialized statistical packages. These packages can be used to explore
and analyze common data types in archaeology: count data, compositional
data and chronological data. Learn more about 'tesselle' at
<https://www.tesselle.org>.

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
