%global packname  polySegratioMM
%global packver   0.6-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.4
Release:          1%{?dist}
Summary:          Bayesian Mixture Models for Marker Dosage in Autopolyploids

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildArch:        noarch
BuildRequires:    R-CRAN-polySegratio 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-lattice 
Requires:         R-CRAN-polySegratio 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-coda 
Requires:         R-lattice 

%description
Fits Bayesian mixture models to estimate marker dosage for dominant
markers in autopolyploids using JAGS (1.0 or greater) as outlined in Baker
et al "Bayesian estimation of marker dosage in sugarcane and other
autopolyploids" (2010, <doi:10.1007/s00122-010-1283-z>). May be used in
conjunction with polySegratio for simulation studies and comparison with
standard methods.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
