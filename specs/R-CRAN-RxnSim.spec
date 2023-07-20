%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RxnSim
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Functions to Compute Chemical and Chemical Reaction Similarity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rcdk >= 3.8.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-fingerprint 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-rcdk >= 3.8.1
Requires:         R-methods 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-fingerprint 
Requires:         R-CRAN-data.table 

%description
Methods to compute chemical similarity between two or more reactions and
molecules. Allows masking of chemical substructures for weighted
similarity computations. Uses packages 'rCDK' and 'fingerprint' for
cheminformatics functionality. Methods for reaction similarity and
sub-structure masking are as described in: Giri et al. (2015)
<doi:10.1093/bioinformatics/btv416>.

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
