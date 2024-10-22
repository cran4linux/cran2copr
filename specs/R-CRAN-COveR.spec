%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  COveR
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering with Overlaps

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3

%description
Provide functions for overlaps clustering, fuzzy clustering and
interval-valued data manipulation. The package implement the following
algorithms: OKM (Overlapping Kmeans) from Cleuziou, G. (2007)
<doi:10.1109/icpr.2008.4761079> ; NEOKM (Non-exhaustive overlapping
Kmeans) from Whang, J. J., Dhillon, I. S., and Gleich, D. F. (2015)
<doi:10.1137/1.9781611974010.105> ; Fuzzy Cmeans from Bezdek, J. C. (1981)
<doi:10.1007/978-1-4757-0450-1> ; Fuzzy I-Cmeans from de A.T. De Carvalho,
F. (2005) <doi:10.1016/j.patrec.2006.08.014>.

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
