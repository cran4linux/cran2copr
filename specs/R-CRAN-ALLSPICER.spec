%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ALLSPICER
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          ALLelic Spectrum of Pleiotropy Informed Correlated Effects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 

%description
Provides statistical tools to analyze heterogeneous effects of rare
variants within genes that are associated with multiple traits. The
package implements methods for assessing pleiotropic effects and
identifying allelic heterogeneity, which can be useful in large-scale
genetic studies. Methods include likelihood-based statistical tests to
assess these effects. For more details, see Lu et al. (2024)
<doi:10.1101/2024.10.01.614806>.

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
