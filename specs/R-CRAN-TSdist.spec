%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TSdist
%global packver   3.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Distance Measures for Time Series Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-locpol 
BuildRequires:    R-CRAN-longitudinalData 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pdc 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TSclust 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-dtw 
Requires:         R-graphics 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-locpol 
Requires:         R-CRAN-longitudinalData 
Requires:         R-methods 
Requires:         R-CRAN-pdc 
Requires:         R-stats 
Requires:         R-CRAN-TSclust 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
A set of commonly used distance measures and some additional functions
which, although initially not designed for this purpose, can be used to
measure the dissimilarity between time series. These measures can be used
to perform clustering, classification or other data mining tasks which
require the definition of a distance measure between time series. U. Mori,
A. Mendiburu and J.A. Lozano (2016), <doi:10.32614/RJ-2016-058>.

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
