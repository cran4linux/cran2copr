%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mop
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Mobility Oriented-Parity Metric

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-terra >= 1.6.7
BuildRequires:    R-CRAN-foreach >= 1.5
BuildRequires:    R-CRAN-doSNOW >= 1.0
BuildRequires:    R-CRAN-snow >= 0.4
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-terra >= 1.6.7
Requires:         R-CRAN-foreach >= 1.5
Requires:         R-CRAN-doSNOW >= 1.0
Requires:         R-CRAN-snow >= 0.4
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
A set of tools to perform multiple versions of the Mobility
Oriented-Parity metric. This multivariate analysis helps to characterize
levels of dissimilarity between a set of conditions of reference and
another set of conditions of interest. If predictive models are
transferred to conditions different from those over which models were
calibrated (trained), this metric helps to identify transfer conditions
that differ substantially from those of calibration. These tools are
implemented following principles proposed in Owens et al. (2013)
<doi:10.1016/j.ecolmodel.2013.04.011>, and expanded to obtain more
detailed results that aid in interpretation.

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
