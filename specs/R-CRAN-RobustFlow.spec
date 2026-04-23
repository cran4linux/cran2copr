%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RobustFlow
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Robustness and Drift Auditing for Longitudinal Decision Systems

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.10.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-rmarkdown >= 2.20
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-scales >= 1.2.0
BuildRequires:    R-CRAN-bslib >= 0.5.0
BuildRequires:    R-CRAN-htmltools >= 0.5.0
BuildRequires:    R-CRAN-golem >= 0.4.0
BuildRequires:    R-CRAN-DT >= 0.27
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-plotly >= 4.10.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-rmarkdown >= 2.20
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-scales >= 1.2.0
Requires:         R-CRAN-bslib >= 0.5.0
Requires:         R-CRAN-htmltools >= 0.5.0
Requires:         R-CRAN-golem >= 0.4.0
Requires:         R-CRAN-DT >= 0.27
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Provides tools for constructing longitudinal decision paths, quantifying
temporal drift, tracking subgroup disparity trajectories, and
stress-testing longitudinal conclusions under hidden bias. Implements
three signature metrics: the Drift Intensity Index (DII), which measures
structural instability in transition dynamics using the Frobenius norm of
consecutive transition matrix differences; the Bias Amplification Index
(BAI), which quantifies whether group disparities widen or converge over
time; and the Temporal Fragility Index (TFI), which estimates the minimum
hidden-bias perturbation required to nullify a longitudinal trend
conclusion. An interactive 'shiny' application supports exploratory
analysis, visualization, and reproducible reporting. Methods are motivated
by applications in educational and social science research, including the
Early Childhood Longitudinal Study (ECLS). The DII is based on the
Frobenius norm as described in Golub and Van Loan (2013,
ISBN:9781421407944). The TFI extends the hidden-bias sensitivity framework
of Rosenbaum (2002, ISBN:9781441912633). The BAI draws on
disparity-trajectory methods discussed in Duncan and Murnane (2011,
ISBN:9780871542731).

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
