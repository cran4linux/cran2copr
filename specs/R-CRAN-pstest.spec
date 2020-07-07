%global packname  pstest
%global packver   0.1.3.900
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3.900
Release:          3%{?dist}
Summary:          Specification Tests for Parametric Propensity Score Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-glmx 
BuildRequires:    R-MASS 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-glmx 
Requires:         R-MASS 
Requires:         R-utils 

%description
The propensity score is one of the most widely used tools in studying the
causal effect of a treatment, intervention, or policy. Given that the
propensity score is usually unknown, it has to be estimated, implying that
the reliability of many treatment effect estimators depends on the correct
specification of the (parametric) propensity score. This package
implements the data-driven nonparametric diagnostic tools for detecting
propensity score misspecification proposed by Sant'Anna and Song (2019)
<doi:10.1016/j.jeconom.2019.02.002>.

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
