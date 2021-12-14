%global __brp_check_rpaths %{nil}
%global packname  aPCoA
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Covariate Adjusted PCoA Plot

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-randomcoloR 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-cluster 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-randomcoloR 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-car 
Requires:         R-CRAN-cluster 

%description
In fields such as ecology, microbiology, and genomics, non-Euclidean
distances are widely applied to describe pairwise dissimilarity between
samples. Given these pairwise distances, principal coordinates analysis
(PCoA) is commonly used to construct a visualization of the data. However,
confounding covariates can make patterns related to the scientific
question of interest difficult to observe. We provide 'aPCoA' as an
easy-to-use tool to improve data visualization in this context, enabling
enhanced presentation of the effects of interest. Details are described in
Yushu Shi, Liangliang Zhang, Kim-Anh Do, Christine Peterson and Robert
Jenq (2020) Bioinformatics, Volume 36, Issue 13, 4099-4101.

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
