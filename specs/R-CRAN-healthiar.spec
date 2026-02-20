%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  healthiar
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Quantifying and Monetizing Health Impacts Attributable to Exposure

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-Rdpack 

%description
This R package has been developed with a focus on air pollution and noise
but can be applied to other exposures. The initial development has been
funded by the European Union project BEST-COST. Disclaimer: It is work in
progress and the developers are not liable for any calculation errors or
inaccuracies resulting from the use of this package. Selection of relevant
references (in chronological order): WHO (2003)
<https://www.who.int/publications/i/item/9241546204>, Murray et al. (2003)
<doi:10.1186/1478-7954-1-1>, Miller & Hurley (2003)
<doi:10.1136/jech.57.3.200>, Steenland & Armstrong (2006)
<doi:10.1097/01.ede.0000229155.05644.43>, WHO (2011)
<https://iris.who.int/items/723ab97c-5c33-4e3b-8df1-744aa5bc1c27>, GBD
2019 Risk Factors Collaborators (2020)
<doi:10.1016/S0140-6736(20)30752-2>.

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
