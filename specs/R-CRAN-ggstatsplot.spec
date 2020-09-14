%global packname  ggstatsplot
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          'ggplot2' Based Plots with Statistical Details

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-broomExtra >= 4.0.5
BuildRequires:    R-CRAN-pairwiseComparisons >= 2.0.1
BuildRequires:    R-CRAN-statsExpressions >= 0.5.0
BuildRequires:    R-CRAN-tidyr >= 0.3.0
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-effectsize 
BuildRequires:    R-CRAN-ggcorrplot 
BuildRequires:    R-CRAN-ggExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggsignif 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-CRAN-ipmisc 
BuildRequires:    R-CRAN-paletteer 
BuildRequires:    R-CRAN-parameters 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
Requires:         R-CRAN-broomExtra >= 4.0.5
Requires:         R-CRAN-pairwiseComparisons >= 2.0.1
Requires:         R-CRAN-statsExpressions >= 0.5.0
Requires:         R-CRAN-tidyr >= 0.3.0
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-effectsize 
Requires:         R-CRAN-ggcorrplot 
Requires:         R-CRAN-ggExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggsignif 
Requires:         R-CRAN-insight 
Requires:         R-CRAN-ipmisc 
Requires:         R-CRAN-paletteer 
Requires:         R-CRAN-parameters 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 

%description
Extension of 'ggplot2', 'ggstatsplot' creates graphics with details from
statistical tests included in the plots themselves. It provides easier API
to generate information-rich plots for statistical analysis of continuous
(violin plots, scatterplots, histograms, dot plots, dot-and-whisker plots)
or categorical (pie and bar charts) data. Currently, it supports only the
most common types of statistical tests: parametric, nonparametric, robust,
and Bayesian versions of t-test/ANOVA, correlation analyses, contingency
table analysis, meta-analysis, and regression analyses.

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
