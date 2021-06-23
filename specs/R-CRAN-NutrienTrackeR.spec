%global __brp_check_rpaths %{nil}
%global packname  NutrienTrackeR
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Food Composition Information and Dietary Assessment

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 

%description
Provides a tool set for food information and dietary assessment. It uses
food composition data from several reference databases, including: 'USDA'
(United States), 'CIQUAL' (France), and 'BEDCA' (Spain). 'NutrienTrackeR'
calculates the intake levels for both macronutrient and micronutrients,
and compares them with the recommended dietary allowances (RDA). It
includes a number of visualization tools, such as time series plots of
nutrient intake, and pie-charts showing the main foods contributing to the
intake level of a given nutrient. A shiny app exposing the main
functionalities of the package is also provided.

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
