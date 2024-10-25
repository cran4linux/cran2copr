%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidysq
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Processing and Analysis of Biological Sequences

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-cli >= 2.0.0
BuildRequires:    R-CRAN-checkmate >= 1.9.0
BuildRequires:    R-CRAN-pillar >= 1.4.2
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-cli >= 2.0.0
Requires:         R-CRAN-checkmate >= 1.9.0
Requires:         R-CRAN-pillar >= 1.4.2
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-vctrs >= 0.3.0

%description
A tidy approach to analysis of biological sequences. All processing and
data-storage functions are heavily optimized to allow the fastest and most
efficient data storage.

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
