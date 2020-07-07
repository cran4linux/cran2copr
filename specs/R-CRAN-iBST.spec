%global packname  iBST
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Improper Bagging Survival Tree

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-survival 
BuildRequires:    R-rpart 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-survival 
Requires:         R-rpart 
Requires:         R-parallel 
Requires:         R-CRAN-Rcpp 

%description
Fit a bagging survival tree on a mixture of population (susceptible and
nonsusceptible) using either a pseudo R2 criterion or an adjusted Logrank
criterion. The predictor is evaluated using the Out Of Bag Integrated
Brier Score (IBS) and several scores of importance are computed for
variable selection. The thresholds values for variable selection are
computed using a nonparametric permutation test.

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
%{rlibdir}/%{packname}/libs
