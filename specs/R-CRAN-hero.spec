%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hero
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Spatio-Temporal (Hero) Sandwich Smoother

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-fields 
Requires:         R-CRAN-Matrix 
Requires:         R-splines 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-fields 

%description
An implementation of the sandwich smoother proposed in Fast Bivariate
Penalized Splines by Xiao et al. (2012) <doi:10.1111/rssb.12007>.  A hero
is a specific type of sandwich.  Dictionary.com (2018)
<https://www.dictionary.com> describes a hero as: a large sandwich,
usually consisting of a small loaf of bread or long roll cut in half
lengthwise and containing a variety of ingredients, as meat, cheese,
lettuce, and tomatoes. Also implements the spatio-temporal sandwich
smoother of French and Kokoszka (2021) <doi:10.1016/j.spasta.2020.100413>.

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
