%global packname  leastcostpath
%global packver   1.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.6
Release:          3%{?dist}
Summary:          Modelling Pathways and Movement Potential Within a Landscape

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
