%global packname  gamlss.dist
%global packver   5.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.1.6
Release:          1%{?dist}
Summary:          Distributions for Generalized Additive Models for Location Scaleand Shape

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
Requires:         R-MASS 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-grDevices 

%description
A set of distributions which can be used for modelling the response
variables in Generalized Additive Models for Location Scale and Shape,
Rigby and Stasinopoulos (2005), <doi:10.1111/j.1467-9876.2005.00510.x>.
The distributions can be continuous, discrete or mixed distributions.
Extra distributions can be created, by transforming, any continuous
distribution defined on the real line, to a distribution defined on ranges
0 to infinity or 0 to 1, by using a ''log'' or a ''logit' transformation
respectively.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
