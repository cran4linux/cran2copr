%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NPBBBdesigns
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Construction and a-Efficiency of Nested Partially Balanced Bipartite Block Designs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Construction and evaluation of nested partially balanced bipartite block
(NPBBB) designs for comparing a set of test treatments with a set of
control treatments under a nested (blocks within blocks) structure. Six
systematic construction methods are provided: composing partially balanced
bipartite block designs with nested balanced incomplete block designs;
augmenting nested partially balanced incomplete block designs with
controls; merging rows of group-divisible nested designs; direct
construction from group-divisible schemes; and expansion of partially
balanced incomplete block designs (Vinayaka et al. 2026: In press). The
A-efficiencies of the block and sub-block classifications are computed
against the A-optimal completely symmetric reference design, following the
test-versus-control optimality framework of Gupta and Parsad (1996)
<doi:10.1080/03610929608831743> and Vinayaka et al. (2024)
<doi:10.1080/03610926.2023.2251623>. These designs are particularly suited
to agricultural, animal husbandry, industrial, and clinical trials
involving multiple standard checks under nested experimental conditions,
such as multi-environment trials where field heterogeneity (blocks) and
within-field variation (sub-blocks) must be controlled simultaneously.

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
