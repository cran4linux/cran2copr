%global packname  SensitivityCaseControl
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          2%{?dist}
Summary:          Sensitivity Analysis for Case-Control Studies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
This package performs sensitivity analysis for case-control studies in
which some cases may meet a more narrow definition of being a case
compared to other cases which only meet a broad definition.  The
sensitivity analyses are described in Small, Cheng, Halloran and Rosenbaum
(2013, "Case Definition and Sensitivity Analysis", Journal of the American
Statistical Association, 1457-1468).  The functions sens.analysis.mh and
sens.analysis.aberrant.rank provide sensitivity analyses based on the
Mantel-Haenszel test statistic and aberrant rank test statistic as
described in Rosenbaum (1991, "Sensitivity Analysis for Matched Case
Control Studies", Biometrics); see also Section 1 of Small et al.  The
function adaptive.case.test provides adaptive inferences as described in
Section 5 of Small et al.  The function adaptive.noether.brown provides a
sensitivity analysis for a matched cohort study based on an adaptive test.
The other functions in the package are internal functions.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
