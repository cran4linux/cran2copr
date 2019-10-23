%global packname  OUwie
%global packver   1.53
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.53
Release:          1%{?dist}
Summary:          Analysis of Evolutionary Rates in an OU Framework

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-lattice 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-paleotree 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-corHMM 
BuildRequires:    R-CRAN-Rmpfr 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-nloptr 
Requires:         R-lattice 
Requires:         R-grDevices 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-paleotree 
Requires:         R-CRAN-phangorn 
Requires:         R-stats 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-corHMM 
Requires:         R-CRAN-Rmpfr 

%description
Calculates and compares rate differences of continuous character evolution
under Brownian motion and a new set of Ornstein-Uhlenbeck based Hansen
models that allow the strength of selection and stochastic motion to vary
across selective regimes. Beaulieu et al (2012)
<doi:10.1111/j.1558-5646.2012.01619.x>.

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
