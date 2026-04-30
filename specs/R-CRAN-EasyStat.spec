%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EasyStat
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Statistical Analysis, Visualization and Multi-Format Narrative Reporting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-glue >= 1.6.0
BuildRequires:    R-CRAN-knitr >= 1.40
BuildRequires:    R-CRAN-kableExtra >= 1.3.4
BuildRequires:    R-CRAN-broom >= 1.0.0
BuildRequires:    R-CRAN-flextable >= 0.9.0
BuildRequires:    R-CRAN-officer >= 0.6.0
BuildRequires:    R-CRAN-htmltools >= 0.5.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-glue >= 1.6.0
Requires:         R-CRAN-knitr >= 1.40
Requires:         R-CRAN-kableExtra >= 1.3.4
Requires:         R-CRAN-broom >= 1.0.0
Requires:         R-CRAN-flextable >= 0.9.0
Requires:         R-CRAN-officer >= 0.6.0
Requires:         R-CRAN-htmltools >= 0.5.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-tools 

%description
Provides automated statistical analysis, rich visualization, and
multi-format narrative reporting through a unified pipeline. Descriptive
statistics are available via easy_describe() and easy_group_summary().
Inferential tests with plain-language narratives are provided by
easy_regression(), easy_logistic_regression(), easy_ttest(), easy_anova(),
easy_chisq(), easy_ztest(), easy_ftest(), easy_correlation(),
easy_wilcox(), and easy_kruskal(). Publication-ready 'ggplot2'
visualizations are produced by easy_histogram(), easy_boxplot(),
easy_scatter(), easy_barplot(), easy_qqplot(), easy_density(),
easy_correlation_heatmap(), easy_regression_diagnostics(), and
easy_odds_ratio_plot(). The core Narrative Generator Module applies
conditional logic to extracted p-values, effect sizes, and model-fit
metrics to produce statistically sound, human-readable explanations
automatically. Results render in the 'RStudio' Viewer (HTML), the console
(ASCII), or export directly to Microsoft Word via 'flextable' and
'officer'.

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
