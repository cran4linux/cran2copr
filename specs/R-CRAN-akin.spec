%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  akin
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Utilities for Data Processing

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RcppAlgos >= 2.9.3
BuildRequires:    R-CRAN-data.table >= 1.18.2.0
BuildRequires:    R-CRAN-RVerbalExpressions >= 0.1.0
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-listenv 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-RcppAlgos >= 2.9.3
Requires:         R-CRAN-data.table >= 1.18.2.0
Requires:         R-CRAN-RVerbalExpressions >= 0.1.0
Requires:         R-CRAN-callr 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-listenv 
Requires:         R-CRAN-Matrix 
Requires:         R-utils 
Requires:         R-methods 

%description
Covers several areas of data processing: batch-splitting, reading and
writing of large data files, data tiling, one-hot encoding and decoding of
data tiles, stratified proportional (random or probabilistic) data
sampling, data normalization and thresholding, substring location and
commonalities inside strings and location and tabulation of amino acids,
modifications or associated monoisotopic masses inside modified peptides.
The extractor utility implements code from 'Matrix.utils', Varrichio C
(2020), <https://cran.r-project.org/package=Matrix.utils>.

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
