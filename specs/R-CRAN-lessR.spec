%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lessR
%global packver   4.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Less Code, More Results

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
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

%description
Each function accomplishes the work of several or more standard R
functions. For example, two function calls, Read() and CountAll(), read
the data and generate summary statistics for all variables in the data
frame, plus histograms and bar charts as appropriate. Other functions
provide for comprehensive summary statistics via pivot tables, a
comprehensive regression analysis, analysis of variance and t-test,
visualizations including the Violin/Box/Scatter plot for a numerical
variable, bar chart, histogram, box plot, density curves, calibrated power
curve, reading multiple data formats with the same function call, variable
labels, color themes, and Trellis graphics. Also includes a confirmatory
factor analysis of multiple indicator measurement models, pedagogical
routines for data simulation such as for the Central Limit Theorem,
generation and rendering of R markdown instructions for interpretative
output, and interactive visualizations.

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
