%global packname  RxCEcolInf
%global packver   0.1-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          2%{?dist}
Summary:          'R x C Ecological Inference With Optional Incorporation ofSurvey Information'

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-mvtnorm 
Requires:         R-lattice 
Requires:         R-CRAN-coda 
Requires:         R-stats 

%description
Fits the R x C inference model described in Greiner and Quinn (2009).
Allows incorporation of survey results.

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
%{rlibdir}/%{packname}/libs
