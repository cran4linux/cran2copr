%global packname  icemelt
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Parameter Estimation in Linear Transformation Model withInterval-Censored Data and Covariate Measurement Error

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-survival >= 2.39.5
Requires:         R-survival >= 2.39.5

%description
Estimates the parameters of the semiparametric linear transformation model
using imputation method, naive method and regression calibration method
when time-to-event is interval-censored and a covariate is measured with
error. A right censoring indicator must be available. The methods
implemented in this package can be found in Mandal, S., Wang, S. and
Sinha, S. (2019+). Analysis of Linear Transformation Models with Covariate
Measurement Error and Interval Censoring. (accepted, Statistics In
Medicine).

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
%{rlibdir}/%{packname}/libs
