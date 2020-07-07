%global packname  SmoothHazard
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          3%{?dist}
Summary:          Estimation of Smooth Hazard Models for Interval-Censored Datawith Applications to Survival and Illness-Death Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.9.1
Requires:         R-core >= 1.9.1
BuildRequires:    R-CRAN-prodlim >= 1.4.9
BuildRequires:    R-CRAN-lava >= 1.4.1
BuildRequires:    R-CRAN-mvtnorm >= 1.0.3
Requires:         R-CRAN-prodlim >= 1.4.9
Requires:         R-CRAN-lava >= 1.4.1
Requires:         R-CRAN-mvtnorm >= 1.0.3

%description
Estimation of two-state (survival) models and irreversible illness- death
models with possibly interval-censored,left-truncated and right-censored
data. Proportional intensities regression models can be specified to allow
for covariates effects separately for each transition. We use either a
parametric approach with Weibull baseline intensities or a semi-parametric
approach with M-splines approximation of baseline intensities in order to
obtain smooth estimates of the hazard functions. Parameter estimates are
obtained by maximum likelihood in the parametric approach and by penalized
maximum likelihood in the semi-parametric approach.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
