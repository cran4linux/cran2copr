%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  raptools
%global packver   1.23.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.23.0
Release:          1%{?dist}%{?buildtag}
Summary:          Risk Assessment Plot and Reclassification Metrics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-ggrepel 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pROC 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-ggrepel 

%description
Assessing the comparative performance of two logistic regression models or
results of such models or classification models. Discrimination metrics
include Integrated Discrimination Improvement (IDI), Net Reclassification
Improvement (NRI), and difference in Area Under the Curves (AUCs), Brier
scores and Brier skill. Plots include Risk Assessment Plots, Decision
curves and Calibration plots. Methods are described in Pickering and Endre
(2012) <doi:10.1373/clinchem.2011.167965> and Pencina et al. (2008)
<doi:10.1002/sim.2929>.

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
