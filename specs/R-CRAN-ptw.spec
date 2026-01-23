%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ptw
%global packver   1.9-17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.17
Release:          1%{?dist}%{?buildtag}
Summary:          Parametric Time Warping

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-RcppDE 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-RcppDE 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Parametric Time Warping aligns patterns, i.e., it aims to put
corresponding features at the same locations. The algorithm searches for
an optimal polynomial describing the warping. It is possible to align one
sample to a reference, several samples to the same reference, or several
samples to several references. One can choose between calculating
individual warpings, or one global warping for a set of samples and one
reference. Two optimization criteria are implemented: RMS (Root Mean
Square error) and WCC (Weighted Cross Correlation). Both warping of peak
profiles and of peak lists are supported. A vignette for the latter is
contained in the inst/doc directory of the source package - the vignette
source can be found on the package github site. See `citation("ptw")` for
more details.

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
