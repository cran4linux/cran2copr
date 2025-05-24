%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rdmulti
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of RD Designs with Multiple Cutoffs or Scores

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rdrobust 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rdrobust 

%description
The regression discontinuity (RD) design is a popular quasi-experimental
design for causal inference and policy evaluation. The 'rdmulti' package
provides tools to analyze RD designs with multiple cutoffs or scores:
rdmc() estimates pooled and cutoff specific effects for multi-cutoff
designs, rdmcplot() draws RD plots for multi-cutoff designs and rdms()
estimates effects in cumulative cutoffs or multi-score designs. See
Cattaneo, Titiunik and Vazquez-Bare (2020)
<https://rdpackages.github.io/references/Cattaneo-Titiunik-VazquezBare_2020_Stata.pdf>
for further methodological details.

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
