%global __brp_check_rpaths %{nil}
%global packname  phylocanvas
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Interactive Phylogenetic Trees Using the 'Phylocanvas'JavaScript Library

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 4.0
BuildRequires:    R-methods >= 3.3.0
BuildRequires:    R-CRAN-phylobase 
BuildRequires:    R-CRAN-htmlwidgets 
Requires:         R-CRAN-ape >= 4.0
Requires:         R-methods >= 3.3.0
Requires:         R-CRAN-phylobase 
Requires:         R-CRAN-htmlwidgets 

%description
Create and customize interactive phylogenetic trees using the
'phylocanvas' JavaScript library and the 'htmlwidgets' package. These
trees can be used directly from the R console, from 'RStudio', in Shiny
apps, and in R Markdown documents.  See <http://phylocanvas.org/> for more
information on the 'phylocanvas' library.

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
%doc %{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/treedata
%{rlibdir}/%{packname}/INDEX
