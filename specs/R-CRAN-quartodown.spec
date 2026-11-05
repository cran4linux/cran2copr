%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  quartodown
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Package Websites Built Entirely with 'Quarto'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-downlit 
BuildRequires:    R-CRAN-fansi 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-quarto 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-downlit 
Requires:         R-CRAN-fansi 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-quarto 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-yaml 

%description
Builds package websites with 'Quarto'. The whole site, help pages and
vignettes included, is rendered by 'Quarto', so every 'Quarto' feature
works, from callouts to code annotations. Functions mentioned in code link
to their help pages, with hover tooltips.

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
