%global packname  mobr
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Measurement of Biodiversity

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-egg 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-geosphere 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-egg 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-geosphere 

%description
Functions for calculating metrics for the measurement biodiversity and its
changes across scales, treatments, and gradients. The methods implemented
in this package are described in: Chase, J.M., et al. (2018)
<doi:10.1111/ele.13151>, McGlinn, D.J., et al. (2019)
<doi:10.1111/2041-210X.13102>, and McGlinn, D.J., et al. (2020)
<doi:10.1101/851717>.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
