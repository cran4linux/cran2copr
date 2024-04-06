%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  r2shortcode
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Shorten Function Names of Functions in Another Package and Create an Index to Make Them Accessible

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel > 3.6
Requires:         R-core > 3.6
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-stringr 

%description
When creating a package, authors may sometimes struggle with coming up
with easy and straightforward function names, and at the same time hoping
that other packages do not already have the same function names. In trying
to meet this goal, sometimes, function names are not descriptive enough
and may confuse the potential users. The purpose of this package is to
serve as a package function short form generator and also provide
shorthand names for other functions. Having this package will entice
authors to create long function names without the fear of users not
wanting to use their packages because of the long names. In a way,
everyone wins - the authors can use long descriptive function names, and
the users can use this package to make short functions names while still
using the package in question.

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
