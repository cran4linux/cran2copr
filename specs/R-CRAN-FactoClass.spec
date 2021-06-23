%global __brp_check_rpaths %{nil}
%global packname  FactoClass
%global packver   1.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.7
Release:          3%{?dist}%{?buildtag}
Summary:          Combination of Factorial Methods and Cluster Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-KernSmooth 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-KernSmooth 

%description
Some functions of 'ade4' and 'stats' are combined in order to obtain a
partition of the rows of a data table, with columns representing variables
of scales: quantitative, qualitative or frequency. First, a principal axes
method is performed and then, a combination of Ward agglomerative
hierarchical classification and K-means is performed, using some of the
first coordinates obtained from the previous principal axes method. See,
for example: Lebart, L. and Piron, M. and Morineau, A.  (2006).
Statistique Exploratoire Multidimensionnelle, Dunod, Paris. In order to
permit to have different weights of the elements to be clustered, the
function 'kmeansW', programmed in C++, is included. It is a modification
of 'kmeans'. Some graphical functions include the option: 'gg=FALSE'.
When 'gg=TRUE', they use the 'ggplot2' and 'ggrepel' packages to avoid the
super-position of the labels.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
