%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tfevents
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Write Events for 'TensorBoard'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-CRAN-blob 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-zeallot 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-ellipsis 
Requires:         R-CRAN-blob 
Requires:         R-CRAN-png 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-zeallot 

%description
Provides a convenient way to log scalars, images, audio, and histograms in
the 'tfevent' record file format. Logged data can be visualized on the fly
using 'TensorBoard', a web based tool that focuses on visualizing the
training progress of machine learning models.

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
