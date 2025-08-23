%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stlnpp
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatio-Temporal Analysis of Point Patterns on Linear Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat >= 3.4.0
BuildRequires:    R-CRAN-spatstat.univar 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-spatstat.linnet 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-spatstat >= 3.4.0
Requires:         R-CRAN-spatstat.univar 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.random 
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-spatstat.linnet 
Requires:         R-stats 
Requires:         R-graphics 

%description
Statistical analysis of spatio-temporal point processes on linear
networks. This packages provides tools to visualise and analyse
spatio-temporal point patterns on linear networks using first, second, and
higher-order summary statistics.

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
