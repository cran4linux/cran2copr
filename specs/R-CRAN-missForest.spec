%global packname  missForest
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          3%{?dist}
Summary:          Nonparametric Missing Value Imputation using Random Forest

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-itertools 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-itertools 

%description
The function 'missForest' in this package is used to impute missing values
particularly in the case of mixed-type data. It uses a random forest
trained on the observed values of a data matrix to predict the missing
values. It can be used to impute continuous and/or categorical data
including complex interactions and non-linear relations. It yields an
out-of-bag (OOB) imputation error estimate without the need of a test set
or elaborate cross-validation. It can be run in parallel to save
computation time.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
