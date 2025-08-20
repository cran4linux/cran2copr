%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  recmap
%global packver   1.0.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.20
Release:          1%{?dist}%{?buildtag}
Summary:          Compute the Rectangular Statistical Cartogram

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5
Requires:         R-core >= 4.5
BuildRequires:    R-CRAN-GA >= 3.1
BuildRequires:    R-CRAN-sp >= 1.3
BuildRequires:    R-CRAN-Rcpp >= 1.0
Requires:         R-CRAN-GA >= 3.1
Requires:         R-CRAN-sp >= 1.3
Requires:         R-CRAN-Rcpp >= 1.0

%description
Implements the RecMap MP2 construction heuristic
<doi:10.1109/INFVIS.2004.57>. This algorithm draws maps according to a
given statistical value, e.g., election results, population, or
epidemiological data. The basic idea of the RecMap algorithm is that each
map region, e.g., different countries, is represented by a rectangle. The
area of each rectangle represents the statistical value provided as input
to maintain zero cartographic error. Computationally intensive tasks are
implemented in C++. The included vignette documents recmap algorithm
usage.

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
