%global packname  Rcpp
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          2%{?dist}
Summary:          Seamless R and C++ Integration

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-utils 

%description
The 'Rcpp' package provides R functions as well as C++ classes which offer
a seamless integration of R and C++. Many R data types and objects can be
mapped back and forth to C++ equivalents which facilitates both writing of
new code as well as easier integration of third-party libraries.
Documentation about 'Rcpp' is provided by several vignettes included in
this package, via the 'Rcpp Gallery' site at <http://gallery.rcpp.org>,
the paper by Eddelbuettel and Francois (2011,
<doi:10.18637/jss.v040.i08>), the book by Eddelbuettel (2013,
<doi:10.1007/978-1-4614-6868-4>) and the paper by Eddelbuettel and
Balamuta (2018, <doi:10.1080/00031305.2017.1375990>); see
'citation("Rcpp")' for details.

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
