%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  neuroSCC
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bridging Simultaneous Confidence Corridors and PET Neuroimaging

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-contoureR 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-memisc 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-contoureR 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-CRAN-memisc 
Requires:         R-CRAN-oro.nifti 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Tools for the structured processing of PET neuroimaging data in
preparation for the estimation of Simultaneous Confidence Corridors (SCCs)
for one-group, two-group, or single-patient vs group comparisons. The
package facilitates PET image loading, data restructuring, integration
into a Functional Data Analysis framework, contour extraction,
identification of significant results, and performance evaluation. It
bridges established packages (e.g., 'oro.nifti') with novel statistical
methodologies (e.g., 'ImageSCC') and enables reproducible analysis
pipelines, including comparison with Statistical Parametric Mapping
('SPM').

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
