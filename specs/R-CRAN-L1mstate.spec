%global __brp_check_rpaths %{nil}
%global packname  L1mstate
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          L1-Regularized Multi-State Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-Matrix >= 1.2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mstate 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-Matrix >= 1.2.10
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-MASS 
Requires:         R-CRAN-mstate 
Requires:         R-CRAN-colorspace 

%description
Fitting the regularization path of the L1-regularized multi-state models
since they can exploit sparsity structure of input. Different tuning
regularization parameter methods are provided. The cumulative hazard rate
estimation and the transition probability predictions can be made from the
fitted models.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
