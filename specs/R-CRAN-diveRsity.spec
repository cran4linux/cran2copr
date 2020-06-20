%global packname  diveRsity
%global packver   1.9.90
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.90
Release:          1%{?dist}
Summary:          A Comprehensive, General Purpose Population Genetics AnalysisPackage

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-grid 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-grid 

%description
Allows the calculation of both genetic diversity partition statistics,
genetic differentiation statistics, and locus informativeness for ancestry
assignment. It also provides users with various option to calculate
bootstrapped 95% confidence intervals both across loci, for pairwise
population comparisons, and to plot these results interactively. Parallel
computing capabilities and pairwise results without bootstrapping are
provided. Also calculates F-statistics from Weir and Cockerham (1984).
Various plotting features are provided, as well as Chi-square tests of
genetic heterogeneity. Functionality for the calculation of various
diversity parameters is possible for RAD-seq derived SNP data sets
containing thousands of marker loci. A shiny application for the
development of microsatellite multiplexes is also available.

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

%files
%{rlibdir}/%{packname}
