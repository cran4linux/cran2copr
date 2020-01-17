%global packname  pairwiseComparisons
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Multiple Pairwise Comparison Tests

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-jmv >= 1.0.8
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-WRS2 >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-rlang >= 0.4.2
BuildRequires:    R-CRAN-forcats >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-broomExtra >= 0.0.6
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-jmv >= 1.0.8
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-WRS2 >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-rlang >= 0.4.2
Requires:         R-CRAN-forcats >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-broomExtra >= 0.0.6
Requires:         R-stats 
Requires:         R-utils 

%description
Multiple pairwise comparison tests for one-way analysis of variance for
both between-subjects and within-subjects designs. Currently, it supports
only the most common types of statistical analyses and tests: parametric
(Welch's and Student's t-test), nonparametric (Durbin-Conover test and
Dwass-Steel-Crichtlow-Fligner test), robust (Yuen’s trimmed means test).

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
