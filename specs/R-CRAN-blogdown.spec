%global __brp_check_rpaths %{nil}
%global packname  blogdown
%global packver   1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.10
Release:          1%{?dist}%{?buildtag}
Summary:          Create Blogs and Websites with R Markdown

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         hugo
Requires:         pandoc
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 2.8
BuildRequires:    R-CRAN-yaml >= 2.1.19
BuildRequires:    R-CRAN-httpuv >= 1.4.0
BuildRequires:    R-CRAN-knitr >= 1.25
BuildRequires:    R-CRAN-xfun >= 0.29
BuildRequires:    R-CRAN-bookdown >= 0.22
BuildRequires:    R-CRAN-servr >= 0.21
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-later 
Requires:         R-CRAN-rmarkdown >= 2.8
Requires:         R-CRAN-yaml >= 2.1.19
Requires:         R-CRAN-httpuv >= 1.4.0
Requires:         R-CRAN-knitr >= 1.25
Requires:         R-CRAN-xfun >= 0.29
Requires:         R-CRAN-bookdown >= 0.22
Requires:         R-CRAN-servr >= 0.21
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-later 

%description
Write blog posts and web pages in R Markdown. This package supports the
static site generator 'Hugo' (<https://gohugo.io>) best, and it also
supports 'Jekyll' (<https://jekyllrb.com>) and 'Hexo' (<https://hexo.io>).

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
