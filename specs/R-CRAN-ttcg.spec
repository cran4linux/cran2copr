%global __brp_check_rpaths %{nil}
%global packname  ttcg
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Three-Term Conjugate Gradient for Unconstrained Optimization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-numDeriv 

%description
Some accelerated three-term conjugate gradient algorithms implemented
purely in R with the same user interface as optim(). The search directions
and acceleration scheme are described in Andrei, N. (2013)
<doi:10.1016/j.amc.2012.11.097>, Andrei, N. (2013)
<doi:10.1016/j.cam.2012.10.002>, and Andrei, N (2015)
<doi:10.1007/s11075-014-9845-9>. Line search is done by a hybrid algorithm
incorporating the ideas in Oliveia and Takahashi (2020)
<doi:10.1145/3423597> and More and Thuente (1994)
<doi:10.1145/192115.192132>.

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
