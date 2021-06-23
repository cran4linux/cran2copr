%global __brp_check_rpaths %{nil}
%global packname  sybilccFBA
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Cost Constrained Flux Balance Analysis (ccFBA): MetabOlicModeling with ENzyme kineTics (MOMENT)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sybil 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
Requires:         R-CRAN-sybil 
Requires:         R-Matrix 
Requires:         R-methods 

%description
Different techniques of cost constrained flux balance analysis. 1-
MetabOlic Modeling with ENzyme kineTics 'MOMENT' which uses enzyme kinetic
data and enzyme molecular weights to constrain flux balance analysis(FBA)
and it is described in Adadi, R., Volkmer, B., Milo, R., Heinemann, M., &
Shlomi, T. (2012). Prediction of Microbial Growth Rate versus Biomass
Yield by a Metabolic Network with Kinetic Parameters, 8(7).
<doi:10.1371/journal.pcbi.1002575>. 2- an improvement of 'MOMENT' that
considers multi-functional enzymes 'ccFBA'. Described in Desouki,
Abdelmoneim. Algorithms for improving the predictive power of flux balance
analysis. PhD dissertation, 2016. FBA is a mathematical technique to find
fluxes in metabolic models at steady state. It is described in Orth, J.D.,
Thiele, I. and Palsson, B.O.  What is flux balance analysis? Nat. Biotech.
28, 245-248(2010).

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
