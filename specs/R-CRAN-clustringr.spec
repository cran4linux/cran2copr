%global packname  clustringr
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Cluster Strings by Edit-Distance

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidygraph 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidygraph 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-ggplot2 

%description
Returns an edit-distance based clusterization of an input vector of
strings. Each cluster will contain a set of strings w/ small mutual
edit-distance (e.g., Levenshtein, optimum-sequence-alignment,
Damerau-Levenshtein), as computed by stringdist::stringdist(). The set of
all mutual edit-distances is then used by graph algorithms (from package
'igraph') to single out subsets of high connectivity.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
