%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  triggerstrategy
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Trigger Strategy in Clinical Trials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-CRAN-GA >= 3.0.0
BuildRequires:    R-CRAN-nleqslv >= 3.0.0
BuildRequires:    R-CRAN-ldbounds >= 2.0.0
BuildRequires:    R-CRAN-mvtnorm >= 1.1.0
Requires:         R-stats >= 4.0.0
Requires:         R-CRAN-GA >= 3.0.0
Requires:         R-CRAN-nleqslv >= 3.0.0
Requires:         R-CRAN-ldbounds >= 2.0.0
Requires:         R-CRAN-mvtnorm >= 1.1.0

%description
The trigger strategy is a general framework for a multistage statistical
design with multiple hypotheses, allowing an adaptive selection of interim
analyses. The selection of interim stages can be associated with some
prespecified endpoints which serve as the trigger. This selection allows
us to refine the critical boundaries in hypotheses testing procedures, and
potentially increase the statistical power. This package includes several
trial designs using the trigger strategy. See Gou, J. (2023), "Trigger
strategy in repeated tests on multiple hypotheses", Statistics in
Biopharmaceutical Research, 15(1), 133-140, and Gou, J. (2022), "Sample
size optimization and initial allocation of the significance levels in
group sequential trials with multiple endpoints", Biometrical Journal,
64(2), 301-311.

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
