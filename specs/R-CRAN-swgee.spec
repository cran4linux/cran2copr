%global packname  swgee
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Simulation Extrapolation Inverse Probability WeightedGeneralized Estimating Equations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gee 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-gee 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-mvtnorm 

%description
Simulation extrapolation and inverse probability weighted generalized
estimating equations method for longitudinal data with missing
observations and measurement error in covariates. References: Yi, G. Y.
(2008) <doi:10.1093/biostatistics/kxm054>; Cook, J. R. and Stefanski, L.
A. (1994) <doi:10.1080/01621459.1994.10476871>; Little, R. J. A. and
Rubin, D. B. (2002, ISBN:978-0-471-18386-0).

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
