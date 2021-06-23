%global __brp_check_rpaths %{nil}
%global packname  powerEQTL
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Power and Sample Size Calculation for Bulk Tissue and Single-Cell eQTL Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-GLMMadaptive 
BuildRequires:    R-CRAN-glmmTMB 
BuildRequires:    R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-GLMMadaptive 
Requires:         R-CRAN-glmmTMB 
Requires:         R-parallel 

%description
Power and sample size calculation for bulk tissue and single-cell eQTL
analysis based on ANOVA, simple linear regression, or linear mixed effects
model. It can also calculate power/sample size for testing the association
of a SNP to a continuous type phenotype. Please see the reference: Dong X,
Li X, Chang T-W, Scherzer CR, Weiss ST, Qiu W. (2021)
<doi:10.1093/bioinformatics/btab385>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
