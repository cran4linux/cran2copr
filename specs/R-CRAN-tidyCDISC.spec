%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyCDISC
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quick Table Generation & Exploratory Analyses on ADaM-Ish Datasets

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tippy == 0.1.0
BuildRequires:    R-CRAN-cicerone 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggcorrplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-IDEAFilter 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-sjlabelled 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-timevis 
Requires:         R-CRAN-tippy == 0.1.0
Requires:         R-CRAN-cicerone 
Requires:         R-CRAN-config 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggcorrplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-golem 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-IDEAFilter 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-sjlabelled 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-timevis 

%description
Provides users a quick exploratory dive into common visualizations without
writing a single line of code given the users data follows the Analysis
Data Model (ADaM) standards put forth by the Clinical Data Interchange
Standards Consortium (CDISC) <https://www.cdisc.org>. Prominent modules/
features of the application are the Table Generator, Population Explorer,
and the Individual Explorer. The Table Generator allows users to drag and
drop variables and desired statistics (frequencies, means, ANOVA, t-test,
and other summary statistics) into bins that automagically create stunning
tables with validated information. The Population Explorer offers various
plots to visualize general trends in the population from various vantage
points. Plot modules currently include scatter plot, spaghetti plot, box
plot, histogram, means plot, and bar plot. Each plot type allows the user
to plot uploaded variables against one another, and dissect the population
by filtering out certain subjects. Last, the Individual Explorer
establishes a cohesive patient narrative, allowing the user to interact
with patient metrics (params) by visit or plotting important patient
events on a timeline. All modules allow for concise filtering &
downloading bulk outputs into html or pdf formats to save for later.

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
