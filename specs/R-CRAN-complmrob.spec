%global packname  complmrob
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          2%{?dist}
Summary:          Robust Linear Regression with Compositional Data as Covariates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-boot 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-ggplot2 
Requires:         R-boot 
Requires:         R-parallel 
Requires:         R-CRAN-scales 

%description
Robust regression methods for compositional data. The distribution of the
estimates can be approximated with various bootstrap methods. These
bootstrap methods are available for the compositional as well as for
standard robust regression estimates. This allows for direct comparison
between them.

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
