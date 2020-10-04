%global packname  SimSCRPiecewise
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          'Simulates Univariate and Semi-Competing Risks Data GivenCovariates and Piecewise Exponential Baseline Hazards'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Contains two functions for simulating survival data from piecewise
exponential hazards with a proportional hazards adjustment for covariates.
The first function SimUNIVPiecewise simulates univariate survival data
based on a piecewise exponential hazard, covariate matrix and true
regression vector. The second function SimSCRPiecewise semi-competing
risks data based on three piecewise exponential hazards, three true
regression vectors and three matrices of patient covariates (which can be
different or the same). This simulates from the Semi-Markov model of Lee
et al (2015) given patient covariates, regression parameters, patient
frailties and baseline hazard functions.

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
