%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ecocomDP
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Create, Use, and Convert ecocomDP Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-neonUtilities >= 2.1.1
BuildRequires:    R-CRAN-EML >= 2.0.5
BuildRequires:    R-CRAN-emld >= 0.5.1
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-neonOS 
Requires:         R-CRAN-neonUtilities >= 2.1.1
Requires:         R-CRAN-EML >= 2.0.5
Requires:         R-CRAN-emld >= 0.5.1
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-neonOS 

%description
Work with the Ecological Community Data Design Pattern. 'ecocomDP' is a
flexible data model for harmonizing ecological community surveys, in a
research question agnostic format, from source data published across
repositories, and with methods that keep the derived data up-to-date as
the underlying sources change. Described in O'Brien et al. (2021),
<doi:10.1016/j.ecoinf.2021.101374>.

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
