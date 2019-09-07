%global packname  TempleMetrics
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Estimating Conditional Distributions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1.0
Requires:         R-core >= 2.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-BMisc 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-stats 
Requires:         R-CRAN-BMisc 
Requires:         R-CRAN-pbapply 

%description
Estimates conditional distributions and conditional quantiles.  The
versions of the methods in this package are primarily for use in multiple
step procedures where the first step is to estimate a conditional
distribution.  In particular, there are functions for implementing
distribution regression, quantile regression, and versions of local linear
distribution regression; all in a unified framework.  Distribution
regression provides a way to flexibly model the distribution of some
outcome Y conditional on covariates X without imposing parametric
assumptions on the conditional distribution but providing more structure
than fully nonparametric estimation (See Foresi and Peracchi (1995)
<doi:10.2307/2291056> and Chernozhukov, Fernandez-Val, and Melly (2013)
<doi:10.3982/ECTA10582>).

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
