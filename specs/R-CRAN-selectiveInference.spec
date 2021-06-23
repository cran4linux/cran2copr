%global __brp_check_rpaths %{nil}
%global packname  selectiveInference
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for Post-Selection Inference

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-intervals 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-adaptMCMC 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-intervals 
Requires:         R-survival 
Requires:         R-CRAN-adaptMCMC 
Requires:         R-MASS 
Requires:         R-CRAN-Rcpp 

%description
New tools for post-selection inference, for use with forward stepwise
regression, least angle regression, the lasso, and the many means problem.
The lasso function implements Gaussian, logistic and Cox survival models.

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
