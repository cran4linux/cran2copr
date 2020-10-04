%global packname  memgene
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Spatial Pattern Detection in Genetic Distance Data Using Moran'sEigenvector Maps

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-gdistance 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-gdistance 
Requires:         R-CRAN-vegan 

%description
Can detect relatively weak spatial genetic patterns by using Moran's
Eigenvector Maps (MEM) to extract only the spatial component of genetic
variation.  Has applications in landscape genetics where the movement and
dispersal of organisms are studied using neutral genetic variation.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
