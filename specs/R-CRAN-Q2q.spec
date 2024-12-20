%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Q2q
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Interpolating Age-Specific Mortality Rates at All Ages

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Mortality rates are typically provided in an abridged format, i.e., by age
groups 0, [1, 5], [5, 10]', '[10, 15]', and so on. Some applications
necessitate a detailed (single) age description. Despite the large number
of proposed approaches in the literature, only a few methods ensure great
performance at both younger and higher ages. For example, the 6-term
'Lagrange' interpolation function is well suited to mortality
interpolation at younger ages (with irregular intervals), but not at older
ages. The 'Karup-King' method, on the other hand, performs well at older
ages but is not suitable for younger ones. Interested readers can find a
full discussion of the two stated methods in the book Shryock, Siegel, and
Associates (1993).The Q2q package combines the two methods to allow for
the interpolation of mortality rates across all age groups. It begins by
implementing each method independently, and then the resulting curves are
linked using a 5-age averaged error between the two partial curves.

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
