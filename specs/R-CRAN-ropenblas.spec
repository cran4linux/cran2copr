%global __brp_check_rpaths %{nil}
%global packname  ropenblas
%global packver   0.2.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.10
Release:          1%{?dist}%{?buildtag}
Summary:          Download, Compile and Link 'OpenBLAS' Library with R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-git2r 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-pingr 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-rvest 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-getPass 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-git2r 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-pingr 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-rvest 

%description
The 'ropenblas' package (<https://prdm0.github.io/ropenblas/>) is useful
for users of any 'GNU/Linux' distribution. It will be possible to
download, compile and link the 'OpenBLAS' library
(<https://www.openblas.net/>) with the R language, always by the same
procedure, regardless of the 'GNU/Linux' distribution used. With the
'ropenblas' package it is possible to download, compile and link the
latest version of the 'OpenBLAS' library even the repositories of the
'GNU/Linux' distribution used do not include the latest versions of
'OpenBLAS'. If of interest, older versions of the 'OpenBLAS' library may
be considered. Linking R with an optimized version of 'BLAS'
(<http://www.netlib.org/blas/>) may improve the computational performance
of R code. The 'OpenBLAS' library is an optimized implementation of 'BLAS'
that can be easily linked to R with the 'ropenblas' package.

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
