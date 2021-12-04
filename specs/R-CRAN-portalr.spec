%global __brp_check_rpaths %{nil}
%global packname  portalr
%global packver   0.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.9
Release:          1%{?dist}%{?buildtag}
Summary:          Create Useful Summaries of the Portal Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-clisymbols 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-lunar 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-clisymbols 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-lunar 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-zoo 

%description
Download and generate summaries for the rodent, plant, ant, and weather
data from the Portal Project. Portal is a long-term (and ongoing)
experimental monitoring site in the Chihuahua desert. The raw data files
can be found at <https://github.com/weecology/portaldata>.

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
