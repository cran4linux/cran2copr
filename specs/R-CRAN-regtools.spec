%global __brp_check_rpaths %{nil}
%global packname  regtools
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Regression and Classification Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-dummies 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-dummies 
Requires:         R-CRAN-sandwich 

%description
Tools for linear, nonlinear and nonparametric regression and
classification.  Novel graphical methods for assessment of parametric
models using nonparametric methods. One vs. All and All vs. All multiclass
classification, optional class probabilities adjustment.  Nonparametric
regression (k-NN) for general dimension, local-linear option.  Nonlinear
regression with Eickert-White method for dealing with heteroscedasticity.
Utilities for converting time series to rectangular form.  Utilities for
conversion between factors and indicator variables.  Some code related to
"Statistical Regression and Classification: from Linear Models to Machine
Learning", N. Matloff, 2017, CRC, ISBN 9781498710916.

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
%doc %{rlibdir}/%{packname}/images
%doc %{rlibdir}/%{packname}/README
%doc %{rlibdir}/%{packname}/vn.save
%{rlibdir}/%{packname}/INDEX
