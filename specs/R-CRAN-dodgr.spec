%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dodgr
%global packver   0.2.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.21
Release:          1%{?dist}%{?buildtag}
Summary:          Distances on Directed Graphs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.6
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-osmdata 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-Rcpp >= 0.12.6
Requires:         R-CRAN-callr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-osmdata 
Requires:         R-CRAN-RcppParallel 

%description
Distances on dual-weighted directed graphs using priority-queue shortest
paths (Padgham (2019) <doi:10.32866/6945>). Weighted directed graphs have
weights from A to B which may differ from those from B to A.
Dual-weighted directed graphs have two sets of such weights. A canonical
example is a street network to be used for routing in which routes are
calculated by weighting distances according to the type of way and mode of
transport, yet lengths of routes must be calculated from direct distances.

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
