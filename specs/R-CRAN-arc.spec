%global packname  arc
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Association Rule Classification

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-arules >= 1.6.6
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-discretization 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-datasets 
Requires:         R-CRAN-arules >= 1.6.6
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-discretization 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-datasets 

%description
Implements the Classification-based on Association Rules (CBA) (Bing Liu,
Wynne Hsu, Yiming Ma (1999)
<https://dl.acm.org/doi/10.5555/3000292.3000305>) algorithm for
association rule classification (ARC). The package also contains several
convenience methods that allow to automatically set CBA parameters
(minimum confidence, minimum support) and it also natively handles numeric
attributes by integrating a pre-discretization step. The rule generation
phase is handled by the 'arules' package. To further decrease the size of
the CBA models produced by the 'arc' package, postprocessing by the 'qCBA'
package is suggested. QCBA package can be obtained from CRAN archive or
from <https://github.com/kliegr/QCBA>.

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
