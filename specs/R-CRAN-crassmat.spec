%global __brp_check_rpaths %{nil}
%global packname  crassmat
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          3%{?dist}%{?buildtag}
Summary:          Conditional Random Sampling Sparse Matrices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-svMisc 
Requires:         R-CRAN-svMisc 

%description
Conducts conditional random sampling on observed values in sparse
matrices. Useful for training and test set splitting sparse matrices prior
to model fitting in cross-validation procedures and estimating the
predictive accuracy of data imputation methods, such as matrix
factorization or singular value decomposition (SVD). Although designed for
applications with sparse matrices, CRASSMAT can also be applied to
complete matrices, as well as to those containing missing values.

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
