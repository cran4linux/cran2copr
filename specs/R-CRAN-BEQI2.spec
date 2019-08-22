%global packname  BEQI2
%global packver   2.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Benthic Ecosystem Quality Index 2

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-methods 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape2 

%description
Tool for analysing benthos data. It estimates several quality indices like
the total abundance of species, species richness, Margalef's d, AZTI
Marine Biotic Index (AMBI), and the BEQI-2 index. Furthermore, additional
(optional) features are provided that enhance data preprocessing: (1)
genus to species conversion, i.e.,taxa counts at the taxonomic genus level
can optionally be converted to the species level and (2) pooling: small
samples are combined to bigger samples with a standardized size to (a)
meet the data requirements of the AMBI, (b) generate comparable species
richness values and (c) give a higher benthos signal to noise ratio.

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
%doc %{rlibdir}/%{packname}/css
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/Rmd
%{rlibdir}/%{packname}/INDEX
