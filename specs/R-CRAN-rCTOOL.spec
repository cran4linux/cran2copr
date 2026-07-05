%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rCTOOL
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Soil Organic Carbon Turnover Modelling with 'C-TOOL'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-utils 

%description
Provides an 'R' interface to the 'C-TOOL' soil carbon turnover model for
simulating soil organic carbon dynamics in agricultural systems. The
package supports the definition of carbon inputs, management schedules,
soil parameters, and temperature forcing, and includes tools for scenario
analysis and calibration of selected model parameters against observed
soil organic carbon stocks. The 'C-TOOL' model and related modelling
framework are described by Petersen et al. (2002)
<doi:10.1016/S0304-3800(02)00034-0>, Petersen et al. (2005)
<doi:10.1016/j.soilbio.2004.08.006>, Petersen et al. (2013)
<doi:10.1016/j.jclepro.2013.03.007>, and Taghizadeh-Toosi et al. (2014)
<doi:10.1016/j.ecolmodel.2014.08.016>. Further applications and
developments are described by Taghizadeh-Toosi et al. (2016)
<doi:10.1016/j.agsy.2016.03.004>, Keel et al. (2017)
<doi:10.1111/ejss.12454>, Taghizadeh-Toosi et al. (2020)
<doi:10.1007/s11104-020-04500-9>, and Taghizadeh-Toosi and Christensen
(2021) <doi:10.1038/s41598-021-97744-z>.

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
