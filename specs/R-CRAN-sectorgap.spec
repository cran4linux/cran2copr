%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sectorgap
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Consistent Economic Trend Cycle Decomposition

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-KFAS 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tempdisagg 
Requires:         R-stats 
Requires:         R-CRAN-KFAS 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tempdisagg 

%description
Determining potential output and the output gap - two inherently
unobservable variables - is a major challenge for macroeconomists.
'sectorgap' features a flexible modeling and estimation framework for a
multivariate Bayesian state space model identifying economic output
fluctuations consistent with subsectors of the economy. The proposed model
is able to capture various correlations between output and a set of
aggregate as well as subsector indicators. Estimation of the latent states
and parameters is achieved using a simple Gibbs sampling procedure and
various plotting options facilitate the assessment of the results. For
details on the methodology and an illustrative example, see Streicher
(2024)
<https://www.research-collection.ethz.ch/handle/20.500.11850/653682>.

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
