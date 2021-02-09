%global packname  detrendr
%global packver   0.6.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.12
Release:          1%{?dist}%{?buildtag}
Summary:          Detrend Images

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-RcppParallel >= 5.0.2
BuildRequires:    R-CRAN-filesstrings >= 3.2
BuildRequires:    R-CRAN-ijtiff >= 2.2
BuildRequires:    R-CRAN-withr >= 2.1
BuildRequires:    R-CRAN-checkmate >= 1.9.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4
BuildRequires:    R-CRAN-autothresholdr >= 1.3.7
BuildRequires:    R-CRAN-arrayhelpers >= 1.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-rlang >= 0.3.3
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-tools 
Requires:         R-CRAN-RcppParallel >= 5.0.2
Requires:         R-CRAN-filesstrings >= 3.2
Requires:         R-CRAN-ijtiff >= 2.2
Requires:         R-CRAN-withr >= 2.1
Requires:         R-CRAN-checkmate >= 1.9.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4
Requires:         R-CRAN-autothresholdr >= 1.3.7
Requires:         R-CRAN-arrayhelpers >= 1.1.0
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-rlang >= 0.3.3
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-parallel 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-purrr 
Requires:         R-tools 

%description
Detrend fluorescence microscopy image series for fluorescence fluctuation
and correlation spectroscopy ('FCS' and 'FFS') analysis. This package
contains functionality published in a 2016 paper
<doi:10.1093/bioinformatics/btx434> but it has been extended since then
with the Robin Hood algorithm and thus contains unpublished work.

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
