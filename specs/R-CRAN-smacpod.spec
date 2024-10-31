%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  smacpod
%global packver   2.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.4
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methods for the Analysis of Case-Control Point Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-smerc 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.random 
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-smerc 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-pbapply 

%description
Statistical methods for analyzing case-control point data.  Methods
include the ratio of kernel densities, the difference in K Functions, the
spatial scan statistic, and q nearest neighbors of cases.

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
