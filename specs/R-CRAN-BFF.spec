%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BFF
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayes Factor Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-BSDA 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-BSDA 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Bayes factors represent the ratio of probabilities assigned to data by
competing scientific hypotheses. Drawbacks of Bayes factors are their
dependence on prior specifications that define null and alternative
hypotheses and difficulties encountered in their computation. To address
these problems we define Bayes factor functions (BFF) directly from common
test statistics. BFFs depend on a single non-centrality parameter that can
be expressed as a function of standardized effect sizes, and plots of BFFs
versus effect size provide informative summaries of hypothesis tests that
can be easily aggregated across studies. Such summaries eliminate the need
for arbitrary bright-line thresholds to determine “statistical
significance.” BFFs are available in closed form and can be computed
easily from z, t, chi^2, and F statistics.

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
