%global __brp_check_rpaths %{nil}
%global packname  INSPECTumours
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          IN-vivo reSPonsE Classification of Tumours

License:          Apache License (== 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-brms 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggeffects 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-modelr 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-CRAN-shinyFeedback 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinytoastr 
BuildRequires:    R-CRAN-shinyvalidate 
BuildRequires:    R-CRAN-tidybayes 
BuildRequires:    R-CRAN-tippy 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-vroom 
BuildRequires:    R-CRAN-waiter 
Requires:         R-CRAN-brms 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggeffects 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-modelr 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyalert 
Requires:         R-CRAN-shinyFeedback 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinytoastr 
Requires:         R-CRAN-shinyvalidate 
Requires:         R-CRAN-tidybayes 
Requires:         R-CRAN-tippy 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-vroom 
Requires:         R-CRAN-waiter 

%description
This is a shiny app used for the statistical classifying and analysing
pre-clinical tumour responses.

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
