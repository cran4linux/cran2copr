%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mapi
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Mapping Averaged Pairwise Information

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-fmesher 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-s2 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-fmesher 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-s2 
Requires:         R-CRAN-sf 

%description
Mapping Averaged Pairwise Information (MAPI) is an exploratory method
providing graphical representations summarizing the spatial variation of
pairwise metrics (eg. distance, similarity coefficient, ...) computed
between georeferenced samples.

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
