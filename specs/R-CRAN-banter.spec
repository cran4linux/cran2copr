%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  banter
%global packver   0.9.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.8
Release:          1%{?dist}%{?buildtag}
Summary:          BioAcoustic eveNT classifiER

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest >= 4.6
BuildRequires:    R-CRAN-ggplot2 >= 3.3.3
BuildRequires:    R-CRAN-tibble >= 3.1.2
BuildRequires:    R-CRAN-rfPermute >= 2.5.1
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-swfscMisc >= 1.5
BuildRequires:    R-CRAN-tidyr >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.6
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
Requires:         R-CRAN-randomForest >= 4.6
Requires:         R-CRAN-ggplot2 >= 3.3.3
Requires:         R-CRAN-tibble >= 3.1.2
Requires:         R-CRAN-rfPermute >= 2.5.1
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-swfscMisc >= 1.5
Requires:         R-CRAN-tidyr >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.6
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-rlang 
Requires:         R-stats 

%description
Create a hierarchical acoustic event species classifier out of multiple
call type detectors as described in Rankin et al (2017)
<doi:10.1111/mms.12381>.

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
