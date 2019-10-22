%global packname  ssym
%global packver   1.5.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.7
Release:          1%{?dist}
Summary:          Fitting Semi-Parametric log-Symmetric Regression Models

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-normalp 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-survival 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-GIGrvg 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-normalp 
Requires:         R-CRAN-Formula 
Requires:         R-survival 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-sandwich 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-utils 

%description
Set of tools to fit a semi-parametric regression model suitable for
analysis of data sets in which the response variable is continuous,
strictly positive, asymmetric and possibly, censored. Under this setup,
both the median and the skewness of the response variable distribution are
explicitly modeled by using semi-parametric functions, whose
non-parametric components may be approximated by natural cubic splines or
P-splines. Supported distributions for the model error include log-normal,
log-Student-t, log-power-exponential, log-hyperbolic,
log-contaminated-normal, log-slash, Birnbaum-Saunders and
Birnbaum-Saunders-t distributions.

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
