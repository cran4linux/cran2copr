%global __brp_check_rpaths %{nil}
%global packname  ts2net
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          From Time Series to Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo >= 1.8.9
BuildRequires:    R-CRAN-minerva >= 1.5.10
BuildRequires:    R-CRAN-dtw >= 1.22.3
BuildRequires:    R-CRAN-igraph >= 1.2.11
BuildRequires:    R-CRAN-infotheo >= 1.2.0
BuildRequires:    R-CRAN-dbscan >= 1.1.10
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-mmpp >= 0.6
BuildRequires:    R-CRAN-nonlinearTseries >= 0.2.11
BuildRequires:    R-parallel 
BuildRequires:    R-compiler 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-zoo >= 1.8.9
Requires:         R-CRAN-minerva >= 1.5.10
Requires:         R-CRAN-dtw >= 1.22.3
Requires:         R-CRAN-igraph >= 1.2.11
Requires:         R-CRAN-infotheo >= 1.2.0
Requires:         R-CRAN-dbscan >= 1.1.10
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-mmpp >= 0.6
Requires:         R-CRAN-nonlinearTseries >= 0.2.11
Requires:         R-parallel 
Requires:         R-compiler 
Requires:         R-stats 
Requires:         R-utils 

%description
Transforming one or multiple time series into networks. This package is
useful for complex systems modeling, time series data mining, or time
series analysis using networks. An introduction to the topic and the
descriptions of the methods implemented in this package can be found in
Mitchell (2006) <doi:10.1016/j.artint.2006.10.002>, Silva and Zhao (2016)
<doi:10.1007/978-3-319-17290-3>, and Silva et al. (2021)
<doi:10.1002/widm.1404>.

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
