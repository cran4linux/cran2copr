%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SPLICE
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Synthetic Paid Loss and Incurred Cost Experience (SPLICE) Simulator

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-SynthETIC >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-SynthETIC >= 1.0.0
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-lifecycle 

%description
An extension to the individual claim simulator called 'SynthETIC' (on
CRAN), to simulate the evolution of case estimates of incurred losses
through the lifetime of an insurance claim. The transactional simulation
output now comprises key dates, and both claim payments and revisions of
estimated incurred losses. An initial set of test parameters, designed to
mirror the experience of a real insurance portfolio, were set up and
applied by default to generate a realistic test data set of incurred
histories (see vignette). However, the distributional assumptions used to
generate this data set can be easily modified by users to match their
experiences. Reference: Avanzi B, Taylor G, Wang M (2021) "SPLICE: A
Synthetic Paid Loss and Incurred Cost Experience Simulator"
<arXiv:2109.04058>.

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
