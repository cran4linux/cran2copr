%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  opinAr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Argentina's Public Opinion Toolbox

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sjPlot 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sjPlot 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-lubridate 

%description
A toolbox for working with public opinion data from Argentina. It
facilitates access to microdata and the calculation of indicators of the
Trust in Government Index (ICG), prepared by the Torcuato Di Tella
University. Although we will try to document everything possible in
English, by its very nature Spanish will be the main language. El paquete
fue pensado como una caja de herramientas para el trabajo con datos de
opinión pública de Argentina. El mismo facilita el acceso a los microdatos
y el cálculos de indicadores del Índice de Confianza en el Gobierno (ICG),
elaborado por la Universidad Torcuato Di Tella.

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
