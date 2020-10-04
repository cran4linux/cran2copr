%global packname  PlaneGeometry
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Plane Geometry

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-uniformly 
BuildRequires:    R-CRAN-sdpt3r 
Requires:         R-CRAN-R6 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-uniformly 
Requires:         R-CRAN-sdpt3r 

%description
An extensive set of plane geometry routines. Provides R6 classes
representing triangles, circles, circular arcs, ellipses, elliptical arcs
and lines, and their plot methods. Also provides R6 classes representing
transformations: rotations, reflections, homotheties, scalings, general
affine transformations, inversions, Möbius transformations.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
