%global packname  modelfree
%global packver   1.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Model-free estimation of a psychometric function

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.8.1
Requires:         R-core >= 2.8.1
BuildArch:        noarch
BuildRequires:    R-CRAN-PolynomF >= 0.93
BuildRequires:    R-CRAN-SparseM >= 0.79
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-base 
Requires:         R-CRAN-PolynomF >= 0.93
Requires:         R-CRAN-SparseM >= 0.79
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-base 

%description
Local linear estimation of psychometric functions. Provides functions for
nonparametric estimation of a psychometric function and for estimation of
a derived threshold and slope, and their standard deviations and
confidence intervals

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
