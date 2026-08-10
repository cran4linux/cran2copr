%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metabodeconplus
%global packver   0.22.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.22.0
Release:          1%{?dist}%{?buildtag}
Summary:          Deconvolution, Alignment and Model Fitting of 1d NMR Spectra

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-toscutil >= 2.8.0
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-readJDX 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-toscutil >= 2.8.0
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-readJDX 
Requires:         R-CRAN-withr 

%description
An integrated framework for deconvolution, alignment and postprocessing of
1-dimensional (1d) nuclear magnetic resonance (NMR) spectra, extended with
end-to-end model fitting that turns the resulting matrix of aligned signal
integrals into classification models. The deconvolution part uses the
algorithm described in Koh et al. (2009) <doi:10.1016/j.jmr.2009.09.003>.
The alignment part is based on functions from the 'speaq' package,
described in Beirnaert et al. (2018) <doi:10.1371/journal.pcbi.1006018>
and Vu et al. (2011) <doi:10.1186/1471-2105-12-405>. A detailed
description and evaluation of an early version of the package can be found
in Haeckl et al. (2021) <doi:10.3390/metabo11070452>. 'metabodeconplus' is
the actively developed successor to the 'metabodecon' package and
introduces backwards-incompatible API changes.

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
