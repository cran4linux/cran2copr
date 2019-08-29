%global packname  gamlss.countKinf
%global packver   3.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.5.1
Release:          1%{?dist}
Summary:          Generating and Fitting K-Inflated 'discrete gamlss.family'Distributions

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.1
Requires:         R-core >= 2.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss >= 5.0.0
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-stats 
Requires:         R-CRAN-gamlss >= 5.0.0
Requires:         R-CRAN-gamlss.dist 
Requires:         R-stats 

%description
This is an add on package to 'GAMLSS'. The main purpose of this package is
generating and fitting inflated distributions at any desired point (0, 1,
2, ...). The function gen.Kinf() generates K-inflated version of an
existing discrete 'GAMLSS' family distribution.

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
