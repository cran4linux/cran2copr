%global packname  EstimationTools
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          3%{?dist}
Summary:          Maximum Likelihood Estimation for Probability Functions fromData Sets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-DEoptim 
Requires:         R-boot 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-Rdpack 
Requires:         R-utils 
Requires:         R-stats 

%description
A routine for parameter estimation for any probability density or mass
function implemented in R via maximum likelihood (ML) given a data set.
This routine is a wrapper function specifically developed for ML
estimation. There are included optimization procedures such as 'nlminb'
and 'optim' from base package, and 'DEoptim' Mullen (2011) <doi:
10.18637/jss.v040.i06>. Standard errors are estimated with 'numDeriv'
Gilbert (2011) <http://CRAN.R-project.org/package=numDeriv> or the option
'Hessian = TRUE' of 'optim' function.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%doc %{rlibdir}/%{packname}/refs.bib
%{rlibdir}/%{packname}/INDEX
