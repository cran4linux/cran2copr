%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jstor
%global packver   0.3.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.11
Release:          1%{?dist}%{?buildtag}
Summary:          Read Data from JSTOR/DfR

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-readr >= 2.0.0
BuildRequires:    R-CRAN-stringr >= 1.3.0
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 0.7.2
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-CRAN-furrr >= 0.1.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-readr >= 2.0.0
Requires:         R-CRAN-stringr >= 1.3.0
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyr >= 0.7.2
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-CRAN-furrr >= 0.1.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pryr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cli 

%description
Functions and helpers to import metadata, ngrams and full-texts delivered
by Data for Research by JSTOR.

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
