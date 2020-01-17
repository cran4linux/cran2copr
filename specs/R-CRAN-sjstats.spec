%global packname  sjstats
%global packver   0.17.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.17.7
Release:          1%{?dist}
Summary:          Collection of Convenient Functions for Common StatisticalComputations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-sjmisc >= 2.8.2
BuildRequires:    R-CRAN-sjlabelled >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-CRAN-insight >= 0.6.0
BuildRequires:    R-CRAN-bayestestR >= 0.4.0
BuildRequires:    R-CRAN-performance >= 0.4.0
BuildRequires:    R-CRAN-parameters >= 0.2.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-modelr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-sjmisc >= 2.8.2
Requires:         R-CRAN-sjlabelled >= 1.1.1
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-CRAN-insight >= 0.6.0
Requires:         R-CRAN-bayestestR >= 0.4.0
Requires:         R-CRAN-performance >= 0.4.0
Requires:         R-CRAN-parameters >= 0.2.0
Requires:         R-utils 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-magrittr 
Requires:         R-MASS 
Requires:         R-CRAN-modelr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
Collection of convenient functions for common statistical computations,
which are not directly provided by R's base or stats packages. This
package aims at providing, first, shortcuts for statistical measures,
which otherwise could only be calculated with additional effort (like
Cramer's V, Phi, or effect size statistics like Eta or Omega squared), or
for which currently no functions available. Second, another focus lies on
weighted variants of common statistical measures and tests like weighted
standard error, mean, t-test, correlation, and more.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
