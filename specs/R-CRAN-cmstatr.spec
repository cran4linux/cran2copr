%global packname  cmstatr
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}
Summary:          Statistical Methods for Composite Material Data

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-kSamples 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-kSamples 
Requires:         R-MASS 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 

%description
An implementation of the statistical methods commonly used for advanced
composite materials in aerospace applications. This package focuses on
calculating basis values (lower tolerance bounds) for material strength
properties, as well as performing the associated diagnostic tests. This
package provides functions for calculating basis values assuming several
different distributions, as well as providing functions for non-parametric
methods of computing basis values. Functions are also provided for testing
the hypothesis that there is no difference between strength and modulus
data from an alternate sample and that from a "qualification" or
"baseline" sample. For a discussion of these statistical methods and their
use, see the Composite Materials Handbook, Volume 1 (2012, ISBN:
978-0-7680-7811-4). Additional details about this package are available in
the paper by Kloppenborg (2020, <doi:10.21105/joss.02265>).

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
