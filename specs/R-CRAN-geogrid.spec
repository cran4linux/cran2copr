%global __brp_check_rpaths %{nil}
%global packname  geogrid
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Turn Geospatial Polygons into Regular or Hexagonal Grids

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-Rcpp 

%description
Turn irregular polygons (such as geographical regions) into regular or
hexagonal grids. This package enables the generation of regular (square)
and hexagonal grids through the package 'sp' and then assigns the content
of the existing polygons to the new grid using the Hungarian algorithm,
Kuhn (1955) (<doi:10.1007/978-3-540-68279-0_2>). This prevents the need
for manual generation of hexagonal grids or regular grids that are
supposed to reflect existing geography.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
