%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  genogeographer
%global packver   0.1.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.19
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Analysing Forensic Ancestry Informative Markers

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-rlang 

%description
Evaluates likelihood ratio tests for alleged ancestry. Implements the
methods of Tvedebrink et al (2018) <doi:10.1016/j.tpb.2017.12.004>.

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
