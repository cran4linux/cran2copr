%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  accessr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Command Line Tools to Produce Accessible Documents using 'R Markdown'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-rmarkdown 

%description
Provides functions to produce accessible 'HTML' slides, 'HTML', 'Word' and
'PDF' documents from input 'R markdown' files. Accessible 'PDF' files are
produced only on a 'Windows' Operating System. One aspect of accessibility
is providing a headings structure that is recognised by a screen reader,
providing a navigational tool for a blind or partially-sighted person. A
key aim is to produce documents of different formats easily from each of a
collection of 'R markdown' source files. Input 'R markdown' files are
rendered using the render() function from the 'rmarkdown' package
<https://cran.r-project.org/package=rmarkdown>. A 'zip' file containing
multiple output files can be produced from one function call. A
user-supplied template 'Word' document can be used to determine the
formatting of an output 'Word' document. Accessible 'PDF' files are
produced from 'Word' documents using 'OfficeToPDF'
<https://github.com/cognidox/OfficeToPDF>. A convenience function,
install_otp() is provided to install this software. The option to print
'HTML' output to (non-accessible) 'PDF' files is also available.

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
