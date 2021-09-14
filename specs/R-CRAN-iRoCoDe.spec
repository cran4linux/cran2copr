%global __brp_check_rpaths %{nil}
%global packname  iRoCoDe
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Incomplete Row-Column Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The Row-column designs are widely recommended for experimental situations
when there are two well-identified factors that are cross-classified
representing known sources of variability. These designs are expected to
result a gain in accuracy of estimating treatment comparisons in an
experiment as they eliminate the effects of the row and column factors.
However, these designs are not readily available when the number of
treatments is more than the levels of row and column blocking factors.
This package named 'iRoCoDe' generates row-column designs with incomplete
rows and columns, by amalgamating two incomplete block designs (D1 and
D2). The selection of D1 and D2 (the input designs) can be done from the
available incomplete block designs, viz., balanced incomplete block
designs/ partially balanced incomplete block designs/ t-designs.
(Mcsorley, J.P., Phillips, N.C., Wallis, W.D. and Yucas, J.L.
(2005).<doi:10.1007/s10623-003-6149-9>).

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
