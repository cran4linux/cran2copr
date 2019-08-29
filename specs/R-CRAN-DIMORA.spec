%global packname  DIMORA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Diffusion Models R Analysis

License:          GPL | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 

%description
The implemented methods are: Bass Standard model, Bass Generalized model
(with rectangular shock, exponential shock, mixed shock and armonic shock.
You can choose to add from 1 to 3 shocks), Guseo-Guidolin model and
Variable Potential Market model. The Bass model consists of a simple
differential equation that describes the process of how new products get
adopted in a population, the Generalized Bass model is a generalization of
the Bass model in which there is a "carrier" function x(t) that allows to
change the speed of time sliding. In some real processes the reachable
potential of the resource available in a temporal instant may appear to be
not constant over time, because of this we use Variable Potential Market
model, in which the Guseo-Guidolin has a particular specification for the
market function.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
