%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rbranding
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Manage Branding and Accessibility of R Projects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-credentials 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-credentials 
Requires:         R-CRAN-ggplot2 
Requires:         R-utils 
Requires:         R-CRAN-yaml 

%description
A tool for building projects that are visually consistent, accessible, and
easy to maintain. It provides functions for managing branding assets,
applying organization-wide themes using 'brand.yml', and setting up new
projects with accessibility features and correct branding. It supports
'quarto', 'shiny', and 'rmarkdown' projects, and integrates with
'ggplot2'. The accessibility features are based on the Web Content
Accessibility Guidelines
<https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1> and Accessible Rich
Internet Applications (ARIA) specifications
<https://www.w3.org/WAI/ARIA/apg/>. The branding framework implements the
'brand.yml' specification <https://posit-dev.github.io/brand-yml/>.

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
