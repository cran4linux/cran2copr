%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  presenter
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Present Data with Style

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-randomcoloR 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-berryFunctions 
BuildRequires:    R-CRAN-rvg 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-formattable 
BuildRequires:    R-CRAN-framecleaner 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-randomcoloR 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-berryFunctions 
Requires:         R-CRAN-rvg 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-formattable 
Requires:         R-CRAN-framecleaner 

%description
Consists of custom wrapper functions using packages 'openxlsx',
'flextable', and 'officer' to create highly formatted MS office friendly
output of your data frames. These viewer friendly outputs are intended to
match expectations of professional looking presentations in business and
consulting scenarios. The functions are opinionated in the sense that they
expect the input data frame to have certain properties in order to take
advantage of the automated formatting.

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
