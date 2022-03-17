%global __brp_check_rpaths %{nil}
%global packname  test2norm
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Normative Standards for Cognitive Tests

License:          CPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-mfp 
Requires:         R-CRAN-mfp 

%description
Package test2norm contains functions to generate formulas for normative
standards applied to cognitive tests. It takes raw test scores (e.g.,
number of correct responses) and converts them to scaled scores and
demographically adjusted scores, using methods described in Heaton et al.
(2003) <doi:10.1016/B978-012703570-3/50010-9> & Heaton et al. (2009,
ISBN:9780199702800). The scaled scores are calculated as quantiles of the
raw test scores, scaled to have the mean of 10 and standard deviation of
3, such that higher values always correspond to better performance on the
test. The demographically adjusted scores are calculated from the
residuals of a model that regresses scaled scores on demographic
predictors (e.g., age). The norming procedure makes use of the mfp()
function from the 'mfp' package to explore nonlinear associations between
cognition and demographic variables.

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
