%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sequential.pops
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Sequential Analysis of Biological Population Sizes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-emdbook 
BuildRequires:    R-CRAN-truncdist 
BuildRequires:    R-CRAN-rlang 
Requires:         R-methods 
Requires:         R-CRAN-emdbook 
Requires:         R-CRAN-truncdist 
Requires:         R-CRAN-rlang 

%description
In population management, data come at more or less regular intervals over
time in sampling batches (bouts) and decisions should be made with the
minimum number of samples and as quickly as possible. This package
provides tools to implement, produce charts with stop lines, summarize
results and assess sequential analyses that test hypotheses about
population sizes. Two approaches are included: the sequential test of
Bayesian posterior probabilities (Rincon, D.F. et al. 2025
<doi:10.1111/2041-210X.70053>), and the sequential probability ratio test
(Wald, A. 1945 <http://www.jstor.org/stable/2235829>).

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
