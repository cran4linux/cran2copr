%global __brp_check_rpaths %{nil}
%global packname  ProcData
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Process Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-keras >= 2.2.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-keras >= 2.2.4
Requires:         R-CRAN-Rcpp >= 0.12.16

%description
Provides tools for exploratory process data analysis. Process data refers
to the data describing participants' problem-solving processes in
computer-based assessments. It is often recorded in computer log files.
This package provides functions to read, process, and write process data.
It also implements two feature extraction methods to compress the
information stored in process data into standard numerical vectors. This
package also provides recurrent neural network based models that relate
response processes with other binary or scale variables of interest. The
functions that involve training and evaluating neural networks are
wrappers of functions in 'keras'.

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
