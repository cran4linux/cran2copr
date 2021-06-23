%global __brp_check_rpaths %{nil}
%global packname  geesmv
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Modified Variance Estimators for Generalized EstimatingEquations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-gee 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-MASS 
Requires:         R-stats 
Requires:         R-nlme 
Requires:         R-CRAN-gee 
Requires:         R-CRAN-matrixcalc 
Requires:         R-MASS 

%description
Generalized estimating equations with the original sandwich variance
estimator proposed by Liang and Zeger (1986), and eight types of more
recent modified variance estimators for improving the finite small-sample
performance.

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
