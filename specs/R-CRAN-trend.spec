%global packname  trend
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Parametric Trend Tests and Change-Point Detection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-extraDistr >= 1.8.0
Requires:         R-CRAN-extraDistr >= 1.8.0

%description
The analysis of environmental data often requires the detection of trends
and change-points. This package includes tests for trend detection
(Cox-Stuart Trend Test, Mann-Kendall Trend Test, (correlated) Hirsch-Slack
Test, partial Mann-Kendall Trend Test, multivariate (multisite)
Mann-Kendall Trend Test, (Seasonal) Sen's slope, partial Pearson and
Spearman correlation trend test), change-point detection (Lanzante's test
procedures, Pettitt's test, Buishand Range Test, Buishand U Test, Standard
Normal Homogeinity Test), detection of non-randomness (Wallis-Moore Phase
Frequency Test, Bartels rank von Neumann's ratio test, Wald-Wolfowitz
Test) and the two sample Robust Rank-Order Distributional Test.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
