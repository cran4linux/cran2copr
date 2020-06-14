%global packname  ggstatsplot
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          2%{?dist}
Summary:          'ggplot2' Based Plots with Statistical Details

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-groupedstats >= 1.0.1
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-pairwiseComparisons >= 1.0.0
BuildRequires:    R-CRAN-broomExtra 
BuildRequires:    R-CRAN-correlation 
BuildRequires:    R-CRAN-cowplot 
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
BuildRequires:    R-CRAN-statsExpressions 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-groupedstats >= 1.0.1
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-pairwiseComparisons >= 1.0.0
Requires:         R-CRAN-broomExtra 
Requires:         R-CRAN-correlation 
Requires:         R-CRAN-cowplot 
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
Requires:         R-CRAN-statsExpressions 
Requires:         R-CRAN-tidyr 

%description
Extension of 'ggplot2', 'ggstatsplot' creates graphics with details from
statistical tests included in the plots themselves. It is targeted
primarily at behavioral sciences community to provide a one-line code to
generate information-rich plots for statistical analysis of continuous
(violin plots, scatterplots, histograms, dot plots, dot-and-whisker plots)
or categorical (pie and bar charts) data. Currently, it supports only the
most common types of statistical tests: parametric, nonparametric, robust,
and bayesian versions of t-test/anova, correlation analyses, contingency
table analysis, meta-analysis, and regression analyses.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
