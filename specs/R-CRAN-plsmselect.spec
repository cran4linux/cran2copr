%global packname  plsmselect
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Linear and Smooth Predictor Modelling with Penalisation andVariable Selection

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-survival >= 2.43.3
BuildRequires:    R-CRAN-glmnet >= 2.0.16
BuildRequires:    R-mgcv >= 1.8.26
BuildRequires:    R-CRAN-dplyr >= 0.7.8
Requires:         R-survival >= 2.43.3
Requires:         R-CRAN-glmnet >= 2.0.16
Requires:         R-mgcv >= 1.8.26
Requires:         R-CRAN-dplyr >= 0.7.8

%description
Fit a model with potentially many linear and smooth predictors.
Interaction effects can also be quantified. Variable selection is done
using penalisation. For l1-type penalties we use iterative steps
alternating between using linear predictors (lasso) and smooth predictors
(generalised additive model).

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
%{rlibdir}/%{packname}/INDEX
