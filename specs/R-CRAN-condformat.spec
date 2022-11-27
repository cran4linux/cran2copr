%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  condformat
%global packver   0.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0
Release:          1%{?dist}%{?buildtag}
Summary:          Conditional Formatting in Data Frames

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.1.5
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-htmlTable >= 1.9
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.3.4
BuildRequires:    R-CRAN-knitr >= 1.20
BuildRequires:    R-CRAN-rmarkdown >= 1.10
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.7
BuildRequires:    R-CRAN-htmltools >= 0.3.6
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-gtable >= 0.2.0
BuildRequires:    R-grDevices 
Requires:         R-CRAN-openxlsx >= 4.1.5
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-htmlTable >= 1.9
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-tibble >= 1.3.4
Requires:         R-CRAN-knitr >= 1.20
Requires:         R-CRAN-rmarkdown >= 1.10
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.7
Requires:         R-CRAN-htmltools >= 0.3.6
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-gtable >= 0.2.0
Requires:         R-grDevices 

%description
Apply and visualize conditional formatting to data frames in R. It renders
a data frame with cells formatted according to criteria defined by rules,
using a tidy evaluation syntax. The table is printed either opening a web
browser or within the 'RStudio' viewer if available. The conditional
formatting rules allow to highlight cells matching a condition or add a
gradient background to a given column. This package supports both 'HTML'
and 'LaTeX' outputs in 'knitr' reports, and exporting to an 'xlsx' file.

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
