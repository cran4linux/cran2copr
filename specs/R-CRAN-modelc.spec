%global packname  modelc
%global packver   1.0.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.0
Release:          1%{?dist}
Summary:          A Linear Model to 'SQL' Compiler

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
This is a cross-platform linear model to 'SQL' compiler. It generates
'SQL' from linear and generalized linear models. Its interface consists of
a single function, modelc(), which takes the output of lm() or glm()
functions (or any object which has the same signature) and outputs a 'SQL'
character vector representing the predictions on the scale of the response
variable as described in Dunn & Smith (2018)
<doi:10.1007/978-1-4419-0118-7> and originating in Nelder & Wedderburn
(1972) <doi:10.2307/2344614>. The resultant 'SQL' can be included in a
'SELECT' statement and returns output similar to that of the glm.predict()
or lm.predict() predictions, assuming numeric types are represented in the
database using sufficient precision. Currently log and identity link
functions are supported.

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
