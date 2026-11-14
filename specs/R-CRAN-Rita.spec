%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rita
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Transformations, Normality Testing, and Reporting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-grid 
Requires:         R-stats 
Requires:         R-CRAN-lattice 
Requires:         R-grid 

%description
Automatically evaluates common normalizing transformations of numeric
variables and selects the best-fitting transformation for each based on
squared correlation with theoretical normal quantiles. Available
transformations include Rankit, arcsine, logit/log-odds, logarithmic,
square-root, and inverse/reciprocal. Performs six normality tests (Thode,
2002, <doi:10.1201/9780203910894>), incorporating simulation-based p-value
calibration for small-sample Jarque–Bera and optionally Lilliefors, as
well as subsampling for Shapiro–Wilk when sample sizes exceed its
supported limit. Available tests include Anderson–Darling, Pearson
chi-square, D'Agostino–Pearson omnibus, Jarque–Bera, Kolmogorov–Smirnov
with Lilliefors correction, and Shapiro–Wilk. A descriptive statistical
report of the retained input data in their original units, including the
five-number summary and mathematical moments, is also presented. The
Rankit empirical normal quantile transformation (ENQT) (Soloman and
Sawilowsky, 2009, <doi:10.22237/jmasm/1257034080>) is provided for those
requiring rank-based normalization and to facilitate its adoption.
Structured analytical results and paired visualizations of original and
transformed distributions are also available.

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
