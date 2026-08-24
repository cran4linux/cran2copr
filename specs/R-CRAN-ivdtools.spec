%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ivdtools
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Tools for Evaluation of in Vitro Diagnostic Reagents

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-nls2 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-VCA 
BuildRequires:    R-CRAN-VFP 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-nls2 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-VCA 
Requires:         R-CRAN-VFP 

%description
Provides statistical workflows used in the evaluation of in vitro
diagnostic reagents. Facilities include method comparison and Bland-Altman
analysis, receiver operating characteristic analysis, qualitative
agreement, precision and variance-component analysis, reference intervals,
stability studies, quality-control charts, curve fitting, analytical
sensitivity, outlier and normality assessment, and sample-size
calculations. For methodological details, see Bland and Altman (1986)
<doi:10.1016/S0140-6736(86)90837-8>, Passing and Bablok (1983)
<doi:10.1515/cclm.1983.21.11.709>, Linnet (1993)
<doi:10.1093/clinchem/39.3.424>, Hanley and McNeil (1982)
<doi:10.1148/radiology.143.1.7063747>, Horn et al. (1998)
<doi:10.1093/clinchem/44.3.622>, Westgard et al. (1981)
<doi:10.1093/clinchem/27.3.493>, and Lu et al. (2016)
<doi:10.1515/ijb-2015-0039>.

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
