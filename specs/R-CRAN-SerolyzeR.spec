%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SerolyzeR
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Reading, Quality Control and Preprocessing of MBA (Multiplex Bead Assay) Data

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-nplr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-svglite 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-nplr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-grid 
Requires:         R-CRAN-png 
Requires:         R-tools 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-svglite 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-rlang 

%description
Speeds up the process of loading raw data from MBA (Multiplex Bead Assay)
examinations, performs quality control checks, and automatically
normalises the data, preparing it for more advanced, downstream tasks. The
main objective of the package is to create a simple environment for a
user, who does not necessarily have experience with R language. The
package is developed within the project 'PvSTATEM', which is an
international project aiming for malaria elimination.

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
