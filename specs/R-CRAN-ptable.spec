%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ptable
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generation of Perturbation Tables for the Cell-Key Method

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-flexdashboard 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-flexdashboard 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 

%description
Tabular data from statistical institutes and agencies are mostly
confidential and must be protected prior to publications. The cell-key
method is a post-tabular Statistical Disclosure Control perturbation
technique that adds random noise to tabular data. The statistical
properties of the perturbations are defined by some noise probability
distributions - also referred to as perturbation tables. This tool can be
used to create the perturbation tables based on a maximum entropy approach
as described for example in Giessing (2016)
<doi:10.1007/978-3-319-45381-1_18>. The perturbation tables created can
finally be used to apply a cell-key method to frequency count or magnitude
tables.

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
