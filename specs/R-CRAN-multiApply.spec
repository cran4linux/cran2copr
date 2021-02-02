%global packname  multiApply
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Apply Functions to Multiple Multidimensional Arrays or Vectors

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-plyr 

%description
The base apply function and its variants, as well as the related functions
in the 'plyr' package, typically apply user-defined functions to a single
argument (or a list of vectorized arguments in the case of mapply). The
'multiApply' package extends this paradigm with its only function, Apply,
which efficiently applies functions taking one or a list of multiple
unidimensional or multidimensional arrays (or combinations thereof) as
input. The input arrays can have different numbers of dimensions as well
as different dimension lengths, and the applied function can return one or
a list of unidimensional or multidimensional arrays as output. This saves
development time by preventing the R user from writing often error-prone
and memory-inefficient loops dealing with multiple complex arrays. Also, a
remarkable feature of Apply is the transparent use of multi-core through
its parameter 'ncores'. In contrast to the base apply function, this
package suggests the use of 'target dimensions' as opposite to the
'margins' for specifying the dimensions relevant to the function to be
applied.

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
