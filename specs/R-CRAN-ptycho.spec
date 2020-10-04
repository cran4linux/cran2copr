%global packname  ptycho
%global packver   1.1-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Variable Selection with Hierarchical Priors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape2 

%description
Bayesian variable selection for linear regression models using
hierarchical priors. There is a prior that combines information across
responses and one that combines information across covariates, as well as
a standard spike and slab prior for comparison. An MCMC samples from the
marginal posterior distribution for the 0-1 variables indicating if each
covariate belongs to the model for each response.

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
