%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bean
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Thinning of Species Occurrences in Environmental Space

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-terra 

%description
A suite of tools to mitigate sampling bias in species occurrence records
by thinning data in the environmental space (E-space). This process can
improve the accuracy and precision of species distribution models (SDM,
also known as ecological niche models, ENM). The package offers a
data-driven protocol to determine thinning parameters using kernel-density
bandwidth selection. Two thinning methods are provided (stochastic and
deterministic) to reduce over-sampled environmental conditions and
down-weight outlier observations. The name 'bean' reflects the core
principle of the method: each 'pod' (a grid cell in E-space) is allowed to
contain only a limited number of 'beans' (occurrence points). See
Silverman (1986, ISBN:978-0-412-24620-3) and Rousseeuw and Leroy (2003,
ISBN:978-0-471-48855-2) for the underlying statistical methods.

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
