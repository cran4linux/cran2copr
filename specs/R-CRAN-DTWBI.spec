%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DTWBI
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Imputation of Time Series Based on Dynamic Time Warping

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-entropy 
BuildRequires:    R-CRAN-lsa 
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-rlist 
Requires:         R-stats 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-entropy 
Requires:         R-CRAN-lsa 

%description
Functions to impute large gaps within time series based on Dynamic Time
Warping methods. It contains all required functions to create large
missing consecutive values within time series and to fill them, according
to the paper Phan et al. (2017), <DOI:10.1016/j.patrec.2017.08.019>.
Performance criteria are added to compare similarity between two signals
(query and reference).

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
