%global packname  MonoPhy
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Allows to Explore Monophyly (or Lack of it) of Taxonomic Groupsin a Phylogeny

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-taxize 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-taxize 

%description
Requires rooted resolved phylogeny as input and creates a table of genera,
their monophyly-status, which taxa cause problems in monophyly etc.
Different information can be extracted from the output and a plot function
allows visualization of the results in a number of ways.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
