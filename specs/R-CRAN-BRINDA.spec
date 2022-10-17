%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BRINDA
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of BRINDA Adjusted Micronutrient Biomarkers for Inflammation

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-berryFunctions 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-berryFunctions 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-rlang 

%description
Inflammation can affect many micronutrient biomarkers and can thus lead to
incorrect diagnosis of individuals and to over- or under-estimate the
prevalence of deficiency in a population. Biomarkers Reflecting
Inflammation and Nutritional Determinants of Anemia (BRINDA) is a
multi-agency and multi-country partnership designed to improve the
interpretation of nutrient biomarkers in settings of inflammation and to
generate context-specific estimates of risk factors for anemia (Suchdev
(2016) <doi:10.3945/an.115.010215>). In the past few years, BRINDA
published a series of papers to provide guidance on how to adjust
micronutrient biomarkers, retinol binding protein, serum retinol, serum
ferritin by Namaste (2020), soluble transferrin receptor (sTfR), serum
zinc, serum and Red Blood Cell (RBC) folate, and serum B-12, using
inflammation markers, alpha-1-acid glycoprotein (AGP) and/or C-Reactive
Protein (CRP) by Namaste (2020) <doi:10.1093/ajcn/nqaa141>, Rohner (2017)
<doi:10.3945/ajcn.116.142232>, McDonald (2020) <doi:10.1093/ajcn/nqz304>,
and Young (2020) <doi:10.1093/ajcn/nqz303>. The BRINDA inflammation
adjustment method mainly focuses on Women of Reproductive Age (WRA) and
Preschool-age Children (PSC); however, the general principle of the BRINDA
method might apply to other population groups. The BRINDA R package is a
user-friendly all-in-one R package that uses a series of functions to
implement BRINDA adjustment method, as described above. The BRINDA R
package will first carry out rigorous checks and provides users guidance
to correct data or input errors (if they occur) prior to inflammation
adjustments. After no errors are detected, the package implements the
BRINDA inflammation adjustment for up to five micronutrient biomarkers,
namely retinol-binding-protein, serum retinol, serum ferritin, sTfR, and
serum zinc (when appropriate), using inflammation indicators of AGP and/or
CRP for various population groups. Of note, adjustment for serum and RBC
folate and serum B-12 is not included in the R package, since evidence
shows that no adjustment is needed for these micronutrient biomarkers in
either WRA or PSC groups (Young (2020) <doi:10.1093/ajcn/nqz303>).

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
