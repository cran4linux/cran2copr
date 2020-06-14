%global packname  sybilcycleFreeFlux
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          2%{?dist}
Summary:          Cycle-Free Flux Balance Analysis (CycleFreeFlux)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-CRAN-sybil 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
Requires:         R-CRAN-sybil 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-methods 

%description
Implement cycle-Free flux balance analysis (CycleFreeFlux), cycle-free
flux variability, and Random Sampling of solution space. Desouki, A. A.,
Jarre, F., Gelius-Dietrich, G., & Lercher, M. J. (2015). CycleFreeFlux:
efficient removal of thermodynamically infeasible loops from flux
distributions. Bioinformatics, 31(13), 2159-2165.
<doi.org/10.1093/bioinformatics/btv096>. Flux balance analysis is a
technique to find fluxes in metabolic models at steady state. It is
described in Orth, J.D., Thiele, I. and Palsson, B.O. What is flux balance
analysis? Nat. Biotech. 28, 245-248 (2010).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
