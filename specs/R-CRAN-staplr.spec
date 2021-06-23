%global __brp_check_rpaths %{nil}
%global packname  staplr
%global packver   3.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Toolkit for PDF Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-rJava 
Requires:         R-tcltk 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-rJava 

%description
Provides function to manipulate PDF files: fill out PDF forms; merge
multiple PDF files into one; remove selected pages from a file; rename
multiple files in a directory; rotate entire pdf document; rotate selected
pages of a pdf file; Select pages from a file; splits single input PDF
document into individual pages; splits single input PDF document into
parts from given points. 'staplr' requires Java 8 installed on your
system.

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
