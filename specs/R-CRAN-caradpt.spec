%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  caradpt
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Covariate-Adjusted Response-Adaptive Designs for Clinical Trials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-survival 

%description
Tools for implementing covariate-adjusted response-adaptive procedures for
binary, continuous and survival responses. Users can flexibly choose
between two functions based on their specific needs for each procedure:
use real patient data from clinical trials to compute allocation
probabilities directly, or use built-in simulation functions to generate
synthetic patient data. Detailed methodologies and algorithms used in this
package are described in the following references: Zhang, L. X., Hu, F.,
Cheung, S. H., & Chan, W. S. (2007)<doi:10.1214/009053606000001424> Zhang,
L. X. & Hu, F. (2009) <doi:10.1007/s11766-009-0001-6> Hu, J., Zhu, H., &
Hu, F. (2015) <doi:10.1080/01621459.2014.903846> Zhao, W., Ma, W., Wang,
F., & Hu, F. (2022) <doi:10.1002/pst.2160> Mukherjee, A., Jana, S., &
Coad, S. (2024) <doi:10.1177/09622802241287704>.

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
