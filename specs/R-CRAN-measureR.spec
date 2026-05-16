%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  measureR
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Educational and Psychological Measurement

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-CTT 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-irr 
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-semPlot 
BuildRequires:    R-CRAN-semptools 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-CTT 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-irr 
Requires:         R-CRAN-mirt 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-semPlot 
Requires:         R-CRAN-semptools 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-viridisLite 

%description
'Provides an interactive toolkit for educational and psychological
measurement implemented using the 'shiny' framework. The package supports
content validity analysis, dimensionality assessment, and Classical Test
Theory using the 'CTT' package (Willse, 2018)
<doi:10.32614/CRAN.package.CTT>. Item Response Theory (IRT) analyses are
conducted via 'mirt' (Chalmers, 2012) <doi:10.18637/jss.v048.i06>.
Exploratory Factor Analysis is performed using 'psych' (Revelle, 2025),
while Confirmatory Factor Analysis (CFA) and Structural Equation Modeling
(SEM) are based on the 'lavaan' framework (Rosseel, 2012)
<doi:10.18637/jss.v048.i02>. The CFA/SEM module features interactive model
specification, automatic model comparison, modification indices,
comprehensive fit diagnostics, path diagram visualization, and HTML report
generation. The application allows users to upload data, evaluate
statistical models, visualize results, and export outputs through an
intuitive graphical interface without requiring programming experience.

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
