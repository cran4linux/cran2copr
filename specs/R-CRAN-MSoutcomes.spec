%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MSoutcomes
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          CORe Multiple Sclerosis Outcomes Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 

%description
Enable operationalized evaluation of disease outcomes in multiple
sclerosis.  ‘MSoutcomes’ requires longitudinally recorded clinical data
structured in long format.  The package is based on the research developed
at Clinical Outcomes Research unit (CORe), University of Melbourne and
Neuroimmunology Centre, Royal Melbourne Hospital. Kalincik et al. (2015)
<doi:10.1093/brain/awv258>. Lorscheider et al.  (2016)
<doi:10.1093/brain/aww173>. Sharmin et al. (2022) <doi:10.1111/ene.15406>.
Dzau et al. (2023) <doi:10.1136/jnnp-2023-331748>.

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
