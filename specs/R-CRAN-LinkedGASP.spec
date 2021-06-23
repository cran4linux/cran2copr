%global __brp_check_rpaths %{nil}
%global packname  LinkedGASP
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Linked Emulator of a Coupled System of Simulators

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-spBayes 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-spBayes 

%description
Prototypes for construction of a Gaussian Stochastic Process emulator
(GASP) of a computer model. This is done within the objective Bayesian
implementation of the GASP. The package allows for construction of a
linked GASP of the composite computer model. Computational implementation
follows the mathematical exposition given in publication: Ksenia N.
Kyzyurova, James O. Berger, Robert L. Wolpert. Coupling computer models
through linking their statistical emulators. SIAM/ASA Journal on
Uncertainty Quantification, 6(3): 1151-1171,
(2018).<DOI:10.1137/17M1157702>.

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
