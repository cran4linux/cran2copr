%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EnsembleCV
%global packver   0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Extensible Package for Cross-Validation-Based Integration of Base Learners

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-EnsembleBase 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
Requires:         R-CRAN-EnsembleBase 
Requires:         R-parallel 
Requires:         R-methods 

%description
Extends the base classes and methods of EnsembleBase package for
cross-validation-based integration of base learners. Default
implementation calculates average of repeated CV errors, and selects the
base learner / configuration with minimum average error. The package takes
advantage of the file method provided in EnsembleBase package for writing
estimation objects to disk in order to circumvent RAM bottleneck. Special
save and load methods are provided to allow estimation objects to be saved
to permanent files on disk, and to be loaded again into temporary files in
a later R session. The package can be extended, e.g. by adding variants of
the current implementation.

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
