%global packname  AROC
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}
Summary:          Covariate-Adjusted Receiver Operating Characteristic CurveInference

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-nor1mix 
BuildRequires:    R-CRAN-spatstat 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-splines 
Requires:         R-CRAN-np 
Requires:         R-Matrix 
Requires:         R-CRAN-Hmisc 
Requires:         R-MASS 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-nor1mix 
Requires:         R-CRAN-spatstat 

%description
Estimates the covariate-adjusted Receiver Operating Characteristic (AROC)
curve and pooled (unadjusted) ROC curve by different methods. Inacio de
Carvalho, V., and Rodriguez-Alvarez, M. X. (2018) <arXiv:1806.00473>.

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
