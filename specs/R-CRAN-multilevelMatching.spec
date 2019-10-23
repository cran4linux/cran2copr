%global packname  multilevelMatching
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Propensity Score Matching and Subclassification in ObservationalStudies with Multi-Level Treatments

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-nnet >= 7.3.8
BuildRequires:    R-MASS >= 7.3.35
BuildRequires:    R-CRAN-Matching >= 4.8.3.4
BuildRequires:    R-boot >= 1.3.13
Requires:         R-nnet >= 7.3.8
Requires:         R-MASS >= 7.3.35
Requires:         R-CRAN-Matching >= 4.8.3.4
Requires:         R-boot >= 1.3.13

%description
Implements methods to estimate causal effects from observational studies
when there are 2+ distinct levels of treatment (i.e., "multilevel
treatment") using matching estimators, as introduced in Yang et al. (2016)
<doi:10.1111/biom.12505>. Matching on covariates, and matching or
stratification on modeled propensity scores, are available. These methods
require matching on only a scalar function of generalized propensity
scores.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
