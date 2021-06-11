%global packname  ecocomDP
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Work with Datasets in the Ecological Community Design Pattern

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.3
BuildRequires:    R-CRAN-EML >= 2.0.5
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-geosphere >= 1.5
BuildRequires:    R-CRAN-neonUtilities >= 1.3.3
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-xml2 >= 1.3.0
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.13.0
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-tidyr >= 0.6.1
BuildRequires:    R-CRAN-emld >= 0.5.1
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-uuid >= 0.1.4
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.3.3
Requires:         R-CRAN-EML >= 2.0.5
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-geosphere >= 1.5
Requires:         R-CRAN-neonUtilities >= 1.3.3
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-xml2 >= 1.3.0
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-data.table >= 1.13.0
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-tidyr >= 0.6.1
Requires:         R-CRAN-emld >= 0.5.1
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-uuid >= 0.1.4
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Tools to create, use, and convert 'ecocomDP' datasets. 'ecocomDP' is a
dataset design pattern for harmonizing ecological community surveys in a
research question agnostic format, from source datasets published across
multiple repositories, and with methods that keep the derived datasets
up-to-date as the underlying sources change.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
