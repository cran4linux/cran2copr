%global __brp_check_rpaths %{nil}
%global packname  proffer
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Profile R Code and Visualize with 'Pprof'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-processx >= 3.4.0
BuildRequires:    R-CRAN-withr >= 2.1.2
BuildRequires:    R-CRAN-pingr >= 2.0.1
BuildRequires:    R-CRAN-cli >= 2.0.0
BuildRequires:    R-CRAN-profile >= 1.0
BuildRequires:    R-CRAN-RProtoBuf >= 0.4.14
BuildRequires:    R-utils 
Requires:         R-CRAN-processx >= 3.4.0
Requires:         R-CRAN-withr >= 2.1.2
Requires:         R-CRAN-pingr >= 2.0.1
Requires:         R-CRAN-cli >= 2.0.0
Requires:         R-CRAN-profile >= 1.0
Requires:         R-CRAN-RProtoBuf >= 0.4.14
Requires:         R-utils 

%description
Like similar profiling tools, the 'proffer' package automatically detects
sources of slowness in R code. The distinguishing feature of 'proffer' is
its utilization of 'pprof', which supplies interactive visualizations that
are efficient and easy to interpret. Behind the scenes, the 'profile'
package converts native Rprof() data to a protocol buffer that 'pprof'
understands. For the documentation of 'proffer', visit
<https://r-prof.github.io/proffer/>. To learn about the implementations
and methodologies of 'pprof', 'profile', and protocol buffers, visit
<https://github.com/google/pprof>.
<https://developers.google.com/protocol-buffers>, and
<https://github.com/r-prof/profile>, respectively.

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
