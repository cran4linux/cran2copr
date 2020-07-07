%global packname  psbcGroup
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          3%{?dist}
Summary:          Penalized Parametric and Semiparametric Bayesian Survival Modelswith Shrinkage and Grouping Priors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
Requires:         gsl
BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-LearnBayes 
BuildRequires:    R-CRAN-SuppDists 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-LearnBayes 
Requires:         R-CRAN-SuppDists 
Requires:         R-CRAN-mvtnorm 

%description
Algorithms for fitting penalized parametric and semiparametric Bayesian
survival models with shrinkage and grouping priors.

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
%{rlibdir}/%{packname}/libs
