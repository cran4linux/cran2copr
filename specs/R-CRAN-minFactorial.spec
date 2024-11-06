%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  minFactorial
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          All Possible Minimally Changed Factorial Run Orders

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-FMC 
Requires:         R-CRAN-FMC 

%description
In many agricultural, engineering, industrial, post-harvest and processing
experiments, the number of factor level changes and hence the total number
of changes is of serious concern as such experiments may consists of
hard-to-change factors where it is physically very difficult to change
levels of some factors or sometime such experiments may require
normalization time to obtain adequate operating condition. For this
reason, run orders that offer the minimum number of factor level changes
and at the same time minimize the possible influence of systematic trend
effects on the experimentation have been sought. Factorial designs with
minimum changes in factors level may be preferred for such situations as
these minimally changed run orders will minimize the cost of the
experiments. For method details see, Bhowmik, A.,Varghese, E., Jaggi, S.
and Varghese, C. (2017)<doi:10.1080/03610926.2016.1152490>.This package
used to construct all possible minimally changed factorial run orders for
different experimental set ups along with different statistical criteria
to measure the performance of these designs. It consist of the function
minFactDesign().

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
