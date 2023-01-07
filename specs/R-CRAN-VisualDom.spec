%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VisualDom
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualize Dominant Variables in Wavelet Multiple Correlation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-waveslim 
BuildRequires:    R-CRAN-wavemulcor 
BuildRequires:    R-CRAN-plot3D 
Requires:         R-CRAN-waveslim 
Requires:         R-CRAN-wavemulcor 
Requires:         R-CRAN-plot3D 

%description
Estimates and plots as a heat map the correlation coefficients obtained
via the wavelet local multiple correlation 'WLMC' (Fernández-Macho 2018)
and the 'dominant' variable/s, i.e., the variable/s that maximizes the
multiple correlation through time and scale (Polanco-Martínez et al. 2020,
Polanco-Martínez 2022). We improve the graphical outputs of WLMC proposing
a didactic and useful way to visualize the 'dominant' variable(s) for a
set of time series. The WLMC was designed for financial time series, but
other kinds of data (e.g., climatic, ecological, etc.) can be used. The
functions contained in 'VisualDom' are highly flexible since these
contains several parameters to personalize the time series under analysis
and the heat maps. In addition, we have also included two data sets (named
'rdata_climate' and 'rdata_Lorenz') to exemplify the use of the functions
contained in 'VisualDom'. Methods derived from Fernández-Macho (2018)
<doi:10.1016/j.physa.2017.11.050>, Polanco-Martínez et al. (2020)
<doi:10.1038/s41598-020-77767-8> and Polanco-Martínez (2023, in press).

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
