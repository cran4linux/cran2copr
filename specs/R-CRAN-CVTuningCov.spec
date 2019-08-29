%global packname  CVTuningCov
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Regularized Estimators of Covariance Matrices with CV Tuning

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
This is a package for selecting tuning parameters based on
cross-validation (CV) in regularized estimators of large covariance
matrices. Four regularized methods are implemented: banding, tapering,
hard-thresholding and soft-thresholding. Two types of matrix norms are
applied: Frobenius norm and operator norm. Two types of CV are considered:
K-fold CV and random CV. Usually K-fold CV use K-1 folds to train a model
and the rest one fold to validate the model. The reverse version trains a
model with 1 fold and validates with the rest with K-1 folds. Random CV
randomly splits the data set to two parts, a training set and a validation
set with user-specified sizes.

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
