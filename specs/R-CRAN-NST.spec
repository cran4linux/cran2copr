%global __brp_check_rpaths %{nil}
%global packname  NST
%global packver   3.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Normalized Stochasticity Ratio

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-iCAMP 
Requires:         R-CRAN-vegan 
Requires:         R-parallel 
Requires:         R-CRAN-permute 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-iCAMP 

%description
To estimate ecological stochasticity in community assembly. Understanding
the community assembly mechanisms controlling biodiversity patterns is a
central issue in ecology. Although it is generally accepted that both
deterministic and stochastic processes play important roles in community
assembly, quantifying their relative importance is challenging. The new
index, normalized stochasticity ratio (NST), is to estimate ecological
stochasticity, i.e. relative importance of stochastic processes, in
community assembly. With functions in this package, NST can be calculated
based on different similarity metrics and/or different null model
algorithms, as well as some previous indexes, e.g. previous Stochasticity
Ratio (ST), Standard Effect Size (SES), modified Raup-Crick metrics (RC).
Functions for permutational test and bootstrapping analysis are also
included. Previous ST is published by Zhou et al (2014)
<doi:10.1073/pnas.1324044111>. NST is modified from ST by considering two
alternative situations and normalizing the index to range from 0 to 1
(Ning et al 2019) <doi:10.1073/pnas.1904623116>. A modified version, MST,
is a special case of NST, used in some recent or upcoming publications,
e.g. Liang et al (2020) <doi:10.1016/j.soilbio.2020.108023>. SES is
calculated as described in Kraft et al (2011)
<doi:10.1126/science.1208584>. RC is calculated as reported by Chase et al
(2011) <doi:10.1890/es10-00117.1> and Stegen et al (2013)
<doi:10.1038/ismej.2013.93>. Version 3 added NST based on phylogenetic
beta diversity, used by Ning et al (2020)
<doi:10.1038/s41467-020-18560-z>.

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
