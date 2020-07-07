%global packname  treeman
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          3%{?dist}
Summary:          Phylogenetic Tree Manipulation Class and Methods

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-bigmemory 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-bigmemory 

%description
S4 class and methods for intuitive and efficient phylogenetic tree
manipulation.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
