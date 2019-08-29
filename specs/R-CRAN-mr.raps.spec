%global packname  mr.raps
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Two Sample Mendelian Randomization using Robust Adjusted ProfileScore

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-nortest 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-nortest 

%description
Mendelian randomization is a method of identifying and estimating a
confounded causal effect using genetic instrumental variables. This
packages implements methods for two-sample Mendelian randomization with
summary statistics by using Robust Adjusted Profile Score (RAPS).
References: Qingyuan Zhao, Jingshu Wang, Jack Bowden, Dylan S. Small.
Statistical inference in two-sample summary-data Mendelian randomization
using robust adjusted profile score. <arXiv:1801.09652>.

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
