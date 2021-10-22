%global __brp_check_rpaths %{nil}
%global packname  fasstr
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze, Summarize, and Visualize Daily Streamflow Data

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-e1071 >= 1.7.0.1
BuildRequires:    R-CRAN-PearsonDS >= 1.1
BuildRequires:    R-CRAN-fitdistrplus >= 1.0.14
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-CRAN-tidyhydat >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-RcppRoll >= 0.3.0
BuildRequires:    R-CRAN-zyp >= 0.10.1.1
BuildRequires:    R-grDevices 
Requires:         R-CRAN-openxlsx >= 4.1.0
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-e1071 >= 1.7.0.1
Requires:         R-CRAN-PearsonDS >= 1.1
Requires:         R-CRAN-fitdistrplus >= 1.0.14
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-CRAN-tidyhydat >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-RcppRoll >= 0.3.0
Requires:         R-CRAN-zyp >= 0.10.1.1
Requires:         R-grDevices 

%description
The Flow Analysis Summary Statistics Tool for R, 'fasstr', provides
various functions to tidy and screen daily stream discharge data,
calculate and visualize various summary statistics and metrics, and
compute annual trending and volume frequency analyses. It features useful
function arguments for filtering of and handling dates, customizing data
and metrics, and the ability to pull daily data directly from the Water
Survey of Canada hydrometric database
(<https://collaboration.cmc.ec.gc.ca/cmc/hydrometrics/www/>).

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
