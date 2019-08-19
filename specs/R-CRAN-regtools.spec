%global packname  regtools
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Regression Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-dummies 
BuildRequires:    R-CRAN-car 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-dummies 
Requires:         R-CRAN-car 

%description
Tools for linear, nonlinear and nonparametric regression and
classification.  Parametric fit assessment using nonparametric methods.
One vs. All and All vs. All multiclass classification.  Nonparametric
regression for general dimension, locally-linear option.  Nonlinear
regression with Eickert-White method for dealing with heteroscedasticity,
k-NN for general dimension and general descriptive functions.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/README
%{rlibdir}/%{packname}/INDEX
