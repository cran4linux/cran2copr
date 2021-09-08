%global __brp_check_rpaths %{nil}
%global packname  isobxr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Stable Isotope Box Modelling in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-metR 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-fs 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-rlang 
Requires:         R-grid 
Requires:         R-CRAN-metR 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-fs 

%description
A set of functions to run simple and composite box-models to describe the
dynamic or static distribution of stable isotopes in open or closed
systems. The package also allows the sweeping of many parameters in both
static and dynamic conditions. It also comes with a post-run plotting
interface built under shiny. The mathematical models used in this package
are derived from Albarede, 1995, Introduction to Geochemical Modelling,
Cambridge University Press, Cambridge <doi:10.1017/CBO9780511622960>.

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
