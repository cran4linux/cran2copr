%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vvdoctor
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Test App with R 'shiny'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-datamods 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-exact2x2 
BuildRequires:    R-CRAN-irr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rintrojs 
BuildRequires:    R-CRAN-rstatix 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
Requires:         R-CRAN-datamods 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-exact2x2 
Requires:         R-CRAN-irr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rintrojs 
Requires:         R-CRAN-rstatix 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 

%description
Provides a user-friendly R 'shiny' app for performing various statistical
tests on datasets. It allows users to upload data in numerous formats and
perform statistical analyses. The app dynamically adapts its options based
on the selected columns and supports both single and multiple column
comparisons. The app's user interface is designed to streamline the
process of selecting datasets, columns, and test options, making it easy
for users to explore and interpret their data. The underlying functions
for statistical tests are well-organized and can be used independently
within other R scripts.

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
