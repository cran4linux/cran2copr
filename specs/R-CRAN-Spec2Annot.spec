%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Spec2Annot
%global packver   1.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Annotation of Mass Spectra

License:          CeCILL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-stringr 

%description
Provides a comprehensive suite of functions to efficiently annotate mass
spectra data. Motivated by the need for rapid and accurate chemical
identification in high-resolution mass spectrometry, it integrates
built-in chemical databases and high-performance C++ algorithms. Users can
perform mass-to-charge (m/Z) and retention time searches, determine
elemental compositions of molecules using heuristic rules, including
specific isotopes, and annotate MS2 spectra with structural metrics using
configurable chemistry rules.

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
