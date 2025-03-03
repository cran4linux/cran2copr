%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  surveynnet
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Neural Network for Complex Survey Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-PracTools 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-PracTools 
Requires:         R-stats 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-survival 

%description
The goal of 'surveynnet' is to extend the functionality of 'nnet', which
already supports survey weights, by enabling it to handle clustered and
stratified data. It achieves this by incorporating design effects through
the use of effective sample sizes as outlined by Chen and Rust (2017),
<doi:10.1093/jssam/smw036>, and performed by 'deffCR' in the package
'PracTools' (Valliant, Dever, and Kreuter (2018),
<doi:10.1007/978-3-319-93632-1>).

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
