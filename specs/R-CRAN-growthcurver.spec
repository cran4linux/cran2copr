%global __brp_check_rpaths %{nil}
%global packname  growthcurver
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simple Metrics to Summarize Growth Curves

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.0
BuildRequires:    R-graphics >= 4.0
BuildRequires:    R-grDevices >= 4.0
BuildRequires:    R-CRAN-minpack.lm >= 1.2
Requires:         R-stats >= 4.0
Requires:         R-graphics >= 4.0
Requires:         R-grDevices >= 4.0
Requires:         R-CRAN-minpack.lm >= 1.2

%description
Fits the logistic equation to microbial growth curve data (e.g., repeated
absorbance measurements taken from a plate reader over time). From this
fit, a variety of metrics are provided, including the maximum growth rate,
the doubling time, the carrying capacity, the area under the logistic
curve, and the time to the inflection point. Method described in
Sprouffske and Wagner (2016) <doi:10.1186/s12859-016-1016-7>.

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
