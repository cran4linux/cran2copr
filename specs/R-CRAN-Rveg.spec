%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rveg
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Digitization of Phytosociological Relevés

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
Requires:         R-utils 
Requires:         R-CRAN-xml2 

%description
Digitizes, manages, and classifies phytosociological vegetation plots.
Includes a checklist of Czech vascular plants based on Danihelka, Chrtek,
and Kaplan (2012) <https://www.preslia.cz/article/159>. Imports vegetation
data from 'TURBOVEG' (Hennekens and Schaminée, 2001) <doi:10.2307/3237010>
and exports data for 'JUICE' (Tichý, 2002)
<doi:10.1111/j.1654-1103.2002.tb02069.x>. Supports vegetation
classification using 'CzechVeg-ESy' expert rules (Chytrý et al., 2020)
<doi:10.5281/zenodo.3605562> and a constancy-based classifier inspired by
'VegKey' (Tichý and Chytrý, 2019) <doi:10.1111/jvs.12799>. The bundled
default classification model was trained on 'CzechVeg-OpenStrat' (Chytrý
et al., 2026) <doi:10.5281/zenodo.19231152>. Resolves plant synonyms using
the World Checklist of Vascular Plants (Govaerts et al., 2021)
<doi:10.1038/s41597-021-00997-6>, the taxonomic backbone of 'Plants of the
World Online'. For package methodology, see Král and Douda (2025)
<doi:10.1111/jvs.70012>.

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
