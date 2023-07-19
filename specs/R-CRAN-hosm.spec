%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hosm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          High Order Spatial Matrix

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-readxl 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-units 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-readxl 

%description
Automatically displays the order and spatial weighting matrix of the
distance between locations. This concept was derived from the research of
Mubarak, Aslanargun, and Siklar (2021) <doi:10.52403/ijrr.20211150> and
Mubarak, Aslanargun, and Siklar (2022) <doi:10.17654/0972361722052>.
Distance data between locations can be imported from 'Ms. Excel', 'maps'
package or created in 'R' programming directly. This package also provides
5 simulations of distances between locations derived from fictitious data,
the 'maps' package, and from research by Mubarak, Aslanargun, and Siklar
(2022) <doi:10.29244/ijsa.v6i1p90-100>.

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
