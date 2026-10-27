%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NSCA
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Necessary and Sufficient Condition Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-NCA >= 5.0.2
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-SCAtools >= 0.5.2
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-NCA >= 5.0.2
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-SCAtools >= 0.5.2
Requires:         R-stats 
Requires:         R-utils 

%description
Tests whether a condition is both necessary and sufficient for an outcome,
that is, whether the outcome cannot be reached without the condition and
is guaranteed in its presence. Such a claim implies that two diagonally
opposite corners of the condition-outcome scatter plot contain no
observations. The package estimates both boundaries with the same data,
scope and frontier technique, reports the effect size and permutation test
of each, and indicates joint support only when both components are
supported. The two components are summarized by the weaker effect, a
balanced combination and the proportion of the scope that the two claims
jointly rule out. A dual-threshold table gives, for each outcome level,
the condition level it requires, the level sufficient for it, and the
interval between them. Results can be compared with regression slopes. The
package also provides plots, influential-case diagnostics,
scope-sensitivity and resampling checks, and simulation and power analysis
for planning studies. The two sides are estimated with the 'NCA' and
'SCAtools' packages.

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
