%global packname  RcmdrPlugin.UCA
%global packver   4.2-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.6
Release:          3%{?dist}%{?buildtag}
Summary:          UCA Rcmdr Plug-in

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 1.6
BuildRequires:    R-CRAN-randtests 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-TeachingDemos 
BuildRequires:    R-CRAN-tseries 
Requires:         R-CRAN-Rcmdr >= 1.6
Requires:         R-CRAN-randtests 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-TeachingDemos 
Requires:         R-CRAN-tseries 

%description
Some extensions to Rcmdr (R Commander), randomness test, variance test for
one normal sample and predictions using active model, made by R-UCA
project and used in teaching statistics at University of Cadiz (UCA).

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/etc
%doc %{rlibdir}/%{packname}/po
%{rlibdir}/%{packname}/INDEX
