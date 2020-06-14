%global packname  EZtune
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          2%{?dist}
Summary:          Tunes AdaBoost, Support Vector Machines, and Gradient BoostingMachines

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ada 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-rpart 
Requires:         R-CRAN-ada 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-optimx 
Requires:         R-rpart 

%description
Contains two functions that are intended to make tuning supervised
learning methods easy. The eztune function uses a genetic algorithm or
Hooke-Jeeves optimizer to find the best set of tuning parameters. The user
can choose the optimizer, the learning method, and if optimization will be
based on accuracy obtained through validation error, cross validation, or
resubstitution. The function eztune.cv will compute a cross validated
error rate. The purpose of eztune_cv is to provide a cross validated
accuracy or MSE when resubstitution or validation data are used for
optimization because error measures from both approaches can be
misleading.

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
%{rlibdir}/%{packname}/INDEX
