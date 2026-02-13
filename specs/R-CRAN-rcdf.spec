%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rcdf
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          A Comprehensive Toolkit for Working with Encrypted Parquet Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-utils >= 4.0.0
BuildRequires:    R-CRAN-RSQLite >= 2.2.0
BuildRequires:    R-CRAN-openssl >= 2.1.1
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-DBI >= 1.1.0
BuildRequires:    R-CRAN-uuid >= 0.1.2
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-duckdb 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-methods 
Requires:         R-utils >= 4.0.0
Requires:         R-CRAN-RSQLite >= 2.2.0
Requires:         R-CRAN-openssl >= 2.1.1
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-DBI >= 1.1.0
Requires:         R-CRAN-uuid >= 0.1.2
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-duckdb 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-glue 
Requires:         R-methods 

%description
Utilities for reading, writing, and managing RCDF files, including
encryption and decryption support. It offers a flexible interface for
handling data stored in encrypted Parquet format, along with metadata
extraction, key management, and secure operations using Advanced
Encryption Standard (AES) and Rivest-Shamir-Adleman (RSA) encryption.

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
