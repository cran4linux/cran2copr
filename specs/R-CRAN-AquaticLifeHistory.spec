%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AquaticLifeHistory
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Life History Analysis Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 

%description
Estimate aquatic species life history using robust techniques. This
package supports users undertaking two types of analysis: 1) Growth from
length-at-age data, and 2) maturity analyses for length and/or age data.
Maturity analyses are performed using generalised linear model approaches
incorporating either a binomial or quasibinomial distribution. Growth
modelling is performed using the multimodel approach presented by Smart et
al. (2016) "Multimodel approaches in shark and ray growth studies:
strengths, weaknesses and the future" <doi:10.1111/faf.12154>.

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
