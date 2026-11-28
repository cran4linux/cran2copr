%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  posthocbounds
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Post Hoc Bounds on True Discoveries for Gaussian Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Computes lower confidence bounds on the number of true discoveries in any
selection of hypotheses, chosen after seeing the data, from independent
one-sided Gaussian test statistics. The bounds hold simultaneously over
all selections, as in the post hoc inference of Goeman and Solari (2011)
<doi:10.1214/11-STS356>. The bound on all hypotheses is the smallest of
the Sidak bound, closed testing with the largest p-value as local test,
and bounds from counts of statistics above thresholds and from a centered
statistic that gathers many weak signals. For a selection, the bound also
uses a reference family of p-value levels as in Blanchard, Neuvial and
Roquain (2020) <doi:10.1214/19-AOS1847>. The package reports bounds for
the most significant hypotheses and a bound on the false discovery
proportion for each hypothesis, and it also covers statistics that are
dependent within independent blocks of bounded size.

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
