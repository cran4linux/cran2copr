%global __brp_check_rpaths %{nil}
%global packname  decido
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Bindings for 'Mapbox' Ear Cutting Triangulation Library

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
Provides constrained triangulation of polygons. Ear cutting (or ear
clipping) applies constrained triangulation by successively 'cutting'
triangles from a polygon defined by path/s. Holes are supported by
introducing a bridge segment between polygon paths. This package wraps the
'header-only' library 'earcut.hpp'
<https://github.com/mapbox/earcut.hpp.git> which includes a reference to
the method used by Held, M. (2001) <doi:10.1007/s00453-001-0028-4>.

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
%{rlibdir}/%{packname}
