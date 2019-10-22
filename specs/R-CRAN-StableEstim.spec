%global packname  StableEstim
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Estimate the Four Parameters of Stable Laws using DifferentMethods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stabledist 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-MASS 
Requires:         R-methods 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-stabledist 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-fBasics 
Requires:         R-MASS 

%description
Estimate the four parameters of stable laws using maximum likelihood
method, generalised method of moments with finite and continuum number of
points, iterative Koutrouvelis regression and Kogon-McCulloch method.  The
asymptotic properties of the estimators (covariance matrix, confidence
intervals) are also provided.

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
%doc %{rlibdir}/%{packname}/Examples
%{rlibdir}/%{packname}/INDEX
