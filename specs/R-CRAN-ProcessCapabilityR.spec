%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ProcessCapabilityR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Classical and Generalized Process Capability Indices

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Computes classical process capability indices (Cp, Cpk, Cpu, Cpl, Cpm,
Cpmk, Pp, Ppk, Ppu, Ppl, Z) and the generalized process capability index
Cpy (Maiti, Saha & Nanda, 2010) <doi:10.1080/16843703.2010.11673233> for
any continuous or discrete quality characteristic. Users supply the
probability density function (PDF) and cumulative distribution function
(CDF) of the characteristic, and the package returns point estimates,
bootstrap confidence intervals (percentile and BCa), and sensitivity
tables/plots across ranges of short-term standard deviation (sigma),
long-term standard deviation (s), desired yield (p0), and significance
levels. Classical indices are recoverable as special cases under the
normal distribution. The package follows the theory and notation of Kane
(1986) <doi:10.1080/00224065.1986.11978984>, Chan, Cheng & Spiring (1988)
<doi:10.1080/00224065.1988.11979102>, Pearn, Kotz & Johnson (1992)
<doi:10.1080/00224065.1992.11979403>, Kotz & Johnson (2002)
<doi:10.1080/00224065.2002.11980119>, Montgomery (2020,
ISBN:978-1-119-39930-8), Juran (1974, ISBN:978-0-07-033176-1), Harry &
Schroeder (2000, ISBN:978-0-385-49437-2), and the AIAG SPC Reference
Manual (2005, ISBN:978-1-60534-026-3).

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
