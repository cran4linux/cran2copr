%global packname  BootValidation
%global packver   0.1.65
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.65
Release:          1%{?dist}
Summary:          Adjusting for Optimism in 'glmnet' Regression usingBootstrapping

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-parallel 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-risksetROC 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-pROC 
Requires:         R-parallel 
Requires:         R-survival 
Requires:         R-CRAN-risksetROC 

%description
Main objective of a predictive model is to provide accurated predictions
of a new observations. Unfortunately we don't know how well the model
performs. In addition, at the current era of omic data where p >> n, is
not reasonable applying internal validation using data-splitting. Under
this background a good method to assessing model performance is applying
internal bootstrap validation (Harrell Jr, Frank E (2015)
<doi:10.1007/978-1-4757-3462-1>.) This package provides bootstrap
validation for the linear, logistic, multinomial and cox 'glmnet' models
as well as lm and glm models.

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
