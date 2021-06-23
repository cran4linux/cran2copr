%global __brp_check_rpaths %{nil}
%global packname  FCSlib
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Fluorescence Fluctuation Spectroscopy Analysis Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tiff 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-CRAN-fields 
Requires:         R-CRAN-tiff 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-bitops 
Requires:         R-CRAN-fields 

%description
This is a package for fluorescence fluctuation spectroscopy data analysis
methods such as spFCS, FCCS, scanning-FCS, pCF, N&B and pCOMB, among
others. In addition, several data detrending tools are provided. For an
extensive user's guide for the use of FCSlib, please navigate to
(<https://github.com/FCSlib/FCSlib/tree/master/Documentation>). Sample
data can be found at
(<https://github.com/FCSlib/FCSlib/tree/master/Sample%%20Data>). The
original paper where this package is presented can be found at
(<doi:10.1093/bioinformatics/btaa876>).

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
