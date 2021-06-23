%global __brp_check_rpaths %{nil}
%global packname  comato
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Concept Maps and Concept Landscapes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-Matrix 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-clusterSim 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-Matrix 
Requires:         R-lattice 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-XML 
Requires:         R-cluster 
Requires:         R-CRAN-clusterSim 
Requires:         R-graphics 
Requires:         R-stats 

%description
Provides methods for the import/export and automated analysis of concept
maps and concept landscapes (sets of concept maps).

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
%{rlibdir}/%{packname}/INDEX
