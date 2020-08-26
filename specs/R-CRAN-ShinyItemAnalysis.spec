%global packname  ShinyItemAnalysis
%global packver   1.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Test and Item Analysis via Shiny

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-difR >= 5.0
BuildRequires:    R-CRAN-difNLR >= 1.3.2
BuildRequires:    R-CRAN-mirt >= 1.24
BuildRequires:    R-CRAN-shiny >= 1.0.3
BuildRequires:    R-CRAN-shinyjs >= 0.9
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-CTT 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-deltaPlotR 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-ltm 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-psychometric 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-difR >= 5.0
Requires:         R-CRAN-difNLR >= 1.3.2
Requires:         R-CRAN-mirt >= 1.24
Requires:         R-CRAN-shiny >= 1.0.3
Requires:         R-CRAN-shinyjs >= 0.9
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-CTT 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-deltaPlotR 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggdendro 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-ltm 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-msm 
Requires:         R-nnet 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-psychometric 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-xtable 

%description
Interactive shiny application for analysis of educational tests and their
items.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
