%global __brp_check_rpaths %{nil}
%global packname  RVowpalWabbit
%global packver   0.0.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.15
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to the Vowpal Wabbit

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    boost-devel
Requires:         boost-program-options
BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
The 'Vowpal Wabbit' project is a fast out-of-core learning system
sponsored by Microsoft Research (having started at Yahoo! Research) and
written by John Langford along with a number of contributors. This R
package does not include the distributed computing implementation of the
cluster/ directory of the upstream sources. Use of the software as a
network service is also not directly supported as the aim is a simpler
direct call from R for validation and comparison. Note that this package
contains an embedded older version of 'Vowpal Wabbit'. The package 'rvw'
at the GitHub repo <https://github.com/eddelbuettel/rvw> can provide an
alternative using an external 'Vowpal Wabbit' library installation.

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
