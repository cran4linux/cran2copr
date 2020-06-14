%global packname  hierarchicalSets
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}
Summary:          Set Data Visualization Using Hierarchies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-ggdendro 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-scales 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-gtable 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-utils 

%description
Pure set data visualization approaches are often limited in scalability
due to the combinatorial explosion of distinct set families as the number
of sets under investigation increases. hierarchicalSets applies a set
centric hierarchical clustering of the sets under investigation and uses
this hierarchy as a basis for a range of scalable visual representations.
hierarchicalSets is especially well suited for collections of sets that
describe comparable comparable entities as it relies on the sets to have a
meaningful relational structure.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
