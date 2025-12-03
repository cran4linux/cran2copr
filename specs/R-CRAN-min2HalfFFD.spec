%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  min2HalfFFD
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Minimally Changed Two-Level Half-Fractional Factorial Designs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-hrtlFMC 
BuildRequires:    R-CRAN-shinybusy 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-hrtlFMC 
Requires:         R-CRAN-shinybusy 

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
experiments. This technique can be employed to any half replicate of two
level factorial run order where the number of factors are greater than
two. For method details see, Bhowmik, A., Varghese, E., Jaggi, S. and
Varghese, C. (2017) <doi:10.1080/03610926.2016.1152490>. This package
generates all possible minimally changed two-level half-fractional
factorial designs for different experimental setups along with various
statistical criteria to measure the performance of these designs through a
user-friendly interface. It consist of the function minimal.2halfFFD()
which launches the application interface.

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
