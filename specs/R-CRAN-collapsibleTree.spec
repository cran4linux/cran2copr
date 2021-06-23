%global __brp_check_rpaths %{nil}
%global packname  collapsibleTree
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          3%{?dist}%{?buildtag}
Summary:          Interactive Collapsible Tree Diagrams using 'D3.js'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-data.tree 
Requires:         R-stats 
Requires:         R-methods 

%description
Interactive Reingold-Tilford tree diagrams created using 'D3.js', where
every node can be expanded and collapsed by clicking on it. Tooltips and
color gradients can be mapped to nodes using a numeric column in the
source data frame. See 'collapsibleTree' website for more information and
examples.

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
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX
