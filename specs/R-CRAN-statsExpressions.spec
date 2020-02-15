%global packname  statsExpressions
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Expressions with Statistical Details

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ipmisc >= 1.1.0
BuildRequires:    R-CRAN-broomExtra >= 1.0.1
BuildRequires:    R-CRAN-BayesFactor 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ez 
BuildRequires:    R-CRAN-metaBMA 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-metaplus 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rcompanion 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sjstats 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-WRS2 
Requires:         R-CRAN-ipmisc >= 1.1.0
Requires:         R-CRAN-broomExtra >= 1.0.1
Requires:         R-CRAN-BayesFactor 
Requires:         R-boot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ez 
Requires:         R-CRAN-metaBMA 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-metaplus 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rcompanion 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sjstats 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-WRS2 

%description
Statistical processing backend for 'ggstatsplot', this package creates
expressions with details from statistical tests. Currently, it supports
only the most common types of statistical tests: parametric,
nonparametric, robust, and bayesian versions of t-test/anova, correlation
analyses, contingency table analysis, and meta-analysis.

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
