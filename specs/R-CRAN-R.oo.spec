%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  R.oo
%global packver   1.27.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.27.1
Release:          1%{?dist}%{?buildtag}
Summary:          R Object-Oriented Programming with or without References

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R.methodsS3 >= 1.8.2
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-R.methodsS3 >= 1.8.2
Requires:         R-methods 
Requires:         R-utils 

%description
Methods and classes for object-oriented programming in R with or without
references.  Large effort has been made on making definition of methods as
simple as possible with a minimum of maintenance for package developers.
The package has been developed since 2001 and is now considered very
stable.  This is a cross-platform package implemented in pure R that
defines standard S3 classes without any tricks.

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
