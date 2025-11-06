%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MLmorph
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Integrating Morphological Modeling and Machine Learning for Decision Support

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 6.0.94
BuildRequires:    R-CRAN-randomForest >= 4.7.1.1
BuildRequires:    R-stats >= 4.3.0
BuildRequires:    R-utils >= 4.3.0
BuildRequires:    R-CRAN-openxlsx >= 4.2.5.2
BuildRequires:    R-CRAN-plotly >= 4.10.4
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-shinyjs >= 2.1.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.8
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-shiny >= 1.10.0
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-shinyFiles >= 0.9.3
BuildRequires:    R-CRAN-bslib >= 0.9.0
BuildRequires:    R-CRAN-htmltools >= 0.5.8.1
BuildRequires:    R-CRAN-reactable >= 0.4.4
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-caret >= 6.0.94
Requires:         R-CRAN-randomForest >= 4.7.1.1
Requires:         R-stats >= 4.3.0
Requires:         R-utils >= 4.3.0
Requires:         R-CRAN-openxlsx >= 4.2.5.2
Requires:         R-CRAN-plotly >= 4.10.4
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-shinyjs >= 2.1.0
Requires:         R-CRAN-jsonlite >= 1.8.8
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-shiny >= 1.10.0
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-shinyFiles >= 0.9.3
Requires:         R-CRAN-bslib >= 0.9.0
Requires:         R-CRAN-htmltools >= 0.5.8.1
Requires:         R-CRAN-reactable >= 0.4.4
Requires:         R-CRAN-magrittr 

%description
Integrating morphological modeling with machine learning to support
structured decision-making (e.g., in management and consulting). The
package enumerates a morphospace of feasible configurations and uses
random forests to estimate class probabilities over that space, bridging
deductive model exploration with empirical validation. It includes
utilities for factorizing inputs, model training, morphospace
construction, and an interactive 'shiny' app for scenario exploration.

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
