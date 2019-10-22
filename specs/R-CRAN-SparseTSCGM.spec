%global packname  SparseTSCGM
%global packver   2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5
Release:          1%{?dist}
Summary:          Sparse Time Series Chain Graphical Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-QUIC 
BuildRequires:    R-CRAN-longitudinal 
BuildRequires:    R-CRAN-flare 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-stats 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-QUIC 
Requires:         R-CRAN-longitudinal 
Requires:         R-CRAN-flare 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-network 
Requires:         R-CRAN-abind 
Requires:         R-stats 

%description
Computes sparse vector autoregressive coefficients and precision matrices
for time series chain graphical models.

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
%{rlibdir}/%{packname}/libs
