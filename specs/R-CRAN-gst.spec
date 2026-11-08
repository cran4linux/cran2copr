%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gst
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Global Statistical Tests for Multiple Endpoints

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forestploter 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-pwr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-bsicons 
BuildRequires:    R-CRAN-datapasta 
BuildRequires:    R-CRAN-sortable 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rclipboard 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forestploter 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-multcomp 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-plotly 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-pwr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-bsicons 
Requires:         R-CRAN-datapasta 
Requires:         R-CRAN-sortable 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rclipboard 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-rlang 

%description
Design and evaluate global statistical tests (GST) that combine several
endpoints into one test, including O'Brien's ordinary and generalized
least squares tests (O'Brien (1984) <doi:10.2307/2531158>), power and
sample size calculations, and an O'Brien-based truncated closed testing
procedure (Luo et al. (2025) <doi:10.1002/pst.70010>). Two 'shiny'
applications support interactive power calculation and the creation of
forest plots for multiple endpoints from summary statistics.

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
