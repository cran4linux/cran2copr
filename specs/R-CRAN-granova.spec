%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  granova
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical Analysis of Variance

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-car >= 2.0.21
Requires:         R-CRAN-car >= 2.0.21

%description
This small collection of functions provides what we call elemental
graphics for display of analysis of variance results, David C. Hoaglin,
Frederick Mosteller and John W. Tukey (1991, ISBN:978-0-471-52735-0), Paul
R. Rosenbaum (1989) <doi:10.2307/2684513>, Robert M. Pruzek and James E.
Helmreich <https://jse.amstat.org/v17n1/helmreich.html>. The term
elemental derives from the fact that each function is aimed at
construction of graphical displays that afford direct visualizations of
data with respect to the fundamental questions that drive the particular
analysis of variance methods. These functions can be particularly helpful
for students and non-statistician analysts. But these methods should be
quite generally helpful for work-a-day applications of all kinds, as they
can help to identify outliers, clusters or patterns, as well as highlight
the role of non-linear transformations of data.

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
