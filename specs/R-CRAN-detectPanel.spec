%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  detectPanel
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Leakage-Aware Discovery of Small Biomarker Panels

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Discovers small binary-classification biomarker panels from count or
expression matrices while prioritizing detectability, expression
stability, and univariate discrimination. Candidate filtering and panel
selection can be repeated inside nested cross-validation to reduce
information leakage. The package provides shared resampling splits,
exhaustive small-panel search, logistic model fitting with an automatic
ridge fallback for unstable separation-prone fits, out-of-fold evaluation,
selection-frequency summaries, and optional 'DESeq2'
differential-expression support. The nested model-selection workflow
follows Varma and Simon (2006) <doi:10.1186/1471-2105-7-91>, and the
optional differential-expression analysis uses Love, Huber, and Anders
(2014) <doi:10.1186/s13059-014-0550-8>.

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
