%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TruncatedPCQM
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Density Estimation for Point-Centered Quarter Method with Truncated Sampling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Implements a systematic methodology for estimating population density from
point-centered quarter method (PCQM) surveys when distance measurements
are truncated by a maximum search radius (right-censored). The package
provides a unified framework for analyzing such incomplete data,
addressing both completely randomly distributed (Poisson) and spatially
aggregated (Negative Binomial) populations. Key features include: (1)
Adjusted moment-based density estimators for censored distances; (2)
Maximum likelihood estimation (MLE) of density under the Poisson (CSR)
model; and (3) Simultaneous MLE of density and an aggregation parameter
under the Negative Binomial model. For more details, see Huang, Shen,
Xing, and Zhao (2026) <doi:10.48550/arXiv.2603.08276>.

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
