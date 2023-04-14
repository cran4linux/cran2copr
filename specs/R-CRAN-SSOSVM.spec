%global __brp_check_rpaths %{nil}
%global packname  SSOSVM
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Stream Suitable Online Support Vector Machines

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-CRAN-mvtnorm 
Requires:         R-MASS 

%description
Soft-margin support vector machines (SVMs) are a common class of
classification models. The training of SVMs usually requires that the data
be available all at once in a single batch, however the Stochastic
majorization-minimization (SMM) algorithm framework allows for the
training of SVMs on streamed data instead Nguyen, Jones &
McLachlan(2018)<doi:10.1007/s42081-018-0001-y>. This package utilizes the
SMM framework to provide functions for training SVMs with hinge loss,
squared-hinge loss, and logistic loss.

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
