%global packname  kosel
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          2%{?dist}
Summary:          Variable Selection by Revisited Knockoffs Procedures

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.1
Requires:         R-core >= 1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ordinalNet 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ordinalNet 

%description
Performs variable selection for many types of L1-regularised regressions
using the revisited knockoffs procedure. This procedure uses a matrix of
knockoffs of the covariates independent from the response variable Y. The
idea is to determine if a covariate belongs to the model depending on
whether it enters the model before or after its knockoff. The procedure
suits for a wide range of regressions with various types of response
variables. Regression models available are exported from the R packages
'glmnet' and 'ordinalNet'. Based on the paper linked to via the URL below:
Gegout A., Gueudin A., Karmann C. (2019) <arXiv:1907.03153>.

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
