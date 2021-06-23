%global __brp_check_rpaths %{nil}
%global packname  caMST
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed Computerized Adaptive Multistage Testing

License:          LGPL (>= 2.0, < 3) | Mozilla Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-catR 
BuildRequires:    R-CRAN-mstR 
BuildRequires:    R-CRAN-diagram 
BuildRequires:    R-methods 
Requires:         R-CRAN-catR 
Requires:         R-CRAN-mstR 
Requires:         R-CRAN-diagram 
Requires:         R-methods 

%description
Provides functions to more easily analyze computerized adaptive tests.
Currently, functions for computerized adaptive tests (CAT), computer
adaptive multistage tests (CMT), and mixed computer adaptive multistage
tests (McaMST) utilizing CAT item-level adaptation for the initial stage
and traditional MST module-level adaptation for the subsequent stages have
been created, and a variation of Hybrid computer adaptive MST is planned
as well. For an in-depth look at CAT and MST, see Weiss & Kingsbury (1984)
<doi:10.1111/j.1745-3984.1984.tb01040.x> and Luecht & Nungester (2000)
<doi:10.1007/0-306-47531-6_6> respectively.

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
