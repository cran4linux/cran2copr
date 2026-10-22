%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IFFuzzyStats
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Intuitionistic Fuzzy Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides constructors and arithmetic for intuitionistic fuzzy values
(intuitionistic fuzzy value, IFV) for intuitionistic fuzzy sets (Atanassov
(1986) <doi:10.1016/S0165-0114(86)80034-3>), including aggregation
operators of Xu (2007) <doi:10.1109/TFUZZ.2006.890678> and Xu and Yager
(2006) <doi:10.1080/03081070600574353>: intuitionistic fuzzy weighted
averaging (IFWA), intuitionistic fuzzy weighted geometric (IFWG),
intuitionistic fuzzy ordered weighted averaging (IFOWA), intuitionistic
fuzzy ordered weighted geometric (IFOWG), intuitionistic fuzzy hybrid
averaging (IFHA), intuitionistic fuzzy hybrid geometric (IFHG), and
Einstein operators; entropy (Szmidt and Kacprzyk (2000)
<doi:10.1016/S0165-0114(98)00402-3>; Vlachos and Sergiadis (2007)
<doi:10.1016/j.patrec.2006.07.004>) and distance and similarity measures,
including Ye (2011) <doi:10.1016/j.mcm.2010.07.022> cosine similarity and
Hamming, Euclidean and Hausdorff distances; intuitionistic fuzzy c-means
and k-means clustering; approximate reasoning via compositional inference;
and multi-criteria decision support via intuitionistic fuzzy Technique for
Order of Preference by Similarity to Ideal Solution (IF-TOPSIS) (Boran et
al. (2009) <doi:10.1016/j.eswa.2009.03.039>) and score ranking. All
computations use only base R with fully vectorised implementations.

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
