%global packname  MultisiteMediation
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}
Summary:          Causal Mediation Analysis in Multisite Trials

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-psych 
Requires:         R-MASS 
Requires:         R-CRAN-ggplot2 

%description
We implement multisite causal mediation analysis using the methods
proposed by Qin and Hong (2017) <doi:10.3102/1076998617694879> and Qin,
Hong, Deutsch, and Bein (under review). It enables causal mediation
analysis in multisite trials, in which individuals are assigned to a
treatment or a control group at each site. It allows for estimation and
hypothesis testing for not only the population average but also the
between-site variance of direct and indirect effects. This strategy
conveniently relaxes the assumption of no treatment-by-mediator
interaction while greatly simplifying the outcome model specification
without invoking strong distributional assumptions. This package also
provides a function that can further incorporate a sample weight and a
nonresponse weight for multisite causal mediation analysis in the presence
of complex sample and survey designs and non-random nonresponse, to
enhance both the internal validity and external validity. Because the
identification assumptions are not always warranted, the package also
provides a weighting-based balance checking function for assessing the
remaining overt bias, as well as a weighting-based sensitivity analysis
function for further evaluating the potential bias related to omitted
confounding or to propensity score model misspecification.

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
