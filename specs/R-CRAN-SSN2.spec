%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SSN2
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Modeling on Stream Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-spmodel 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-stats 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-tibble 
Requires:         R-graphics 
Requires:         R-CRAN-spmodel 
Requires:         R-CRAN-RSQLite 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Spatial statistical modeling and prediction for data on stream networks,
including models based on in-stream distance (Ver Hoef, J.M. and Peterson,
E.E., (2010) <DOI:10.1198/jasa.2009.ap08248>.) Models are created using
moving average constructions. Spatial linear models, including explanatory
variables, can be fit with (restricted) maximum likelihood.  Mapping and
other graphical functions are included.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
