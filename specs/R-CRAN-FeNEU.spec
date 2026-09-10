%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FeNEU
%global packver   3.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Routines for Evaluating Forest Inventory Data

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildArch:        noarch
BuildRequires:    R-CRAN-ForestElementsR >= 3.0.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-ForestElementsR >= 3.0.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-lifecycle 
Requires:         R-parallel 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-sf 

%description
Provides a collection of routines for evaluating data from larger forest
management units, typically sample inventories, but also stand-wise
inventories. The idea is to support modern forest planning approaches and
to be open by design to new data sources and evaluation methods. For the
methodological background of forest inventories see Kangas and Maltamo
(2006) "Forest Inventory: Methodology and Applications"
<doi:10.1007/1-4020-4381-3>.

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
