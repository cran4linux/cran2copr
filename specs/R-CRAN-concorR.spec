%global packname  concorR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          CONCOR and Supplemental Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-sna 
Requires:         R-stats 
Requires:         R-graphics 

%description
Contains the CONCOR (CONvergence of iterated CORrelations) algorithm and a
series of supplemental functions for easy running, plotting, and
blockmodeling. The CONCOR algorithm is used on social network data to
identify network positions based off a definition of structural
equivalence; see Breiger, Boorman, and Arabie (1975)
<doi:10.1016/0022-2496(75)90028-0> and Wasserman and Faust's book Social
Network Analysis: Methods and Applications (1994). This version allows
multiple relationships for the same set of nodes and uses both incoming
and outgoing ties to find positions.

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
