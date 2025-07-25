%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cleanepi
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Clean and Standardize Epidemiological Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-linelist >= 1.0.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-matchmaker 
BuildRequires:    R-CRAN-numberize 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-linelist >= 1.0.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-matchmaker 
Requires:         R-CRAN-numberize 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 

%description
Cleaning and standardizing tabular data package, tailored specifically for
curating epidemiological data. It streamlines various data cleaning tasks
that are typically expected when working with datasets in epidemiology. It
returns the processed data in the same format, and generates a
comprehensive report detailing the outcomes of each cleaning task.

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
