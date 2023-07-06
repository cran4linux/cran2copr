%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  oHMMed
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          HMMs with Ordered Hidden States and Emission Densities

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cvms 
BuildRequires:    R-CRAN-ggmcmc 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-mistr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-vcd 
Requires:         R-CRAN-cvms 
Requires:         R-CRAN-ggmcmc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-mistr 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-vcd 

%description
Inference using a class of Hidden Markov models (HMMs) called
'oHMMed'(ordered HMM with emission densities
<doi:10.1101/2023.06.26.546495>): The 'oHMMed' algorithms identify the
number of comparably homogeneous regions within observed sequences with
autocorrelation patterns. These are modelled as discrete hidden states;
the observed data points are then realisations of continuous probability
distributions with state-specific means that enable ordering of these
distributions. The observed sequence is labelled according to the hidden
states, permitting only neighbouring states that are also neighbours
within the ordering of their associated distributions. The parameters that
characterise these state-specific distributions are then inferred.
Relevant for application to genomic sequences, time series, or any other
sequence data with serial autocorrelation.

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
