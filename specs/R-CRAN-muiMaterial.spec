%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  muiMaterial
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          'Material UI' for 'shiny' Apps and 'Quarto'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-htmltools >= 0.5.0
BuildRequires:    R-CRAN-shiny.react >= 0.4.0
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-htmltools >= 0.5.0
Requires:         R-CRAN-shiny.react >= 0.4.0

%description
Wraps the 'Material UI' React components <https://mui.com/> for use in R,
'shiny' applications and 'quarto' documents, including inputs, layouts,
navigation, and surfaces. All inputs come with R usage examples.

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
