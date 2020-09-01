%global packname  spatialwidget
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Formats Spatial Data for Use in Htmlwidgets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-geojsonsf >= 1.3.3
BuildRequires:    R-CRAN-jsonify >= 1.1.1
BuildRequires:    R-CRAN-colourvalues >= 0.3.4
BuildRequires:    R-CRAN-sfheaders >= 0.2.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-geometries 
BuildRequires:    R-CRAN-rapidjsonr 
Requires:         R-CRAN-Rcpp 

%description
Many packages use 'htmlwidgets'
<https://CRAN.R-project.org/package=htmlwidgets> for interactive plotting
of spatial data. This package provides functions for converting R objects,
such as simple features, into structures suitable for use in 'htmlwidgets'
mapping libraries.

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
