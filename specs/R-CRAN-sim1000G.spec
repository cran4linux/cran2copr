%global packname  sim1000G
%global packver   1.40
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.40
Release:          2%{?dist}
Summary:          Genotype Simulations for Rare or Common Variants UsingHaplotypes from 1000 Genomes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.2
Requires:         R-core >= 2.15.2
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-hapsim 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-readr 
Requires:         R-stats 
Requires:         R-CRAN-hapsim 
Requires:         R-MASS 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-readr 

%description
Generates realistic simulated genetic data in families or unrelated
individuals.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/datasets
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
