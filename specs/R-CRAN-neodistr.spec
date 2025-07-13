%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  neodistr
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Neo-Normal Distribution

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-brms 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-brms 
Requires:         R-CRAN-rstan 
Requires:         R-stats 
Requires:         R-CRAN-Rmpfr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rstantools

%description
Calculating the density, cumulative distribution, quantile, and random
number of neo-normal distribution. It also interfaces with the 'brms'
package, allowing the use of the neo-normal distribution as a custom
family. This integration enables the application of various 'brms'
formulas for neo-normal regression.  Modified to be Stable as Normal from
Burr (MSNBurr), Modified to be Stable as Normal from Burr-IIa
(MSNBurr-IIa), Generalized of MSNBurr (GMSNBurr), Jones-Faddy Skew-t,
Fernandez-Osiewalski-Steel Skew Exponential Power, and Jones Skew
Exponential Power distributions are supported. References: Choir, A. S.
(2020).Unpublished Dissertation, Iriawan, N. (2000).Unpublished
Dissertation, Rigby, R. A., Stasinopoulos, M. D., Heller, G. Z., &
Bastiani, F. D. (2019) <doi:10.1201/9780429298547>.

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
