%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  visStatistics
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Selection and Visualisation of Statistical Hypothesis Tests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vcd 
Requires:         R-CRAN-Cairo 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-nortest 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-vcd 

%description
Automatically selects and visualises appropriate statistical hypothesis
tests between a response and a feature variable in a data frame. The
choice of test depends on the class, distribution, and sample size of the
input variables, as well as the user-defined 'conf.level'. Well suited for
web-based or server-side R applications. Implemented tests: t.test(),
wilcox.test(), aov(), oneway.test(), kruskal.test(), lm(), fisher.test(),
chisq.test(). Tests for normality: shapiro.test(), ad.test(). Tests for
equal variances: bartlett.test(). Post-hoc tests: TukeyHSD(),
pairwise.wilcox.test().

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
