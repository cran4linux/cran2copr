%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  disk.frame
%global packver   0.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          1%{?dist}%{?buildtag}
Summary:          Larger-than-RAM Disk-Based Data Manipulation Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-glue >= 1.3.1
BuildRequires:    R-CRAN-fs >= 1.3.1
BuildRequires:    R-CRAN-future.apply >= 1.3.0
BuildRequires:    R-CRAN-future >= 1.14.0
BuildRequires:    R-CRAN-data.table >= 1.12.2
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-fst >= 0.8.0
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-bigreadr >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-CRAN-pryr >= 0.1.4
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-benchmarkme 
BuildRequires:    R-CRAN-globals 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-arrow 
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-glue >= 1.3.1
Requires:         R-CRAN-fs >= 1.3.1
Requires:         R-CRAN-future.apply >= 1.3.0
Requires:         R-CRAN-future >= 1.14.0
Requires:         R-CRAN-data.table >= 1.12.2
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-fst >= 0.8.0
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-bigreadr >= 0.2.0
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-CRAN-pryr >= 0.1.4
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-benchmarkme 
Requires:         R-CRAN-globals 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-arrow 

%description
A disk-based data manipulation tool for working with large-than-RAM
datasets. Aims to lower the barrier-to-entry for manipulating large
datasets by adhering closely to popular and familiar data manipulation
paradigms like 'dplyr' verbs and 'data.table' syntax.

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
