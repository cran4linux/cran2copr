%global packname  dnr
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}
Summary:          Simulate Dynamic Networks using Exponential Random Graph Models(ERGM) Family

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-ergm 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-network 
Requires:         R-CRAN-ergm 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-glmnet 

%description
Functions are provided to fit temporal lag models to dynamic networks. The
models are build on top of exponential random graph models (ERGM)
framework. There are functions for simulating or forecasting networks for
future time points. Stable Multiple Time Step Simulation/Prediction from
Lagged Dynamic Network Regression Models. Mallik, Almquist (2017, under
review).

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
