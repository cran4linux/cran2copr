%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dgraphs
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data-Derived Graph Construction Utilities

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-igraph >= 2.2.0
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-igraph >= 2.2.0
Requires:         R-CRAN-FNN 
Requires:         R-parallel 

%description
Constructs data-derived graphs from numerical observations using mutual,
shared-neighbor, intersection, geodesic, radius, adaptive-radius, and
minimum-spanning-tree completion methods. Provides graph conversion,
pruning, diagnostics, spectral embedding, endpoint detection, and path
utilities. The implemented graph constructions include methods described
by Jarvis and Patrick (1973) <doi:10.1109/T-C.1973.223640>, Brito et al.
(1997) <doi:10.1016/S0167-7152(96)00213-1>, Berry and Sauer (2019)
<doi:10.3934/fods.2019001>, and Gower and Ross (1969)
<doi:10.2307/2346439>.

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
