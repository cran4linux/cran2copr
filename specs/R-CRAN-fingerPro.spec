%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fingerPro
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Unmixing Model Framework

License:          GPL-2
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
Requires:         R-CRAN-Ternary >= 1.2.2
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-reshape >= 0.8.7
Requires:         R-CRAN-klaR >= 0.6.12
Requires:         R-CRAN-scales >= 0.5.0
Requires:         R-CRAN-RcppProgress >= 0.4
Requires:         R-CRAN-Rcpp >= 0.11.3

%description
Quantifies the provenance of sediments by applying a mixing model
algorithm to end sediment mixtures based on a comprehensive
characterization of the sediment sources. The 'fingerPro' model builds
upon the foundational concept of using mass balance linear equations for
sediment source quantification by incorporating several distinct technical
advancements. It employs an optimization approach to normalize
discrepancies in tracer ranges and minimize the objective function. Latin
hypercube sampling is used to explore all possible combinations of source
contributions (0-100%%), mitigating the risk of local minima. Uncertainty
in source estimates is quantified through a Monte Carlo routine, and the
model includes additional metrics, such as the normalized error of the
virtual mixture, to detect mathematical inconsistencies, non-physical
solutions, and biases. A new linear variability propagation (LVP) method
is also included to address and quantify potential bias in model outcomes,
particularly when dealing with dominant or non-contributing sources and
high source variability, offering a significant advancement for field
studies where direct comparison with theoretical apportionments is not
feasible. In addition to the unmixing model, a complete framework for
tracer selection is included. Several methods are implemented to evaluate
tracer behaviour by considering both source and mixture information. These
include the Consistent Tracer Selection (CTS) method to explore all tracer
combinations and select the optimal ones improving the robustness and
interpretability of the model results. A Conservative Balance (CB) method
is also incorporated to enable the use of isotopic tracers. The package
also provides several graphical tools to support data exploration and
interpretation, including box plots, correlation plots, Linear
Discriminant Analysis (LDA) and Principal Component Analysis (PCA).

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
