%global packname  mixtools
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Tools for Analyzing Finite Mixture Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-segmented 
BuildRequires:    R-stats 
BuildRequires:    R-survival 
Requires:         R-CRAN-kernlab 
Requires:         R-MASS 
Requires:         R-CRAN-segmented 
Requires:         R-stats 
Requires:         R-survival 

%description
Analyzes finite mixture models for various parametric and semiparametric
settings.  This includes mixtures of parametric distributions (normal,
multivariate normal, multinomial, gamma), various Reliability Mixture
Models (RMMs), mixtures-of-regressions settings (linear regression,
logistic regression, Poisson regression, linear regression with
changepoints, predictor-dependent mixing proportions, random effects
regressions, hierarchical mixtures-of-experts), and tools for selecting
the number of components (bootstrapping the likelihood ratio test
statistic, mixturegrams, and model selection criteria).  Bayesian
estimation of mixtures-of-linear-regressions models is available as well
as a novel data depth method for obtaining credible bands.  This package
is based upon work supported by the National Science Foundation under
Grant No. SES-0518772.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
