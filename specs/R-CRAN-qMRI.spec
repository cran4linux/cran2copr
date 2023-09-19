%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qMRI
%global packver   1.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Quantitative Magnetic Resonance Imaging ('qMRI')

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-aws >= 2.4
BuildRequires:    R-CRAN-awsMethods >= 1.0
BuildRequires:    R-CRAN-oro.nifti >= 0.9
BuildRequires:    R-CRAN-adimpro >= 0.9
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-aws >= 2.4
Requires:         R-CRAN-awsMethods >= 1.0
Requires:         R-CRAN-oro.nifti >= 0.9
Requires:         R-CRAN-adimpro >= 0.9
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-stringr 

%description
Implementation of methods for estimation of quantitative maps from
Multi-Parameter Mapping (MPM) acquisitions (Weiskopf et al. (2013)
<doi:10.3389/fnins.2013.00095>) including adaptive smoothing methods in
the framework of the ESTATICS model (Estimating the apparent transverse
relaxation time (R2*) from images with different contrasts, Weiskopf et
al. (2014) <doi:10.3389/fnins.2014.00278>). The smoothing method is
described in Mohammadi et al. (2017). <doi:10.20347/WIAS.PREPRINT.2432>.
Usage of the package is also described in Polzehl and Tabelow (2019),
Magnetic Resonance Brain Imaging, Chapter 6, Springer, Use R! Series.
<doi:10.1007/978-3-030-29184-6_6>.

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
