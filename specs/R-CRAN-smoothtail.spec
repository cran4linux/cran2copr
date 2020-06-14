%global packname  smoothtail
%global packver   2.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5
Release:          2%{?dist}
Summary:          Smooth Estimation of GPD Shape Parameter

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-logcondens >= 2.0.0
BuildRequires:    R-stats 
Requires:         R-CRAN-logcondens >= 2.0.0
Requires:         R-stats 

%description
Given independent and identically distributed observations X(1), ..., X(n)
from a Generalized Pareto distribution with shape parameter gamma in
[-1,0], offers several estimates to compute estimates of gamma. The
estimates are based on the principle of replacing the order statistics by
quantiles of a distribution function based on a log--concave density
function. This procedure is justified by the fact that the GPD density is
log--concave for gamma in [-1,0].

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
