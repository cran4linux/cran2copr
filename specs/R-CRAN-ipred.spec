%global packname  ipred
%global packver   0.9-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9
Release:          2%{?dist}
Summary:          Improved Predictors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-rpart >= 3.1.8
BuildRequires:    R-MASS 
BuildRequires:    R-survival 
BuildRequires:    R-nnet 
BuildRequires:    R-class 
BuildRequires:    R-CRAN-prodlim 
Requires:         R-rpart >= 3.1.8
Requires:         R-MASS 
Requires:         R-survival 
Requires:         R-nnet 
Requires:         R-class 
Requires:         R-CRAN-prodlim 

%description
Improved predictive models by indirect classification and bagging for
classification, regression and survival problems as well as resampling
based estimators of prediction error.

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
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
