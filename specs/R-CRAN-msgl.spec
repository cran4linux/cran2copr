%global packname  msgl
%global packver   2.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.9
Release:          2%{?dist}
Summary:          Multinomial Sparse Group Lasso

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildRequires:    R-CRAN-sglOptim >= 1.3.7
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-sglOptim >= 1.3.7
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-stats 

%description
Multinomial logistic regression with sparse group lasso penalty.
Simultaneous feature selection and parameter estimation for
classification. Suitable for high dimensional multiclass classification
with many classes. The algorithm computes the sparse group lasso penalized
maximum likelihood estimate. Use of parallel computing for cross
validation and subsampling is supported through the 'foreach' and
'doParallel' packages. Development version is on GitHub, please report
package issues on GitHub.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
