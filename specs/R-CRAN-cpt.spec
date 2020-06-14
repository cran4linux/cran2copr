%global packname  cpt
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}
Summary:          Classification Permutation Test

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-MASS 
Requires:         R-nnet 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-glmnet 

%description
Non-parametric test for equality of multivariate distributions.  Trains a
classifier to classify (multivariate) observations as coming from one of
several distributions.  If the classifier is able to classify the
observations better than would be expected by chance (using permutation
inference), then the null hypothesis that the distributions are equal is
rejected.

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
