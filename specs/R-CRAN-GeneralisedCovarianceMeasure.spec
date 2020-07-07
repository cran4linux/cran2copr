%global packname  GeneralisedCovarianceMeasure
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Test for Conditional Independence Based on the GeneralizedCovariance Measure (GCM)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-CVST 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-mgcv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-CVST 
Requires:         R-graphics 
Requires:         R-CRAN-kernlab 
Requires:         R-mgcv 
Requires:         R-stats 
Requires:         R-CRAN-xgboost 

%description
A statistical hypothesis test for conditional independence. It performs
nonlinear regressions on the conditioning variable and then tests for a
vanishing covariance between the resulting residuals. It can be applied to
both univariate random variables and multivariate random vectors. Details
of the method can be found in Rajen D. Shah and Jonas Peters (2018)
<arXiv:1804.07203>.

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
