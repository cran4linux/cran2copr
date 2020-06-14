%global packname  rabi
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}
Summary:          Generate Codes to Uniquely and Robustly Identify Individuals forAnimal Behavior Studies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-numbers 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-numbers 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-stringdist 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 

%description
Facilitates the design and generation of optimal color (or symbol) codes
that can be used to mark and identify individual animals. These codes are
made such that the IDs are robust to partial erasure: even if sections of
the code are lost, the entire identity of the animal can be reconstructed.
Thus, animal subjects are not confused and no ambiguity is introduced.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/gui-example
%{rlibdir}/%{packname}/INDEX
