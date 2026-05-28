%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BIOEFIC
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Relative Bioefficiency via Simultaneous Regressions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-minpack.lm 
Requires:         R-stats 

%description
Fits simultaneous regression models to compare two sources (reference and
test) and estimates relative bioefficiency. Includes simultaneous
exponential model with common asymptote (model = 1), slope-ratio model
(model = 2), quadratic model (model = 3), linear-response plateau model
(model = 4), and Michaelis-Menten model (model = 5). Output style follows
the 'easyreg' package. Methods are based on Finney (1978,
ISBN:0-85264-252-0), Mercer et al. (1978) <doi:10.1093/jn/108.8.1244>,
Robbins et al. (1979) <doi:10.1093/jn/109.10.1710>, Noll et al. (1984)
<doi:10.3382/ps.0632458>, Gallant and Fuller (1973)
<doi:10.1080/01621459.1973.10481356>, Littell et al. (1997)
<doi:10.2527/1997.75102672x>, and Burnham and Anderson (2002,
ISBN:978-0-387-95364-9).

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
