%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mixedfact
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generate and Analyze Mixed-Level Blocked Factorial Designs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Generates blocked designs for mixed-level factorial experiments for a
given block size. Internally, it uses finite-field based, collapsed, and
heuristic methods to construct block structures that minimize confounding
between block effects and factorial effects. The package creates the full
treatment combination table, partitions runs into blocks, and computes
detailed confounding diagnostics for main effects and two-factor
interactions. It also checks orthogonal factorial structure (OFS) and
computes efficiencies of factorial effects using the methods of Nair and
Rao (1948) <doi:10.1111/j.2517-6161.1948.tb00005.x>. When OFS is not
satisfied but the design has equal treatment replications and equal block
sizes, a general method based on the C-matrix and custom contrast vectors
is used to compute efficiencies. The output includes the generated design,
finite-field metadata, confounding summaries, OFS diagnostics, and
efficiency results.

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
