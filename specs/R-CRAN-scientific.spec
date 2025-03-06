%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scientific
%global packver   2025.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2025.1
Release:          1%{?dist}%{?buildtag}
Summary:          Two Highly Customizable 'rmarkdown' Themes for Scientific Reports

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-xfun 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-xfun 

%description
Offers 'markdown' output formats designed with various styles, allowing
users to generate HTML reports tailored for scientific or machine learning
showcase. The output has a contemporary appearance with vibrant visuals,
providing numerous styles for effective highlighting. Created using the
'tufte' <https://rstudio.github.io/tufte/> package code as a starting
point.

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
