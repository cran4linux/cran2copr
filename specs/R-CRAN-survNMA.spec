%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  survNMA
%global packver   1.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Network Meta-Analysis Combining Survival and Count Outcomes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-netmeta 
Requires:         R-stats 
Requires:         R-CRAN-netmeta 

%description
Network meta-analysis for survival outcome data often involves several
studies only involve dichotomized outcomes (e.g., the numbers of event and
sample sizes of individual arms).  To combine these different outcome
data, Woods et al. (2010) <doi:10.1186/1471-2288-10-54> proposed a
Bayesian approach using complicated hierarchical models. Besides,
frequentist approaches have been alternative standard methods for the
statistical analyses of network meta-analysis, and the methodology has
been well established. We proposed an easy-to-implement method for the
network meta-analysis based on the frequentist framework in Noma and Maruo
(2025) <doi:10.1101/2025.01.23.25321051>. This package involves some
convenient functions to implement the simple synthesis method.

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
