%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FAfA
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Factor Analysis for All

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-EFA.MRFA 
BuildRequires:    R-CRAN-EFA.dimensions 
BuildRequires:    R-CRAN-EFAtools 
BuildRequires:    R-CRAN-EGAnet 
BuildRequires:    R-CRAN-MBESS 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-ggcorrplot 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-mctest 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-mvnormalTest 
BuildRequires:    R-CRAN-pastecs 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-psychometric 
BuildRequires:    R-CRAN-semPlot 
BuildRequires:    R-CRAN-semTools 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-sirt 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-readxl 
Requires:         R-CRAN-EFA.MRFA 
Requires:         R-CRAN-EFA.dimensions 
Requires:         R-CRAN-EFAtools 
Requires:         R-CRAN-EGAnet 
Requires:         R-CRAN-MBESS 
Requires:         R-CRAN-config 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-ggcorrplot 
Requires:         R-CRAN-golem 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-mctest 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-mvnormalTest 
Requires:         R-CRAN-pastecs 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-psychometric 
Requires:         R-CRAN-semPlot 
Requires:         R-CRAN-semTools 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-sirt 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-readxl 

%description
Provides a comprehensive Shiny-based graphical user interface for
conducting a wide range of factor analysis procedures. 'FAfA' (Factor
Analysis for All) guides users through data uploading, assumption checking
(descriptives, collinearity, multivariate normality, outliers), data
wrangling (variable exclusion, data splitting), factor retention analysis
(e.g., Parallel Analysis, Hull method, EGA), Exploratory Factor Analysis
(EFA) with various rotation and extraction methods, Confirmatory Factor
Analysis (CFA) for model testing, Reliability Analysis (e.g., Cronbach's
Alpha, McDonald's Omega), Measurement Invariance testing across groups,
and item weighting techniques. The application leverages established R
packages such as 'lavaan' and 'psych' to perform these analyses, offering
an accessible platform for researchers and students. Results are presented
in user-friendly tables and plots, with options for downloading outputs.

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
