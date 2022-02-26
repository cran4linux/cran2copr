%global __brp_check_rpaths %{nil}
%global packname  cati
%global packver   0.99.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.4
Release:          1%{?dist}%{?buildtag}
Summary:          Community Assembly by Traits: Individuals and Beyond

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-rasterVis 
BuildRequires:    R-CRAN-hypervolume 
BuildRequires:    R-CRAN-FD 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-rasterVis 
Requires:         R-CRAN-hypervolume 
Requires:         R-CRAN-FD 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-vegan 

%description
Detect and quantify community assembly processes using trait values of
individuals or populations, the T-statistics and other metrics, and
dedicated null models.

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
