%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clinDataReview
%global packver   1.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Clinical Data Review Tool

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-clinUtils >= 0.1.0
BuildRequires:    R-CRAN-bookdown 
BuildRequires:    R-CRAN-crosstalk 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-jsonvalidate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-xfun 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-CRAN-clinUtils >= 0.1.0
Requires:         R-CRAN-bookdown 
Requires:         R-CRAN-crosstalk 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-jsonvalidate 
Requires:         R-methods 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-xfun 
Requires:         R-CRAN-base64enc 

%description
Creation of interactive tables, listings and figures ('TLFs') and
associated report for exploratory analysis of data in a clinical trial,
e.g. for clinical oversight activities. Interactive figures include
sunburst, treemap, scatterplot, line plot and barplot of counts data.
Interactive tables include table of summary statistics (as counts of
adverse events, enrollment table) and listings. Possibility to compare
data (summary table or listing) across two data batches/sets. A clinical
data review report is created via study-specific configuration files and
template 'R Markdown' reports contained in the package.

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
