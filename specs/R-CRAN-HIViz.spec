%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HIViz
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Dashboard for 'HIV' Data Visualization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-paletteer 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-tools 
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-paletteer 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-tools 

%description
An interactive 'Shiny' dashboard for visualizing and exploring key metrics
related to HIV/AIDS, including prevalence, incidence, mortality, and
treatment coverage. The dashboard is designed to work with a dataset
containing specific columns with standardized names. These columns must be
present in the input data for the app to function properly: year: Numeric
year of the data (e.g. 2010, 2021); sex: Gender classification (e.g. Male,
Female); age_group: Age bracket (e.g. 15–24, 25–34); hiv_prevalence:
Estimated HIV prevalence percentage; hiv_incidence: Number of new HIV
cases per year; aids_deaths: Total AIDS-related deaths; plhiv: Estimated
number of people living with HIV; art_coverage: Percentage receiving
antiretroviral therapy (ART); testing_coverage: HIV testing services
coverage; causes: Description of likely HIV transmission cause (e.g.
unprotected sex, drug use). The dataset structure must strictly follow
this column naming convention for the dashboard to render correctly.

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
