%global packname  HBglm
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Hierarchical Bayesian Regression for GLMs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-bayesm 
BuildRequires:    R-CRAN-sns 
BuildRequires:    R-CRAN-MfUSampler 
BuildRequires:    R-stats 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-bayesm 
Requires:         R-CRAN-sns 
Requires:         R-CRAN-MfUSampler 
Requires:         R-stats 

%description
Convenient and efficient functions for performing 2-level hierarchical
Bayesian regression analysis for multi-group data. The lowest level may
belong to the generalized linear model (GLM) family while the prior level,
which effects pooling, allows for linear regression on lower level
covariates. Constraints on all or part of the parameter set maybe
specified with ease. A rich set of methods is included to visualize and
analyze results.

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
