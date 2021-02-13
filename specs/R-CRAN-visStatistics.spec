%global packname  visStatistics
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Visualization of Statistical Tests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-vcd 
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-nortest 
Requires:         R-CRAN-vcd 
Requires:         R-CRAN-Cairo 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-multcompView 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-nortest 

%description
Visualization of the most powerful statistical hypothesis test. The
function vistat() visualizes the statistical hypothesis testing between
the dependent variable (response) varsample and the independent variable
(feature) varfactor. The statistical hypothesis test (including the
eventual corresponding post-hoc analysis) with the highest statistical
power fulfilling the assumptions of the corresponding test is chosen based
on a decision tree. A graph displaying the raw data accordingly to the
chosen test is generated, the test statistics including eventual
post-hoc-analysis are returned. The automated workflow is especially
suited for browser based interfaces to server-based deployments of R.
Implemented tests: lm(), t.test(), wilcox.test(), aov(), kruskal.test(),
fisher.test(), chisqu.test(). Implemented tests to check the normal
distribution of standardized residuals: shapiro.test() and ad.test().
Implemented post-hoc tests: TukeyHSD() for aov() and
pairwise.wilcox.test() for kruskal.test(). For the comparison of averages,
the following algorithm is implemented: If the p-values of the
standardized residuals of both shapiro.test() or ad.test() are smaller
than 1-conf.level, kruskal.test() resp. wilcox.test() are performed,
otherwise the oneway.test() and aov() resp. t.test() are performed and
displayed. Exception: If the sample size is bigger than 100, t.test() is
always performed and wilcox.test() is never executed (Lumley et al. (2002)
<doi:10.1146/annurev.publhealth.23.100901.140546>). For the test of
independence of count data, Cochran's rule (Cochran (1954)
<doi:10.2307/3001666>) is implemented: If more than 20 percent of all
cells have a count smaller than 5, fisher.test() is performed and
displayed, otherwise chisqu.test(). In both cases case an additional
mosaic plot is generated.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
