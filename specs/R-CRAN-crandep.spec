%global packname  crandep
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Network Analysis of Dependencies of CRAN Packages

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-igraph 

%description
The dependencies of CRAN packages can be analysed in a network fashion.
Through scrapping the page of a package on CRAN, we can obtain the
packages that it depends, imports, suggests, etc. By iterating this
procedure over a number of packages, we can build the dependency network
and represent it by a graph object, most easily through the 'igraph'
package. Subsequently, the dependency network can be visualised and
analysed using social network analysis methods, enabling us to have a
bird's-eye view of the CRAN ecosystem.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
