%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ncdfCF
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Easy Access to NetCDF Files with CF Metadata Conventions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-CFtime >= 1.4.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-RNetCDF 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-CFtime >= 1.4.1
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-RNetCDF 
Requires:         R-CRAN-stringr 

%description
Network Common Data Form ('netCDF') files are widely used for scientific
data. Library-level access in R is provided through packages 'RNetCDF' and
'ncdf4'. Package 'ncdfCF' is built on top of 'RNetCDF' and makes the data
and its attributes available as a set of R6 classes that are informed by
the Climate and Forecasting Metadata Conventions. Access to the data uses
standard R subsetting operators and common function forms.

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
