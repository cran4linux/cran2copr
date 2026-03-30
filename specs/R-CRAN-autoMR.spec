%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  autoMR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Mendelian Randomization Workflows and Visualizations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.1
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-nortest >= 1.0.4
BuildRequires:    R-CRAN-R2jags >= 0.8.9
BuildRequires:    R-CRAN-coda >= 0.19.4.1
BuildRequires:    R-CRAN-MendelianRandomization >= 0.10.0
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 >= 4.0.1
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-nortest >= 1.0.4
Requires:         R-CRAN-R2jags >= 0.8.9
Requires:         R-CRAN-coda >= 0.19.4.1
Requires:         R-CRAN-MendelianRandomization >= 0.10.0
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 

%description
Provides tools to summarize, analyze, and visualize results from Mendelian
randomization studies using summarized genetic association data. The
package includes functions for generating forest plots and scatter plots
at the single-nucleotide polymorphism and Mendelian randomization method
levels, and for fitting multiple estimators in a unified workflow,
including inverse-variance weighted estimation, Mendelian randomization
Egger regression, the weighted median estimator, the robust adjusted
profile score, Mendelian randomization pleiotropy residual sum and
outlier, Mendelian randomization with the genotype recoding invariance
property, and a Bayesian horseshoe method. Related methods are described
by Burgess (2013) <doi:10.1002/gepi.21758>, Bowden (2015)
<doi:10.1093/ije/dyv080>, Bowden (2016) <doi:10.1002/gepi.21965>, Zhao
(2020) <doi:10.1214/19-AOS1866>, Verbanck (2018)
<doi:10.1038/s41588-018-0099-7>, Dudbridge (2025)
<doi:10.1371/journal.pgen.1011967>, and Grant and Burgess (2024)
<doi:10.1016/j.ajhg.2023.12.002>. Related open-source software includes
'TwoSampleMR' <https://github.com/MRCIEU/TwoSampleMR>, 'mr.raps'
<https://github.com/qingyuanzhao/mr.raps>, 'MR-PRESSO'
<https://github.com/rondolab/MR-PRESSO>, and 'MR-Horse'
<https://github.com/aj-grant/mrhorse>.

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
