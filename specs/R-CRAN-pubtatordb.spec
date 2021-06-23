%global __brp_check_rpaths %{nil}
%global packname  pubtatordb
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Create and Query a Local 'PubTator' Database

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 

%description
'PubTator' <https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/PubTator/> is
a National Center for Biotechnology Information (NCBI) tool that enhances
the annotation of articles on PubMed
<https://www.ncbi.nlm.nih.gov/pubmed/>. It makes it possible to rapidly
identify potential relationships between genes or proteins using text
mining techniques. In contrast, manually searching for and reading the
annotated articles would be very time consuming. 'PubTator' offers both an
online interface and a RESTful API, however, neither of these approaches
are well suited for frequent, high-throughput analyses. The package
'pubtatordb' provides a set of functions that make it easy for the average
R user to download 'PubTator' annotations, create, and then query a local
version of the database.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
