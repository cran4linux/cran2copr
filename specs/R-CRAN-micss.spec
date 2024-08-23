%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  micss
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Modified Iterative Cumulative Sum of Squares Algorithm

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 

%description
Companion package of Carrion-i-Silvestre & Sansó (2023): "Generalized
Extreme Value Approximation to the CUMSUMQ Test for Constant Unconditional
Variance in Heavy-Tailed Time Series". It implements the Modified
Iterative Cumulative Sum of Squares Algorithm, which is an extension of
the Iterative Cumulative Sum of Squares (ICSS) Algorithm of Inclan and
Tiao (1994), and it checks for changes in the unconditional variance of a
time series controlling for the tail index of the underlying distribution.
The fourth order moment is estimated non-parametrically to avoid the size
problems when the innovations are non-Gaussian (see, Sansó et al., 2004).
Critical values and p-values are generated using a Generalized Extreme
Value distribution approach. References Carrion-i-Silvestre J.J & Sansó A
(2023) <https://www.ub.edu/irea/working_papers/2023/202309.pdf>. Inclan C
& Tiao G.C (1994) <doi:10.1080/01621459.1994.10476824>, Sansó A & Aragó V
& Carrion-i-Silvestre J.L (2004)
<https://dspace.uib.es/xmlui/bitstream/handle/11201/152078/524035.pdf>.

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
