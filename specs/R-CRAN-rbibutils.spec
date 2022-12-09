%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rbibutils
%global packver   2.2.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.11
Release:          1%{?dist}%{?buildtag}
Summary:          Read 'Bibtex' Files and Convert Between Bibliography Formats

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-utils 
BuildRequires:    R-tools 
Requires:         R-utils 
Requires:         R-tools 

%description
Read and write 'Bibtex' files. Convert between bibliography formats,
including 'Bibtex', 'Biblatex', 'PubMed', 'Endnote', and 'Bibentry'.
Includes a port of the 'bibutils' utilities by Chris Putnam
<https://sourceforge.net/projects/bibutils/>. Supports all bibliography
formats and character encodings implemented in 'bibutils'.

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
