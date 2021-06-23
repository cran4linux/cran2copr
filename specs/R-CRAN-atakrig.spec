%global __brp_check_rpaths %{nil}
%global packname  atakrig
%global packver   0.9.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.8
Release:          1%{?dist}%{?buildtag}
Summary:          Area-to-Area Kriging

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-snow 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-snow 
Requires:         R-CRAN-FNN 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rcpp 

%description
Point-scale variogram deconvolution from irregular/regular spatial support
according to Goovaerts, P., (2008) <doi: 10.1007/s11004-007-9129-1>;
ordinary area-to-area (co)Kriging and area-to-point (co)Kriging.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
