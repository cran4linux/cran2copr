%global packname  economiccomplexity
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Methods Used in the Economic Complexity Literature

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-rlang 

%description
A wrapper of different indices and networks commonly used in Economic
Complexity to explore bipartite relations such as countries and their
exported products. These methods are also useful for different kind of
relations such as countries and their spoken languages. The functions
within this package correspond to code implementations of the equations
described in Hausmann, et al. (2005) <doi:10.3386/w11905>, Hausmann, et
al. (2014) <doi:10.7551/mitpress/9647.001.0001>, and Mariani, et al.
(2015) <doi:10.1140/epjb/e2015-60298-7>.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/paper.md
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
