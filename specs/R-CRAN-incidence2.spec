%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  incidence2
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Compute, Handle and Plot Incidence of Dated Events

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ympes >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-grates >= 1.0.0
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-ympes >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-grates >= 1.0.0
Requires:         R-grDevices 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-pillar 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-vctrs 

%description
Provides functions and classes to compute, handle and visualise incidence
from dated events for a defined time interval. Dates can be provided in
various standard formats. The class 'incidence2' is used to store computed
incidence and can be easily manipulated, subsetted, and plotted. This
package is part of the RECON (<https://www.repidemicsconsortium.org/>)
toolkit for outbreak analysis (<https://www.reconverse.org>).

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
