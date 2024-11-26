%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  r2resize
%global packver   1.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          In-Text Resize for Images, Tables and Fancy Resize Containers in 'shiny', 'rmarkdown' and 'quarto' Documents

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel > 3.6
Requires:         R-core > 3.6
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-quickcode 
BuildRequires:    R-CRAN-DT 
Requires:         R-utils 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-quickcode 
Requires:         R-CRAN-DT 

%description
Automatic resizing toolbar for containers, images and tables. Various
resizer or expandable container functionalities are also included. Most
suitable to include in 'shiny', 'markdown' and 'quarto' documents.

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
