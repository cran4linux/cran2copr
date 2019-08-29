%global packname  DiSSMod
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Fitting Sample Selection Models for Discrete Response Variables

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-MASS 
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-psych 
Requires:         R-MASS 

%description
Tools to fit sample selection models in case of discrete response
variables, through a parametric formulation which represents a natural
extension of the well-known Heckman selection model are provided in the
package. The response variable can be of Bernoulli, Poisson or Negative
Binomial type. The sample selection mechanism allows to choose among a
Normal, Logistic or Gumbel distribution.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
