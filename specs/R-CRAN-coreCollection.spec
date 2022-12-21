%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  coreCollection
%global packver   0.9.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.5
Release:          1%{?dist}%{?buildtag}
Summary:          Core Collection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-R6 >= 2.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-methods 
Requires:         R-CRAN-R6 >= 2.4.0
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-methods 

%description
Create a custom sized Core Collection based on a distance matrix and
applying the A-NE (accession nearest entry), E-NE (entry nearest entry) or
E-E (entry entry) method as introduced in Jansen and van Hintum (2007)
<doi:10.1007/s00122-006-0433-9> and further elaborated on in Odong, T.L.
(2012) <https://edepot.wur.nl/212422>. Optionally a list of preselected
accessions to be included into the core can be set. For each accession in
the computed core, if available nearby accessions are retrievable that can
be used as an alternative.

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
