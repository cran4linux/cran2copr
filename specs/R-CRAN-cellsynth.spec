%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cellsynth
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cell-Wise Synthetic Copies of De-Identified Tables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rpart 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Turns de-identified tables ('Excel' workbooks or delimited text files)
into synthetic counterparts with the same layout, the same identifiers and
the same data-entry quirks. Every non-identifier cell, missingness
included, is censored once per sweep and redrawn by copying the raw value
of a donor drawn from a classification and regression tree leaf fitted on
the rest of the table, in the spirit of the sequential tree-based
synthesis of Reiter (2005) "Using CART to generate partially synthetic
public use microdata", Journal of Official Statistics 21(3):441-462, and
Nowok, Raab and Dibben (2016) <doi:10.18637/jss.v074.i11>. Identifiers are
kept so that tables stay joinable, and columns of other tables can
condition the synthesis so cross-table associations survive a later join.
Synthetic copies are intended for developing and testing analysis code;
they are not an anonymisation method.

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
