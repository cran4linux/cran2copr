%global packname  mbsts
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Multivariate Bayesian Structural Time Series

License:          LGPL-2.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-KFAS 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-pscl 
Requires:         R-MASS 
Requires:         R-CRAN-KFAS 
Requires:         R-CRAN-MCMCpack 
Requires:         R-Matrix 

%description
Multivariate time series regression using dynamic linear models fit by
MCMC. See Qiu, Jammalamadaka and Ning (2018)
<http://www.jmlr.org/papers/volume19/18-009/18-009.pdf>.

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
