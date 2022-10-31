%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VIC5
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          The Variable Infiltration Capacity (VIC) Hydrological Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-foreach 

%description
The Variable Infiltration Capacity (VIC) model is a macroscale hydrologic
model that solves full water and energy balances, originally developed by
Xu Liang at the University of Washington (UW). The version of VIC source
code used is of 5.0.1 on <https://github.com/UW-Hydro/VIC/>, see Hamman et
al. (2018). Development and maintenance of the current official version of
the VIC model at present is led by the UW Hydro (Computational Hydrology
group) in the Department of Civil and Environmental Engineering at UW. VIC
is a research model and in its various forms it has been applied to most
of the major river basins around the world, as well as globally
<http://vic.readthedocs.io/en/master/Documentation/References/>.
References: "Liang, X., D. P. Lettenmaier, E. F. Wood, and S. J. Burges
(1994), A simple hydrologically based model of land surface water and
energy fluxes for general circulation models, J. Geophys. Res., 99(D7),
14415-14428, <doi:10.1029/94JD00483>"; "Hamman, J. J., Nijssen, B., Bohn,
T. J., Gergel, D. R., and Mao, Y. (2018), The Variable Infiltration
Capacity model version 5 (VIC-5): infrastructure improvements for new
applications and reproducibility, Geosci. Model Dev., 11, 3481-3496,
<doi:10.5194/gmd-11-3481-2018>".

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
