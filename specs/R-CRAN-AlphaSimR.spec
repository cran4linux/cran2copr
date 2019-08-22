%global packname  AlphaSimR
%global packver   0.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0
Release:          1%{?dist}
Summary:          Breeding Program Simulations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.500.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-methods 
Requires:         R-CRAN-R6 

%description
The successor to the 'AlphaSim' software for breeding program simulation
[Faux et al. (2016) <doi:10.3835/plantgenome2016.02.0013>]. Used for
stochastic simulations of breeding programs to the level of DNA sequence
for every individual. Contained is a wide range of functions for modeling
common tasks in a breeding program, such as selection and crossing. These
functions allow for constructing simulations of highly complex plant and
animal breeding programs via scripting in the R software environment. Such
simulations can be used to evaluate overall breeding program performance
and conduct research into breeding program design, such as implementation
of genomic selection. Included is the 'Markovian Coalescent Simulator'
('MaCS') for fast simulation of biallelic sequences according to a
population demographic history [Chen et al. (2009)
<doi:10.1101/gr.083634.108>].

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
