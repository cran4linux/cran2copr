%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  amadeus
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Accessing and Analyzing Large-Scale Environmental Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-testthat >= 3.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sftime 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-exactextractr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-nhdplusTools 
BuildRequires:    R-CRAN-archive 
BuildRequires:    R-CRAN-collapse 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-testthat >= 3.0.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sftime 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-exactextractr 
Requires:         R-utils 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stars 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-nhdplusTools 
Requires:         R-CRAN-archive 
Requires:         R-CRAN-collapse 
Requires:         R-CRAN-Rdpack 

%description
Functions are designed to facilitate access to and utility with large
scale, publicly available environmental data in R. The package contains
functions for downloading raw data files from web URLs (download_data()),
processing the raw data files into clean spatial objects
(process_covariates()), and extracting values from the spatial data
objects at point and polygon locations (calculate_covariates()). These
functions call a series of source-specific functions which are tailored to
each data sources/datasets particular URL structure, data format, and
spatial/temporal resolution. The functions are tested, versioned, and open
source and open access. For sum_edc() method details, see Messier, Akita,
and Serre (2012) <doi:10.1021/es203152a>.

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
