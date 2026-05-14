%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hydroeval
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hydrological Evaluation Metrics and Goodness-of-Fit Summaries

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Computes scalar performance metrics and goodness-of-fit summaries for
comparing simulated and observed hydrological or regression values.
Provides error metrics, percentage bias, Nash-Sutcliffe efficiency,
Kling-Gupta efficiency variants, correlation measures, agreement indices,
and comparison tables via gof() and gof_compare(). Metric definitions are
registry-governed with shared validation, provenance-aware wrappers, and
explicit handling of undefined or degenerate cases. Methods include Nash
and Sutcliffe (1970) <doi:10.1016/0022-1694(70)90255-6>, Gupta et al.
(2009) <doi:10.1016/j.jhydrol.2009.08.003>, Kling et al. (2012)
<doi:10.1016/j.jhydrol.2012.01.011>, and Willmott et al. (2012)
<doi:10.1002/joc.2419>.

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
