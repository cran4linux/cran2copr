%global packname  AutoModel
%global packver   0.4.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.9
Release:          1%{?dist}
Summary:          Automated Hierarchical Multiple Regression with AssumptionsChecking

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-rowr 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-BaylorEdPsych 
BuildRequires:    R-CRAN-aod 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-car 
Requires:         R-MASS 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-rowr 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-BaylorEdPsych 
Requires:         R-CRAN-aod 
Requires:         R-CRAN-gtools 

%description
A set of functions that automates the process and produces reasonable
output for hierarchical multiple regression models.  It allows you to
specify predictor blocks, from which it generates all of the linear
models, and checks the assumptions of the model, producing the requisite
plots and statistics to allow you to judge the suitability of the model.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
