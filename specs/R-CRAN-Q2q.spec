%global __brp_check_rpaths %{nil}
%global packname  Q2q
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interpolating Age-Specific Mortality Rates at All Ages

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch

%description
Mortality Rates are usually published following an abridged description,
i.e., by age groups 0, [1, 5[, [5, 10[, [10, 15[ and so on. For some
applications, a detailed (single) ages description is required. Despite
the huge number of the proposed methods in the literature, there is a
limited number of methods ensuring a high performance at lower and higher
ages in the same time. For example, the 6-terms 'Lagrange' interpolation
function is well adapted to mortality interpolation at lower ages (with
unequal intervals) but is not adapted to higher ages. On the other hand,
the 'Karup-King' method allows a good performance at higher ages but not
adapted to lower ages. Interested readers can refer to the book of
Shryock, Siegel and Associates (1993) for a detailed overview of the two
cited methods.The package Q2q allows combining both the two methods to
allow interpolating mortality rates at all ages. First, it starts by
implementing each method separately, then the resulted curves are joined
based on a 5-age averaged error between the two curves.

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
