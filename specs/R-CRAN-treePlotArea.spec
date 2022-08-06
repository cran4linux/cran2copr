%global __brp_check_rpaths %{nil}
%global packname  treePlotArea
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Correction Factors for Tree Plot Areas Intersected by Stand Boundaries

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fritools 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
Requires:         R-CRAN-fritools 
Requires:         R-graphics 
Requires:         R-CRAN-sf 
Requires:         R-stats 

%description
The German national forest inventory uses angle count sampling, a sampling
method first published as `Bitterlich, W.: Die Winkelzählmessung.
Allgemeine Forst- und Holzwirtschaftliche Zeitung, 58. Jahrg., Folge 11/12
vom Juni 1947` and extended by Grosenbaugh
(<https://academic.oup.com/jof/article-abstract/50/1/32/4684174>) as
probability proportional to size sampling. When plots are located near
stand boundaries, their sizes and hence their probabilities need to be
corrected.

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
