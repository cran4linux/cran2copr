%global __brp_check_rpaths %{nil}
%global packname  newFocus
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          True Discovery Guarantee by Combining Partial Closed Testings

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ctgt 
Requires:         R-CRAN-ctgt 

%description
Closed testing has been proved powerful for true discovery guarantee. The
computation of closed testing is, however, quite burdensome. A general way
to reduce computational complexity is to combine partial closed testings
for some prespecified feature sets of interest. Partial closed testings
are performed at Bonferroni-corrected alpha level to guarantee the lower
bounds for the number of true discoveries in prespecified sets are
simultaneously valid. For any post hoc chosen sets of interest, coherence
property is used to get the lower bound. In this package, we implement
closed testing with globaltest to calculate the lower bound for number of
true discoveries, see Ningning Xu et.al (2021) <arXiv:2001.01541> for
detailed description.

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
