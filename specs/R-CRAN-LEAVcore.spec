%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LEAVcore
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Constitution of Core Collections using Length of Encoded Attribute Values

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stratification 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-stratification 

%description
Construct core collections using the information measure 'Length of
Encoded Attribute Values' (LEAV) using qualitative and/or quantitative
trait data as described by Balakrishnan and Suresh (2001a)
<https://indianjournals.com/article/ijpgr-14-1-006> and (2001b)
<https://indianjournals.com/article/ijpgr-14-3-005>.

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
