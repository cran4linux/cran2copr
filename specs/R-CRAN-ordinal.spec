%global __brp_check_rpaths %{nil}
%global packname  ordinal
%global packver   2019.12-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2019.12.10
Release:          3%{?dist}%{?buildtag}
Summary:          Regression Models for Ordinal Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-ucminf 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-numDeriv 

%description
Implementation of cumulative link (mixed) models also known as ordered
regression models, proportional odds models, proportional hazards models
for grouped survival times and ordered logit/probit/... models. Estimation
is via maximum likelihood and mixed models are fitted with the Laplace
approximation and adaptive Gauss-Hermite quadrature. Multiple random
effect terms are allowed and they may be nested, crossed or partially
nested/crossed. Restrictions of symmetry and equidistance can be imposed
on the thresholds (cut-points/intercepts). Standard model methods are
available (summary, anova, drop-methods, step, confint, predict etc.) in
addition to profile methods and slice methods for visualizing the
likelihood function and checking convergence.

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
