%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gimme
%global packver   0.7-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.13
Release:          1%{?dist}%{?buildtag}
Summary:          Group Iterative Multiple Model Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-imputeTS >= 3.0
BuildRequires:    R-CRAN-igraph >= 1.0.0
BuildRequires:    R-CRAN-lavaan >= 0.6.9
BuildRequires:    R-CRAN-MIIVsem >= 0.5.4
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-aTSA 
Requires:         R-CRAN-imputeTS >= 3.0
Requires:         R-CRAN-igraph >= 1.0.0
Requires:         R-CRAN-lavaan >= 0.6.9
Requires:         R-CRAN-MIIVsem >= 0.5.4
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-nloptr 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-aTSA 

%description
Data-driven approach for arriving at person-specific time series models.
The method first identifies which relations replicate across the majority
of individuals to detect signal from noise. These group-level relations
are then used as a foundation for starting the search for person-specific
(or individual-level) relations. See Gates & Molenaar (2012)
<doi:10.1016/j.neuroimage.2012.06.026>.

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
