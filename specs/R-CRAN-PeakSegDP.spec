%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PeakSegDP
%global packver   2024.1.24
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2024.1.24
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Programming Algorithm for Peak Detection in ChIP-Seq Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10

%description
A quadratic time dynamic programming algorithm can be used to compute an
approximate solution to the problem of finding the most likely
changepoints with respect to the Poisson likelihood, subject to a
constraint on the number of segments, and the changes which must
alternate: up, down, up, down, etc. For more info read
<http://proceedings.mlr.press/v37/hocking15.html> "PeakSeg: constrained
optimal segmentation and supervised penalty learning for peak detection in
count data" by TD Hocking et al, proceedings of ICML2015.

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
