%global packname  ggstatsplot
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          'ggplot2' Based Plots with Statistical Details

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-psych >= 1.9.12.31
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-scales >= 1.1.0
BuildRequires:    R-CRAN-broomExtra >= 1.0.1
BuildRequires:    R-CRAN-cowplot >= 1.0.0
BuildRequires:    R-CRAN-paletteer >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-WRS2 >= 1.0.0
BuildRequires:    R-CRAN-ggExtra >= 0.9
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-ggrepel >= 0.8.1
BuildRequires:    R-CRAN-insight >= 0.8.0
BuildRequires:    R-CRAN-ggsignif >= 0.6.0
BuildRequires:    R-CRAN-performance >= 0.4.3
BuildRequires:    R-CRAN-rlang >= 0.4.2
BuildRequires:    R-CRAN-parameters >= 0.4.1
BuildRequires:    R-CRAN-forcats >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-statsExpressions >= 0.3.0
BuildRequires:    R-CRAN-pairwiseComparisons >= 0.2.0
BuildRequires:    R-CRAN-ggcorrplot >= 0.1.3
BuildRequires:    R-CRAN-groupedstats >= 0.1.1
BuildRequires:    R-grid 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-psych >= 1.9.12.31
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-scales >= 1.1.0
Requires:         R-CRAN-broomExtra >= 1.0.1
Requires:         R-CRAN-cowplot >= 1.0.0
Requires:         R-CRAN-paletteer >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-WRS2 >= 1.0.0
Requires:         R-CRAN-ggExtra >= 0.9
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-ggrepel >= 0.8.1
Requires:         R-CRAN-insight >= 0.8.0
Requires:         R-CRAN-ggsignif >= 0.6.0
Requires:         R-CRAN-performance >= 0.4.3
Requires:         R-CRAN-rlang >= 0.4.2
Requires:         R-CRAN-parameters >= 0.4.1
Requires:         R-CRAN-forcats >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-statsExpressions >= 0.3.0
Requires:         R-CRAN-pairwiseComparisons >= 0.2.0
Requires:         R-CRAN-ggcorrplot >= 0.1.3
Requires:         R-CRAN-groupedstats >= 0.1.1
Requires:         R-grid 
Requires:         R-stats 

%description
Extension of 'ggplot2', 'ggstatsplot' creates graphics with details from
statistical tests included in the plots themselves. It is targeted
primarily at behavioral sciences community to provide a one-line code to
generate information-rich plots for statistical analysis of continuous
(violin plots, scatterplots, histograms, dot plots, dot-and-whisker plots)
or categorical (pie and bar charts) data. Currently, it supports only the
most common types of statistical tests: parametric, nonparametric, robust,
and bayesian versions of t-test/anova, correlation analyses, contingency
table analysis, and regression analyses.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
