%global packname  ctgdist
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Likert Category Distance Calculator

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-stats 
Requires:         R-CRAN-mirt 
Requires:         R-stats 

%description
It is assumed that psychological distances between the categories are
equal for the measurement instruments consisted of polytomously scored
items. According to Muraki, this assumption must be tested. In the
examination process of this assumption, the fit indexes are obtained and
evaluated. This package provides that this assumption is removed. By with
this package, the converted scale values of all items in a measurement
instrument can be calculated by estimating a category parameter set for
each item. Thus, the calculations can be made without any need to usage of
the common category parameter set. Through this package, the psychological
distances of the items are scaled. The scaling of a category parameter set
for each item cause differentiation of score of the categories will be got
from items. Also, the total measurement instrument score of an individual
can be calculated according to the scaling of item score categories by
with this package.This package provides that the place of individuals
related to the structure to be measured with a measurement instrument
consisted of polytomously scored items can be reveal more accurately. In
this way, it is thought that the results obtained about individuals can be
made more sensitive, and the differences between individuals can be
revealed more accurately. On the other hand, it can be argued that more
accurate evidences can be obtained regarding the psychometric properties
of the measurement instruments.

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
