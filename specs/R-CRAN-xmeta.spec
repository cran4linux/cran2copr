%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xmeta
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Toolbox for Multivariate Meta-Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-aod 
BuildRequires:    R-CRAN-glmmML 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-mvmeta 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-aod 
Requires:         R-CRAN-glmmML 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-mvmeta 
Requires:         R-stats 
Requires:         R-CRAN-MASS 

%description
A toolbox for meta-analysis. This package includes: 1,a robust
multivariate meta-analysis of continuous or binary outcomes; 2, a
bivariate Egger's test for detecting small study effects; 3, Galaxy Plot:
A New Visualization Tool of Bivariate Meta-Analysis Studies; 4, a
bivariate T&F method accounting for publication bias in bivariate
meta-analysis, based on symmetry of the galaxy plot. Hong C. et al(2020)
<doi:10.1093/aje/kwz286>, Chongliang L. et al(2020)
<doi:10.1101/2020.07.27.20161562>.

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
