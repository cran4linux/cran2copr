%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  confidenceSim
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Highly Customizable, Parallelized Simulations of Frequentist Confidence Clinical Trials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-rpact >= 4.0.0
BuildRequires:    R-CRAN-genodds >= 1.1.2
BuildRequires:    R-CRAN-confidenceCurves >= 0.2.0
Requires:         R-CRAN-rpact >= 4.0.0
Requires:         R-CRAN-genodds >= 1.1.2
Requires:         R-CRAN-confidenceCurves >= 0.2.0

%description
Simulate one or many frequentist confidence clinical trials based on a
specified set of parameters.  From a two-arm, single-stage trial to a
perpetually run Adaptive Platform Trial, this package offers vast
flexibility to customize your trial and observe operational
characterisitics over thousands of instances.

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
