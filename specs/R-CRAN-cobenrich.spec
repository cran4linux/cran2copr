%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cobenrich
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Using Multiple Continuous Biomarkers for Patient Enrichment in Two-Stage Clinical Designs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-CRAN-tmvtnorm >= 1.2
Requires:         R-stats >= 4.0.0
Requires:         R-CRAN-tmvtnorm >= 1.2

%description
Enrichment strategies play a critical role in modern clinical trial
design, especially as precision medicine advances the focus on
patient-specific efficacy. Recent developments in enrichment design have
introduced biomarker randomness and accounted for the correlation
structure between treatment effect and biomarker, resulting in a two-stage
threshold enrichment design. We propose novel two-stage enrichment designs
capable of handling two or more continuous biomarkers. See Zhang, F. and
Gou, J. (2025). Using multiple biomarkers for patient enrichment in
two-stage clinical designs. Technical Report.

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
