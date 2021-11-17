%global __brp_check_rpaths %{nil}
%global packname  Rpadrino
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Interact with the 'PADRINO' IPM Database

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-ipmr >= 0.0.4
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-truncdist 
BuildRequires:    R-utils 
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-ipmr >= 0.0.4
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-tools 
Requires:         R-CRAN-truncdist 
Requires:         R-utils 

%description
'PADRINO' houses textual representations of Integral Projection Models
which can be converted from their table format into full kernels to
reproduce or extend an already published analysis. 'Rpadrino' is an R
interface to this database. For more information on Integral Projection
Models, see Easterling et al. (2000)
<doi:10.1890/0012-9658(2000)081[0694:SSSAAN]2.0.CO;2>, Merow et al. (2013)
<doi:10.1111/2041-210X.12146>, Rees et al. (2014)
<doi:10.1111/1365-2656.12178>, and Metcalf et al. (2015)
<doi:10.1111/2041-210X.12405>. See Levin et al. (2021) for more
information on 'ipmr', the engine that powers model reconstruction
<doi:10.1111/2041-210X.13683>.

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
