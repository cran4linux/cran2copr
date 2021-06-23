%global __brp_check_rpaths %{nil}
%global packname  addhazard
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Fit Additive Hazards Models for Survival Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ahaz 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-rootSolve 
Requires:         R-CRAN-ahaz 
Requires:         R-survival 
Requires:         R-CRAN-rootSolve 

%description
Contains tools to fit the additive hazards model to data from a cohort,
random sampling, two-phase Bernoulli sampling and two-phase finite
population sampling, as well as calibration tool to incorporate phase I
auxiliary information into the two-phase data model fitting.  This package
provides regression parameter estimates and their model-based and robust
standard errors. It also offers tools to make prediction of individual
specific hazards.

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
