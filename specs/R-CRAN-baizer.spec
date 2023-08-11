%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  baizer
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Useful Functions for Data Processing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-diffobj 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rematch2 
BuildRequires:    R-CRAN-seriation 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-tibble >= 3.1
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-curl 
Requires:         R-CRAN-diffobj 
Requires:         R-grDevices 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rematch2 
Requires:         R-CRAN-seriation 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 

%description
In ancient Chinese mythology, Bai Ze is a divine creature that knows the
needs of everything. 'baizer' provides data processing functions
frequently used by the author. Hope this package also knows what you want!

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
