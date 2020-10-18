%global packname  cdata
%global packver   1.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Fluid Data Transformations

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-wrapr >= 2.0.2
BuildRequires:    R-CRAN-rquery >= 1.4.5
BuildRequires:    R-CRAN-rqdatatable >= 1.2.8
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-wrapr >= 2.0.2
Requires:         R-CRAN-rquery >= 1.4.5
Requires:         R-CRAN-rqdatatable >= 1.2.8
Requires:         R-methods 
Requires:         R-stats 

%description
Supplies higher-order coordinatized data specification and fluid transform
operators that include pivot and anti-pivot as special cases. The
methodology is describe in 'Zumel', 2018, "Fluid data reshaping with
'cdata'",
<https://winvector.github.io/FluidData/FluidDataReshapingWithCdata.html> ,
<DOI:10.5281/zenodo.1173299> . This package introduces the idea of
explicit control table specification of data transforms. Works on
in-memory data or on remote data using 'rquery' and 'SQL' database
interfaces.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
