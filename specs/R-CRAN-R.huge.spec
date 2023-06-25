%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  R.huge
%global packver   0.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Accessing Huge Amounts of Data [deprecated]

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R.methodsS3 >= 1.7.0
BuildRequires:    R-CRAN-R.utils >= 1.34.0
BuildRequires:    R-CRAN-R.oo >= 1.23.0
Requires:         R-CRAN-R.methodsS3 >= 1.7.0
Requires:         R-CRAN-R.utils >= 1.34.0
Requires:         R-CRAN-R.oo >= 1.23.0

%description
DEPRECATED. Do not start building new projects based on this package.
Cross-platform alternatives are the following packages: bigmemory (CRAN),
ff (CRAN), BufferedMatrix (Bioconductor).  The main usage of it was inside
the aroma.affymetrix package. (The package currently provides a class
representing a matrix where the actual data is stored in a binary format
on the local file system.  This way the size limit of the data is set by
the file system and not the memory.)

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
