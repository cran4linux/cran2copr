%global packname  MTE
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Maximum Tangent Likelihood and Other Robust Estimation forHigh-Dimensional Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-parcor 
Requires:         R-stats 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-parcor 

%description
Provides several robust estimators for linear regression and variable
selection. They are Maximum tangent likelihood estimator (Qin, et al.
(2017) <arXiv:1708.05439>), least absolute deviance estimator, and Huber
loss. The penalized version of each of these estimator incorporates L1
penalty function, i.e., LASSO and Adaptive Lasso. They are able to produce
consistent estimates for both fixed and high-dimensional settings.

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
