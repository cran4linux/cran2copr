%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geneSLOPE
%global packver   0.38.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.38.2
Release:          1%{?dist}%{?buildtag}
Summary:          Genome-Wide Association Study with SLOPE

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-SLOPE 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-grid 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-SLOPE 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-bigmemory 
Requires:         R-grid 
Requires:         R-utils 
Requires:         R-stats 

%description
Genome-wide association study (GWAS) performed with SLOPE, short for
Sorted L-One Penalized Estimation, a method for estimating the vector of
coefficients in a linear model. In the first step of GWAS, single
nucleotide polymorphisms (SNPs) are clumped according to their
correlations and distances. Then, SLOPE is performed on the data where
each clump has one representative. Malgorzata Bogdan, Ewout van den Berg,
Chiara Sabatti, Weijie Su and Emmanuel Candes (2014) "SLOPE - Adaptive
Variable Selection via Convex Optimization" <arXiv:1407.3824>.

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
