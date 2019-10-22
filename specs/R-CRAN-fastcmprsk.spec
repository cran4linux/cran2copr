%global packname  fastcmprsk
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Fine-Gray Regression via Forward-Backward Scan

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-dynpred 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-survival 
Requires:         R-CRAN-dynpred 
Requires:         R-CRAN-foreach 
Requires:         R-survival 

%description
In competing risks regression, the proportional subdistribution hazards
(PSH) model is popular for its direct assessment of covariate effects on
the cumulative incidence function. This package allows for both penalized
and unpenalized PSH regression in linear time using a novel
forward-backward scan. Penalties include Ridge, Lease Absolute Shrinkage
and Selection Operator (LASSO), Smoothly Clipped Absolute Deviation
(SCAD), Minimax Concave Plus (MCP), and elastic net.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
