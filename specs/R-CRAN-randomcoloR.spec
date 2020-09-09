%global packname  randomcoloR
%global packver   1.1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generate Attractive Random Colors

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-V8 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-grDevices 
BuildRequires:    R-cluster 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-V8 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-Rtsne 
Requires:         R-grDevices 
Requires:         R-cluster 

%description
Simple methods to generate attractive random colors. The random colors are
from a wrapper of 'randomColor.js'
<https://github.com/davidmerfield/randomColor>. In addition, it also
generates optimally distinct colors based on k-means (inspired by
'IWantHue' <https://github.com/medialab/iwanthue>).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
