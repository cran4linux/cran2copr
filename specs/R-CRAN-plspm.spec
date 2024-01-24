%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plspm
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Partial Least Squares Path Modeling (PLS-PM)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tester 
BuildRequires:    R-CRAN-turner 
BuildRequires:    R-CRAN-diagram 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-amap 
BuildRequires:    R-methods 
Requires:         R-CRAN-tester 
Requires:         R-CRAN-turner 
Requires:         R-CRAN-diagram 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-amap 
Requires:         R-methods 

%description
Partial Least Squares Path Modeling (PLS-PM), Tenenhaus, Esposito Vinzi,
Chatelin, Lauro (2005) <doi:10.1016/j.csda.2004.03.005>, analysis for both
metric and non-metric data, as well as REBUS analysis, Esposito Vinzi,
Trinchera, Squillacciotti, and Tenenhaus (2008) <doi:10.1002/asmb.728>.

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
