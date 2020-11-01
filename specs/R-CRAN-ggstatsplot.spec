%global packname  ggstatsplot
%global packver   0.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.5
Release:          1%{?dist}%{?buildtag}
Summary:          'ggplot2' Based Plots with Statistical Details

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-broomExtra >= 4.1.0
BuildRequires:    R-CRAN-ipmisc >= 4.1.0
BuildRequires:    R-CRAN-pairwiseComparisons >= 3.1.0
BuildRequires:    R-CRAN-parameters >= 0.9.0
BuildRequires:    R-CRAN-statsExpressions >= 0.6.0
BuildRequires:    R-CRAN-effectsize >= 0.4.0
BuildRequires:    R-CRAN-insight >= 0.10.0
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggcorrplot 
BuildRequires:    R-CRAN-ggExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggsignif 
BuildRequires:    R-CRAN-paletteer 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-broomExtra >= 4.1.0
Requires:         R-CRAN-ipmisc >= 4.1.0
Requires:         R-CRAN-pairwiseComparisons >= 3.1.0
Requires:         R-CRAN-parameters >= 0.9.0
Requires:         R-CRAN-statsExpressions >= 0.6.0
Requires:         R-CRAN-effectsize >= 0.4.0
Requires:         R-CRAN-insight >= 0.10.0
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggcorrplot 
Requires:         R-CRAN-ggExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggsignif 
Requires:         R-CRAN-paletteer 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
Extension of 'ggplot2', 'ggstatsplot' creates graphics with details from
statistical tests included in the plots themselves. It provides an easier
API to generate information-rich plots for statistical analysis of
continuous (violin plots, scatterplots, histograms, dot plots,
dot-and-whisker plots) or categorical (pie and bar charts) data.
Currently, it supports only the most common types of statistical tests:
parametric, nonparametric, robust, and Bayesian versions of t-test/ANOVA,
correlation analyses, contingency table analysis, meta-analysis, and
regression analyses.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
