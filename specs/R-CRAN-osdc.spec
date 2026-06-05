%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  osdc
%global packver   0.11.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.3
Release:          1%{?dist}%{?buildtag}
Summary:          Open Source Diabetes Classifier for Danish Registers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dbplyr >= 2.5.1
BuildRequires:    R-CRAN-lubridate >= 1.9.5
BuildRequires:    R-CRAN-purrr >= 1.2.1
BuildRequires:    R-CRAN-tidyselect >= 1.2.1
BuildRequires:    R-CRAN-dplyr >= 1.2.0
BuildRequires:    R-CRAN-rlang >= 1.1.7
BuildRequires:    R-CRAN-duckplyr >= 1.1.3
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-codeCollection 
BuildRequires:    R-CRAN-fabricatr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-dbplyr >= 2.5.1
Requires:         R-CRAN-lubridate >= 1.9.5
Requires:         R-CRAN-purrr >= 1.2.1
Requires:         R-CRAN-tidyselect >= 1.2.1
Requires:         R-CRAN-dplyr >= 1.2.0
Requires:         R-CRAN-rlang >= 1.1.7
Requires:         R-CRAN-duckplyr >= 1.1.3
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-codeCollection 
Requires:         R-CRAN-fabricatr 
Requires:         R-CRAN-lifecycle 
Requires:         R-stats 
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
