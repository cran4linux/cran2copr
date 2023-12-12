%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ruminate
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Pharmacometrics Data Transformation and Analysis Tool

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-onbrand >= 1.0.3
BuildRequires:    R-CRAN-PKNCA >= 0.10.2
BuildRequires:    R-CRAN-formods >= 0.1.2
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-onbrand >= 1.0.3
Requires:         R-CRAN-PKNCA >= 0.10.2
Requires:         R-CRAN-formods >= 0.1.2
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-yaml 

%description
Exploration of pharmacometrics data involves both general tools
(transformation and plotting) and specific techniques (non-compartmental
analysis). This kind of exploration is generally accomplished by utilizing
different packages. The purpose of 'ruminate' is to create a 'shiny'
interface to make these tools more broadly available while creating
reproducible results.

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
