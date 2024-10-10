%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PriceIndices
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Calculating Bilateral and Multilateral Price Indexes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-reclin2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-strex 
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-reclin2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-strex 

%description
Preparing a scanner data set for price dynamics calculations (data
selecting, data classification, data matching, data filtering). Computing
bilateral and multilateral indexes. For details on these methods see:
Diewert and Fox (2020) <doi:10.1080/07350015.2020.1816176>, Białek (2019)
<doi:10.2478/jos-2019-0014> or Białek (2020) <doi:10.2478/jos-2020-0037>.

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
