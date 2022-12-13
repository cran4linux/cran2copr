%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TIMP
%global packver   1.13.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.13.6
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Separable Nonlinear Models in Spectroscopy and Microscopy

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-fields >= 4.1
BuildRequires:    R-CRAN-minpack.lm >= 1.1.1
BuildRequires:    R-CRAN-nnls >= 1.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-gclus 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-fields >= 4.1
Requires:         R-CRAN-minpack.lm >= 1.1.1
Requires:         R-CRAN-nnls >= 1.1
Requires:         R-methods 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-gclus 
Requires:         R-CRAN-gplots 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-utils 

%description
A problem solving environment (PSE) for fitting separable nonlinear models
to measurements arising in physics and chemistry experiments, as described
by Mullen & van Stokkum (2007) <doi:10.18637/jss.v018.i03> for its use in
fitting time resolved spectroscopy data, and as described by Laptenok et
al. (2007) <doi:10.18637/jss.v018.i08> for its use in fitting Fluorescence
Lifetime Imaging Microscopy (FLIM) data, in the study of Förster Resonance
Energy Transfer (FRET).  `TIMP` also serves as the computation backend for
the `GloTarAn` software, a graphical user interface for the package, as
described in Snellenburg et al. (2012) <doi:10.18637/jss.v049.i03>.

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
