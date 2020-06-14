%global packname  tsc
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          2%{?dist}
Summary:          Likelihood-ratio Tests for Two-Sample Comparisons

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Performs the two-sample comparisons using the following exact test
procedures: the exact likelihood-ratio test (LRT) for equality of two
normal populations proposed in Zhang et al. (2012); the combined test
based on the LRT and Shapiro-Wilk test for normality via the Bonferroni
correction technique; the newly proposed density-based empirical
likelihood (DBEL) ratio test. To calculate p-values of the DBEL
procedures, three procedures are used: (a) the traditional Monte Carlo
(MC) method implemented in C++, (b) a new interpolation method based on
regression techniques to operate with tabulated critical values of the
test statistic; (c) a Bayesian type method that uses the tabulated
critical values as the prior information and MC generated
DBEL-test-statistic's values as data.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
