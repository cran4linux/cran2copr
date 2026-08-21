%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bbssr
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Blinded Sample Size Re-Estimation for Binary Endpoints

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-fpCompare 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-fpCompare 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Tools for blinded sample size re-estimation (BSSR) in two-arm clinical
trials with binary endpoints, together with the exact power and sample
size calculations that the re-estimation relies on. Five exact statistical
tests are implemented: Pearson chi-squared, Fisher exact, Fisher mid-p,
Z-pooled exact unconditional, and Boschloo exact unconditional. Each test
is available with a one-sided or a two-sided alternative, and the exact
unconditional tests can be combined with the Berger-Boos procedure. Sample
sizes can be re-estimated either at the planning stage, to study the
operating characteristics of a design, or from the blinded data of a trial
that is under way. Statistical methods based on Mehrotra et al. (2003)
<doi:10.1111/1541-0420.00051>, Berger and Boos (1994)
<doi:10.1080/01621459.1994.10476836> and Kieser (2020)
<doi:10.1007/978-3-030-49528-2_21>.

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
