%global packname  bmeta
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Meta-Analysis and Meta-Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-forestplot 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-forestplot 

%description
Provides a collection of functions for conducting meta-analyses under
Bayesian context in R. The package includes functions for computing
various effect size or outcome measures (e.g. odds ratios, mean difference
and incidence rate ratio) for different types of data based on MCMC
simulations. Users are allowed to fit fixed- and random-effects models
with different priors to the data. Meta-regression can be carried out if
effects of additional covariates are observed. Furthermore, the package
provides functions for creating posterior distribution plots and forest
plot to display main model output. Traceplots and some other diagnostic
plots are also available for assessing model fit and performance.

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
