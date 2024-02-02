%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  readODS
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Read and Write ODS Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-readr >= 1.2.1
BuildRequires:    R-CRAN-cpp11 >= 0.4.6
BuildRequires:    R-CRAN-vctrs >= 0.4.2
BuildRequires:    R-CRAN-cellranger 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-tools 
Requires:         R-CRAN-readr >= 1.2.1
Requires:         R-CRAN-vctrs >= 0.4.2
Requires:         R-CRAN-cellranger 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-zip 
Requires:         R-tools 

%description
Read ODS (OpenDocument Spreadsheet) into R as data frame. Also support
writing data frame into ODS file.

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
