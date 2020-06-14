%global packname  reutils
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          2%{?dist}
Summary:          Talk to the NCBI EUtils

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-RCurl 
Requires:         R-stats 
Requires:         R-CRAN-XML 

%description
An interface to NCBI databases such as PubMed, GenBank, or GEO powered by
the Entrez Programming Utilities (EUtils). The nine EUtils provide
programmatic access to the NCBI Entrez query and database system for
searching and retrieving biological data.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
