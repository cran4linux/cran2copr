%global packname  AurieLSHGaussian
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}
Summary:          Creates a Neighbourhood Using Locality Sensitive Hashing forGaussian Projections

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-lsa 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-flexclust 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-lsa 
Requires:         R-stats 
Requires:         R-CRAN-flexclust 

%description
Uses locality sensitive hashing and creates a neighbourhood graph for a
data set and calculates the adjusted rank index value for the same. It
uses Gaussian random planes to decide the nature of a given point. Datar,
Mayur, Nicole Immorlica, Piotr Indyk, and Vahab S. Mirrokni(2004)
<doi:10.1145/997817.997857>.

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
