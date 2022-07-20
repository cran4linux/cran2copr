%global __brp_check_rpaths %{nil}
%global packname  refineR
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Reference Interval Estimation using Real-World Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ash 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-parallel 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-ash 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-parallel 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Indirect method for the estimation of reference intervals using Real-World
Data ('RWD'). It takes routine measurements of diagnostic tests,
containing pathological and non-pathological samples as input and uses
sophisticated statistical methods to derive a model describing the
distribution of the non-pathological samples. This distribution can then
be used to derive reference intervals. Furthermore, the package offers
functions for printing and plotting the results of the algorithm. See
?refineR for a more comprehensive description of the features. Version 1.0
of the algorithm is described in detail in Ammer T., Schuetzenmeister A.,
Prokosch H.-U., Rauh M., Rank C.M., Zierk J. "refineR: A Novel Algorithm
for Reference Interval Estimation from Real-World Data". Scientific
Reports (2021) <doi:10.1038/s41598-021-95301-2>.

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
