%global packname  LNIRT
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          2%{?dist}
Summary:          LogNormal Response Time Item Response Theory Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Allows the simultaneous analysis of responses and response times in an
Item Response Theory (IRT) modelling framework. Supports variable person
speed functions (intercept, trend, quadratic), and covariates for item and
person (random) parameters. Data missing-by-design can be specified.
Parameter estimation is done with a MCMC algorithm. LNIRT replaces the
package CIRT, which was written by Rinke Klein Entink. For reference, see
the paper by Fox, Klein Entink and Van der Linden (2007), "Modeling of
Responses and Response Times with the Package cirt", Journal of
Statistical Software, <doi:10.18637/jss.v020.i07>.

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
