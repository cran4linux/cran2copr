%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PKbioanalysis
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pharmacokinetic Bioanalysis Experiments Design and Exploration

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-reticulate >= 1.44.1
BuildRequires:    R-CRAN-duckdb >= 1.0.0
BuildRequires:    R-CRAN-ggiraph >= 0.9.3
BuildRequires:    R-CRAN-ggforce >= 0.4.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-bsicons 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RTMB 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-RaMS 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-ellmer 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shinychat 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-sortable 
BuildRequires:    R-CRAN-writexl 
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-reticulate >= 1.44.1
Requires:         R-CRAN-duckdb >= 1.0.0
Requires:         R-CRAN-ggiraph >= 0.9.3
Requires:         R-CRAN-ggforce >= 0.4.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-bsicons 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-units 
Requires:         R-stats 
Requires:         R-CRAN-shinyalert 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-rlang 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-rhandsontable 
Requires:         R-methods 
Requires:         R-CRAN-RTMB 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-RaMS 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-ellmer 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shinychat 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-sortable 
Requires:         R-CRAN-writexl 

%description
Automate pharmacokinetic/pharmacodynamic bioanalytical procedures based on
best practices and regulatory recommendations. The package impose
regulatory constrains and sanity checking for common bioanalytical
procedures. Additionally, 'PKbioanalysis' provides a relational
infrastructure for plate management and injection sequence.

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
