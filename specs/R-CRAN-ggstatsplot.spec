%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggstatsplot
%global packver   0.12.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.4
Release:          1%{?dist}%{?buildtag}
Summary:          'ggplot2' Based Plots with Statistical Details

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-glue >= 1.7.0
BuildRequires:    R-CRAN-paletteer >= 1.6.0
BuildRequires:    R-CRAN-statsExpressions >= 1.5.5
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-patchwork >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-rlang >= 1.1.4
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-ggrepel >= 0.9.5
BuildRequires:    R-CRAN-correlation >= 0.8.5
BuildRequires:    R-CRAN-ggsignif >= 0.6.4
BuildRequires:    R-CRAN-ggside >= 0.3.1
BuildRequires:    R-CRAN-parameters >= 0.22.0
BuildRequires:    R-CRAN-insight >= 0.20.1
BuildRequires:    R-CRAN-performance >= 0.12.0
BuildRequires:    R-CRAN-datawizard >= 0.11.0
BuildRequires:    R-CRAN-ggcorrplot >= 0.1.4.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-glue >= 1.7.0
Requires:         R-CRAN-paletteer >= 1.6.0
Requires:         R-CRAN-statsExpressions >= 1.5.5
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-patchwork >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-rlang >= 1.1.4
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-ggrepel >= 0.9.5
Requires:         R-CRAN-correlation >= 0.8.5
Requires:         R-CRAN-ggsignif >= 0.6.4
Requires:         R-CRAN-ggside >= 0.3.1
Requires:         R-CRAN-parameters >= 0.22.0
Requires:         R-CRAN-insight >= 0.20.1
Requires:         R-CRAN-performance >= 0.12.0
Requires:         R-CRAN-datawizard >= 0.11.0
Requires:         R-CRAN-ggcorrplot >= 0.1.4.1
Requires:         R-stats 
Requires:         R-utils 

%description
Extension of 'ggplot2', 'ggstatsplot' creates graphics with details from
statistical tests included in the plots themselves. It provides an easier
syntax to generate information-rich plots for statistical analysis of
continuous (violin plots, scatterplots, histograms, dot plots,
dot-and-whisker plots) or categorical (pie and bar charts) data.
Currently, it supports the most common types of statistical approaches and
tests: parametric, nonparametric, robust, and Bayesian versions of
t-test/ANOVA, correlation analyses, contingency table analysis,
meta-analysis, and regression analyses. References: Patil (2021)
<doi:10.21105/joss.03236>.

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
