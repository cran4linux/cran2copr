%global packname  bastah
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          2%{?dist}
Summary:          Big Data Statistical Analysis for High-Dimensional Models

License:          GPL (== 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BigQuic 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-scalreg 
Requires:         R-CRAN-BigQuic 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-lars 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-CRAN-scalreg 

%description
Big data statistical analysis for high-dimensional models is made possible
by modifying lasso.proj() in 'hdi' package by replacing its
nodewise-regression with sparse precision matrix computation using
'BigQUIC'.

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
