%global packname  HRW
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}
Summary:          Datasets, Functions and Scripts for Semiparametric RegressionSupporting Harezlak, Ruppert & Wand (2018)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-KernSmooth 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
Requires:         R-KernSmooth 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-splines 
Requires:         R-stats 

%description
The book "Semiparametric Regression with R" by J. Harezlak, D. Ruppert &
M.P. Wand (2018, Springer; ISBN: 978-1-4939-8851-8) makes use of datasets
and scripts to explain semiparametric regression concepts. Each of the
book's scripts are contained in this package as well as datasets that are
not within other R packages. Functions that aid semiparametric regression
analysis are also included.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
