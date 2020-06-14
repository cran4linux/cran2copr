%global packname  gamlss.mx
%global packver   4.3-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.5
Release:          2%{?dist}
Summary:          Fitting Mixture Distributions with GAMLSS

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.1
Requires:         R-core >= 2.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-nnet 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-gamlss 
Requires:         R-nnet 
Requires:         R-stats 
Requires:         R-graphics 

%description
The main purpose of this package is to allow fitting of mixture
distributions with GAMLSS models.

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
