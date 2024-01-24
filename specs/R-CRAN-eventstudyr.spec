%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eventstudyr
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Visualization of Linear Panel Event Studies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-estimatr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-car 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-estimatr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-stringr 

%description
Estimates linear panel event study models. Plots coefficients following
the recommendations in Freyaldenhoven et al. (2021) <doi:10.3386/w29170>.
Includes sup-t bands, testing for key hypotheses, least wiggly path
through the Wald region. Allows instrumental variables estimation
following Freyaldenhoven et al. (2019) <doi:10.1257/aer.20180609>.

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
