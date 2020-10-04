%global packname  BaMORC
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Model Optimized Reference Correction Method forAssigned and Unassigned Protein NMR Spectra

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-docopt 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-RBMRB 
BuildRequires:    R-CRAN-BMRBr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-docopt 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-RBMRB 
Requires:         R-CRAN-BMRBr 

%description
Provides reference correction for protein NMR spectra. Bayesian Model
Optimized Reference Correction (BaMORC) is utilizing Bayesian
probabilistic framework to perform protein NMR referencing correction,
currently for alpha and beta carbon-13 chemical shifts, without any
resonance assignment and/or three-dimensional protein structure. For more
detailed explanation, please refer to the paper "Automatic 13C Chemical
Shift Reference Correction for Unassigned Protein NMR Spectra"
<https://rdcu.be/4ly5> (Journal of Biomolecular NMR, Aug 2018)"
<doi:10.1007/s10858-018-0202-5>.

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
%doc %{rlibdir}/%{packname}/exec
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
