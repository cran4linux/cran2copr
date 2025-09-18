%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BOLDconnectR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Retrieve, Transform and Analyze the Barcode of Life Data Systems Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 5.5
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-maps >= 3.3
BuildRequires:    R-CRAN-vegan >= 2.5.7
BuildRequires:    R-CRAN-skimr >= 2.1.2
BuildRequires:    R-CRAN-BAT >= 2.0
BuildRequires:    R-CRAN-jsonlite >= 1.7
BuildRequires:    R-CRAN-httr >= 1.4.2
BuildRequires:    R-CRAN-data.table >= 1.13
BuildRequires:    R-CRAN-tidyr >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.1
BuildRequires:    R-CRAN-sf >= 0.9.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-utils 
Requires:         R-CRAN-ape >= 5.5
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-maps >= 3.3
Requires:         R-CRAN-vegan >= 2.5.7
Requires:         R-CRAN-skimr >= 2.1.2
Requires:         R-CRAN-BAT >= 2.0
Requires:         R-CRAN-jsonlite >= 1.7
Requires:         R-CRAN-httr >= 1.4.2
Requires:         R-CRAN-data.table >= 1.13
Requires:         R-CRAN-tidyr >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.1
Requires:         R-CRAN-sf >= 0.9.4
Requires:         R-methods 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-utils 

%description
Facilitates retrieval, transformation and analysis of the data from the
Barcode of Life Data Systems (BOLD) database <https://boldsystems.org/>.
This package allows both public and private user data to be easily
downloaded into the R environment using a variety of inputs such as: IDs
(processid, sampleid), BINs, dataset codes, project codes, taxonomy,
geography etc. It provides frictionless data conversion into formats
compatible with other R-packages and third-party tools, as well as
functions for sequence alignment & clustering, biodiversity analysis and
spatial mapping.

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
