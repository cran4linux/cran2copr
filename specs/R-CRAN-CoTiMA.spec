%global __brp_check_rpaths %{nil}
%global packname  CoTiMA
%global packver   0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          Continuous Time Meta-Analysis ('CoTiMA')

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MBESS >= 4.6.0
BuildRequires:    R-CRAN-openxlsx >= 4.2.2
BuildRequires:    R-CRAN-ctsem >= 3.3.11
BuildRequires:    R-CRAN-OpenMx >= 2.18.1
BuildRequires:    R-CRAN-psych >= 1.9.12
BuildRequires:    R-CRAN-rootSolve >= 1.8.2
BuildRequires:    R-CRAN-foreach >= 1.5.1
BuildRequires:    R-CRAN-abind >= 1.4.5
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-zcurve >= 1.0.7
BuildRequires:    R-CRAN-stringi >= 1.0.7
BuildRequires:    R-CRAN-doParallel >= 1.0.15
BuildRequires:    R-CRAN-lavaan >= 0.6
BuildRequires:    R-CRAN-RPushbullet >= 0.3.3
BuildRequires:    R-CRAN-scholar >= 0.2.0
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-MBESS >= 4.6.0
Requires:         R-CRAN-openxlsx >= 4.2.2
Requires:         R-CRAN-ctsem >= 3.3.11
Requires:         R-CRAN-OpenMx >= 2.18.1
Requires:         R-CRAN-psych >= 1.9.12
Requires:         R-CRAN-rootSolve >= 1.8.2
Requires:         R-CRAN-foreach >= 1.5.1
Requires:         R-CRAN-abind >= 1.4.5
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-zcurve >= 1.0.7
Requires:         R-CRAN-stringi >= 1.0.7
Requires:         R-CRAN-doParallel >= 1.0.15
Requires:         R-CRAN-lavaan >= 0.6
Requires:         R-CRAN-RPushbullet >= 0.3.3
Requires:         R-CRAN-scholar >= 0.2.0
Requires:         R-CRAN-MASS 

%description
The 'CoTiMA' package performs meta-analyses of correlation matrices of
repeatedly measured variables taken from studies that used different time
intervals. Different time intervals between measurement occasions impose
problems for meta-analyses because the effects (e.g. cross-lagged effects)
cannot be simply aggregated, for example, by means of common fixed or
random effects analysis. However, continuous time math, which is applied
in 'CoTiMA', can be used to extrapolate or intrapolate the results from
all studies to any desired time lag. By this, effects obtained in studies
that used different time intervals can be meta-analyzed. 'CoTiMA' fits
models to empirical data using the structural equation model (SEM) package
'ctsem', the effects specified in a SEM are related to parameters that are
not directly included in the model (i.e., continuous time parameters;
together, they represent the continuous time structural equation model,
CTSEM). Statistical model comparisons and significance tests are then
performed on the continuous time parameter estimates. 'CoTiMA' also allows
analysis of publication bias (Egger's test, PET-PEESE estimates, zcurve
analysis etc.) and analysis of statistical power (post hoc power, required
sample sizes). See Dormann, C., Guthier, C., & Cortina, J. M. (2019)
<doi:10.1177/1094428119847277>. and Guthier, C., Dormann, C., & Voelkle,
M. C. (2020) <doi:10.1037/bul0000304>.

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
