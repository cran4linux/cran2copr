%global __brp_check_rpaths %{nil}
%global packname  rgabriel
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Gabriel Multiple Comparison Test and Plot the Confidence Interval on Barplot

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
This package was created to analyze multi-level one-way experimental
designs. It is designed to handle vectorized observation and factor data
where there are unequal sample sizes and population variance homogeneity
can not be assumed. To conduct the Gabriel test, create two vectors: one
for your observations and one for the factor level of each observation.
The function, rgabriel, conduct the test and save the output as a vector
to input into the gabriel.plot function, which produces a confidence
interval plot for Multiple Comparison.

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
