%global __brp_check_rpaths %{nil}
%global packname  bbw
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Blocked Weighted Bootstrap

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-car 
Requires:         R-CRAN-withr 

%description
The blocked weighted bootstrap (BBW) is an estimation technique for use
with data from two-stage cluster sampled surveys in which either prior
weighting (e.g. population-proportional sampling or PPS as used in
Standardized Monitoring and Assessment of Relief and Transitions or SMART
surveys) or posterior weighting (e.g. as used in rapid assessment method
or RAM and simple spatial sampling method or S3M surveys) is implemented.
See Cameron et al (2008) <doi:10.1162/rest.90.3.414> for application of
bootstrap to cluster samples. See Aaron et al (2016)
<doi:10.1371/journal.pone.0163176> and Aaron et al (2016)
<doi:10.1371/journal.pone.0162462> for application of the blocked weighted
bootstrap to estimate indicators from two-stage cluster sampled surveys.

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
