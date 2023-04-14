%global __brp_check_rpaths %{nil}
%global packname  orcutt
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          3%{?dist}%{?buildtag}
Summary:          Estimate Procedure in Case of First Order Autocorrelation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-stats 
Requires:         R-CRAN-lmtest 
Requires:         R-stats 

%description
Solve first order autocorrelation problems using an iterative method. This
procedure estimates both autocorrelation and beta coefficients recursively
until we reach the convergence (8th decimal as default). The residuals are
computed after estimating Beta using EGLS approach and Rho is estimated
using the previous residuals.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
