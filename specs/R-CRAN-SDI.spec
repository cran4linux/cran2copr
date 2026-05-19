%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SDI
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Slow Digestibility Index

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-topsis 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-liver 
Requires:         R-CRAN-topsis 
Requires:         R-stats 
Requires:         R-CRAN-liver 

%description
The Slow Digestibility Index (SDI) is a tool that helps users evaluate the
slow-digestion properties of crops or food matrices by combining multiple
factors into a single score. It considers parameters related to starch
composition [total starch (TS), amylose/amylopectin ratio (Aratio), total
amylose content (TAC), and total amylopectin content (TAPC)], starch
digestibility [rapidly digestible starch (RDS), slowly digestible starch
(SDS) and resistant starch (RS)], structural properties [relative
crystallinity (RC)], non-starch components [total protein, total oil
content (TOC), and total phenolic content (TPC)], and pasting behaviour
[peak viscosity (PV), pasting temperature (PT), holding strength (HS), and
final viscosity (FV)].The SDI is flexible and allows users to calculate
the index using all parameters or only selected ones, depending on the
data available. Users can also compute a starch-based SDI (using only
starch-related parameters) or a principal component analysis (PCA)-based
SDI, where weights are determined automatically from the data. Thus, the
SDI provides a simple way to compare and rank crops or food samples based
on their slow digestion potential. The package implements
SDI(),starchSDI(), genSDI(), scoreSDI(), and pcaSDI() for estimating slow
digestibility index using predefined weighted TOPSIS, starch-specific
TOPSIS, user-defined weighted TOPSIS, score-based normalization, and PCA
based approaches, respectively. The package has been developed using the
algorithm of Pandey et al. (2026) <doi:10.1016/j.jff.2026.107208>.

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
