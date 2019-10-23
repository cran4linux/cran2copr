%global packname  mvProbit
%global packver   0.1-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}
Summary:          Multivariate Probit Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4.0
Requires:         R-core >= 2.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bayesm >= 2.2.4
BuildRequires:    R-CRAN-abind >= 1.3.0
BuildRequires:    R-CRAN-maxLik >= 1.0.0
BuildRequires:    R-CRAN-mvtnorm >= 0.9.9994
BuildRequires:    R-CRAN-miscTools >= 0.6.11
Requires:         R-CRAN-bayesm >= 2.2.4
Requires:         R-CRAN-abind >= 1.3.0
Requires:         R-CRAN-maxLik >= 1.0.0
Requires:         R-CRAN-mvtnorm >= 0.9.9994
Requires:         R-CRAN-miscTools >= 0.6.11

%description
Tools for estimating multivariate probit models, calculating conditional
and unconditional expectations, and calculating marginal effects on
conditional and unconditional expectations.

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
