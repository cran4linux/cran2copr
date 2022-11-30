%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gquad
%global packver   2.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Prediction of G Quadruplexes and Other Non-B DNA Motifs

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 5.6.2
BuildRequires:    R-CRAN-seqinr >= 4.2.23
Requires:         R-CRAN-ape >= 5.6.2
Requires:         R-CRAN-seqinr >= 4.2.23

%description
Genomic biology is not limited to the confines of the canonical B-forming
DNA duplex, but includes over ten different types of other secondary
structures that are collectively termed non-B DNA structures. Of these
non-B DNA structures, the G-quadruplexes are highly stable four-stranded
structures that are recognized by distinct subsets of nuclear factors.
This package provide functions for predicting intramolecular G
quadruplexes. In addition, functions for predicting other intramolecular
nonB DNA structures are included.

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
