%global packname  lessR
%global packver   3.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.9.7
Release:          1%{?dist}%{?buildtag}
Summary:          Less Code, More Results

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-triangle 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-knitr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-leaps 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-triangle 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-knitr 

%description
Each function accomplishes the work of several or more standard R
functions. For example, two function calls, Read() and CountAll(), read
the data and generate summary statistics for all variables in the data
frame, plus histograms and bar charts as appropriate. Other functions
provide for descriptive statistics, a comprehensive regression analysis,
analysis of variance and t-test, plotting including the introduced here
Violin/Box/Scatter plot for a numerical variable, bar chart, histogram,
box plot, density curves, calibrated power curve, reading multiple data
formats with the same function call, variable labels, color themes,
Trellis graphics and a built-in help system. Also includes a confirmatory
factor analysis of multiple indicator measurement models, pedagogical
routines for data simulation such as for the Central Limit Theorem, and
generation and rendering of R markdown instructions for interpretative
output.

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
