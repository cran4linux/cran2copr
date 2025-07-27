%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eyeris
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible, Extensible, & Reproducible Pupillometry Preprocessing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-eyelinker 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gsignal 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-eyelinker 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gsignal 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rmarkdown 

%description
Pupillometry offers a non-invasive window into the mind and has been used
extensively as a psychophysiological readout of arousal signals linked
with cognitive processes like attention, stress, and emotional states
[Clewett et al. (2020) <doi:10.1038/s41467-020-17851-9>; Kret & Sjak-Shie
(2018) <doi:10.3758/s13428-018-1075-y>; Strauch (2024)
<doi:10.1016/j.tins.2024.06.002>]. Yet, despite decades of pupillometry
research, many established packages and workflows to date lack design
patterns based on Findability, Accessibility, Interoperability, and
Reusability (FAIR) principles [see Wilkinson et al. (2016)
<doi:10.1038/sdata.2016.18>]. 'eyeris' provides a modular, performant, and
extensible preprocessing framework for pupillometry data with BIDS-like
organization and interactive output reports [Esteban et al. (2019)
<doi:10.1038/s41592-018-0235-4>; Gorgolewski et al. (2016)
<doi:10.1038/sdata.2016.44>]. Development was supported, in part, by the
Stanford Wu Tsai Human Performance Alliance, Stanford Ric Weiland Graduate
Fellowship, Stanford Center for Mind, Brain, Computation and Technology,
NIH National Institute on Aging Grants (R01-AG065255, R01-AG079345), NSF
GRFP (DGE-2146755), McKnight Brain Research Foundation Clinical
Translational Research Scholarship in Cognitive Aging and Age-Related
Memory Loss, American Brain Foundation, and the American Academy of
Neurology.

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
