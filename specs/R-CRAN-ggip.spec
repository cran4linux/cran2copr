%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggip
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Visualization for IP Addresses and Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-ipaddress >= 0.5.1
BuildRequires:    R-CRAN-rlang >= 0.4.2
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-ipaddress >= 0.5.1
Requires:         R-CRAN-rlang >= 0.4.2
Requires:         R-CRAN-vctrs >= 0.3.0
Requires:         R-CRAN-glue 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-tidyr 

%description
A 'ggplot2' extension that enables visualization of IP (Internet Protocol)
addresses and networks. The address space is mapped onto the Cartesian
coordinate system using a space-filling curve. Offers full support for
both IPv4 and IPv6 (Internet Protocol versions 4 and 6) address spaces.

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
