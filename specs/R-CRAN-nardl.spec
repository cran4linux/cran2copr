%global packname  nardl
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          2%{?dist}
Summary:          Nonlinear Cointegrating Autoregressive Distributed Lag Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-gtools 
Requires:         R-stats 
Requires:         R-CRAN-strucchange 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-gtools 

%description
Computes the nonlinear cointegrating autoregressive distributed lag model
with p lags of the dependent variables and q lags of independent variables
proposed by (Shin, Yu & Greenwood-Nimmo, 2014
<doi:10.1007/978-1-4899-8008-3_9>).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
