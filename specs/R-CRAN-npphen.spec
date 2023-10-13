%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  npphen
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Vegetation Phenological Cycle and Anomaly Detection using Remote Sensing Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra >= 1.5.17
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-terra >= 1.5.17
Requires:         R-CRAN-ks 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-lubridate 

%description
Calculates phenological cycle and anomalies using a non-parametric
approach applied to time series of vegetation indices derived from remote
sensing data or field measurements. The package implements basic and
high-level functions for manipulating vector data (numerical series) and
raster data (satellite derived products). Processing of very large raster
files is supported. For more information, please check the following
paper: Chávez et al. (2023) <doi:10.3390/rs15010073>.

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
