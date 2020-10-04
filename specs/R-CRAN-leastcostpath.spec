%global packname  leastcostpath
%global packver   1.7.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.4
Release:          1%{?dist}%{?buildtag}
Summary:          Modelling Pathways and Movement Potential Within a Landscape(Version 1.7.4)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.4.1
BuildRequires:    R-CRAN-raster >= 2.6.7
BuildRequires:    R-CRAN-pbapply >= 1.4.2
BuildRequires:    R-CRAN-rgdal >= 1.3.3
BuildRequires:    R-CRAN-sp >= 1.3.1
BuildRequires:    R-CRAN-gdistance >= 1.2.2
BuildRequires:    R-CRAN-rgeos >= 0.3.28
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-parallel >= 3.4.1
Requires:         R-CRAN-raster >= 2.6.7
Requires:         R-CRAN-pbapply >= 1.4.2
Requires:         R-CRAN-rgdal >= 1.3.3
Requires:         R-CRAN-sp >= 1.3.1
Requires:         R-CRAN-gdistance >= 1.2.2
Requires:         R-CRAN-rgeos >= 0.3.28
Requires:         R-methods 
Requires:         R-stats 

%description
Provides functionality to calculate cost surfaces based on slope (e.g.
Herzog, 2010; Llobera and Sluckin, 2007 <doi:10.1016/j.jtbi.2007.07.020>;
París Roche, 2002; Tobler, 1993), traversing slope (Bell and Lock, 2000),
and landscape features (Llobera, 2000) to be used when modelling pathways
and movement potential within a landscape (e.g. Llobera, 2015; Verhagen,
2013; White and Barber, 2012 <doi:10.1016/j.jas.2012.04.017>).

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
