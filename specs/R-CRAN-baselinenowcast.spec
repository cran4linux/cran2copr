%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  baselinenowcast
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Baseline Nowcasting for Right-Truncated Epidemiological Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-checkmate 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-purrr 

%description
Nowcasting right-truncated epidemiological data is critical for timely
public health decision-making, as reporting delays can create misleading
impressions of declining trends in recent data. This package provides
nowcasting methods based on using empirical delay distributions and
uncertainty from past performance. It is also designed to be used as a
baseline method for developers of new nowcasting methods. For more details
on the performance of the method(s) in this package applied to case
studies of COVID-19 and norovirus, see our recent paper at
<https://wellcomeopenresearch.org/articles/10-614>. The package supports
standard data frame inputs with reference date, report date, and count
columns, as well as the direct use of reporting triangles, and is
compatible with 'epinowcast' objects. Alongside an opinionated default
workflow, it has a low-level pipe-friendly modular interface, allowing
context-specific workflows. It can accommodate a wide spectrum of
reporting schedules, including mixed patterns of reference and reporting
(daily-weekly, weekly-daily). It also supports sharing delay distributions
and uncertainty estimates between strata, as well as custom uncertainty
models and delay estimation methods.

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
