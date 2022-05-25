%global __brp_check_rpaths %{nil}
%global packname  AntibodyTiters
%global packver   0.1.24
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.24
Release:          1%{?dist}%{?buildtag}
Summary:          Antibody Titer Analysis of Vaccinated Patients

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.2.4
BuildRequires:    R-CRAN-DescTools >= 0.99.43
Requires:         R-CRAN-openxlsx >= 4.2.4
Requires:         R-CRAN-DescTools >= 0.99.43

%description
Visualization of antibody titer scores is valuable for examination of
vaccination effects. 'AntibodyTiters' visualizes antibody titers of all or
selected patients. This package also produces empty excel files in a
specified format, in which users can fill in experimental data for
visualization. Excel files with toy data can also be produced, so that
users can see how it is visualized before obtaining real data. The data
should contain titer scores at pre-vaccination, after-1st shot, after-2nd
shot, and at least one additional sampling points. Patients with missing
values can be included. The first two sampling points (pre-vaccination and
after-1st shot) will be plotted discretely, whereas those following will
be plotted on a continuous time scale that starts from the day of second
shot. Half-life of titer can also be calculated for each pair of sampling
points.

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
