%global packname  getmstatistic
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Quantifying Systematic Heterogeneity in Meta-Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stargazer >= 5.1
BuildRequires:    R-CRAN-metafor >= 1.9.6
BuildRequires:    R-CRAN-psych >= 1.5.1
BuildRequires:    R-CRAN-ggplot2 >= 1.0.1
BuildRequires:    R-CRAN-gridExtra >= 0.9.1
BuildRequires:    R-CRAN-gtable >= 0.1.2
Requires:         R-CRAN-stargazer >= 5.1
Requires:         R-CRAN-metafor >= 1.9.6
Requires:         R-CRAN-psych >= 1.5.1
Requires:         R-CRAN-ggplot2 >= 1.0.1
Requires:         R-CRAN-gridExtra >= 0.9.1
Requires:         R-CRAN-gtable >= 0.1.2

%description
Quantifying systematic heterogeneity in meta-analysis using R. The M
statistic aggregates heterogeneity information across multiple variants
to, identify systematic heterogeneity patterns and their direction of
effect in meta-analysis. It's primary use is to identify outlier studies,
which either show "null" effects or consistently show stronger or weaker
genetic effects than average across, the panel of variants examined in a
GWAS meta-analysis. In contrast to conventional heterogeneity metrics
(Q-statistic, I-squared and tau-squared) which measure random
heterogeneity at individual variants, M measures systematic (non-random)
heterogeneity across multiple independently associated variants.
Systematic heterogeneity can arise in a meta-analysis due to differences
in the study characteristics of participating studies. Some of the
differences may include: ancestry, allele frequencies, phenotype
definition, age-of-disease onset, family-history, gender, linkage
disequilibrium and quality control thresholds. See
<https://magosil86.github.io/getmstatistic/> for statistical statistical
theory, documentation and examples.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
