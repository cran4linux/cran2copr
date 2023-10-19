%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gnumeric
%global packver   0.7-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.10
Release:          1%{?dist}%{?buildtag}
Summary:          Read Data from Files Readable by 'gnumeric'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.8.1
Requires:         R-core >= 2.8.1
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-utils 
Requires:         R-CRAN-XML 
Requires:         R-utils 

%description
Read data files readable by 'gnumeric' into 'R'. Can read whole sheet or a
range, from several file formats, including the native format of
'gnumeric'. Reading is done by using 'ssconvert' (a file converter utility
included in the 'gnumeric' distribution <http://www.gnumeric.org>) to
convert the requested part to CSV. From 'gnumeric' files (but not other
formats) can list sheet names and sheet sizes or read all sheets.

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
