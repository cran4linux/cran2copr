%global packname  OTE
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Optimal Trees Ensembles for Regression, Classification and ClassMembership Probability Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-stats 
Requires:         R-CRAN-randomForest 
Requires:         R-stats 

%description
Functions for creating ensembles of optimal trees for regression,
classification and class membership probability estimation are given. A
few trees are selected from an initial set of trees grown by random forest
for the ensemble on the basis of their individual and collective
performance. Trees are assessed on out-of-bag data and on an independent
training data set for individual and collective performance respectively.
The prediction functions return estimates of the test responses and their
class membership probabilities. Unexplained variations, error rates,
confusion matrix, Brier scores, etc. are also returned for the test data.

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
