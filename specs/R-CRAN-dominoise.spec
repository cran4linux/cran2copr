%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dominoise
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Parsimonious Noise Perturbation for Magnitude Tables

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-rlang 

%description
Protects magnitude tables, such as tables of enterprise turnover, by
multiplying each total by a Gaussian noise combining a dominance-driven
component and a general-purpose one, governed by three parameters only.
Information loss and disclosure risks for three attack scenarios (external
inference, internal inference and differencing) are available in closed
form, so that calibration requires neither simulation nor re-estimation on
the data. The package guides that calibration step by step, from the
differencing noise to the dominance parameters, with decision tables and
risk-utility plots, applies the mechanism to an aggregated table using
SHA-512 hashed random keys for consistency over time, and reports the risk
and utility actually achieved. The method is described in Jamme (2027)
<doi:10.1007/978-3-032-37883-5_9>.

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
