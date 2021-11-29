%global __brp_check_rpaths %{nil}
%global packname  rsleep
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Sleep Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-edfReader 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-phonTools 
BuildRequires:    R-CRAN-psd 
Requires:         R-CRAN-edfReader 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-phonTools 
Requires:         R-CRAN-psd 

%description
Provides users functions for sleep data management and analysis such as
European Data Format (EDF) to Morpheo Data Format (MDF) conversion:
P.Bouchequet, D.Jin, G.Solelhac, M.Chennaoui, D.Leger (2018)
<doi:10.1016/j.msom.2018.01.130> "Morpheo Data Format (MDF), un nouveau
format de donnees simple, robuste et performant pour stocker et analyser
les enregistrements de sommeil". Provides hypnogram statistics computing
and visualisation functions from the American Academy of Sleep Medicine
(AASM) manual "The AASM Manual for the Scoring of Sleep and Associated
Events" <https://aasm.org/clinical-resources/scoring-manual/>.

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
