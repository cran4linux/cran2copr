%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  statuser
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Tools Designed for End Users

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-rsvg 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-utils 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-rsvg 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-lmtest 
Requires:         R-utils 

%description
The statistical tools in this package do one of four things: 1) Enhance
basic statistical functions with more flexible inputs, smarter defaults,
and richer, clearer, and ready-to-use output (e.g., t.test2()) 2) Produce
publication-ready commonly needed figures with one line of code (e.g.,
plot_cdf()) 3) Implement novel analytical tools developed by the authors
(e.g., twolines()) 4) Deliver niche functions of high value to the authors
that are not easily available elsewhere (e.g., clear(), convert_to_sql(),
resize_images()).

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
