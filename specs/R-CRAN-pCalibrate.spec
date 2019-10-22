%global packname  pCalibrate
%global packver   0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Bayesian Calibrations of P-Values

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-epitools 
BuildRequires:    R-CRAN-exact2x2 
BuildRequires:    R-CRAN-MCMCpack 
Requires:         R-CRAN-epitools 
Requires:         R-CRAN-exact2x2 
Requires:         R-CRAN-MCMCpack 

%description
Implements transformations of P-values to the smallest possible Bayes
factor within the specified class of alternative hypotheses, as described
in Held & Ott (2017, On p-values and Bayes factors, Annual Review of
Statistics and Its Application, 5, to appear). Covers several common
testing scenarios such as z-tests, t-tests, likelihood ratio tests and the
F-test of overall significance in the linear model.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
