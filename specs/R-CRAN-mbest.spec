%global packname  mbest
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          3%{?dist}
Summary:          Moment-Based Estimation for Hierarchical Models

License:          Apache License (== 2.0) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-nlme >= 3.1.124
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-logging 
Requires:         R-nlme >= 3.1.124
Requires:         R-CRAN-abind 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-logging 

%description
Fast moment-based hierarchical model fitting. Implements methods from the
papers "Fast Moment-Based Estimation for Hierarchical Models," by Perry
(2017) and "Fitting a Deeply Nested Hierarchical Model to a Large Book
Review Dataset Using a Moment-Based Estimator," by Zhang, Schmaus, and
Perry (2018).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
