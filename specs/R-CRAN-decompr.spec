%global __brp_check_rpaths %{nil}
%global packname  decompr
%global packver   6.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Global Value Chain Decomposition

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-matrixStats 

%description
Three global value chain (GVC) decompositions are implemented. The
Leontief decomposition derives the value added origin of exports by
country and industry as in Hummels, Ishii and Yi (2001). The Koopman, Wang
and Wei (2014) decomposition splits country-level exports into 9 value
added components, and the Wang, Wei and Zhu (2013) decomposition splits
bilateral exports into 16 value added components. Various GVC indicators
based on these decompositions are computed in the complimentary 'gvc'
package. --- References: --- Hummels, D., Ishii, J., & Yi, K. M. (2001).
The nature and growth of vertical specialization in world trade. Journal
of international Economics, 54(1), 75-96. Koopman, R., Wang, Z., & Wei, S.
J. (2014). Tracing value-added and double counting in gross exports.
American Economic Review, 104(2), 459-94. Wang, Z., Wei, S. J., & Zhu, K.
(2013). Quantifying international production sharing at the bilateral and
sector levels (No. w19677). National Bureau of Economic Research.

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
