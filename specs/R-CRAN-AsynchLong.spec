%global __brp_check_rpaths %{nil}
%global packname  AsynchLong
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Regression Analysis of Sparse Asynchronous Longitudinal Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 

%description
Estimation of regression models for sparse asynchronous longitudinal
observations, where time-dependent response and covariates are mismatched
and observed intermittently within subjects. Kernel weighted estimating
equations are used for generalized linear models with either
time-invariant or time-dependent coefficients. Cao, H., Li, J., and Fine,
J. P. (2016) <doi:10.1214/16-EJS1141>. Cao, H., Zeng, D., and Fine, J. P.
(2015) <doi:10.1111/rssb.12086>.

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
