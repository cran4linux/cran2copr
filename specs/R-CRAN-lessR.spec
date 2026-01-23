%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lessR
%global packver   4.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Less Code with More Comprehensive Results

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.11.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-conflicted 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-plotly >= 4.11.0
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-leaps 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-conflicted 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-htmltools 

%description
Each function replaces multiple standard R functions. For example, two
function calls, Read() and CountAll(), generate summary statistics for all
variables in the data frame, plus histograms and bar charts. Other
functions provide data aggregation via pivot tables; comprehensive
regression, ANOVA, and t-test; visualizations including integrated
Violin/Box/Scatter plot for a numerical variable, bar chart, histogram,
box plot, density curves, calibrated power curve; reading multiple data
formats with the same call; variable labels; time series with aggregation
and forecasting; color themes; and Trellis (facet) graphics. Also includes
a confirmatory factor analysis of multiple-indicator measurement models,
pedagogical routines for data simulation (e.g., Central Limit Theorem),
generation and rendering of regression instructions for interpretative
output, and both interactive construction of visualizations and
interactive visualizations with plotly.

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
