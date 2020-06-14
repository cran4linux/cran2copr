%global packname  cosso
%global packver   2.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          2%{?dist}
Summary:          Fit Regularized Nonparametric Regression Models Using COSSOPenalty.

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-Rglpk 
Requires:         R-parallel 
Requires:         R-CRAN-glmnet 

%description
COSSO is a new regularization method that automatically estimates and
selects important function components by a soft-thresholding penalty in
the context of smoothing spline ANOVA models. Implemented models include
mean regression, quantile regression, logistic regression and the Cox
regression models.

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
