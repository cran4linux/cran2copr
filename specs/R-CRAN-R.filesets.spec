%global __brp_check_rpaths %{nil}
%global packname  R.filesets
%global packver   2.15.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.15.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easy Handling of and Access to Files Organized in Structured Directories

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R.oo >= 1.24.0
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-R.methodsS3 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-R.cache 
BuildRequires:    R-stats 
Requires:         R-CRAN-R.oo >= 1.24.0
Requires:         R-CRAN-digest 
Requires:         R-CRAN-R.methodsS3 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-R.cache 
Requires:         R-stats 

%description
A file set refers to a set of files located in one or more directories on
the file system.  This package provides classes and methods to locate,
setup, subset, navigate and iterate such sets.  The API is designed such
that these classes can be extended via inheritance to provide a richer API
for special file formats.  Moreover, a specific name format is defined
such that filenames and directories can be considered to have full names
which consists of a name followed by comma-separated tags.  This adds
additional flexibility to identify file sets and individual files.  NOTE:
This package's API should be considered to be in an beta stage.  Its main
purpose is currently to support the aroma.* packages, where it is one of
the main core components; if you decide to build on top of this package,
please contact the author first.

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
