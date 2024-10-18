%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  combat.enigma
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fit and Apply ComBat, LMM, or Prescaling Harmonization for ENIGMA and Other Multisite MRI Data

License:          Artistic License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-nlme 
Requires:         R-CRAN-car 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-nlme 

%description
Fit and apply ComBat, linear mixed-effects models (LMM), or prescaling to
harmonize magnetic resonance imaging (MRI) data from different sites.
Briefly, these methods remove differences between sites due to using
different scanning devices, and LMM additionally tests linear hypotheses.
As detailed in the manual, the original ComBat function was first modified
for the harmonization of MRI data (Fortin et al. (2017)
<doi:10.1016/j.neuroimage.2017.11.024>) and then modified again to create
separate functions for fitting and applying the harmonization and allow
missing values and constant rows for its use within the Enhancing Neuro
Imaging Genetics through Meta-Analysis (ENIGMA) Consortium (Radua et al.
(2020) <doi:10.1016/j.neuroimage.2017.11.024>); this package includes the
latter version. LMM calls "lme" massively considering specific brain
imaging details. Finally, prescaling is a good option for fMRI, where
different devices can have varying units of measurement.

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
