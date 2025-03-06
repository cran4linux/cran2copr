%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RHC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Rangeland Health and Condition

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-FD 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-permute 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-FD 
Requires:         R-CRAN-randomForest 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 

%description
The evaluation criteria of rangeland health, condition and landscape
function analysis based on species diversity and functional diversity of
rangeland plant communities.

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
