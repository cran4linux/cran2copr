%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  safeconduct
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fetch Files Through a Real Browser When a Plain Request is Refused

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 5.0
BuildRequires:    R-CRAN-chromote >= 0.3.0
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-processx 
Requires:         R-CRAN-curl >= 5.0
Requires:         R-CRAN-chromote >= 0.3.0
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-processx 

%description
Some servers refuse any request that does not come from a web browser,
with a browser check or a block page instead of the file, 'Cloudflare'
being the common case. This package opens a real 'Chrome' with a throwaway
profile, lets any check run, and fetches the file or page: through 'curl'
carrying the clearance the browser was given where the server accepts
that, and through the browser itself where it does not. Nothing is
simulated; where a check asks a person to click, a window waits for them.
Built on 'chromote'.

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
