%global __brp_check_rpaths %{nil}
%global packname  ezmmek
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Easy Michaelis-Menten Enzyme Kinetics

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-assertable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-nls2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-assertable 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-nls2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 

%description
Serves as a platform for published fluorometric enzyme assay protocols.
'ezmmek' calibrates, calculates, and plots enzyme activities as they
relate to the transformation of synthetic substrates. At present, 'ezmmek'
implements two common protocols found in the literature, and is modular to
accommodate additional protocols. Here, these protocols are referred to as
the In-Sample Calibration (Hoppe, 1983; <doi:10.3354/meps011299>) and
In-Buffer Calibration (German et al., 2011;
<doi:10.1016/j.soilbio.2011.03.017>). protocols. By containing multiple
protocols, 'ezmmek' aims to stimulate discussion about how to best
optimize fluorometric enzyme assays. A standardized approach would make
studies more comparable and reproducible.

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
