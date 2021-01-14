%global packname  crunchy
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Shiny Apps on Crunch

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstudioapi >= 0.4
BuildRequires:    R-CRAN-crunch 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-httpcache 
BuildRequires:    R-CRAN-miniUI 
Requires:         R-CRAN-rstudioapi >= 0.4
Requires:         R-CRAN-crunch 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-httpcache 
Requires:         R-CRAN-miniUI 

%description
To facilitate building custom dashboards on the Crunch data platform
<https://crunch.io/>, the 'crunchy' package provides tools for working
with 'shiny'. These tools include utilities to manage authentication and
authorization automatically and custom stylesheets to help match the look
and feel of the Crunch web application. The package also includes several
gadgets for use in 'RStudio'.

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
