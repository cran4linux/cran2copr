%global packname  PGRdup
%global packver   0.2.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3.5
Release:          1%{?dist}
Summary:          Discover Probable Duplicates in Plant Genetic ResourcesCollections

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-data.table >= 1.9.3
BuildRequires:    R-CRAN-stringdist >= 0.9.4
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-data.table >= 1.9.3
Requires:         R-CRAN-stringdist >= 0.9.4
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 

%description
Provides functions to aid the identification of probable/possible
duplicates in Plant Genetic Resources (PGR) collections using 'passport
databases' comprising of information records of each constituent sample.
These include methods for cleaning the data, creation of a searchable Key
Word in Context (KWIC) index of keywords associated with sample records
and the identification of nearly identical records with similar
information by fuzzy, phonetic and semantic matching of keywords.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
