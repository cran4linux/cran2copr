%global packname  tilemaps
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Generate Tile Maps

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lwgeom 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-smoothr 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lwgeom 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-smoothr 

%description
Implements an algorithm for generating maps, known as tile maps, in which
each region is represented by a single tile of the same shape and size.
The algorithm was first proposed in "Generating Tile Maps" by Graham
McNeill and Scott Hale (2017) <doi:10.1111/cgf.13200>. Functions allow
users to generate, plot, and compare square or hexagon tile maps.

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
