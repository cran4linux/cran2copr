%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hrtlFMC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Half Replicate of Two Level Factorial Run Order with Minimum Level Changes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-FMC 
Requires:         R-CRAN-FMC 

%description
It is used to construct run sequences with minimum changes for half
replicate of two level factorial run order. Experimenter can save time and
resources by minimizing the number of changes in levels of individual
factor and therefore the total number of changes. It consists of the
function minimal_hrtlf(). This technique can be employed to any half
replicate of two level factorial run order where the number of factors are
greater than two. In Design of Experiments (DOE) theory, two level of a
factor can be represented as integers e.g. - 1 for low and 1 for high.
User is expected to enter total number of factors to be considered in the
experiment. minimal_hrtlf() provides the required run sequences for the
input number of factors.  The output also gives the number of changes of
each factor along with total number of changes in the run sequence. Due to
restricted randomization the minimally changed run sequences of half
replicate of two level factorial run order will be affected by trend
effect. The output also provides the Trend Factor value of the run order.
Trend factor value will lies between 0 to 1. Higher the values, lesser the
influence of trend effects on the run order.

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
