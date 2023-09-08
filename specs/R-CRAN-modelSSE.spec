%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  modelSSE
%global packver   0.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Modelling Infectious Disease Superspreading from Contact Tracing Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Delaporte 
Requires:         R-CRAN-Delaporte 

%description
Comprehensive analytical tools are provided to characterize infectious
disease superspreading from contact tracing surveillance data. The
underlying theoretical frameworks of this toolkit include branching
process with transmission heterogeneity (Lloyd-Smith et al. (2005)
<doi:10.1038/nature04153>), case cluster size distribution (Nishiura et
al. (2012) <doi:10.1016/j.jtbi.2011.10.039>, Blumberg et al. (2014)
<doi:10.1371/journal.ppat.1004452>, and Kucharski and Althaus (2015)
<doi:10.2807/1560-7917.ES2015.20.25.21167>), and decomposition of
reproduction number (Zhao et al. (2022)
<doi:10.1371/journal.pcbi.1010281>).

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
