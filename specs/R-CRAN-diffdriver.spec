%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  diffdriver
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Identify Differential Selection

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-brglm 
BuildRequires:    R-CRAN-fastTopics 
BuildRequires:    R-CRAN-SQUAREM 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-brglm 
Requires:         R-CRAN-fastTopics 
Requires:         R-CRAN-SQUAREM 

%description
Tests for context-dependent selection on cancer driver genes using somatic
mutation data. The package implements the DiffDriver statistical framework
to assess whether the strength of positive selection on mutations in a
driver gene is associated with tumor- or individual-level context
variables, such as clinical traits, genomic features, or immune
microenvironment subtypes. DiffDriver estimates individual- and
position-specific background mutation rates, models selection as a
deviation from the background rate using functional annotations, and tests
context effects through a latent-variable logistic model. It provides
utilities for preparing mutation and annotation data, fitting
differential-selection models, running gene-level association tests,
summarizing candidate genes, and visualizing mutation patterns. The method
is described in Zhou et al. (2026) "Detecting context-dependent selection
on cancer driver genes with DiffDriver" <doi:10.64898/2026.04.06.716771>.

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
