%global packname  lg
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          3%{?dist}
Summary:          Locally Gaussian Distributions: Estimation and Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-localgauss 
BuildRequires:    R-CRAN-logspline 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-tseries 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-localgauss 
Requires:         R-CRAN-logspline 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-np 
Requires:         R-CRAN-tseries 

%description
An implementation of locally Gaussian distributions. It provides methods
for implementing locally Gaussian multivariate density estimation,
conditional density estimation, various independence tests for iid and
time series data, a test for conditional independence and a test for
financial contagion.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
