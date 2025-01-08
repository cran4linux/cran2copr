%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  memoiR
%global packver   1.3-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Markdown and Bookdown Templates to Publish Documents

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bookdown 
BuildRequires:    R-CRAN-distill 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rmdformats 
BuildRequires:    R-CRAN-usethis 
Requires:         R-CRAN-bookdown 
Requires:         R-CRAN-distill 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rmdformats 
Requires:         R-CRAN-usethis 

%description
Producing high-quality documents suitable for publication directly from R
is made possible by the R Markdown ecosystem. 'memoiR' makes it easy. It
provides templates to knit memoirs, articles and slideshows with helpers
to publish the documents on GitHub Pages and activate continuous
integration.

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
