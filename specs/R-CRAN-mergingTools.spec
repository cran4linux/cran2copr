%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mergingTools
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Merge Hardware Event Monitors (HEMs) Coming from Separate Subexperiments into One Single Dataframe

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-MASS 

%description
Implementation of two tools to merge Hardware Event Monitors (HEMs) from
different subexperiments. Hardware Reading and Merging (HRM), which uses
order statistics to merge; and MUlti-Correlation HEM (MUCH) which merges
using a multivariate normal distribution. The reference paper for HRM is:
S. Vilardell, I. Serra, R. Santalla, E. Mezzetti, J. Abella and F. J.
Cazorla, "HRM: Merging Hardware Event Monitors for Improved Timing
Analysis of Complex MPSoCs," in IEEE Transactions on Computer-Aided Design
of Integrated Circuits and Systems, vol. 39, no. 11, pp. 3662-3673, Nov.
2020, <doi:10.1109/TCAD.2020.3013051>. For MUCH: S. Vilardell, I. Serra,
E. Mezzetti, J. Abella, and F. J. Cazorla. 2021. "MUCH: exploiting
pairwise hardware event monitor correlations for improved timing analysis
of complex MPSoCs". In Proceedings of the 36th Annual ACM Symposium on
Applied Computing (SAC '21). Association for Computing Machinery.
<doi:10.1145/3412841.3441931>. This work has been supported by the
European Research Council (ERC) under the European Union's Horizon 2020
research and innovation programme (grant agreement No. 772773).

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
