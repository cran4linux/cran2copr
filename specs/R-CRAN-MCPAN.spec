%global packname  MCPAN
%global packver   1.1-21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.21
Release:          1%{?dist}
Summary:          Multiple Comparisons Using Normal Approximation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-multcomp 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-plyr 

%description
Multiple contrast tests and simultaneous confidence intervals based on
normal approximation. With implementations for binomial proportions in a
2xk setting (risk difference and odds ratio), poly-3-adjusted tumour
rates, biodiversity indices (multinomial data) and expected values under
lognormal assumption. Approximative power calculation for multiple
contrast tests of binomial and Gaussian data.

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
