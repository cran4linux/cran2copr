%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RAS
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Regional Association Score for Genome-Wide Association Studies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-segmented 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-CRAN-segmented 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Implements the Regional Association Score (RAS) method for genome-wide
association studies (GWAS). For each single nucleotide polymorphism (SNP),
RAS quantifies the strength of association within its surrounding genomic
region, arranges these regional scores along the chromosome into a signal
profile, and locates association regions on that profile with one of two
detectors: the original changepoint detector, or a box-scan region
detector that also delimits broad plateau-shaped regions. Genotypes can be
streamed from a chunked on-disk format through compiled code so that peak
memory no longer grows with chromosome size, and the regional weights can
be taken from an independent external GWAS (harmonised summary statistics)
instead of a within-sample split. The method is described in Jiang and
Zhang (2025) <doi:10.1073/pnas.2419721122>.

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
