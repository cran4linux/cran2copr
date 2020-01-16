%global packname  trend
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}
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


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
