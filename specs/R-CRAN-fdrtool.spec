%global packname  fdrtool
%global packver   1.2.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.15
Release:          1%{?dist}
Summary:          Estimation of (Local) False Discovery Rates and Higher Criticism

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Estimates both tail area-based false discovery rates (Fdr) as well as
local false discovery rates (fdr) for a variety of null models (p-values,
z-scores, correlation coefficients, t-scores).  The proportion of null
values and the parameters of the null distribution are adaptively
estimated from the data.  In addition, the package contains functions for
non-parametric density estimation (Grenander estimator), for monotone
regression (isotonic regression and antitonic regression with weights),
for computing the greatest convex minorant (GCM) and the least concave
majorant (LCM), for the half-normal and correlation distributions, and for
computing empirical higher criticism (HC) scores and the corresponding
decision threshold.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
