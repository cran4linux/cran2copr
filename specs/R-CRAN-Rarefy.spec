%global packname  Rarefy
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Rarefaction Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-adiv 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-adiv 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geiger 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-vegan 

%description
Includes functions for the calculation of spatially and non-spatially
explicit rarefaction curves using different indices of taxonomic,
functional and phylogenetic diversity. The user can also rarefy any
biodiversity metric as provided by a self-written function (or an already
existent one) that gives as output a vector with the values of a certain
index of biodiversity calculated per plot (Ricotta, C., Acosta, A.,
Bacaro, G., Carboni, M., Chiarucci, A., Rocchini, D., Pavoine, S. (2019)
<doi:10.1016/j.ecolind.2019.105606>; Bacaro, G., Altobelli, A., Cameletti,
M., Ciccarelli, D., Martellos, S., Palmer, M. W., … Chiarucci, A. (2016)
<doi:10.1016/j.ecolind.2016.04.026>; Bacaro, G., Rocchini, D., Ghisla, A.,
Marcantonio, M., Neteler, M., & Chiarucci, A. (2012)
<doi:10.1016/j.ecocom.2012.05.007>).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
