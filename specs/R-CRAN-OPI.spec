%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OPI
%global packver   3.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Open Perimetry Interface

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-openssl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-openssl 

%description
Implementation of the Open Perimetry Interface (OPI) for simulating and
controlling visual field machines using R. The OPI is a standard for
interfacing with visual field testing machines (perimeters) first started
as an open source project with support of Haag-Streit in 2010. It
specifies basic functions that allow many visual field tests to be
constructed. As of February 2022 it is fully implemented on the
Haag-Streit Octopus 900 and 'CrewT ImoVifa' ('Topcon Tempo') with partial
implementations on the Centervue Compass, Kowa AP 7000 and Android phones.
It also has a cousin: the R package 'visualFields', which has tools for
analysing and manipulating visual field data.

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
