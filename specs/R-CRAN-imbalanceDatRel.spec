%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  imbalanceDatRel
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Relocated Data Oversampling for Imbalanced Data Classification

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-rcccd 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-SMOTEWB 
Requires:         R-CRAN-rcccd 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-SMOTEWB 

%description
Relocates oversampled data from a specific oversampling method to cover
area determined by pure and proper class cover catch digraphs (PCCCD). It
prevents any data to be generated in class overlapping area. For more
details, see the corresponding publication: F. Sağlam (2025)
<doi:10.1007/s10994-025-06755-8>.

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
