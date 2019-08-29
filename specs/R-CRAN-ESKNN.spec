%global packname  ESKNN
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Ensemble of Subset of K-Nearest Neighbours Classifiers forClassification and Class Membership Probability Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-stats 
Requires:         R-CRAN-caret 
Requires:         R-stats 

%description
Functions for classification and group membership probability estimation
are given. The issue of non-informative features in the data is addressed
by utilizing the ensemble method. A few optimal models are selected in the
ensemble from an initially large set of base k-nearest neighbours (KNN)
models, generated on subset of features from the training data. A two
stage assessment is applied in selection of optimal models for the
ensemble in the training function. The prediction functions for
classification and class membership probability estimation returns class
outcomes and class membership probability estimates for the test data. The
package includes measure of classification error and brier score, for
classification and probability estimation tasks respectively.

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
