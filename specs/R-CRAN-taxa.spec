%global packname  taxa
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          3%{?dist}
Summary:          Taxonomic Classes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-taxize 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-taxize 

%description
Provides taxonomic classes for groupings of taxonomic names without data,
and those with data. Methods provided are "taxonomically aware", in that
they know about ordering of ranks, and methods that filter based on
taxonomy also filter associated data. This package is described in the
publication: "Taxa: An R package implementing data standards and methods
for taxonomic data", Zachary S.L. Foster, Scott Chamberlain, Niklaus J.
Grünwald (2018) <doi:10.12688/f1000research.14013.2>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/ignore
%{rlibdir}/%{packname}/INDEX
