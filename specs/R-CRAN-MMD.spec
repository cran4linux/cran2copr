%global __brp_check_rpaths %{nil}
%global packname  MMD
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Minimal Multilocus Distance (MMD) for Source Attribution and Loci Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-bigmemory 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-bigmemory 

%description
The aim of the package is two-fold: (i) To implement the MMD method for
attribution of individuals to sources using the Hamming distance between
multilocus genotypes. (ii) To select informative genetic markers based on
information theory concepts (entropy, mutual information and redundancy).
The package implements the functions introduced by Perez-Reche, F. J.,
Rotariu, O., Lopes, B. S., Forbes, K. J. and Strachan, N. J. C. Mining
whole genome sequence data to efficiently attribute individuals to source
populations. Scientific Reports 10, 12124 (2020)
<doi:10.1038/s41598-020-68740-6>. See more details and examples in the
README file.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
