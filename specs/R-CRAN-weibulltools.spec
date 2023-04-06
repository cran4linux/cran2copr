%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  weibulltools
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methods for Life Data Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-lifecycle >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-segmented 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-lifecycle >= 1.0.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-segmented 
Requires:         R-CRAN-tibble 

%description
Provides statistical methods and visualizations that are often used in
reliability engineering. Comprises a compact and easily accessible set of
methods and visualization tools that make the examination and adjustment
as well as the analysis and interpretation of field data (and bench tests)
as simple as possible. Non-parametric estimators like Median Ranks,
Kaplan-Meier (Abernethy, 2006, <ISBN:978-0-9653062-3-2>), Johnson
(Johnson, 1964, <ISBN:978-0444403223>), and Nelson-Aalen for failure
probability estimation within samples that contain failures as well as
censored data are included. The package supports methods like Maximum
Likelihood and Rank Regression, (Genschel and Meeker, 2010,
<DOI:10.1080/08982112.2010.503447>) for the estimation of multiple
parametric lifetime distributions, as well as the computation of
confidence intervals of quantiles and probabilities using the delta method
related to Fisher's confidence intervals (Meeker and Escobar, 1998,
<ISBN:9780471673279>) and the beta-binomial confidence bounds. If desired,
mixture model analysis can be done with segmented regression and the EM
algorithm. Besides the well-known Weibull analysis, the package also
contains Monte Carlo methods for the correction and completion of
imprecisely recorded or unknown lifetime characteristics. (Verband der
Automobilindustrie e.V. (VDA), 2016, <ISSN:0943-9412>). Plots are created
statically ('ggplot2') or interactively ('plotly') and can be customized
with functions of the respective visualization package. The graphical
technique of probability plotting as well as the addition of regression
lines and confidence bounds to existing plots are supported.

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
