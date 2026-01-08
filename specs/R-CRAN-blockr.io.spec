%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  blockr.io
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive File Import and Export Blocks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-blockr.core >= 0.1.1
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-blockr.core >= 0.1.1
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-zip 

%description
Extends 'blockr.core' with interactive blocks for reading and writing data
files. Supports CSV, Excel, Parquet, RDS, and other formats through a
graphical interface without writing code directly. Includes file browser
integration and configurable import/export options.

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
