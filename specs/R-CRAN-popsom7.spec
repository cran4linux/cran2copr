%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  popsom7
%global packver   7.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A User-Friendly Implementation of Self-Organizing Maps

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-som 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-fields 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-hash 
Requires:         R-stats 
Requires:         R-CRAN-som 
Requires:         R-grDevices 

%description
Self-organizing maps with a number of distinguishing features: (1)
Automatic centroid detection and cluster visualization using starbursts,
for more details see the paper "Improved Interpretability of the Unified
Distance Matrix with Connected Components" by Hamel and Brown (2011) in
<ISBN:1-60132-168-6>. (2) Two models of the data: (a) a self organizing
map model, (b) a centroid based clustering model. (3) A number of easily
accessible quality metrics, Hamel (2016)
<doi:10.1007/978-3-319-28518-4_4>.

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
