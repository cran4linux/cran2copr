%global packname  rmda
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          2%{?dist}
Summary:          Risk Model Decision Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-caret 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-pander 
Requires:         R-MASS 
Requires:         R-CRAN-caret 

%description
Provides tools to evaluate the value of using a risk prediction instrument
to decide treatment or intervention (versus no treatment or intervention).
Given one or more risk prediction instruments (risk models) that estimate
the probability of a binary outcome, rmda provides functions to estimate
and display decision curves and other figures that help assess the
population impact of using a risk model for clinical decision making.
Here, "population" refers to the relevant patient population. Decision
curves display estimates of the (standardized) net benefit over a range of
probability thresholds used to categorize observations as 'high risk'. The
curves help evaluate a treatment policy that recommends treatment for
patients who are estimated to be 'high risk' by comparing the population
impact of a risk-based policy to "treat all" and "treat none" intervention
policies.  Curves can be estimated using data from a prospective cohort.
In addition, rmda can estimate decision curves using data from a
case-control study if an estimate of the population outcome prevalence is
available.  Version 1.4 of the package provides an alternative framing of
the decision problem for situations where treatment is the
standard-of-care and a risk model might be used to recommend that low-risk
patients (i.e., patients below some risk threshold) opt out of treatment.
Confidence intervals calculated using the bootstrap can be computed and
displayed. A wrapper function to calculate cross-validated curves using
k-fold cross-validation is also provided.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/notes
%{rlibdir}/%{packname}/INDEX
