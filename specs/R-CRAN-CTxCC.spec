%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CTxCC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Normal Mean Monitoring Through Critical-to-X Control Chart

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-CompQuadForm 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-matrixcalc 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-CompQuadForm 

%description
A comprehensive set of functions designed for multivariate mean monitoring
using the Critical-to-X Control Chart. These functions enable the
determination of optimal control limits based on a specified in-control
Average Run Length (ARL), the calculation of out-of-control ARL for a
given control limit, and post-signal analysis to identify the specific
variable responsible for a detected shift in the mean. This suite of tools
provides robust support for precise and effective process monitoring and
analysis.

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
