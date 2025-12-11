%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  osdc
%global packver   0.9.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.17
Release:          1%{?dist}%{?buildtag}
Summary:          Open Source Diabetes Classifier for Danish Registers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-codeCollection 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-duckplyr 
BuildRequires:    R-CRAN-fabricatr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-codeCollection 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-duckplyr 
Requires:         R-CRAN-fabricatr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rvest 
Requires:         R-stats 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 

%description
The algorithm first identifies a population of individuals from Danish
register data with any type of diabetes as individuals with two or more
inclusion events. Then, it splits this population into individuals with
either type 1 diabetes or type 2 diabetes by identifying individuals with
type 1 diabetes and classifying the remainder of the diabetes population
as having type 2 diabetes.

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
