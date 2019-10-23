%global packname  sensmediation
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Parametric Estimation and Sensitivity Analysis of Direct andIndirect Effects

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-maxLik >= 1.3.4
BuildRequires:    R-CRAN-mvtnorm >= 1.0.8
BuildRequires:    R-stats 
Requires:         R-CRAN-maxLik >= 1.3.4
Requires:         R-CRAN-mvtnorm >= 1.0.8
Requires:         R-stats 

%description
We implement functions to estimate and perform sensitivity analysis to
unobserved confounding of direct and indirect effects introduced in
Lindmark, de Luna and Eriksson (2018) <doi:10.1002/sim.7620>. The
estimation and sensitivity analysis are parametric, based on probit and/or
linear regression models. Sensitivity analysis is implemented for
unobserved confounding of the exposure-mediator, mediator-outcome and
exposure-outcome relationships.

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
%{rlibdir}/%{packname}/INDEX
