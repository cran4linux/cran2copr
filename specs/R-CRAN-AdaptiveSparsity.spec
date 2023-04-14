%global __brp_check_rpaths %{nil}
%global packname  AdaptiveSparsity
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Adaptive Sparsity Models

License:          LGPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-Rcpp >= 0.12.13

%description
Implements Figueiredo EM algorithm for adaptive sparsity (Jeffreys prior)
(see Figueiredo, M.A.T.; , "Adaptive sparseness for supervised learning,"
Pattern Analysis and Machine Intelligence, IEEE Transactions on , vol.25,
no.9, pp. 1150- 1159, Sept. 2003) and Wong algorithm for adaptively sparse
gaussian geometric models (see Wong, Eleanor, Suyash Awate, and P. Thomas
Fletcher. "Adaptive Sparsity in Gaussian Graphical Models." In Proceedings
of the 30th International Conference on Machine Learning (ICML-13), pp.
311-319. 2013.)

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
