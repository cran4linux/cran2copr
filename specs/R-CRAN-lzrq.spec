%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lzrq
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quantile Regression for Logarithmic Relationships with Non-Positive Outcome Values

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-quantreg 
Requires:         R-stats 

%description
Provides the lzrq() function for estimating logarithmic regression slopes
in quantile regression models, permitting the outcome variable to take on
non-positive values. lzrq() conducts regression after replacing
non-positive values with a sufficiently negative value. If the fitted
values of a quantile regression on this transformed outcome are all
greater than the negative value, then results are displayed. The resulting
coefficients can be meaningfully interpreted as logarithmic
intensive-margin relationships between the outcome variable and the
independent variables, even with non-positive values in the outcome
variable. If the condition does not hold for the specified quantile, then
the command iteratively makes the value larger and checks again. After ten
iterations where the condition does not hold, the functions return an
error and suppress results. This is an automated adaptation of the
algorithm described by Liu & Kaplan (2025)
<https://drive.google.com/file/d/1F3dnhm8MrlO5aRrGt48rBWAEaBqdCBH-/view>
and implemented in the companion 'Stata' command 'lzqreg', described in
Fitzgerald et al. (2026) <doi:10.31222/osf.io/juda7_v1>.

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
