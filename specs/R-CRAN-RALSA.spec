%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RALSA
%global packver   1.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.5
Release:          1%{?dist}%{?buildtag}
Summary:          R Analyzer for Large-Scale Assessments

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-archive 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-import 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-rclipboard 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-archive 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-import 
Requires:         R-methods 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-rclipboard 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 

%description
Download, prepare and analyze data from large-scale assessments and
surveys with complex sampling and assessment design (see 'Rutkowski', 2010
<doi:10.3102/0013189X10363170>). Such studies are, for example,
international assessments like 'TIMSS', 'PIRLS' and 'PISA'. A graphical
interface is available for the non-technical user.The package includes
functions to covert the original data from 'SPSS' into 'R' data sets
keeping the user-defined missing values, merge data from different
respondents and/or countries, generate variable dictionaries, modify data,
produce descriptive statistics (percentages, means, percentiles,
benchmarks) and multivariate statistics (correlations, linear regression,
binary logistic regression). The number of supported studies and analysis
types will increase in future. For a general presentation of the package,
see 'Mirazchiyski', 2021a (<doi:10.1186/s40536-021-00114-4>). For detailed
technical aspects of the package, see 'Mirazchiyski', 2021b
(<doi:10.3390/psych3020018>).

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
