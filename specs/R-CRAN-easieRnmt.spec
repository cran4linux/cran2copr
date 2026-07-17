%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  easieRnmt
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Local Machine-Translation with 'EasyNMT' from 'R'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-emoji 
BuildRequires:    R-CRAN-fastText 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-textclean 
BuildRequires:    R-CRAN-tokenizers 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-emoji 
Requires:         R-CRAN-fastText 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-textclean 
Requires:         R-CRAN-tokenizers 

%description
'R' wrapper around the 'Python' library 'EasyNMT', enabling easy-to-use,
local, reproducible machine translation. Supports translation between
multiple language pairs. The package takes care of preprocessing and
language detection using 'fastText' from 'R'. 'Python' backend and
installation of 'PyTorch' is handled by 'reticulate' and 'uv'.

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
