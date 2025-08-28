%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fingerPro
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Comprehensive Package for Sediment Source Unmixing

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-MASS >= 7.3.45
BuildRequires:    R-CRAN-plotly >= 4.10.3
BuildRequires:    R-grid >= 3.1.1
BuildRequires:    R-CRAN-car >= 3.0.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-crayon >= 1.4.2
BuildRequires:    R-CRAN-GGally >= 1.3.2
BuildRequires:    R-CRAN-rgl >= 1.2.8
BuildRequires:    R-CRAN-Ternary >= 1.2.2
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-reshape >= 0.8.7
BuildRequires:    R-CRAN-klaR >= 0.6.12
BuildRequires:    R-CRAN-scales >= 0.5.0
BuildRequires:    R-CRAN-RcppProgress >= 0.4
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-CRAN-RcppGSL 
Requires:         R-CRAN-MASS >= 7.3.45
Requires:         R-CRAN-plotly >= 4.10.3
Requires:         R-grid >= 3.1.1
Requires:         R-CRAN-car >= 3.0.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-crayon >= 1.4.2
Requires:         R-CRAN-GGally >= 1.3.2
Requires:         R-CRAN-rgl >= 1.2.8
Requires:         R-CRAN-Ternary >= 1.2.2
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-reshape >= 0.8.7
Requires:         R-CRAN-klaR >= 0.6.12
Requires:         R-CRAN-scales >= 0.5.0
Requires:         R-CRAN-RcppProgress >= 0.4
Requires:         R-CRAN-Rcpp >= 0.11.3

%description
"This package quantifies the provenance of sediments in a catchment or
study area. Based on a characterization of the sediment sources and the
end sediment mixtures, a mixing model algorithm is applied to the sediment
mixtures to estimate the relative contribution of each potential source.
The package includes several graphs to help users in their data
understanding, such as box plots, correlation, PCA, and LDA graphs. In
addition, new developments such as the Consensus Ranking (CR), Consistent
Tracer Selection (CTS), and Linear Variability Propagation (LVP) methods
are included to correctly apply the fingerprinting technique and increase
dataset and model understanding. A new method based on Conservative
Balance (CB) method has also been included to enable the use of isotopic
tracers."

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
