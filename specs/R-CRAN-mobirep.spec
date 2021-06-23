%global __brp_check_rpaths %{nil}
%global packname  mobirep
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Models Bivariate Dependence and Produces Bivariate Return Periods

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-texmex 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-copBasic 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-SpatialExtremes 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-texmex 
Requires:         R-stats 
Requires:         R-CRAN-copBasic 
Requires:         R-grDevices 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-SpatialExtremes 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-viridis 

%description
Models the dependence between two variables in the extremes, identifies
most relevant models among six models: the conditional extremes model, the
Jt-KDE model and four copulae (Gumbel, Galambos, Normal, FGM). Bivariate
return periods for the six models and bivariate level curves can be
created. Methods used in the package are described in the following
reference: Tilloy, Malamud, Winter and Joly-Laugel (2020)
<doi:10.5194/nhess-20-2091-2020> Supporting references for the conditional
extremes model, Jt-KDE model and for copula modelling are the following:
Heffernan and Tawn (2004) <doi:10.1111/j.1467-9868.2004.02050.x> Cooley,
Thibaud, Castillo and Wehner (2019) <doi:10.1007/s10687-019-00348-0>
Nelsen (2006) <doi:10.1007/0-387-28678-0>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
