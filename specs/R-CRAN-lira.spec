%global __brp_check_rpaths %{nil}
%global packname  lira
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          LInear Regression in Astronomy

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-rjags 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-rjags 

%description
Performs Bayesian linear regression and forecasting in astronomy. The
method accounts for heteroscedastic errors in both the independent and the
dependent variables, intrinsic scatters (in both variables) and scatter
correlation, time evolution of slopes, normalization, scatters, Malmquist
and Eddington bias, upper limits and break of linearity. The posterior
distribution of the regression parameters is sampled with a Gibbs method
exploiting the JAGS library.

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
