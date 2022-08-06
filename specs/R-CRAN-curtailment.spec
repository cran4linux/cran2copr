%global __brp_check_rpaths %{nil}
%global packname  curtailment
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Finds Binary Outcome Designs Using Stochastic Curtailment

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-pkgcond 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-pkgcond 
Requires:         R-stats 

%description
Finds single- and two-arm designs using stochastic curtailment, as
described by Law et al. (2019) <arXiv:1909.03017> and Law et al. (2021)
<doi:10.1002/pst.2067> respectively. Designs can be single-stage or
multi-stage. Non-stochastic curtailment is possible as a special case.
Desired error-rates, maximum sample size and lower and upper anticipated
response rates are inputted and suitable designs are returned with
operating characteristics. Stopping boundaries and visualisations are also
available. The package can find designs using other approaches, for
example designs by Simon (1989) <doi:10.1016/0197-2456(89)90015-9> and
Mander and Thompson (2010) <doi:10.1016/j.cct.2010.07.008>. Other
features: compare and visualise designs using a weighted sum of expected
sample sizes under the null and alternative hypotheses and maximum sample
size; visualise any binary outcome design.

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
