%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidytlg
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Create TLGs using the 'tidyverse'

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-huxtable >= 5.1.0
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-stats >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-glue >= 1.4.2
BuildRequires:    R-CRAN-crayon >= 1.4.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-readxl >= 1.3.1
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-cellranger >= 1.1.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-forcats >= 0.5.1
BuildRequires:    R-CRAN-rlang >= 0.4.10
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-assertthat >= 0.2.1
BuildRequires:    R-CRAN-rstudioapi >= 0.13
BuildRequires:    R-CRAN-png >= 0.1.7
BuildRequires:    R-methods 
Requires:         R-CRAN-huxtable >= 5.1.0
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-stats >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-glue >= 1.4.2
Requires:         R-CRAN-crayon >= 1.4.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-readxl >= 1.3.1
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-cellranger >= 1.1.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-forcats >= 0.5.1
Requires:         R-CRAN-rlang >= 0.4.10
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-rstudioapi >= 0.13
Requires:         R-CRAN-png >= 0.1.7
Requires:         R-methods 

%description
Generate tables, listings, and graphs (TLG) using 'tidyverse.' Tables can
be created functionally, using a standard TLG process, or by specifying
table and column metadata to create generic analysis summaries. The
'envsetup' package can also be leveraged to create environments for table
creation.

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
