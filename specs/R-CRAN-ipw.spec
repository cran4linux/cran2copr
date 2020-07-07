%global packname  ipw
%global packver   1.0-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.11
Release:          3%{?dist}
Summary:          Estimate Inverse Probability Weights

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-nnet 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-MASS 
Requires:         R-nnet 
Requires:         R-survival 
Requires:         R-CRAN-geepack 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 

%description
Functions to estimate the probability to receive the observed treatment,
based on individual characteristics. The inverse of these probabilities
can be used as weights when estimating causal effects from observational
data via marginal structural models. Both point treatment situations and
longitudinal studies can be analysed. The same functions can be used to
correct for informative censoring.

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
