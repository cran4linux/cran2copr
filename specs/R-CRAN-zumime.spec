%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  zumime
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Media Type Detection from Bytes and File Names

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1

%description
Tells what a file is from its first bytes and from its name, with no
system library. Implements the Web Hypertext Application Technology
Working Group (WHATWG) Multipurpose Internet Mail Extensions (MIME)
Sniffing Standard <https://mimesniff.spec.whatwg.org/> over raw vectors
and paths. Reads inside containers to tell 'Office' documents from plain
'ZIP' archives, audio from video in 'MP4' files, and 'Word' from 'Excel'
in legacy 'Office' files, and recognises the data files 'R' users hold,
such as files saved by 'R', 'Parquet', 'SQLite' and 'Stata' files. Every
type has a parent in a hierarchy, and an extension table generated from
the Internet Assigned Numbers Authority (IANA) media types registry and
the 'Apache' 'httpd' type map answers from the name. One call reports both
answers, whether they agree, and whether a file is compressed, encrypted
or truncated.

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
