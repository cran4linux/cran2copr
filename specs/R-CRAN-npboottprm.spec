%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  npboottprm
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Bootstrap Test with Pooled Resampling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-fGarch 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lmPerm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-MKinfer 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-sn 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-fGarch 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lmPerm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-MKinfer 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-sn 

%description
Addressing crucial research questions often necessitates a small sample
size due to factors such as distinctive target populations, rarity of the
event under study, time and cost constraints, ethical concerns, or
group-level unit of analysis. Many readily available analytic methods,
however, do not accommodate small sample sizes, and the choice of the best
method can be unclear. The 'npboottprm' package enables the execution of
nonparametric bootstrap tests with pooled resampling to help fill this
gap. Grounded in the statistical methods for small sample size studies
detailed in Dwivedi, Mallawaarachchi, and Alvarado (2017)
<doi:10.1002/sim.7263>, the package facilitates a range of statistical
tests, encompassing independent t-tests, paired t-tests, and one-way
Analysis of Variance (ANOVA) F-tests. The nonparboot() function undertakes
essential computations, yielding detailed outputs which include test
statistics, effect sizes, confidence intervals, and bootstrap
distributions. Further, 'npboottprm' incorporates an interactive 'shiny'
web application, nonparboot_app(), offering intuitive, user-friendly data
exploration.

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
